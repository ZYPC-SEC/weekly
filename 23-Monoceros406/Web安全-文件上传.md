---
title: Web安全-文件上传
date: 2023-12-02 14:29:36
tags: Web
mathjax: true
---

# Web安全-文件上传

## MIME类型

```
.html:text/html
.txt:text/plain
.pdf:application/pdf
.word:application/msword
.png:image/png
.gif:image/gif
.mpg .mpeg:video/mpeg
.avi:video/x-msvideo
```

## 黑名单绕过

```
后缀大小写绕过：.Php
空格绕过：.php 
点绕过：.php.（Windows系统文件名特性会自动去掉后缀名最后.）
::$DATA绕过：Windows下NTFS文件系统特性
Apache解析漏洞：解析文件从右往左判断，不可解析再往左判断，例如：aa.php.owf.rar
.htaccess文件：以php的方式解析，例如：
	<FilesMatch "as.png">
	SetHandler application/x-httpd-php
	</FilesMatch>
```

## 白名单绕过

```
%00与0x00绕过：as.php%00.png
```

常见文件幻数：

jpg:FF D8 FF E0 00 10 4A 46 49 46

git:47 49 46 38 39 61

## Web解析漏洞

### Apache解析漏洞

test.php.qwe.asd

### IIS 6.0解析漏洞

目录解析：www.xxx.com/xx.asp/xx.jpg 默认.asp目录下文件解析成asp文件。

文件解析：www.xxx.com/xx.asp;.jpg 不解析;后面内容，被解析成asp文件。

### IIS 7.0解析漏洞

任意文件名/任意文件名.php

### Nginx解析漏洞

一种同上，另一种：任意文件名%00.php
