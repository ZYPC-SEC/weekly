---
title: Python-Django实战
date: 2023-12-11 19:18:32
tags:Django
mathjax: true
---

# Python-Django实战

## 部署

### 安装

```bash
pip install Django
```

###  创建项目

```bash
django-admin startproject blog #blog为项目名
python manage.py runserver
```

### 创建应用

```bash
python manage.py startapp article #article为应用名
```

在`blog/settings.py`中`INSTALLED_APPS`字段中加入`'article.apps.ArticalConfig'`。

## 数据模型

### 添加数据模型

在`article/models.py`文件创建模型类：

```python
from django.db import models
class User(models.Model):
    id=models.IntegerField(primary_key=True) #主键
    username=models.CharField(max_length=30)
    #...
class Article(models.Model):
    content=models.TextField(verbose_name='内容')
    publish_date=models.DateTimeField()
    user=models.ForeignKey(User,on_delete=models.CASCADE) #一用户对多文章
    def __repr__(self):
        return Article.title
    def short_content(self):
        return self.content[:50]
    short_content.short_description='content' #XREF:class ArticleAdmin
```

### 数据库迁移

默认SQLite，如果要改为MySQL，需要修改`blog\settings.py`的`DATABASES`字段：

```python
DATABASES={
    'default':{
        'ENGINE':'django.db.backends.mysql',
        'NAME':'xxx', #数据库名
        'USER':'root', #用户名
        'PASSWORD':'root' #密码
    }
}
```

进入数据库：

```bash
mysql -u root -p
```

创建库：

```sql
create database xxx default character set utf8;
```

安装MySQL驱动：

```bash 
pip install pymysql
```

在`blog\blog\__init__.py`文件行首添加代码：

```python
import pymysql
pymysql.version_info(1,3,13,"final",0)#设置mysqlclient版本
pymysql.install_as_MySQLdb()
```

创建数据表，生成迁移文件：

```bash
python manage.py makemigrations
```

迁移数据库：

```bash
python manage.py migrate
```

### 数据API

#### 导入数据模型

进入命令行：

```bash
python manage.py shell
```

以下代码均在命令行中执行。

导入数据模型：

```python
from article.models import User,Article
```

#### 添加数据

```python
#法一
user1=User.objects.create(id=1,username="andy",email="xxx")
user2=User(id=2,username="zhangshan",email="xxx")

#法二
user2.save()
```

#### 查询数据

```python
users=User.objects.all()
for user in users:
    print(f'{user.id},{user.username}')
    
#其他命令：
User.objects.first() #获取第一个记录
Person.objects.get(id=1)
User.objects.filter(username__exact='andy')
User.objects.filter(username__iexact='andy') #不区分大小写
User.objects.filter(id__gt=1) #>1
User.objects.filter(id__lt=100) #<100
User.objects.filter(username__contains='n').order_by('id')
User.objects.filter(username__icontains='n')
```

#### 修改数据

```python
user=User.objects.get(id=1)
user.username='xxx'
user.save()
```

#### 删除数据

```python
User.objects.get(id=1).delete()
```

## 管理后台

### 创建管理后台

执行命令：

```bash
python manage.py createsuperuser
```

在`article/admin.py`配置文件中创建后台控制模型类，并绑定到管理后台，添加以下代码：

