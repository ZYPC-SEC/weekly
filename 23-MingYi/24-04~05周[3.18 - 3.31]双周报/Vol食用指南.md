# Volatility 食用指南

Volatility 的安装是真尼玛的麻烦，还好有封装好的exe版

感谢 Hello-CTF 上的内存取证模块

本文命令以 Windows 系统下的封装 Vol2.6 为准(PowerShell)

***谨以此文，记录我学习内存取证的过程，那是一段充满折磨的苦痛时光***

# 基础指令

- 查看内存镜像的基本情况

```Bash
.\vol.exe -f .\ez333.raw iamgeinfo
```

- 获取正在运行的程序

```Bash
.\vol.exe -f .\ez333.raw --profile=Win7SP1x64 pslist
```

- 提取正在运行的程序

```Bash
.\vol.exe -f .\ez333.raw --profile=Win7SP1x64 procdump -p [PID] -D ./
```

- 查看CMD中执行过的命令

```Bash
.\vol.exe -f .\ez333.raw --profile=Win7SP1x64 cmdscan
```

cmdline 更详细些
```Bash
.\vol.exe -f .\ez333.raw --profile=Win7SP1x64 cmdline
```

- 查看浏览器历史记录,获取当前系统浏览器搜索过的关键词

```Bash
.\vol.exe -f .\ez333.raw --profile=Win7SP1x64 iehistory
```

- 扫描所有的文件列表

```Bash
.\vol.exe -f .\ez333.raw --profile=Win7SP1x64 filescan
```

可配合 Select-string 代替 Linux 的 grep
```Bash
.\vol.exe -f .\ez333.raw --profile=Win7SP1x64 filescan | Select-string "png|jpg|gif|zip|rar|7z|pdf|txt|doc|pptx|xlex|docx"

// desktop(扫桌面)
```

再配合 dumpfiles 根据查出来的地址提取文件

```Bash
.\vol.exe -f .\ez333.raw --profile=Win7SP1x64 dumpfiles -Q [addr] -D .\(.\代表当前文件夹)
```

- 恢复被删除的文件

```Bash
.\vol.exe -f .\ez333.raw --profile=Win7SP1x64 mftparser
```

- 提取执行的命令行历史记录

```Bash
.\vol.exe -f .\ez333.raw --profile=Win7SP1x64 consoles
```

- 查看环境变量

```Bash
.\vol.exe -f .\ez333.raw --profile=Win7SP1x64 envars
```

- 提取进程

```Bash
.\vol.exe -f .\ez333.raw --profile=Win7SP1x64 memdump -p xxx --dump-dir=./
```

- 查看剪切板内容

```Bash
.\vol.exe -f .\chall.vmem --profile=Win7SP1x64 clipboard
```

- 查看强密码

```Bash
.\vol.exe -f .\chall.vmem --profile=Win7SP1x64 lsadump
```

- 显示有关编辑控件（曾经编辑过的内容）的信息 

```Bash
.\vol.exe -f .\chall.vmem --profile=Win7SP1x64 editbox
```

