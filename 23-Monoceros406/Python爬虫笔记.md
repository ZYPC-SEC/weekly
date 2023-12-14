---
title: Python爬虫笔记
date: 2023-10-15 21:06:24
tags: 爬虫
mathjax: true
---

# Python爬虫笔记

## urllib

### GET请求

```python
import urllib.request
url='https://...'
response=urllib.request.urlopen(url=url)
response.status #返回请求码 200
response.getheaders() #返回响应头信息
    [('Connection','close'),('Content-Length','48955'),('Server','nginx'),...]
response.read().decode('utf-8') #返回HTML代码
```

### POST请求

```python
import urllib.request
import urllib.parse
url='...'
data=bytes(urllib.parse.urlencode({'hello':'python'}),encoding='utf-8')
response=urllib.request.urlopen(url=url,data=data)
print(response.read(),decode('utf-8')) #读取HTML
```

### timeout参数

```python
import urllib.request
import urllib.error
import socket
url='...'
try:
    response=urllib.request.urlopen(url=url,timeout=0.1)
    ...
except urllib.error.URLError as error:
    if isinstance(error.reason,socket.timeout):
        #超时
```

### 设置请求头

```python
import urllib.request
import urllib.parse
url='...'
headers={'User-Agent':'Mozilla/5.0 ...'}
data=bytes(urllib.parse.urlencode({'hello':'python'}),encoding='utf-8') #POST
r=urllib.request.Request(url=url,data=data,headers=headers,method='POST')
response=urllib.request.urlopen(r)
print(response.read().decode('utf-8'))
```

### 获取cookie

```python
import urllib.request
import urllib.parse
import urllib.cookiejar
import json
url='...'
data=bytes(urllib.parse.urlencode({'username':'mrsoft','password':'mrsoft'}),encoding='utf-8')
cookie_file='cookie.txt'
cookie=http.cookiejar.LWPCookieJar(cookie_file)
cookie=http.cookiejar.CookieJar()
cookie_processor=urllib.request.HTTPCookieProcessor(cookie)
cookie.load(cookie_file,ignore_expires=True,ignore_discard=True)
opener=urllib.request.build_opener(cookie_processor)
response=opener.open(url,data=data)
response=json.loads(response.read().decode('utf-8'))['msg']
if response=='登录成功！':
    for i in cookie:
        print(i.name+'='+i.value)
```

### 设置代理IP

```python
import urllib.request
url="..."
proxy_handler=urllib.request.ProxyHandler({'https':'58.220.95.114:10053'})
opener=urllib.request.build_opener(proxy_handler)
response=opener.open(url,timeout=2)
print(response.read().decode('utf-8'))
```

### 异常处理

```python
import urllib.request
import urllib.error
try:
    response=urllib.request.urlopen('...')
except urllib.error.HTTPError as error:
    print(error.code)#状态码
    print(error.reason)#Not Found
    print(error.headers)#请求头
except urllib.error.URLError as error:
    print(error.reason)
```

### 解析链接

#### 拆分url

```python
import urllib.parse
parse_result=urllib.parse.urlparse('https://doc.python.org/3/library/urllib.parse.html')
print(parse_result.scheme)#https
print(parse_result.netloc)#docs.python.org
print(parse_result.path)#/3/library/urllib.parse.html
print(parse_result.params)#参数
print(parse_result.query)#查询条件
print(parse_result.fragment)#片段标识符
```

#### 组合url

```python
import urllib.parse
list_url=['https','docs.python.org','/3/library/urllib.parse.html','','','']
tuple_url=('https','docs.python.org','/3/library/urllib.parse.html','','','')
dict_url={'scheme':'https','netloc':'docs.python.org','path':'/3/library/urllib.parse.html','params':'','query':'','fragment':''}
print(urllib.parse.urlunparse(list_url))#相同方法
print(urllib.parse.urlunparse(tuple_url))
print(urllib.parse.urlunparse(dict_url))
```

#### 连接url

```python
import urllib.parse
base_url='...'
print(urllib.parse.urljoin(base_url,'../../ *.html'))#如果第二个参数为完整url，直接反应对应的值
```

#### url编码解码

```python
import urllib.parse
params={'name':'Jack','country':'中国','age':30}
print(urllib.parse.urlencode(params))#name=...&country=...&age=...
print(urllib.parse.quote('中国'))#直接编码
print(urllib.parse.unquote(u))#解码
```

