#   关于python的学习

######   首先对于 python  在我的了解，是一门高级，比较易懂，解释型的编程语言，它的核心特点大概有以下这么几种：

##### 1. 语法简单易懂

##### 2.解释型语言，基本上在每个系统内都可以运行

##### 3.动态的类型（即变量不需要声明其类型）

##### 4.标注库比较丰富，大多数任务不需要安装第三方库就能完成

###### 接下来先入门一下：（我这里的python是3.14.8，若有版本问题可以参考官方文档： **[https://docs.python.org](https://docs.python.org/)** ）

  python 的环境可以自己去网上找到教程

## 1.首先写一个简单的 python 的代码：

```python
print("Hello,Python!")

name = input("请输入你的姓名：")
age = int(input("请输入你的年龄："))
city = input("请输入你所在的城市：")

print(f"你好,{name}!你今天{age}岁，来自{city}。")
```



![image-20261019191902220](C:\Users\乔佳宇\AppData\Roaming\Typora\typora-user-images\image-20261019191902220.png)

运行程序和，确认能正常输入和输出。

```python
name = input("请输入你的姓名：")  #这里可以看到运到了一个input()的函数其结果默认是字符串
age = int(input("请输入你的年龄：")) #这里input()外面加了一个int()的函数，在这里由于年龄是一个整数，然后input()的默认是字符串，所以年龄使用int()来进行转型，转化为一个整型，此外还有float()转化为整型
```

```python
print(f"你好,{name}!你今天{age}岁，来自{city}。")
```

在这段代码中注意到了{f"  *{  }*  "}有一个 f (这里是`f-string` 是 Python 中用来**把变量或表达式嵌入字符串**的一种写法，从 Python 3.6 开始支持。)也可以把 f 理解为一个格式化字符串。而{name}则是替换变量的值。

## 2.接下来学习一些 python 常见的数据类型，以及其类型转化，算术运算和比较运算。

1.先认识四种基本的数据类型：

| 类型    | 含义               | 示例                 |
| ------- | ------------------ | -------------------- |
| `int`   | 整数               | `18`、`-5`、`100`    |
| `float` | 小数               | `3.14`、`0.5`        |
| `str`   | 字符串             | `"Python"`、`"你好"` |
| `bool`  | 布尔值，只有真或假 | `True`、`False`      |

```python
输入：
age = 18
height = 1.75
name = "小明"
is_student = True

print(type(age))
print(type(height))
print(type(name))
print(type(is_student))

输出：
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

如果不清楚数据的类型，在 python 里面有一个专用的函数 type() 可以查看一个数据的类型，如上面代码所示。

2.类型转换

常见的类型转化：

```python
number = int("18")       # 字符串转整数
price = float("9.9")     # 字符串转小数
text = str(123)          # 整数转字符串
```

`input()` 得到的永远是字符串。如果用户输入的是数字，并且你需要进行计算，就要用 `int()` 或 `float()` 转换。

3.算术运算符

```python
a = 10
b = 3

print(f"加法：{a + b}")   13
print(f"减法：{a - b}")    7
print(f"乘法：{a * b}")   30
print(f"除法：{a / b}")    3.33333333
print(f"整除：{a // b}")   3
print(f"取余：{a % b}")    1
print(f"乘方：{a ** b}")   8
重点观察下面的一些例子：
10 / 3    # 结果是 3.3333333333333335，除法结果一定是小数
10 // 3   # 结果是 3，只保留整数部分
10 % 3    # 结果是 1，表示 10 除以 3 的余数
2 ** 3    # 结果是 8，表示 2 的 3 次方
```

4.比较运算

比较运算的结果是 bool 类型：注意：判断两个值是否相等要用 `==`，一个等号 `=` 是赋值

```python
print(10 > 3)     # True
print(10 < 3)     # False
print(10 == 10)   # True
print(10 != 3)    # True
```

## 3.条件判断 if /elif /else

###  **1.首先写一个简单的 if** 

```python
age = int(input("请输入你的年龄："))

if age >= 18:
    print("你已经成年")
