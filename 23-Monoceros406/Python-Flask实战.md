---
title: Python-Flask实战
date: 2023-12-08 19:58:56
tags: Flask
mathjax: true
---

# Python-Flask实战

## 部署

### Python部署

```bash
cat/etc/issue #查看系统版本号
python --version
python3 --version
sudo apt install python3 -pip
pip3 --version
sudo pip3 install virtualenv
sudo mkdir /var/www/html/flask_test
sudo chown -R  ubuntu/var/www/html/flask_test
cd /var/www/html/flask_test

#虚拟环境配置
virtualenv -p python3 venv
source venv/bin/activate

#flask安装
pip install flask
vim run.py #flask入口
python run.py
```

### Gunicorn部署

#### 法一：直接启动

```python
pip install gunicore
gunicore -w 3 -b 0.0.0.0:9100 run:app
#-w：处理工作的进程数量 -b：绑定运行的主机和端口 run：run.py app：APP应用名称

#其他常用参数
#-c CONFIG --config=CONFIG 指定配置文件
#-b BIND --bind=BIND 绑定的主机加端口
#-w INT --workers INT 用于处理工作进程的数量 默认1
#-k STRING,--worker-class STRING 使用的工作模式，默认异步sync 其他eventlet gevent tornado gthread gaiohttp
#--threads INT 工作线程数 默认1
#--worker-connections INT 最大并发 默认1000
#--backlog INT 等待连接的最大数 默认2048
#-p FILE --pid FILE pid文件名，不设置则不创建
#--access-logfile FILE 日志文件路径
#--access-logformat STRING 日志格式
#--error-logfile FILE --log-file FILE 错误日志文件路径
#--log-level LEVEL 日志输出等级
#--limit-request-line INT 限制HTTP请求行的允许大小 默认4094 取值0~8190 防DDoS
#--limit-request-fields INT 限制HTTP请求头字段数量 默认100 最大32768 防DDos
#--limit-request-fileld-size INT 限制HTTP请求头大小 默认8190 为0时不限制
#-t INT,--timeout INT 超时后工作被杀掉并重启 默认30s，Nginx默认60s
#--reload 代码改变时自动重启 默认False
#--daemon 以守护进程启动 默认False
#--chdir 加载应用程序前切换目录
#--gracful-timeout INT 默认30 从接收到重启信号开始超时后仍存活的工作将被强行杀死
#--keep-alive INT keep-alive连接等待秒数 默认2 一般1~5s
#--spew 打印服务器执行过的每一条语句 默认False
#--check-config 显示当前配置 默认False显示
#-e ENV --env ENV 设置环境变量
```

#### 法二：配置文件启动

启动配置文件：

```bash
mkdir /var/www/html/flask_test/gunicorn
cd /var/www/html/flask_test/gunicorn
vim gunicorn_conf.py
```

Python配置文件：

```python
import multiprocessing
bind='0.0.0.0:9100'
workers=multiprocessing.cpu_count()*2+1
reload=True
loglevel='info'
timeout=600
log_path="/tmp/logs/flask_test"
accesslog=log_path+'/gunicorn.access.log'
errorlog=log_path+'/gunicorn.error.log'
```

终止并加载配置文件启动：

```bash
pkill gunicorn
gunicorn -c
```

### Nginx部署

#### 安装

```bash
sudo apt-get install nginx #安装后默认开启服务
```

#### 基本命令

```bash
nginx -s <signal>
#signal:
#stop 急停
#quit 关闭
#reload 重新加载配置文件 如果语法不正确则回滚变化
#reopen 重新打开日志文件
```

#### 静态文件配置

进入`/etc/nginx/sites-enabled`目录，该目录下所有文件都会被作为配置文件被加载进来。创建文件`demo`。

```
server{
	location / {
		root /var/www/html
	}
	location /images/ {
		root /var/www/html/images
	}
}
```

例如访问`http://localhost/welcome.html`即为访问`/var/www/html/welcome.html`。

然后重新加载：

```bash
nginx -s reload
```

#### 代理服务器

新建配置文件：

