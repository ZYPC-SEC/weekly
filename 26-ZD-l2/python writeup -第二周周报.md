

# 我的 Python 复习记录 1 —— 基础部分

## 目录

1. Python 环境
2. Python 基本语法
3. Python 基本逻辑
4. Python 常用数据结构
5. Python 函数基础
6. Python 模块
7. Python I/O 模块

---

## 1. Python 环境

Python 需要解释器/编译器才能运行。比较方便的方法是使用 VS Code，安装 Python 插件后即可在 VS Code 中运行。

如果想在电脑上直接使用，也可以安装 IDLE，并把 Python 安装目录配置到环境变量 `PATH` 中。

如果代码中包含中文，建议声明编码，例如：

```python
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
```

注意：编码声明中的感叹号和冒号应使用英文符号，不要写成中文符号。

---

## 2. Python 基本语法

本文主要讨论 Python 3 环境下的代码。

在 Python 2 中，`print` 可以不加括号；在 Python 3 中，`print` 是函数，需要写成 `print()` 形式。如果维护 Python 2 代码，可以使用：

```python
from __future__ import print_function
```

### 2.1 缩进

Python 中缩进是区分代码块的重要因素，因此必须保持正确缩进。

示例：

```python
if True:
    print("Answer")
    print("True")
else:
    print("Answer")
    print("False")
```

如果缩进不一致，可能出现：

```text
IndentationError: unindent does not match any outer indentation level
```

这通常表示代码中混用了 Tab 和空格。建议统一使用 4 个空格缩进。

### 2.2 多行语句

Python 语句一般以新行作为结束符。可以使用反斜杠 `\` 将一条语句拆分为多行，以增强可读性：

```python
members = mem_one + \
          mem_two + \
          mem_three
```

如果语句中包含 `[]`、`{}` 或 `()` 括号，可以直接换行，不需要使用反斜杠：

```python
hahaha = ['wu', 'great', 'fun',
          'sucka', 'funky']
```

### 2.3 一行多条语句

Python 可以在同一行中使用多条语句，语句之间用分号 `;` 分割：

```python
import sys; x = 'runoob'; sys.stdout.write(x + '\n')
```

### 2.4 输出与换行

Python 3 中 `print()` 默认换行。如果要实现不换行，应使用 `end` 参数：

```python
print(1)
print(2, end="")
print(3)
print(4)
print(5)
```

输出：

```text
1
23
4
5
```

注意：原文中“在变量末尾加逗号取消换行”属于 Python 2 的写法；Python 3 应使用 `end=""`。

---

## 3. Python 基本逻辑

### 3.1 代码组

像 `if`、`while`、`def` 和 `class` 这样的复合语句，首行以关键字开始，以冒号 `:` 结束，后面一行或多行代码构成代码组。首行及后面的代码组可以称为一个子句。

### 3.2 条件语句 `if`

`if` 用于逻辑判断；如果有其他筛选条件，可以使用 `elif`：

```python
score = 85

if score >= 90:
    print("优秀")
elif score >= 60:
    print("及格")
else:
    print("不及格")
```

### 3.3 循环语句 `while`

`while` 用于循环，括号内为循环条件判断。需要注意避免死循环。

```python
win0 = True

while win0:
    print("Given flag is really true")
    break
```

如果需要补充条件不满足时的情况，可以使用 `else`：

```python
i = 0

while i < 3:
    print(i)
    i += 1
else:
    print("循环结束")
```

### 3.4 循环语句 `for`

`for` 以元素为单位进行遍历，例如字符串中的字符、元组中的元素等；通常和 `in range()` 配合使用。

```python
for letter in 'Python':
    print(letter)
```

输出：

```text
P
y
t
h
o
n
```

### 3.5 `break` 与 `continue`

与 C 语言类似：

- `break`：跳出当前循环。
- `continue`：跳过本轮循环，进入下一轮。

### 3.6 循环嵌套

Python 中的循环可以嵌套，注意每层使用不同的缩进。

### 3.7 循环与条件综合案例

```python
i = 0

while i < 100:
    i += 1
    print("i现在的数值为", i)

    for n in range(1, 5):
        if n == 1:
            i += 20
        elif n == 2:
            print("n的值为", n)
            continue
        elif n == 3:
            print("n的值为", n)
            break
else:
    print("i的值不小于100，而是", i)
```

输出：

```text
i现在的数值为 1
n的值为 2
n的值为 3
i现在的数值为 22
n的值为 2
n的值为 3
i现在的数值为 43
n的值为 2
n的值为 3
i现在的数值为 64
n的值为 2
n的值为 3
i现在的数值为 85
n的值为 2
n的值为 3
i的值不小于100，而是 105
```

注意：`i += 1,` 中的逗号会让 `1,` 变成元组 `(1,)`，从而导致：

```text
TypeError: unsupported operand type(s) for +=: 'int' and 'tuple'
```

正确写法是：

```python
i += 1
```

### 3.8 `pass` 空语句

`pass` 可以填入暂时没有内容的函数或代码块中，避免语法报错：

```python
def awslaaaaaaaaa(a):
    pass
```

---

## 4. Python 常用数据结构

### 4.1 字符串

```python
r1 = 'Hello World!'
```

Python 不支持单字符类型，单字符在 Python 中也是字符串。

### 4.2 列表 List

列表使用 `[]` 包含，元素之间用 `,` 分隔：

```python
list1 = ['physics', 'chemistry', 1997, 2000]
```

列表的数值是可修改的。列表索引从 0 开始，可以进行截取、组合等操作。

```python
print(list1[0])
print(list1[1:3])