#### 参数转为字典类型

```python
import urllib.parse
url=''
q=urllib.parse.urlsplit(url).query
q_dict=urllib.parse.parse_qs(q)
```

#### 参数转为列表类型

```python
import urllib.parse
str_params='...'
list_params=urllib.parse.parse_qsl(str_params)
```

## urllib3

### GET

```python
import urllib3
urllib3.disable_warnings()#关闭ssl警告
url1='...'
url2='...'
http=urllib3.PoolManager()
r1=http.request('GET',url1)
r2=http.request('GET',url2)
```

### POST

```python
import urllib3
urllib3.disable_warnings()
url='...'
params={'':'',...}
http=urllib3.PoolManager()
r=http.request('POST',url,fields=params)
print(r.data.decode('utf-8'))
print(r.data.decode('unicode_escape'))#中文
```

### 重试请求

```python
#...
r=http.request('POST',url)#默认3次
r=http.request('POST',url,retries=5)#重试5次
r=http.request('POST',url,retries=False)#关闭重试
#...
```

### 获取响应头

```python
response_header=r.info()
for key in response_header.keys():
    print(key,':',response_header.get(key))
```

### json信息

```python
j=json.loads(r.data.decode('unicode_escape'))
print(j.get('...'))
print(j.get('...').get('...'))
```

### 二进制数据

```python
r=http.request('GET',url)
f=open('*.png','wb+')
f.write(r.data)
f.close()
```

### 设置请求头

```python
header={'User-Agent':'Mozilla/5.0 (Wind...'}
r=http.request('GET',url,headers=headers)
```

### 设置超时

```python
r=http.request('GET',url,timeout=0.01)
###
import urllib3
from urllib3 import timeout
urllib3.disable_warnings()
timeout=Timeout(connect=0.5,read=0.1)
http=urllib3.PoolManager(timeout=timeout)
http.request('GET','http://...')
#或
http=urllib3.PoolManager()
http.request('GET','...',timeout=timeout)
```

### 设置代理

```python
import urllib3
url='...'
headers={'User-Agent':'...'}
proxy=urllib3.ProxyManager('http://...:80',headers=headers)
r=proxy.request('get',url,timeout=2.0)
print(r.data.decode())
```

### 上传文件

#### fields上传

```python
import urllib3
with open('text.txt') as f:
    data=f.read()
http=urllib3.PoolManager()
r=http.request('POST','...',fields={'filefield':('example.txt',data),})
```

#### body上传

```python
import urllib3
with open('*.jpg','rb') as f:
    data=f.read()
http=urllib3.PoolManager()
r=http.request('POST','...',body=data,headers={'Content-Type':'image/jpeg'})
```

## request

### GET

```python
import requests
response=requests.get('...')
print(response.status_code)
print(response.url)
print(response.headers)
print(response.cookies)
```

### 对响应结果编码

```python
response.encoding='utf-8'
print(response.text)
```

### 爬取二进制数据

```python
import requests
response=requests.get('.../*.png')
with open("*.png",'wb') as f:
    f.write(response.content)
```

### GET请求

```python
import requests
data={'name':'Micheal',...}
response=requests.get('...',params=data)
response__dict=json.loads(response.text)
```

### POST请求

```python
import requests
data={'1':'...',...}
response=requests.post('...',data=data)
#...
```

### 元组、列表、字典转json

```python
data=...
data=json.dumps(data)
```

### 添加headers

```python
import requests
url=''
headers={'User-Agent':'...'}
response=requests.get(url,headers=headers)
print(response.status_code)
```

### 验证cookies

```python
import requests
from lxml import etree
cookies='...'
headers={
    'Host':'...',
    ...
};
cookies_jar=requests.cookies.RequestsCookieJar()
for cookie in cookies.split(';'):
    key,value=cookie.split('=',1)
    cookies_jars.set(key,value)
response=requests.get('https://...',headers=headers,cookies=cookies_jar)
if response.status_code==200:
    html=etree.HTML(response.text)
    name=html.xpath('//*[@id="db-global-nav"]/div/div[1]/ul/li[2]/a/span[1]/text()')
    print(name[0]) #输出账号
```

### 会话请求

相当于再开一个选项卡，一个负责登录，一个负责获取登录后数据