```

语法要求：

- `if` 条件后面必须有英文冒号 `:`
- 下一行必须缩进，通常用 4 个空格
- 条件成立时，才会执行缩进的代码

### **2.if / else**   

```python
age = int(input("请输入你的年龄："))

if age >= 18:
    print("你已经成年")
else:
    print("你还未成年")
```

### **3.if / elif / else**

```python
score = int(input("请输入成绩："))

if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")
```

*`elif` 的判断是有顺序的。程序一旦遇到成立的条件，就会执行对应代码，并跳过后面的分支。*(相当于只执行这一个的对应的语句，后面的条件不再判断也不在执行，随后跳出整条判断链，继续执行判断以外的语句。)

### 4. 比较运算符

| 运算符 | 含义       |
| ------ | ---------- |
| `>`    | 大于       |
| `<`    | 小于       |
| `>=`   | 大于或等于 |
| `<=`   | 小于或等于 |
| `==`   | 是否相等   |
| `!=`   | 是否不相等 |

### 5. 逻辑运算符

```python
and   # 两个条件都成立，结果才为 True
or    # 至少一个条件成立，结果就为 True
not   # 取反
```

## 4.循环结构 for 和 while。（主要的任务是让程序自动的重复执行代码）

### **1.for 循环** ：循环适合执行次数明确的重复任务！

先写一个简单的 for 循环：

```python
for i(参数可以任意定制，在有些算法中会将其写为 _ ) in range(5):#range的范围为左闭右开所以不会包含5
    print(i)
```

```python
输出：
0
1
2
3
4
```

***这里强调一下 range 的常见写法：

```python
range(5)          # 0, 1, 2, 3, 4
range(1, 6)       # 1, 2, 3, 4, 5
range(1, 10, 2)   # 1, 3, 5, 7, 9
range(5, 0, -1)   # 5, 4, 3, 2, 1
range(开始值, 结束值, 步长) #结束值不会被包含
```

### **2.使用循环累加**

```python
total = 0   #一定要将初值定为0，才能继续累加

for number in range(1, 6):
    total = total + number
    print(f"当前数字：{number}，累计和：{total}")

print(f"最终结果：{total}")
```

`otal = total + number` 可以简写为：

```python
total += number
```

### **3.遍历字符串** （将字符串所有的字符打印出来）

```python
输入：
for letter in "Python":
    print(letter)
输出：
P
y
t
h
o
n
```

### **4.break 和 continue** 

break ：立即结束整个循环。

```python
for number in range(1, 10):
    if number == 5:
        break
    print(number)
```

最后输出 1,2,3,4 后结束循环。

contiune： 跳过本轮的剩余代码，进行下一轮的循环。

```python
for number in range(1, 6):
    if number == 3:
        continue
    print(number)
```

最后输出 1,2 4,5. 除了 3 以外全部输出。

### 5.while 循环。

`while` 循环适合**不确定循环次数，只知道停止条件**的场景。

写一个简单的循环：

```python
count = 1

while count <= 5:
    print(f"第 {count} 次执行")
    count += 1

print("循环结束")
```

执行过程：

1. 判断 `count <= 5` 是否成立
2. 成立就执行缩进代码
3. 执行 `count += 1`
4. 重新判断条件
5. 条件不成立时退出循环

## 5.函数

函数的目标就是把重复的代码封装成可以反复调用的函数。

### 1. 为什么需要函数？

假设需要在程序中多次输出一段欢迎语：

```python
print("=" * 30)
print("欢迎使用学生管理系统")
print("=" * 30)
```

如果每处都复制一遍，代码会很重复。可以把它封装成函数：

```python
def print_welcome():
    print("=" * 30)
    print("欢迎使用学生管理系统")
    print("=" * 30)

print_welcome()
print_welcome()
```

、输出两次欢迎语。

函数的作用是：

- 把一段代码封装起来
- 给这段代码起一个名字
- 需要时反复调用
- 修改时只改一个地方

### 2. 定义函数和调用函数

python的函数相对于较为简单，语法也比较简单

```python
def 函数名():
    函数体 