```
server{
	listen 8000;
	listen [::]:8000;
	server_name 182.254.163.147;
	location / {
		proxy_pass http://182.254.163.147:9100;
		proxy_set_header Host $host;
		proxy_set_header X-Real-IP $remote_addr;
	}
}
```

### Supervisor部署

#### 基本操作

在`/home/ubuntu`下新建一个虚拟环境：

```bash
 virtualenv venv
 source venv/bin/activate
 pip install supervisor
 echo_supervisord_conf
 sudo su - root -c "echo_supervisord_conf > /etc/supervisor/supervisord.conf"
```

将`/etc/supervisor`下`supervisord.conf`编辑最后一行，以及其他位置作修改：

```ini
[include]
;files=relative/directory/*.ini
files=/etc/supervisor/conf.d/*.ini

[supervisorctl]
serverurl=unix://var/run/supervisor.sock

[unix_http_server]
file=/var/run/supervisor.sock

[supervisord]
logfile=/var/log/supervisord.log
pidfile=/var/run/supervisord.pid
```

进入`/etc/supervisor/conf.d`编辑`test.ini`：

```ini
[program:foo]
command=/bin/cat
```

启动supervisor：

```bash
sudo supervisord -c /etc/supervisor/supervisor.conf
sudo supervisorctl status #查看进程状态
```

其他常用supervisorctl命令：

```
status <name>
start <name>
stop <name>
stop all
restart <name>
restart all
reload 重启远程监督者
reread 重新加载守护程序的配置文件 无需添加删除
add <name>
remove <name>
update 重新加载配置并添加删除 重启受影响的程序
tail 输出最新log信息
shutdown 关闭supervisord
```

#### 守护Flask

`/etc/supervisor/conf.d`下新建配置文件`flask_test`：

 ```ini
 [program:flask_test]
 command=/var/www/html/flask_test/venv/bin/gunicorn -c gunicorn/gunicorn_conf.py run:app
 ;守护前cd到目录：
 directory=/var/www/html/flask_test
 user=root
 autostart=true
 autorestart=true
 ;延时启动，默认10：
 startsecs=10
 ;启动重试次数，默认3：
 startretries=3
 stdout_logfile=/var/log/flask_test_error.log
 stderr_logfile=/var/log/flask_test_out.log
 ;将停止信号发送到整个过程组 killasgroup为true
 stopasgroup=true
 ;停止信号
 stopsignal=QUIT
 ```

重启：

```bash
sudo supervisorctl reload
sudo supervisorctl status #查看进程状态
sudo pkill gunicorn #杀死进程后可自动重启
```

## Flask

### 基础

```python
from flask import Flask
app=Flask(__name__)
@app.route('/')
def index():
    return 'Hello World!'
if __name__=='__main__':
    app.run(debug=True,port=8000) #设置调试模式、端口
```

### 路由

```python
from flask import Flask
app=Flask(__name__)
@app.route('/')
def index():
    return 'Hello World!'
@app.route('/user/<username>')
def show_user_profile(usernname):
    return f'{username}'
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'{post_id}'
if __name__=='__main__':
    app.run()
```

### 构造URL

```python
from flask import Flask,url_for,redirect
app=Flask(__name__)
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'{post_id}'
@app.route('/')
def index():
    return redirect(url_for('show_post',post_id=2))
if __name__=='__main__':
    app.run()
```

### 渲染模板

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" href="/static/css/bootstrap.css">
        <script src="/static/js/jquery.js"></script>
        <script src="/static/js/bootstrap.js"></script>
    </head>
    <body>
        <nav class="navbar navbar-expand-sm bg-primary navbar-dark">
            <ul class="navbar-nav">
                <li class="nav-item active">
                    <a class="nav-link" href="#">首页</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">学员</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">图书</a>
                </li>
                <li class="nav-item dropdown">
                    <a class="nav-link dropdonw-toggle" href="#" id="navbardrop" data-toggle="dropdown">关于我们</a>
                    <div class="dropdown-menu">
                        <a class="dropdown-item" href="#">公司简介</a>
                        <a class="dropdown-item" href="#">企业文化</a>
                        <a class="dropdown-item" href="#">联系我们</a>
                    </div>
                </li>
            </ul>
        </nav>
        <div class="jumbotron">
            <h1 class="display-3">欢迎来到{{name}}</h1>
            <p>
                {{message}}
            </p>
            <hr class="my-4">
            <p>
                <a class="btn btn-primary btn-lg" href="#" role="button">了解更多</a>
            </p>
        </div>
    </body>
