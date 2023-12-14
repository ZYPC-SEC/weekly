---
title: Pintools基本用法
date: 2023-11-28 20:38:12
tags: Pintools
mathjax: true
---

# Pintools基本用法

## 安装

### Linux/Ubuntu

下载源码，在`source/tools/`目录下找到文件夹`MyPintools`，把自己的`mypintool.cpp`复制过来（或用示例文件）。然后`make`，即：

```bash
cp mypintools.cpp source/tools/MyPintools
cd source/tools/MyPintools
make obj-ia32/mypintool.so TARGET=ia32 #32位架构
make obj-intel64/mypintool.so TARGET=intel64 #64位架构
```

### Windows

下载源码，将目录添加到环境变量。Pintools区分32位和64位，目录中的为32位的。为方便使用，将原`pin.exe`命名为`pin.bak`，不使用。新建`pin32.bat`，内容如下：

```bash
@echo off
%~dp0\ia32\bin\pin.exe %*
```

再新建`pin64.bat`，内容如下：

```bash
@echo off
%~dp0\intel64\bin\pin.exe %*
```

找到`source\tools\MyPinTool`目录下有个`MyPinTool.vcxproj`，拿VS打开生成解决方案，即可得`.dll`文件。

## 使用