```python
from article import User,Article
class UserAdmin(admin.ModelAdmin):
    list_display=('username','email') #列表展示
    list_filter=('username','email') #右侧过滤框查询字段
    search_fields=(['username','email']) #右侧搜索框可搜索的字段
def upper_case_name(obj):
    return ("%s %s"%(obj.id,obj.title)).upper()
class PubblishYearFilter(admin.SimpleListFilter):
    title=_("发布年份") #可读标题
    parameter_name='year' #用于url查询的参数
    def lookups(self,request,model_admin):
        return(
            ('2020',_('2020年')),
            ('2019',_('2019年')),
        ) #第一元给queryset 第二元可读
    def queryset(self,request,queryset):
        if self.value()=='2019':
            return queryset.filter(publish_date__gte=date(2019,1,1),puslish_date__lte=date(2019,12,31))
        if self.value()=='2020':
            return queryset.filter(publish_date__gte=date(2020,1,1),publish_date__lte=date(2020,12,31))
class ArticleAdmin(admin.ModelAdmin):
    list_display=('title','content','publish_date','short_content') #XREF:class Article
    list_display_link=('id','title') #要连接到页面的字段名
    list_editable=('title','publish_date') #可修改的字段名
    list_filter=('title',PublishYearFilter) #过滤查询字段
    
    #写法一：
    list_display=(upper_case_name,)
    #写法二：
    list_display=('upper_case_name',)
    def upper_case_name(self,obj):
        return ("%s %s"%(obj.id,obj.title)).upper()
    upper_case_name.short_description='Name'

    list_filter=('title','user__username') #可跨表，用__连接
    search_fields=('title',)
    fields=(('id','title'),'content','publish_date') #定义添加数据时要显示的字段 id和title在同一行
    fieldset=(
        ('Main',{
            'fields':('id','title','publish_date') #Main组内拥有的字段
        }),
        ('Advance',{
            'classes':('collapse',), #collapse为默认折叠 wide水平更宽
            'fields':('content',),
        })
    )
admin.site.register(User,UserAdmin)
admin.site.register(Article,ArticleAdmin)
```

## 路由

### 格式转换类型

```
str 除/以外的非空字符
int 0和正整数
slug 字母数字-_
uuid 
path 非空 包括路径分隔符 全集
```

### 定义并创建路由

在`blog/urls.py`中添加：

```python
from django.urls import re_path,include
from . import views
urlpatterns=[
    path('admin/',admin.site.urls),
    path('articles/',views.article_list), #http://127.0.0.1:8000/articles/
    path('articles/<int:year>/',views.year_archive), #http://127.0.0.1:8000/articles/2020/
    path('articles/<int:year>/<int:month>/',views.month_archive), #http://127.0.0.1:8000/articles/2020/05
    path('articles/<int:year>/<int:month>/<slug:slug>/',views.article_detail) #http://127.0.0.1:8000/articles/2020/05/python
    #正则写法：?P<name>pattern
    re_path(r'^articles/(?P<year>[0-9]{4})/(?<month>[0-9]{2})/(?P<slug>[\w-]+)/$',views.article_detail)
    #include写法：
    path('articles/',include('article.urls'))
]
```

再创建`views.py`：

```python
from django.http import HttpResponse
def article_list(request):
    return HttpResponse('xxx')
def year_archive(request,year):
    return HttpResponse(f'{year}')
def month_archive(request,year,month):
    return HttpResponse(f'{year},{month}')
def article_detail(request,year,month,slug):
    return HttpResponse(f'{year},{month},{slug}')
```

如果使用上述include写法，需要新建`article/urls.py` ：

```python
from django.urls import path
from . import views
urlpatterns=[
    path('',views.article_list),
    path('<int:year>/<int:month>/<slug:slug>/',views.article_detail)
]
```

还要目录下新建`views.py`：

```python
from django.http import HttpResponse
def article_list(request):
    return HttpResponse('xxx')
def article_details(request,year,month,slug):
    return HttpResponse(f'{year},{month},{slug}')
```

## 视图

### FBV

接上话使用include定义路由，并在`article/urls.py` 中添加：

```python
urlpatterns=[
    path('current',views.get_current_datetime)
]
```

并在`article/views.py`中：

```python
from datetime import datetime
def get_current_datetime(request):
    today=datetime.today()
    formatted_today=today.strftime("%Y-%m-%d")
    html=f"<html><body>今天是{formatted_today}</body></html>"
    return HttpResponse(html)
```

### CBV

```python
from django.views import View
class ArticleForm(View):
    def get(self,request,*args,*kwargs):
        return HttpResponse('xxx') #收到get请求自动调用
    def post(self,request,*args,**kwargs):
        return HttpResponse('xxx') #收到post请求自动调用
```

## 模板

### 创建并渲染