```

注意：

- `def` 表示定义函数
- 函数名后面有括号
- 定义函数时，行尾必须有英文冒号
- 函数体必须缩进
- 定义函数不会立即执行，只有调用时才执行

```python
def say_hello():
    print("你好")

say_hello()   # 调用函数，才会输出“你好”
```

### 3. 带参数的函数

```python
def greet(name):
    print(f"你好，{name}！")

greet("小明")
greet("小红")
```

输出：

```python
你好，小明！
你好，小红！
```

在这里：

```python
def greet(name):
```

`name` 是函数定义时接收数据的变量。

```python
greet("小明")
```

`"小明"` 是调用函数时传入的具体数据。

也可以传入多个参数：

```python
def introduce(name, age):
    print(f"我叫{name}，今年{age}岁。")

introduce("小明", 18)
```

注意：参数的顺序要对应。

```python
introduce(18, "小明")   # 顺序错误，输出内容也会错误
```

### 4. 使用 `return` 返回结果

有些函数不需要返回结果，只负责执行某个动作，例如打印文字。

但很多函数需要把计算结果交给调用者，这时使用 `return`：

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)
```

输出：

```python
8
```

### 5. `print()` 和 `return` 的区别

这是今天最重要的知识点之一。

```python
def add_with_print(a, b):
    print(a + b)

result1 = add_with_print(2, 3)
print(result1)
```

输出：

```python
5
None
```

原因：

- `print(a + b)` 只是把结果输出到屏幕
- 函数没有 `return`，所以调用结果默认是 `None`

再看：

```python
def add_with_return(a, b):
    return a + b

result2 = add_with_return(2, 3)
print(result2)
```

输出：

```python
5
```

区别可以这样记：

```python
print()：把结果显示出来
return：把结果交给调用函数的地方
```

一个函数执行到 `return` 后，会立即结束：

```python
def test():
    print("开始")
    return 100
    print("这句话不会执行")

result = test()
print(result)
```

输出:

```python
开始
100
```

### 6.默认参数

函数参数可以参考设置的默认值。

```python
def greet(name = "同学")
    print(f"你好,{name}")
    
greet()
greet("小明")

输出
你好，同学！
你好，小明！
```

如果在函数调用中没有传入值的话，则会使用赋予的默认值。

## 6.函数的进阶与作用域

**参数传递。**

### 1. 位置参数

参数按照顺序传递：

```python
def introduce(name, age, city):
    print(f"我叫{name}，今年{age}岁，来自{city}。")

introduce("小明", 18, "上海")
```

参数顺序必须对应：

```python
introduce("上海", 18, "小明")   # 内容会错乱
```

输出：

```python
我叫上海，今年18岁，来自小明。
```

### 2. 关键字参数

调用函数时，可以写出参数名：

```python
introduce(name="小明", age=18, city="上海")
```

使用关键字参数时，顺序可以调整：

```python
introduce(city="上海", age=18, name="小明")
```

输出仍然是：

```python
我叫小明，今年18岁，来自上海。
```

### 3. 位置参数和关键字参数混用

混合使用时，**位置参数必须写在关键字参数前面**。

正确：

```python
introduce("小明", age=18, city="上海")
```

错误：

```python
introduce(name="小明", 18, "上海")
```

会报语法错误：

```python
SyntaxError
```

------

### 4. 默认参数

定义函数时，可以给参数设置默认值：

```python
def greet(name="同学", city="北京"):
    print(f"你好，{name}！你来自{city}。")
```

调用：

```python
greet()
greet("小明")
greet("小红", "上海")
greet(name="小刚", city="广州")
```

输出：

```python
你好，同学！你来自北京。
你好，小明！你来自北京。
你好，小红！你来自上海。
你好，小刚！你来自广州。
```

注意：定义函数时，带默认值的参数通常放在没有默认值的参数后面。

### 5.变量作用域

#### 1. 函数内部的变量是局部的

```python
def calculate():
    number = 10
    print(number)

calculate()
print(number)
```

输出：

```python
10
```

然后报错：

```python
NameError: name 'number' is not defined
```

原因：`number` 是在函数内部定义的变量，函数执行结束后，外面无法直接使用它。

需要把结果返回：

```python
def calculate():
    number = 10
    return number

result = calculate()
print(result)
```