del list1[2]
print(list1)
```

### 4.3 元组 Tuple

元组使用 `()` 包含：

```python
p1 = ('physics', 'chemistry', 1997, 2000, 'boom')
```

元组可以理解为不可写的列表，其他访问方式与列表类似。

### 4.4 字典 Dictionary

字典格式为：

```python
d = {key1: value1, key2: value2}
```

示例：

```python
d = {'key1': 'value1', 'key2': 'value2'}

print(d['key1'])   # 按键取值
print(d.keys())    # 所有键
print(d.values())  # 所有值
print(d.items())   # 所有键值对
```

注意：

1. 不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住。
2. 键必须不可变，所以可以使用数字、字符串或元组充当键，不能使用列表。
3. 迭代字典时默认遍历键；按键取值使用 `d[key]`，取所有值使用 `d.values()`，不存在 `d.value()`。

---

## 5. Python 函数基础

### 5.1 创建函数

使用 `def` 定义函数：

```python
def 函数名(参数):
    pass
```

### 5.2 函数调用与参数传递

Python 函数可以传可变参数和不可变参数。

如果传不可变参数，则不会产生名称不统一的映射：

```python
def change_int(a):
    a = 10

b = 2
change_int(b)
print(b)
```

输出：

```text
2
```

如果传可变参数，则函数内部修改会影响外部对象：

```python
def changeme(mylist):
    mylist.append([1, 2, 3, 4])
    print("函数内取值:", mylist)

mylist = [10, 20, 30]
changeme(mylist)
print("函数外取值:", mylist)
```

输出：

```text
函数内取值: [10, 20, 30, [1, 2, 3, 4]]
函数外取值: [10, 20, 30, [1, 2, 3, 4]]
```

### 5.3 `return`

`return` 的使用方法与 C 函数类似，用于返回函数结果。

---

## 6. Python 模块

一个写好的 Python `.py` 脚本，可以作为一个模块进行调用。

### 6.1 模块搜索顺序

导入模块时，Python 解析器对模块位置的搜索顺序是：

1. 当前目录
2. 如果不在当前目录，Python 搜索 `PYTHONPATH` 下的每个目录
3. 如果都找不到，Python 会查看默认路径。UNIX 下默认路径一般为 `/usr/local/lib/python/`

因此，建立完整的目录树并整理所有脚本是有效的。

### 6.2 `import` 语句

例如，同文件夹下有两个文件。

`aaa.py`：

```python
def turn2zero(a):
    return 0
```

`2.py`：

```python
import aaa

for i in range(1, 5):
    print(aaa.turn2zero(i))
```

输出：

```text
0
0
0
0
```

注意：`range(1, 5)` 生成 `1, 2, 3, 4` 共 4 个数，因此输出 4 个 `0`。也可以使用 `from aaa import turn2zero` 后直接调用 `turn2zero(i)`。

### 6.3 `from ... import ...` 语句

用于从模块中抽取特定函数进行调用，而不抽取其他函数：

```python
from aaa import turn2zero

print(turn2zero(10))
```

### 6.4 `dir()` 函数

对一个模块使用 `dir()` 函数，可以得到其中所有函数名：

```python
import math

print(dir(math))
```

### 6.5 包 Package

一个包可以包含多个模块。包就是文件夹，但该文件夹下必须存在 `__init__.py` 文件。该文件内容可以为空，`__init__.py` 用于标识当前文件夹是一个包。

---

## 7. Python I/O 模块

### 7.1 标准输入输出

`input()` 用于接收标准输入，返回字符串：

```python
name = input("请输入姓名: ")
age = int(input("请输入年龄: "))

print(f"姓名: {name}, 年龄: {age}")
```

注意：`input()` 返回的是字符串；如果需要数字，应使用 `int()` 或 `float()` 转换。

`print()` 常用参数：

```python
print("a", "b", sep="-", end="!\n")
```

输出：

```text
a-b!
```

常用格式化输出方式：

```python
x = 3.14159

print("x = %.2f" % x)
print("x = {:.2f}".format(x))
print(f"x = {x:.2f}")
```

### 7.2 文件读写

常用文件模式：

| 模式 | 含义 |
| --- | --- |
| `r` | 只读，默认模式 |
| `w` | 只写，清空原文件或创建新文件 |
| `a` | 追加写入 |
| `r+` | 读写 |
| `b` | 二进制模式，如 `rb`、`wb` |
| `encoding` | 文本文件编码，如 `encoding="utf-8"` |

写文件：

```python
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("第一行\n")
    f.write("第二行\n")
```

读文件：

```python
with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
```

按行读取：

```python
with open("test.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
```

其他常用方法：

- `readline()`：读取一行
- `readlines()`：读取所有行到列表
- `write()`：写入字符串
- `writelines()`：写入字符串列表

### 7.3 标准库 `sys` 与 JSON I/O

使用 `sys.stdin`、`sys.stdout`、`sys.stderr` 进行标准输入输出和错误输出：

```python
import sys

sys.stdout.write("标准输出\n")
sys.stderr.write("标准错误\n")

line = sys.stdin.readline()
print("输入内容为:", line)
```

JSON 读写：

```python
import json

data = {"name": "Alice", "age": 18}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open("data.json", "r", encoding="utf-8") as f:
    obj = json.load(f)

print(obj)
```

### 7.4 文件异常处理

```python
try:
    with open("not_exist.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("文件不存在")
```

---