```python
import requests
s=requests.Session()
data={'username':'...','password':'...'}#登录信息
response=s.post('http://.../chklogin.html',data=data)
response2=s.get('http://...')
print(response.text,response2.text)
```

### 验证请求

```python
import requests
from requests.auth import HTTPBasicAuth
url='...'
ah=HTTPBasicAuth('username','password')
response=requests.get(url=url,auth=ah)
if response.status_code==200:
    print(response.text)
```

### 设置超时

```python
import requests
try:
    response=requests.get('...',timeout=0.1)
    ...
except Exception as e:
    print(str(e))
```

### 识别异常

```python
import requests
from requests.exceptions import ReadTimeout,HTTPError,RequestException
try:
    response=requests.get('...',timeout=0.1)
    print(response.status_code)
except ReadTimeout: #超时异常
    ...
except HTTPError: #HTTP异常
    ...
except RequestException: #请求异常
    ...
```

### 上传文件

```python
import requests
bd=open('*.png','rb')
file={'file':bd}
response=requests.post('...',files=file)
print(response.text)
```

### 设置代理

```python
import requests
headers={'User-Agent':'Mozilla'
                      '...'}
proxy={'http':'http://*.*.*.*:3000',
       'https':'...'}
try:
    response-requests.get('http://...',headers=headers,proxies=proxy,verify=False,timeout=3)
    print(response.status_code)
except Exception as e:
    print(e)
```

### 获取免费代理IP

```python
import requests
from lxml import etree
import pandas as pd
ip_list=[]
def get_ip(url,headers):
    response=requests.get(url,headers=headers)
    response.encoding='utf-8'
    if response.status_code==200:
        html=etree.HTML(response.text)
        li_all=html.xpath('//li[@class="f-list col-lg-12 col-md-12 col-sm-12 col-xs-12"]')
        for i in li_all:
            ip=i.xpath('span[@class="f-address"]/text()')[0]
            port=i.xpath('span[@class=f-address]/text()')[0]
            ip_list.append(ip+':'+port)
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                      'AppleWebkit/537.36 (KHTML, like Gecko)'
                      'Chrome/72.0.3626.121 Safari/537.36'}
if __name__=='__main__':
    ip_table=pd.DataFrame(columns=['ip'])
    for i in range(1,5):
        url='https://.../{page}.html'.format(page=i)
        get_ip(url,headers)
    ip_table['ip']=ip_list
    ip_table.to_excel('ip.xlsx',sheet_name='data')
```

### 检测代理IP是否有效

```python
import requests
import pandas
from lxml import etree
ip_table=pandas.read_excel('ip.xlsx')
ip=ip_table['ip']
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                      'AppleWebkit/537.36 (KHTML, like Gecko)'
                      'Chrome/72.0.3626.121 Safari/537.36'}
for i in ip:
    proxies={'http':'http://{ip}'.format(ip=i),
             'https':'https://{ip}'.format(ip=i)}
    try:
        response=requests.get('http://202020.ip138.com/',headers=headers.proxies=proxies,timeout=2)
        if response.status_code==200:
            response.encoding='utf-8'
            html=etree.HTML(response.text)
            info=html.xpath('/html/body/p[1]//text()')
            print(info) #\r\n您的iP地址是：[*.*.*.*] 来自：*省*市 ***（运营公司）\r\n
    except Exception as e:
        pass
```

## requests_cache

### 打印当前版本

```python
import requests_cache
version=requests_cache.__version__
print(version)
```

### 缓存设置

```python
"""
    install_cache(cache_name='cache',backend=None,expire_after=None,allowable_codes=(200,),allowable_methods=('GET',),session_factory=<class 'requests_cache.core.CacheSession'>,**backend_options)
        cache_name 缓存文件名 默认cache
        backend 储存机制 默认None 默认使用sqlite储存
            memory 内存
            sqlite
            mongo
            redis
        expire_after 缓存有效时间 默认None 永久有效
        allowable_codes 设置状态码 默认200
        allowable_methods 设置请求方式 默认GET 表示只有GET请求才可以生成缓存
        session_factory 设置缓存执行的对象 需要实现CachedSession类
        **backend_options 如果存储方式为sqlite、mongo、redis 则设置连接方式
"""
import requests_cache
import requests
requests_cache.install_cache()
requests_cache.clear()
url='...'
r=requests.get(url)
print(r.from_cache) #False不存在缓存
r=requests.get(url)
print(r.from_cache) #True存在缓存
```