<html>
```

使用`render_template`渲染：

```python
from flask import Flask,url_for,redirect,render_template
app=Flask(__name__,template_folder='.')
@app.route('/')
def index():
    name="这是名字"
    message="""
        这是Message
    """
    return render_template("tmp.html",name=name,message=message)
if __name__=='__main__':
    app.run()
```

### 模板过滤器

#### 变量过滤器

```html
<p>{{mydict['key']}}</p>
<p>{{mylist[2]}}</p>
<p>{{mylist[myintvar]}}</p>
<p>{{myobj.somemethod()}}</p>
```

#### 内置过滤器

```html
<!--name会首字母大写，其他字母小写-->
<p>{{name|capitalize}}</p>
```

其他常见过滤器：

```
safe 渲染时不转义
capitalize
lower
upper
title
trim
striptags 删掉html标签
default(value,default_value=u'',boolean=False) 默认值 别名d
escape(s) 转义html 别名e
first(seq) 返回序列第一个元素
last(seq) 最后一个
length(object) 返回长度
random(seq) 序列中随机值
max(value,case_sensitive=False,attribute=None) 序列最大值
min(value,case_sensitive=False,attribute=None) 序列最小值
unique(value,case_sensitive=False,attribute=None) 不重复的值
wordcount(s) 单词数
tojson(value,indent=None) 变量值转json
truncate(s.length=255,killwords=False,end='...',leeway=None) 截断 length长度 killwords截断单词 end结尾符号
```

#### 自定义过滤器

**法一：**

```python
def count_length(arg):
    return len(arg)
app=Flask(__name__)
app.secret_key='xxx' #密钥
app.add_template_filter(count_length,'count_length')
```

模板：

```html
<div>全文共{{content|count_length}}</div>
```

**法二：**

```python
@app.template_filter()
def count_length(arg):
    return len(arg)
```

### 控制结构

```html
{% if user %}
Hello, {{user}}!
{% else %}
Hello, Stranger!
{% endif %}

<ul>
    {% for comment in comments %}
    <li>{{comment}}</li>
    {% endfor %}
</ul>
```

### Session

```python
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        if username=='xxx' and password=='xxx':
            session['username']=username
            session['logged_in']=True
            return redirect(url_for('index'))
    return render_template('login.html')
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))
```

HTML模板：

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>用户登录</title>
    </head>
    <body>
        {% if session['logged_in'] %}
            欢迎{{session['username']}}登录
        {% else %}
            请先登录
        {% endif %}
    </body>
</html>
```

### 模板继承

base.html父模板：

```html
{% include '_nav.html' %}
{% block content %}
{% endblock %}
```

index.html子模板：

```html
{% extends 'base.html' %}
{% block content %}
<!--内容-->
{% endblock %}
```

### 消息闪现

```python
from flask import Flask,request,render_template,redirect,url_for,flash
app=Flash(__name__)
app.secret_key='xxx'
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        if username=='xxx' and password=='xxx':
            flash('登录成功','success')
        else:
            flash('用户名或密码错误','error')
        return redirect(url_for('login'))
    return render_template('login.html')
if __name=='__main__':
    app.run()
```

HTML模板：

```html
<head>
    <style>
        .error{color:red}
        .success{color:blue}
    </style>
</head>
<body>
    <div style="padding:20px">
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                <ul class="flashes">
                    {% for category,message in messages %}
                        <li class="{{category}}">{{message}}</li>
                    {% endfor %}
                </ul>
            {% endif %}
        {% endwith %}
    </div>
</body>
```

### 自定义错误页面

```python
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404h
```

