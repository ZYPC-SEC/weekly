---
title: Python代码保护技术
date: 2023-12-09 14:25:06
tags: Python
mathjax: true
---

# Python代码保护技术

## Oxyry Python Obfuscator

https://pyob.oxyry.com/

## Stegosaurus

https://github.com/AngelKitty/stegosaurus

先检查最多可包含的Payload字节数：

```bash
stegosaurus example.py -r
```

写入Payload：

```python
stegosaurus example.py -s --payload "xxx"
```

也可以是十六进制：

```bash
stegosaurus example.py -s --payload "\xeb\x2a\x5e\x89\x76"
```

解密：

```bash
stegosaurus example.pyc -x
```

### pyc_obscure

https://github.com/c10udlnk/pyc_obscure

Python字节码花指令构造：通过JUMP_ABSOLUTE跳过无意义字节，但无意义字节仍会被反汇编器处理，导致报错。

```python
from pyc_obscure import Obscure
obs=Obscure('test.pyc')
obs.basic_obscure()
obs.write_pyc('obs_test.pyc')
```

解决方法：将这些语句patch为“\x09\x00\x09\x00”。