### 缓存应用

```python
import requests_cache
import time
requests_cache.install_cache()
requests_cache.clear()
def make_throttle_hook(timeout=0.1):
    def hook(response,*args,**kwargs):
        print(response.text)
        if not getattr(response,'from_cache',False):
            time.sleep(timeout) #等待2秒
        else:
            print(response.from_cache) #存在缓存
        return response
    return hook
if __name__=='__main__':
    requests_cache.install_cache()
    requests_cache.clear()
    s=requests_cache.CachedSession()
    s.hooks={'response':make_throttle_hook(2)} #配置钩子函数
    s.get('http://...') #不存在缓存
    s.get('http://...') #存在缓存
```

## requests-html

### get()请求

```python
from requests_html import HTMLSession
session=HTMLSession()
url='http://...'
r=session.get(url)
print(r.html)
```

### post()请求

```python
data={
    'user':'admin',
    'password':123456
}
r=session.post('http://...',data=data)
if r.status_code==200:
    print(r.text)
```

### 随机请求头

```python
from requests_html import UserAgent,HTMLSession
session=HTMLSession()
ua=UserAgent().random
r=session.get('http://...',headers={'user-agent':ua})
if r.status_code==200:
    print(r.text)
```

### 爬取新闻

```python
from requests_html import HTMLSession,UserAgent
session=HTMLSession()
ua=UserAgent().random
r=session.get('http://...',headers={'user-agent':ua})
r.encoding='gb2312'
if r.status_code==200:
    li_all=r.html.xpath('.//ul[@class="tj3_1"]/li')
    for li in li_all:
        news_title=li.find('a')[0].text
        new_href='http://'+li.find('a[href]')[0].attrs.get('href').lstrip('.')
        news_time=li.find('font')[0].text
        #...
```

### find()方法

```python
li_all=html.find('li',containing='新冠病毒')
```

### search()方法

```python
for li in r.html.find('li',containing='新冠病毒'):
    a=li.search('<a href="{}">{}</a>')
    news_title=a[1]
    news_href='http://...'+a[0]
    news_time=li.search('<font>{}</font>')[0]
```

### search_all()方法

```python
import re
class_tj3_1=r.html.xpath('.//ul[@class="tj3_1"]')
li_all=class_tj3_1[0].search_all('<li>{}</li>')
for li  in li_all:
    if '新冠病毒' in li[0]:
        a=re.findall('<font>(.*?)</font><a href="(.*?)">(.*?)</a>',li[0])
        news_title=a[0][2]
        news_href='http://...'+a[0][1]
        news_time=a[0][0]
```

## 正则表达式

```python
import re
match=re.search('模式字符串','匹配字符串',re.I) #re.I 可选 不区分大小写
```

```
(\d?)+ 多个数字可有可无
\s 空格
([\u4e00-\u9fa5]?)+ 多个汉字可有可无
\b 匹配字符串开头处、结尾处、空格、标点符号、换行
.*(\d+) 贪婪匹配
```

## 视频下载

```python
video_response=requests.get(url=video_url,headers=headers)
data=video_response.content
file=open('*.mp4','wb')
file.write(data)
file.close()
```

## XPath解析

### parse()方法-解析HTML文件

```python
from lxml import etree
parser=etree.HTMLParser()
html=etree.parse('demo.html',parser=parser)
html_txt=etree.toString(html,encoding='utf-8')
print(html_txt.decode('utf-8'))
```

### HTML()方法-解析字符串型HTML代码

```python
from lxml import etree
html_str="""
            ...
         """
html=etree.HTML(html_str)
html_txt=etree.toString(html,encoding='utf-8')
print(html_txt.decode('utf-8'))
```

### 解析HTML代码

```python
from lxml import etree
import requests
from requests.auth import HTTPBasicAuth
url='http://...'
ah=HTTPBasicAuth('admin','admin') #用户名密码
response=requests.get(url=url,auth=ah)
if response.status_code==200:
    html=etree.HTML(response.text)
    html_txt=etree.tostring(html,encoding='utf-8')
    print(html_txt.decode('utf-8'))
```

### 获取节点

