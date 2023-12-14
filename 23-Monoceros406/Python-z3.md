---
title: Python-z3
date: 2023-10-15 20:58:33
tags: z3
mathjax: true
---

# Python-z3

## 快速上手

### 安装

```bash
pip install z3_solver
```

### 使用

```python
from z3 import *
```

### 整形

```python
n=Int('n')
a,s,d=Ints('a s d')
x=Solver()
x.add(a-d==18)
x.add(a+s==12)
x.add(s-d==20)
#...
check=x.check()
print(check)#sat有解 unsat无解
model=x.model()
print(model)#输出解
```

### 有理数

```python
m=Real(m)
x,y=Reals('x y')
s=Solver()
s.add(x**2+y**2==3)
s.add(x**3==2)
check=s.check()
print(check)
model=s.model()
print(model)
```

### 二进制位运算

```python
m=BitVec('m',8)#8bit=1Byte
x,y,z=BitVecs('x y z',8)
s=Solver()
s.add(x^y&z==12)
s.add(y&z>>3==3)
s.add(z^y==4)
check=s.check()
print(check)
model=s.model()
print(model)
```

## 入门

### slove

```python
>>> from z3 import *
>>> x = Int('x')
>>> y = Int('y')
>>> solve(x > 2, y < 10, x + 2*y == 7)
[y = 0, x = 7]
```

### simplify

```pyhon
>>> simplify(x + y + 2*x + 3)
3 + 3*x + y
>>> simplify(x < y + x + 2)
Not(y <= -2)
>>> simplify(And(x + 1 >= 3, x**2 + x**2 + y**2 + 2 >= 5))
And(x >= 2, 2*x**2 + y**2 >= 3)
>>> simplify((x + 1)*(y + 1))
(1 + x)*(1 + y)
>>> simplify((x + 1)*(y + 1), som=True)     # sum-of-monomials：单项式的和
1 + x + y + x*y
>>> t = simplify((x + y)**3, som=True)
>>> t
x*x*x + 3*x*x*y + 3*x*y*y + y*y*y
>>> simplify(t, mul_to_power=True)          # mul_to_power 将乘法转换成乘方
x**3 + 2*y*x**2 + x**2*y + 3*x*y**2 + y**3
```

### 表达式解析

```python
>>> n = x + y >= 3
>>> "num args: ", n.num_args()
('num args: ', 2)
>>> "children: ", n.children()
('children: ', [x + y, 3])
>>> "1st child:", n.arg(0)
('1st child:', x + y)
>>> "2nd child:", n.arg(1)
('2nd child:', 3)
>>> "operator: ", n.decl()
('operator: ', >=)
>>> "op name:  ", n.decl().name()
('op name:  ', '>=')
```

### set_param

```python
>>> x = Real('x')
>>> y = Real('y')
>>> solve(x**2 + y**2 == 3, x**3 == 2)
[x = 1.2599210498?, y = -1.1885280594?]
>>>
>>> set_param(precision=30)
>>> solve(x**2 + y**2 == 3, x**3 == 2)
[x = 1.259921049894873164767210607278?,
 y = -1.188528059421316533710369365015?]
```

### 逻辑运算

```python
>>> p = Bool('p')
>>> q = Bool('q')
>>> r = Bool('r')
>>> solve(Implies(p, q), r == Not(q), Or(Not(p), r))
[q = False, p = False, r = True]
>>>
>>> x = Real('x')
>>> solve(Or(x < 5, x > 10), Or(p, x**2 == 2), Not(p))
[x = -1.4142135623?, p = False]
```

### Solver

```python
>>> x = Int('x')
>>> y = Int('y')
>>> s = Solver()    # 创造一个通用 solver
>>> type(s)         # Solver 类
<class 'z3.z3.Solver'>
>>> s
[]
>>> s.add(x > 10, y == x + 2)   # 添加约束到 solver 中
>>> s
[x > 10, y == x + 2]
>>> s.check()       # 检查 solver 中的约束是否满足
sat                 # satisfiable/满足
>>> s.push()        # 创建一个回溯点，即将当前栈的大小保存下来
>>> s.add(y < 11)
>>> s
[x > 10, y == x + 2, y < 11]
>>> s.check()
unsat               # unsatisfiable/不满足
>>> s.pop(num=1)    # 回溯 num 个点
>>> s
[x > 10, y == x + 2]
>>> s.check()
sat
>>> for c in s.assertions():    # assertions() 返回一个包含所有约束的AstVector
...     print(c)
...
x > 10
y == x + 2
>>> s.statistics()  # statistics() 返回最后一个 check() 的统计信息
(:max-memory   6.26
 :memory       4.37
 :mk-bool-var  1
 :num-allocs   331960806
 :rlimit-count 7016)
>>> m = s.model()   # model() 返回最后一个 check() 的 model
>>> type(m)         # ModelRef 类
<class 'z3.z3.ModelRef'>
>>> m
[x = 11, y = 13]
>>> for d in m.decls():         # decls() 返回 model 包含了所有符号的列表
...     print("%s = %s" % (d.name(), m[d]))
...
x = 11
y = 13
```

### 数值类型

```python
>>> 1/3
0.3333333333333333
>>> RealVal(1)/3
1/3
>>> Q(1, 3)      # Q(a, b) 返回有理数 a/b
1/3
>>>
>>> x = Real('x')
>>> x + 1/3
x + 3333333333333333/10000000000000000
>>> x + Q(1, 3)
x + 1/3
>>> x + "1/3"
x + 1/3
>>> x + 0.25
x + 1/4
>>> solve(3*x == 1)
[x = 1/3]
>>> set_param(rational_to_decimal=True) # 以十进制形式表示有理数
>>> solve(3*x == 1)
[x = 0.3333333333?]
```

### 混合类型

```python
>>> x = Real('x')
>>> y = Int('y')
>>> a, b, c = Reals('a b c')        # 返回一个实数常量元组
>>> s, r = Ints('s r')              # 返回一个整数常量元组
>>> x + y + 1 + a + s
x + ToReal(y) + 1 + a + ToReal(s)   # ToReal() 将整数表达式转换成实数表达式
>>> ToReal(y) + c
ToReal(y) + c
```

### 位向量

```python
>>> x = BitVec('x', 16)     # 16 位，命名为 x
>>> y = BitVec('x', 16)
>>> x + 2
x + 2
>>> (x + 2).sexpr()         # .sexpr() 返回内部表现形式
'(bvadd x #x0002)'
>>> simplify(x + y - 1)     # 16 位整数的 -1 等于 65535
65535 + 2*x
>>> a = BitVecVal(-1, 16)   # 16 位，值为 -1
>>> a
65535
>>> b = BitVecVal(65535, 16)
>>> b
65535
>>> simplify(a == b)
True
```