------

#### 2. 全局变量

在函数外部定义的变量叫全局变量：

```python
name = "小明"

def show_name():
    print(name)

show_name()
```

函数可以读取全局变量，但一般不建议依赖它完成计算。

------

#### 3. 函数内部赋值不会修改全局变量

```python
name = "小明"

def change_name():
    name = "小红"
    print(f"函数内部：{name}")

change_name()
print(f"函数外部：{name}")
```

输出：

```python
函数内部：小红
函数外部：小明
```

函数里的 `name = "小红"` 创建了一个新的局部变量，没有修改外面的全局变量。

虽然可以使用 `global` 关键字修改全局变量，但初学阶段不建议这样做。更推荐：

```python
def change_name(current_name):
    return "小红"

name = "小明"
name = change_name(name)
print(name)
```

输出：

```python
小红
```

核心原则：

> 少用全局变量，多通过参数传入数据，通过 `return` 返回结果。

## 7.列表

### 1.什么是列表？

列表就是可以在一个变量之中保存多个元素。

```python
fruits = ["苹果", "香蕉", "橙子"]
numbers = [10, 20, 30, 40]
empty_list = []
```

列表特点：

- 使用中括号 `[]`
- 数据之间用英文逗号分隔
- 数据有顺序
- 列表可以被修改

### 2. 通过索引访问元素

列表索引从 `0` 开始：

```python
fruits = ["苹果", "香蕉", "橙子"]

print(fruits[0])
print(fruits[1])
print(fruits[2])
```

输出：

```python
苹果
香蕉
橙子
```

索引对应关系：

```python
列表元素：  苹果    香蕉    橙子
正索引：     0       1       2
负索引：    -3      -2      -1
```

使用负索引访问末尾元素：

```python
print(fruits[-1])   # 橙子
print(fruits[-2])   # 香蕉
```

如果访问不存在的索引：

```python
print(fruits[10])
```

会报错：

```python
IndexError: list index out of range
```

### 3.获取列表长度

使用 len() 获取元素个数：

```python
fruits = ["苹果", "香蕉", "橙子"]
print(len(fruits))

输出：
3
```

### 4.修改列表中的元素

可以通过索引来修改已有的元素：

```python
fruits = ["苹果", "香蕉", "橙子"]
fruits[1] = "葡萄"

print(fruits)

输出：
['苹果', '葡萄', '橙子']
#注意如果索引不存在，不能直接赋值，并且会报错。
```

### 5.常用的列表操作

#### 1.在末尾添加元素：append()

```python
fruits = ["苹果", "香蕉"]
fruits.append("橙子")

print(fruits)
输出：
['苹果', '香蕉', '橙子']
```

#### 2.在指定的位置插入元素：insert()

```python
fruits = ["苹果", "香蕉"]
fruits.insert(1, "葡萄")

print(fruits)
输出：
['苹果', '葡萄', '香蕉']
```

#### 3.根据值删除元素：remove()

```python
fruits = ["苹果", "香蕉", "橙子"]
fruits.remove("香蕉")

print(fruits)
输出：
['苹果', '橙子']
```

#### 4.根据索引删除元素：pop()

```python
fruits = ["苹果", "香蕉", "橙子"]
removed = fruits.pop(1)

print(removed)
print(fruits)
输出：
香蕉
['苹果', '橙子']
```

注意：如果不写索引，`pop()` 默认删除最后一个元素。

### 6.判断元素是否在列表中

使用 `in`：

```python
fruits = ["苹果", "香蕉", "橙子"]

if "香蕉" in fruits:
    print("列表中有香蕉")
else:
    print("列表中没有香蕉")
```

使用 `not in` 判断不存在：

```python
if "西瓜" not in fruits:
    print("列表中没有西瓜")
```

### 7.遍历列表

```python
fruits = ["苹果", "香蕉", "橙子"]

for fruit in fruits:
    print(fruit)
输出：
苹果
香蕉
橙子
```

如果需要同时得到索引和元素，可以使用 `enumerate()`：

```python
fruits = ["苹果", "香蕉", "橙子"]

for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")
```