渲染模板：

```python
from django.shortcuts import render
from article.models import Article,User
def article_list(request):
    articles=Article.objects.all()
    return render(request,'article_list.html',{'article':article})
```

新建目录`blog\article\templates`，新建`base.html`作为模板：

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>
            {% block title %}
            {% endblock %}
        </title>
        {% load static %}
        <link rel="stylesheet" type="text/css" href="{% static 'css/bootstrap.css' %}">
        <script src="{% static 'js/jquery.js' %}"></script>
        <script src="{% static 'js/bootstrap.js' %}"></script>
    </head>
    <body class="container">
        <nav class="navbar navbar-expand-sm bg-primary navbar-dark">
            <!--省略-->
        </nav>
        {% block content %}
        {% endblock %}
    </body>
</html>
```

创建`article_list.html`作为子模板：

```html
{% extends "base.html" %}
{% block tite %}
    文章列表
{% endblock %}
{% block content %}
    <div style="margin-top:20px">
        <h3>文章列表</h3>
        <table class="table table-bordered">
            <thead>
                <tr>
                    <th>文章ID</th>
                    <th>作者</th>
                    <th>标题</th>
                    <th>发布时间</th>
                </tr>
            </thead>
            <tbody>
                {% for article in articles %}
                    <tr>
                        <td>{{article.id}}</td>
                        <td>{{article.user.username}}</td>
                        <td>{{article.title}}</td>
                        <td>{{article.publish_date|date:'Y-m-d'}}</td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
{% endblock %}
```

其他过滤器：

```
{{value|default:"nothing"}} 指定默认值
{{value|length}} 列表或字符串长度
{{value|lower}} 变为小写字母
{{value|date}} 日期格式转换为字符串格式
{{value|safe}} 不转义
{{value|filesizeformat}} 人类可读文件大小
{{value|truncatewords:30}} 取固定长度
```

## 表单

创建表单类，该类会呈现为HTML代码：

```python
from django import forms
class LoginForm(forms.Form):
    username=forms.CharField(
        label='姓名',
        required=True,
        min_length=3,
        max_length=10,
        widget=forms.TextInput(attrs={'class':'form-control'}),
        error_message={
            'required':'用户名不能为空',
            'min_length':'长度不能小于5个字符',
            'max_length':'长度不能超过10个字符',
        }
    )
    email=forms.CharField(
        label='邮箱',
        required=True,
        max_length=50,
        widget=forms.Textinput(attrs={'class':'form-control'}),
        error_message={
            'required':'邮箱不能为空',
            'max_length':'长度不能超过50个字符',
        }
    )
```

在`article\urls.py`中创建路由：

```python
from django.urls import path
from . import views
urlpatterns=[
    path('login',views.LoginFormView.as_view())
]
```

在`article\views.py`中添加视图函数：

```python
class LoginFormView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'login.html',{'form':LoginForm()})
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POS #如果输入合法
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            return HttpResponse(f'{username},{email}') #登陆成功界面
        else:
            return render(request,'login.html',{'form':form}) #登录不成功，返回登录界面并显示错误，信息为form
```

在`article\templates`下创建模板`login.html`文件：

```html
{% extends "base.html" %}
{% block title %}
    登录页面
{% endblock %}
<style type="text/css">
    .errorlist{
        color:red
    }
</style>
<div class="container" style="margin-top:50px">
    <form action="" method="post">
        {% csrf_token %}
        <div class="form-group">
            <label>{{form.username.label}}</label>
            {{form.username}}
            {{form.username.errors}}
        </div>
        <div class="form-group">
            <label>{{form.email.label}}</label>
            {{form.email}}
            {{form.email.errors}}
        </div>
        <button type="submit" class="btn btn-primary">提交</button>
    </form>