```python
#获取所有节点
from lxml import etree
html_str="""
            ...
         """
html=etree.HTML(html_str)
node_add=html.xpath('//*')
print([i.tag for i in node_all])
#获取所有"li"节点
li_all=html.xpath('//li')
#获取"li"节点的直接子节点
a_all=html.xpath('//li/a')
#获取"li"节点的子孙节点
a_all=html.xpath('//li//a')
#获取"a"节点的父节点
a_all_parent=html.xpath('//a/..')
a_all_parent=html.xpath('//a/parent::*')
```

### 获取节点文本信息

```python
html=etree.HTML(html_str)
a_text=html.xpath('//a/text()') #获取所有"a"节点的文本信息
print(a_text)
```

### 属性匹配

```python
div_one=html.xpath('//div[@class="level one"]/text()')
div_all=html.xpath('//div[contains(@class,"level")]/text()')
```

### 获取属性

```python
li_all=html.xpath('//div/li/a/@title')
print(li_all)
```

### 按序获取属性

```python
li=html.xpath('//div/li[last()]/a/@title') #最后一个
li=html.xpath('//div/li[position()=1]/a/@title') #第一个
li=html.xpath('//div/li[last()-1]/a/@title') #倒数第二个
li=html.xpath('//div/li[position()>1]/a/@title') #位置大于1
```

### 节点轴

```python
li=html.xpath('//li[2]/ancestor::*') #li[2]所有祖先节点名称
li=html.xpath('//li[2]/ancestor::body') #li[2]指定祖先节点名称
li=html.xpath('//li[2]/ancestor::*[@class="video_scroll"]') #li[2]指定属性的祖先节点名称
li=html.xpath('//li[2]/a/attribute::*') #li[2]所有属性值
li=html.xpath('//li[2]/child::*') #li[2]所有子节点名称
li=html.xpath('//li[2]/descendant::*') #li[2]所有子孙节点名称
li=html.xpath('//li[2]/following::*') #li[2]之后的所有节点名称
li=html.xpath('//li[2]/following-sibling::*') #li[2]之后所有同级节点名称
li=html.xpath('//li[2]/preceding::*') #li[2]之前所有节点名称
```

## Beautiful Soup

### 解析HTML代码

```python
from bs4 import BeautifulSoup
html_doc="""
            ...
         """
soup=BeautifulSoup(html_doc,features='lxml')
print(soup)
#从文件解析
soup=BeautifulSoup(open('index.html'),'lxml')
print(soup.prettify()) #格式化
```

### 获取节点

```python
#获取节点内容
print(soup.head)
print(soup.body)
print(soup.title)
print(soup.p) #只打印第一个节点
#获取节点名称
print(soup.head.name)
print(soup.body.name)
print(soup.title.name)
print(soup.p.name)
#获取节点属性
print(soup.meta.attrs) #返回字典
print(soup.link.attrs)
print(soup.div.attrs)
#获取节点文本内容
print(soup.title.string)
print(soup.h3.string)
```

### 关联获取

```python
#获取子节点
print(soup.head.contents) #列表形式
for i in soup.head.children: #可迭代对象形式
    print(i)
#获取孙节点
for i in soup.body.descendants:
    print(i)
#获取父节点
print(soup.title.parent) #打印父节点内容
for i in soup.title.parents:
    prnt(i.name) #从内向外打印，最后[document]代表整个HTML文档
#兄弟节点
print(soup.p.next_sibling)
print(soup.p.previous_sibling)
print(list(soup.p.next_siblings))
print(list(soup.p.previous_siblings))
```

### find()方法获取内容

```python
#name参数
print(soup.find_all(name='p')[0])
#attr参数
print(soup.find_all(attrs={'value':'1'}))
print(soup.find_all(class_='p-1'))
print(soup.find_all(value='3'))
#text参数
print(soup.find_all(text='...'))
print(soup.find_all(text=re.compile('...')))
#其他方法
find()
find_all()
find_parent()
find_parents()
find_next_sibling()
find_next_siblings()
find_previous_sibling()
find_previous_siblings()
find_next()
find_all_next()
find_previous()
find_all_previous()
```

### CSS选择器