输出：

```python
1. 苹果
2. 香蕉
3. 橙子
```

`start=1` 表示编号从 1 开始。

### 8.列表切片

切片可以获取列表中的一部分：

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
```

输出：

```
[20, 30, 40]
```

切片规则：

```python
numbers[开始索引:结束索引]
```

包含开始索引，不包含结束索引。

常见例子：

```python
numbers[:3]    # 前三个元素
numbers[-2:]   # 最后两个元素
numbers[:]     # 整个列表的副本
```

### 9.常用的统计函数

```python
scores = [85, 92, 58, 76, 61]

print(sum(scores))   # 总和
print(len(scores))   # 元素个数
print(max(scores))   # 最大值
print(min(scores))   # 最小值
```

## 8.字典

### 1.什么是字典？

可以通过列表的概念所知，列表通过“索引”查找数据，字典通过“键 ”查找数据。字典一般使用 {} 定义。

```python
student = {
    "name": "小明",
    "age": 18,
    "score": 92
}
```

它由一组组“键值对”组成：

```python
"name"  → "小明"
"age"   → 18
"score" → 92
```

其中：

- `"name"`、`"age"`、`"score"` 是**键**
- `"小明"`、`18`、`92` 是对应的**值**
- 键和值之间使用英文冒号 `:`
- 不同键值对之间使用英文逗号 `,`

可以创建一个空字典：

```python
empty_dict = {}
```

注意: **[]**  为空列表，{} 为空字典。

### 2. 通过键访问值

```python
student = {
    "name": "小明",
    "age": 18,
    "score": 92
}

print(student["name"])
print(student["age"])
print(student["score"])
```

输出：

```python
小明
18
92
```

如果访问不存在的键：

```python
print(student["city"])
```

会报错：

```python
KeyError: 'city'
```

### 3. 使用 get() 安全获取值

get() 在键不存在时候不会报错，而是返回制定的默认值或者返回 None 。

```python
student = {
    "name": "小明",
    "age": 18
}

print(student.get("name"))
print(student.get("city", "未登记"))
```

输出：

```python
小明
未登记
```

如果键不存在，又没有提供默认值：

```python
print(student.get("city"))
```

会得到：

```python
None
```

### 4. 添加和修改键值对

如果键不存在，赋值就是添加：

```python
student = {
    "name": "小明",
    "age": 18
}

student["city"] = "上海"
```

现在字典变成：

```python
{
    "name": "小明",
    "age": 18,
    "city": "上海"
}
```

如果键已经存在，赋值就是修改：

```python
student["age"] = 19
`age` 的值会从 `18` 变成 `19`
```

### 5. 删除键值对

使用 `del`：

```python
student = {
    "name": "小明",
    "age": 18,
    "city": "上海"
}

del student["city"]
```

也可以使用 `pop()` 删除，并获取被删除的值：

```python
removed = student.pop("age")
print(removed)
```

输出：

```python
18
```

如果删除不存在的键，会报 `KeyError`。

可以给 `pop()` 一个默认值，避免报错：

```python
removed = student.pop("score", None)

if removed is None:
    print("没有这个键")
```

### 6. 判断键是否存在

使用 `in` 判断的是键，不是值：

```python
student = {
    "name": "小明",
    "age": 18
}

if "name" in student:
    print("存在 name 这个键")

if "小明" in student:
    print("存在小明")
else:
    print("不存在小明")
```

第二个判断会进入 `else`，因为 `"小明"` 是值，不是键。

------

### 7. 获取字典长度

```python
student = {
    "name": "小明",
    "age": 18,
    "score": 92
}

print(len(student))
```

输出：

```python
3
```

表示字典中有 3 组键值对。

------

### 8. 遍历字典

#### 遍历所有键

```python
for key in student:
    print(key)
```

也可以写成：

```python
for key in student.keys():
    print(key)
```

#### 遍历所有值

```python
for value in student.values():
    print(value)
```



#### 同时遍历键和值

```python
for key, value in student.items():
    print(f"{key}: {value}")
```

输出：

```python
name: 小明
age: 18
score: 92
```

最常用的是 `.items()`。
