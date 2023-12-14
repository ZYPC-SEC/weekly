---
title: Python沙盒逃逸绕过方法合集
date: 2023-12-04 19:10:14
tags: PyJail
mathjax: true
---

# Python沙盒逃逸绕过方法合集

## 模块删除绕过

### 模块删除

删除方法：

```python
del __builtin__.__dict__['eval']
```

reload恢复：

```python
import importlib
reload(__builtin__)
```

## 模块修改

修改方法：

```python
sys.modules['os']='not allowed'
```

恢复：

```python
del sys.modules['os']
import os
os.system('ls')
```