```python
print(soup.select('p')) #打印所有p节点内容
print(soup.select('p')[1]) #打印所有p节点中第2个p节点
print(soup.select('html head title')) #打印逐层获取的title节点
print(soup.select('.test_2')) #打印类名为test_2对应的节点
print(soup.select('#class_1')) #打印id为class_1对应的节点
#其他方法
soup.select('div[class="test_1"]')[0].select('p')[0] #嵌套获取名为test_1对应div中第一个p节点
soup.select('p')[0]['value'] #获取p节点中第一个节点value属性对应的值
soup.select('p')[0].attrs['value']
soup.select('p')[0].get_text() #获取p中第一个节点内文本
soup.select('p')[0].string
soup.select('p')[1:] #获取p节点中第二个以后的p节点
soup.select('.p-1,.p-5') #获取class为p-1与p-5对应的节点
soup.select('a[href]') #获取存在href属性的节点
soup.select('p[value="1"]') #获取属性value="1"的p节点
#select_one()方法
soup.select_one('a') #获取a节点中第一个a节点内容
```

## 动态渲染信息

### Ajax

F5刷新网页，F12中找到“网络”，选择“XHR”，选择某请求后查看“相应”，追到JSON信息，解析即可。消息头中有“请求网址”。

```python
import requests,time,random,os,re
json_url='http://api.vc.bilibili.com/board/v1/ranking/top?page_size=10&next_offset={page}1&tag=...&platform=pc'
class Crawl():
    def __init__(self):
        self.headers={'User-Agent':'Mozilla/5.0 ...'}
    def get_json(self,json_url):
        response=requests.get(json_url,headers=self.headers)
        if response.status_code==200:
            return response.json()
        else:
            #获取JSON失败
    #视频批量下载：
    def download_video(self,video_url,titlename):
        response=requests.get(video_url,headers=self.headers,stream=True)
        if not os.path.exists('video'):
            os.mkdir('video')
        if response.status_code==200:
            with open('video/'+titilename_'.mp4','wb')as f:
                for data in resposne.iter_content(chunk_size=1024):
                    f.write(data)
                    f.flush()
                print('下载完毕')
        else:
            print('获取失败')
if __name__=='__main__':
    c=Crawl()
    for page in raneg(0,10):
        json=c.get_json(json_url.format(page=page))
        infos=json['data']['items']
        for info in infos:
            title=info['item']['description']
            video_url=info['item']['video_playurl']
            print(title,video_url)
        time.sleep(random.randint(3,6))
    comp=re.compile('[^A-Z^a-z^0-9^\u4e00-\u9fa5]') #只中英文、数字
    title=comp.sub('',titile) #其他替换为空
    c.download_video(video_url,title)
```

### selenium

Edge驱动安装方法：

去这里下载符合自己版本的驱动：https://developer.microsoft.com/zh-cn/microsoft-edge/tools/webdriver/，解压并设置为环境变量，改名为`MicrosoftWebDriver.exe`。

运行以下代码能打开百度就行：

```python
from selenium import webdriver
driver=webdriver.Edge()
driver.get("https://www.baidu.com")
```

以下代码以Chrome驱动为例：获取京东商品信息。

```python
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
try:
    chrome_options=webdriver.ChromeOptions()#加载驱动器参数对象
    prefs={"profile.managed_default_content_settings.images":2}#不加载图片
    chrome_options.add_experimental_option("prefs",prefs)
    chrome_options.add_argument('--headless')#无界面浏览器模式
    chrome_options.add_argument('--disable-gpu')
    driver=webdriver.Chrome(options=chrome_options,executeable_path='.../chromedriver.exe')#加载驱动
    driver.get('https://item.jd.com/12353915.html')#请求
    wait=WebDriverWait(driver,10)#等10秒
    wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"m-item-inner")))#等待加载class名称为m-item-inner的节点，该节点包含商品信息
    name_div=driver.find_element_by_css_selector('#name').find_elements_by_tag_name('div')#name节点中所有div节点
    summary_price=driver.find_element_by_id('summary-price')
    print(name_div[0].text.name_div[1].text,name_div[4].text,summary_price.text)#商品标题、宣传语、编著信息、价格信息
    driver.quit()#退出浏览器驱动
except Exception as e:
    print(e)
```

获取网页节点有两种方法：

**法一：**

> 获取多个节点时，在element后加s即可。

```python
driver.find_element_by_id()
driver.find_element_by_name()
driver.find_element_by_xpath()
driver.find_element_by_link_text()
driver.find_element_by_tag_name()
driver.find_element_by_class_name()
driver.find_element_by_css_selector()
```

