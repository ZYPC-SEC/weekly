---
title: Angr符号执行笔记
date: 2023-10-29 20:56:26
tags: Angr
mathjax: true
---

# Angr符号执行笔记

## Angr安装

```bash
pip install angr
```

## 引子：[网鼎杯 2020 青龙组]singal

考点：**虚拟机、符号执行**

这题本身是个虚拟机题，给出了程序序列，要求找到合适的输入。本题采用符号执行最简便。

```python
import angr,sys
path="D:\\CTF-Workbench\\signal.exe"
project=angr.Project(path,auto_load_libs=False)
initial_state=project.factory.entry_state()
simulation=project.factory.simulation_manager(initial_state)
simulation.explore(find=0x0040179E,avoid=0x004016E6)
if simulation.found:
    for i in simulation.found:
        solution_state=i
        print(solution_state.posix.dumps(0))
else:
    print("no\n")
```

## 顶层接口

```python
import angr,sys
path="D:\\CTF-Workbench\\signal.exe"
project=angr.Project(path,auto_load_libs=False)
```

参数load-options指明加载方式：

| 名称                   | 描述                       | 传入参数 |
| ---------------------- | -------------------------- | -------- |
| `auto_load_libs`       | 是否自动加载程序的依赖。   | 布尔     |
| `skip_libs`            | 希望避免加载的库。         | 库名     |
| `excepts_missing_libs` | 无法解析库时是否抛出异常。 | 布尔     |
| `force_load_libs`      | 强制加载的库。             | 库名     |
| `ld_path`              | 共享库的优先搜索路径。     | 路径名   |

少加载无关结果的库能显著提高效率。

Project类中还有很多有用的方法、属性：

| 方法/属性                     | 含义       | 举例              |
| ----------------------------- | ---------- | ----------------- |
| `project.arch`                | 架构       | <Arch AMD64 (LE)> |
| `hex(project.entry)`          | 程序入口点 | 0x4023c0          |
| `project.filename`            | 文件名     | /bin/true         |
| `project.arch.bits`           | 位         | 64                |
| `project.arch.memory_endness` | 大小端     | Iend_LE           |

## 状态

```python
initial_state=project.factory.entry_state()
```

预设状态：

| 预设状态方式         | 描述                                                         |
| -------------------- | ------------------------------------------------------------ |
| `entry_state`        | 初始化状态为程序运行到程序入口点处的状态。                   |
| `blank_state(addr=)` | 大多数数据都没有初始化，状态中下一条指令为addr处的指令。用于跳过降低angr效率的指令。 |
| `full_init_state`    | （不常用）共享库和预定义内容已经加载完毕，例如刚加载玩共享库。 |
| `call_status`        | （不常用）准备调用函数的状态。                               |

手动指定开始地址：

```python
initial_state=project.factory.blank_state(addr=0x4007E8)
```

当没有库函数后，需要Hook函数：

```python
#对算法分析没有帮助，直接return
project.hook_symble('printf',angr.SIM_PROCEDURES['stubs']['ReturnUnconstrained'](),replace=True)
project.hook_symble('fflush',angr.SIM_PROCEDURES['stubs']['ReturnUnconstrained'](),replace=True)
```

## 模拟管理器

```python
simulation=project.factory.simulation_manager(initial_state)
simulation.explore(find=0x0040179E,avoid=0x004016E6)
```

find、avoid具名参数分别表示目标地址和需要回避的地址，如果不唯一，可以以list形式传参。

## 优化

* 开启LAZY_SOLVES，显著加速，但可能会无解。

    ```python
    simulation.one_active.options.add(angr.options.LAZY_SOLVES)
    ```

* 取缔标准输入，直接写入内存，创建用户输入：

    ```python
    p=angr.Project('./baby-re',auto_load_libs=False)
    state=p.factory.blank_state(addr=0x4028E0)
    flags_chars=[claripy.BVS('flag_%d'%i,32)for i in range(13)]
    for i in xrange(13):
        state.mem[state.regs.rsp+i*4].dword=flag_chars[i]
    state.regs.rdi=state.regs.rsp
    s=p.factory.simulation_manager(state)
    s.one_active.options.add(angr.options.LAZY_SOLVES)
    s.explore(find=0x4028E9,avoid=0x402941)
    flag=''.join(chr(s.one_found.solver.eval(c))for c in flag_chars)
    print(flag)
    ```

* 有时函数返回false的方式为内存写入，利用IDAPython提取：

    ```python
    import idc
    p=0x850
    end=0x10FF5
    addr=[]
    while p<=end:
        asm=idc.GetDisasm(p)
        if asm=='mov	[rbp+var_1E49], 0':
            addr.append(p+0x400000)
        p=idc.NextHead(p)
    print(addr)
    ```

    程序可能开启PIE保护，但是在angr中，固定在0x400000处。

    ```python
    avoids=[...]
    avoids.append(0x110EC+0x400000)
    proj=angr.Project('./sakura')
    state=proj.factory.entry_state()
    simgr=proj.factory.simulation_manager(state)
    simgr.one_active.options.add(angr.options.LAZY_SOLVES)
    simgr.explore(find=(0x110CA+0x400000),avoid=avoids)
    found=simgr.one_found
    flag=found.solver.eval(found.memory.load(0x612040,400),cast_to=bytes)
    ```

    继续优化：

    ```python
    state=proj.factory.blank_state(addr=(0x110BA+0x400000))
    simfd=state.posix.get_fd(0)
    data,real_size=simfd.read_data(400)
    state.memory.store(0x6121E0,data)
    ```

* Hook函数方法：

    ```python
    def set_hook(addrs,hooks):
        for i in addrs:
            proj.hook(i,hook=hooks,length=5)
    def my_sub_11146(state):
        state.regs.rax=state.regs.rdi+24
        return
    t=[...]
    set_hook(t,my_sub_11146)
    ```