</div>
{% endblock %}
```

## Session会话

### 启用

默认开启，删除方法：在`settings.py`中删除MIDDLEWARE中SessionMiddleware，从INSTALLED_APPS中删除django.contrib.sessions。

### 常用引擎

```python
request.session['key']=123 #设置或更新
request.session.setdefault('key',123) #存在则不设置
a=request.session['key'] #获取指定key
a=request.session.get('key',None) #如果不存在返回None
a=request.session.pop('key') #弹出删除
del request.session['key'] #删除
request.session.delete("session_key") #删除当前用户所有数据
request.session.clear() #清除用户数据
request.session.flush() #删除数据并删除对话cookie
a=request.session.session_key #获取用户Session的随机字符串
request.session.clear_expired() #删除失效日期小于当前日期的数据
a=request.session.exists('session_key') #检查用户Session随机字符串在数据库中是否存在
a=request.session.keys() #获取所有键
a=request.session.values() #获取所有值
a=request.session.items() #获取所有键值对
a=request.session.iterkeys() #获取所有键的可迭代对象
a=request.session.itervalues() #获取所有值的可迭代对象
a=request.session.iteritems() #获取所有键值对的可迭代对象
request.session.set_expiry(value) #设置Session过期时间
"""
	value参数说明：
		整数：这些秒数后失效
		datatime或timedelta：这个时间后失效
		0 关闭浏览器失效
		None 依赖全局失效策略
"""
```

### 实现登录

进入shell：

```bash
python manage.py shell
```

创建用户：

```python
from django.contrib.auth.models import User
User.objects.create_user(username='andy',password='xxx')
```

验证用户名和密码是否正确：

```python
from django.contrib.auth import authenticate
user=authenticate(username='andy',password='xxx') #如果都正确返回User对象，不正确返回None
```

实现用户登录表单`blog\article\forms.py`：

```python
class LoginForm(forms.Form):
    username=forms.CharField(
        label='姓名',
        required=True,
        min_length=3,
        max_length=10,
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':"请输入用户名"
        }),
        error_message={
            'required':'用户名不能为空',
            'min_length':'长度不能小于3个字符',
            'max_length':'长度不能超过10个字符',
        }
    )
    password=forms.CharField(
        label='密码',
        required=True,
        min_length=6,
        max_length=50,
        widget=forms.passwordInput(attrs={
            'class':'form-control mb-0',
            'placeholder':"请输入密码"
        }),
        error_message={
            'required':'用户名不能为空',
            'min_length':'长度不能少于6个字符',
            'max_length':'长度不能超过50个字符',
        }
    )
```

修改路由，略。

打开`blog\article\views.py`，添加代码：

```python
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.http import HttpResponseRedirect
class LoginFormView(View):
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/articles')
            else:
                message.add_message(request,messages.WARNING,'用户名和密码不匹配')
        return render(request,'login.html',{'form':form})
```

模板文件`blog\article\templates\login.html`：

```html
<div class="container" style="margin-top:50px">
    {% if messages %}
        {% for message in messages %}
            <div class="alert alert-{{message.tags}} alert-dismissible fade show" role="alert">
                <strong>{{message}}</strong>
                <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
        {% endfor %}
    {% endif %}
    <form action="" method="post">
        {% csrf_token %}
        <div class="form-group">
            <label>{{form.username.label}}:</label>
            {{form.username}}
            {{form.username.errors}}
        </div>
        <div class="form-group">
            <label>{{form.password.label}}</label>
            {{form.password}}
            {{form.password.errors}}
        </div>
        <button type="submit" class="btn btn-primary">提交</button>
    </form>
</div>
```

退出登录，创建路由：

```python
urlpatterns=[
    path('logout',view.logout),
]
```

在`blog\article\views.py`中创建`logout`函数：

```python
from django.contrib.auth import authenticate,login,logout as django_logout
def logout(request):
    django_logout(request)
    return HttpResponseRedirect('/login')
```

验证用户是否登录，如果登录，则可以访问`article`：

```python
from django.contrib.auth.decorators import login_required
@login_required
def article_list(request):
    articles=Article.objects.all()
    return render(request,'article_list.html'{'article':articles})
```

如果没有登录，会跳转到404，可在`blog\blog\settings.py`中设置跳转路径：

```python
LOGIN_URL='/articles/login'
```