**法二：**

```python
name_div=driver.find_element(By.ID,'name').find_element(By.TAG_NAME,'div')
print(name_div[0].text)
```

其他属性：

```
By.ID By.LINK_TEXT By.PARTIAL_LINK_TEXT By.NAME By.TAG_NAME By.CLASS_NAME By.CSS_SELECTOR By.XPATH
```

获取属性方法：

```python
href=driver.find_element(By.XPATH,'//*[@id="p-author"]/a[1]').get_attribute('href')
print(href)
```

## 进程与线程

### 线程创建

#### threading模块创建：

```python
import threading,time
def process():
    for i in range(3):
        time.sleep(1)
        print(threading.current_thread().name)
if __name__=='__main__':
    threads=[threading.Thread(target=process)for i in range(4)] #args、kwargs等参数详情Python笔记
    for t in threads:
        t.start()
    for t in threads:
        t.join()
```

#### Thread子类创建：

```python
import threading,time
class SubThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg=self.name+str(i)
            print(msg)
if __name__=='__main__':
    t1=SubThread()
    t2=SubThread()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
```

### 互斥锁

```python
from threading import Thread,Lock
import time
n=100
def task():
    global n
    mutex.acquire()#其他线程等待该线程release
    temp=n
    time.sleep(0.1)
    n=temp-1
    mutex.release()
if __name__=='__main__':
    mutex=Lock()
    t_l=[]
    for i in range(10):
        t=Thread(taret=task)
        t_l.append(t)
        t.start()
    for t in t_l:
        t.join()
```

### 线程间通信

使用Queue模块，Producer将数据加入Queue，Consumer从Queue中获取，有则取出，无则阻塞等待。

```python
from queue import Queue
import random,threading,time
class Producer(threading.Thread):
    def __init__(self,name,queue):
        threading.Thread.__init__(self,name=name)
        self.data=queue
    def run(self):
        for i in range(5):
            self.data.put(i)
            time.sleep(random.random())
class Consumer(threading.Thread):
    def __init__(self,name,queue):
        threading.Thread.__init__(self,name=name)
        self.data=queue
    def run(self):
        for i in range(5):
            val=self.data.get()
            time.sleep(random.random())
if __name__=='__main__':
    queue=Queue()
    producer=Producer('Producer',queue)
    consumer=Consumer('Consumer',queue)
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
```

### 进程创建

#### 使用multiprocessing模块创建：

```python
from multiprocessing import Process
import time,os
def child_1(interval):
    print(os.getpid(),os.getppid()) #子进程pid 父进程pid
    t_start=time.time()
    time.sleep(interval)
    t_end=time.time()
    print(os.getpid(),t_end-t_start)
def child_2(interval):
    print(os.getpid(),os.getppid())
    t_start=time.time()
    time.sleep(interval)
    t_end=time.time()
    print(os.getpid(),t_end-t_start)
if __name__=='__main__':
    print(os.getpid())
    p1=Process(target=child_1,args=(1,))
    p2=Process(target=child_2,name="xxx",args=(2,))
    p1.start()
    p2.start()
    print(p1.is_alive())
    print(p2.is_alive())
    print(p1.name,p1.pid,p2.name,p2.pid)
    p1.join()
```

常用方法、属性：

```python
is_alive() 判断是否还在执行
join([timeout]) 是否等待进程执行结束，或等待多少秒
start() 启动
run() 如果没有给定target参数，调用start方法时执行对象中的run方法
terminate() 不管任务完成是否，立即终止
```

#### 使用Process子类创建进程

```python
from multiprocessing import Process
import time,os
class SubProcess(Process): #继承Process
    def __init__(self,interval,name=''): #重写__init__
        Process.__init__(self)
        self.interval=interval
        if name:
            self.name=name
    def run(self): #重写run
        print(os.getpid(),os.getppid())
        t_start=time.time()
        time.sleep(self.interval)
        t_stop=time.time()
        print(os.getpid(),t_stop-t_start)
if __name__=='__main__':
    print(os.getpid())
    p1=SubProcess(interval=1,name='xxx')
    p2=SubProcess(interval=2)
    p1.start()
    p2.start()
    print(p1.is_alive(),p2.is_alive,p1.name,p1.pid,p2.name,p2.pid)
    p1.join()
    p2.join()
```

#### 使用进程池创建

```python
from multiprocessing import Pool
import os,time,random
def task(name):
    print('子进程%s:%s'%(os.getpid(),name))
    time.sleep(1)
if __name__=='__main__':
    print('%s'%os.getpid())
    p=Pool(3)
    for i in range(10):
        p.apply_async(task,args=(i,))
    print('等待所有子进程结束')
    p.close()
    p.join()
    print('所有子进程结束')
```

### 消息队列

```python
from multiprocessing import Process,Queue
import time
def write_task(q):
    if not q.full():
        for i in range(5):
            message='message'+str(i)
            q.put(message)
            print('write:%s'%message)
def read_task(q):
    time.sleep(1)
    while not q.empty():
        print('read:%s'%q.get(True,2)) #等2秒，没读到则抛出Queue.Empty异常
if __name__=='__main__':
    q=Queue()
    pw=Process(target=write_task,args=(q,))
    pr=Process(target=read_task,args(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.join()
```

常用方法：

```python
Queue.qsize() 返回包含的信息数量
Queue.empty() 队列为空返回True，否则False
Queue.full() 队列满了返回True，否则False
Queue.get([block[,timeout]]) 获取一条信息并删除
	当block为默认True时，程序被阻塞，知道读到消息。如果设置了timeout，则等待timeout无消息抛出Queue.Empty异常。
    当block为False时，如果队列为空，立即抛出Queue.Empty异常。
Queue.get_nowait()
Queue.put(item,[block[,timeout]]) 写入队列
	当没有空间可写时，等待腾出空间。机制同get，抛出Queue.Full异常。
```

### 实战

```python
import requests,re,time
from fake_useragent import UserAgent
from multiprocessing import Pool
from bs4 import BeautifulSoup
class Spider():
    def __init__(self):
        self.info_urls=[]
    def get_home(self,home_url):
        header=UserAgent().random
        home_response=requests.get(home_url,header)
        if home_response.status_code==200:
            home_response.encoding='gb2312'
            html=home_response.text
            details_urls=re.findall('<a href="(.*?)" class="ulink">',html)
            self.info_urls.extend(details_urls)
if __name__=='__main__':
    home_url=['http://www.ygdy8.net/html/gndy/dyzz/list_23_{}.html'.format(str(i))for i in range(1,11)]
    s=Spider()
    pool=Pool(processes=4)
    pool.map(s.get_home,home_url)
```

## 验证码识别

### 安装

Tesseract下载地址：https://github.com/UB-Mannheim/tesseract/wiki。默认安装，将\Tesseract-OCR\tessdata文件夹设为TESSDATA_PREFIX环境变量。安装tesseract模块：

```bash
pip install tesserocr
```

### 验证码图片下载

```python
import requests,urllib.request
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
header={'User-Agent':UserAgent().random}
url='http://xxx'
response=requests.get(url,header)
response.encoding='utf-8'
html=BeautifulSoup(response.text,"html.parser")
src=html.find('img').get('src')
img_url=url+src
urllib.request.urlretrieve(img_url,'code.png')
```

### 验证码识别

```python
import tesserocr
from PIL import Image
img=Image.open('*.jpg')

#常规识别
code=tesserocr.image_to_text(img)
print(code)

#灰度图片
img=img.conver('L')
code=tesserocr.image_to_text(img)
print(code)

#二值化处理
img=img.conver('L')
t=155 #阈值 可调
table=[]
for i in range(256):
    if i<t:
        table.append(0)
    else:
        table.append(1)
img=img.point(table,'1')
code=tesserocr.image_to_text(img)
print(code)
```

### 滑动拼图验证码

```python
from selenium import webdriver
import re
driver=webdriver.Chrome()
driver.get('http://xxx/')
swiper=driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/span[1]') #获取按钮滑块
action=webdriver.ActionChains(driver)
action.click_and_hold(swiper).perform()
action.move_by_offset(0,0).perform() #不滑动，不松手 不然无法获得left值
verify_style=driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[1]').get_attribute('style') #图形滑块
verified_style=driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]').get_attribute('style') #空缺滑块
verified_left=float(re.findall('left: (.*?)px;',verified_style)[0])
verify_left=float(re.findall('left: (.*?)px;',verify_style)[0])
action.move_by_offset(verified_left-verify_left,0) #向右滑动
action.release().perform()
```

