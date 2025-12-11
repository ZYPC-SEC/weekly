# <font style="color:rgb(38, 218, 38);">完成事项# </font>

python逆向-逆向pyinstaller打包的exe程序反编译获取源代码
--------------------------------------

# 常见工具

- ## Pyinstaller

- pyinstaller 是一个用于将 Python 程序打包成独立可执行文件的工具，能够在没有 Python 解释器的情况下运行。 Python 脚本转换为 Windows、macOS 和 Linux 操作系统上的可执行文件。
  
  ```
  #安装pyinstaller 
  pip install pyinstaller 
  #打包 
  pyinstaller your_script.py
  ```
  
  

https://img.cdn1.vip/i/69396c442a3fe_1765370948.webp



- ## Uncompyle6

- `uncompyle6`：将 `.pyc` 文件还原为 `.py` 文件。
  
  ```
  #安装方法uncompyle6  
  pip install uncompyle
  ```



https://img.cdn1.vip/i/693aadf00903c_1765453296.webp\



- ## Pycdc和Pycdas

- `pycdc` 和 `pycdas`：分别是反编译工具和动态分析工具。
  
  ```
  #下载网址 
  https://gitcode.com/open-source-toolkit/faa06/blob/main/Pycdc%20and%20Pycdas.zip
  ```

- ## Pylingual
  
  在线反编译的网站
  
  ```
  https://pylingual.io/
  ```
  
  

以上为所需工具，接下来开始了解此类题目

# 1.什么是pyc文件

- `pyc` 是 Python 源代码（`.py`）文件被编译后的字节码文件，通常位于 `__pycache__` 文件夹中。
* 在 CTF 中的常见考点：
  * 恶意字节码修改
  * 防止直接反编译的干扰
  * 反编译字节码
  * py 代码逆向
  * 隐藏的调试信息

# 2.pyc文件结构与原理

**2.1. 文件结构**

* 文件头部：包含 Python 版本、时间戳等信息
    Python3.3 以下版本文件头仅包含：
  
        Magic Number（4 字节，小端序）
        时间戳（4 字节，记录文件编译时间，POSIX 时间戳）
  
    Python3.3 到 Python3.7（不包含 3.7）文件头包含：
  
        Magic Number（4 字节，小端序）
        时间戳（8 字节，扩展为 64 位精度）
        字节码大小（4 字节，用于校验文件完整性）
  
    Python3.7+,引入了字节码缓存目录的全新文件格式。后者对文件反编译没有影响，全部填充0即可
  
        Magic Number（4 字节，小端序）
        flags（4 字节，从 Python 3.7 开始引入，默认值为 0。）
        文件哈希值（8 字节，取代时间戳和大小信息，用于更强的文件完整性校验）

* 字节码内容：存储程序的操作指令。

# **3. pyc 逆向通用解题步骤**

## 3.1 检查文件的版本

- 用die或者exeinfo（或者其他图形化工具）来分析文件类型和版本。

- 使用 `file`或者`binwalk`命令分析文件头
  
      file example.pyc

- 根据版本号选择合适的反编译工具。
  
  - 示例：
  * Python 3.7：`uncompyle6`
  * Python 3.9+：`pycdc`（据说推荐，有待实践）

## 3.2 提取.pyc文件

- 使用工具pyinstxtractor.py提取.pyc文件
  
  
  
  https://img.cdn1.vip/i/693aab314fa5d_1765452593.png
  
  

- 使用方法：在该pyinstxtractor.py文件所在目录打开终端
  
  ```
  #在目录栏输入cmd
  python pyinstxtractor.py [文件完整路径]
  ```
  
  这条指令的意思是用python解释器运行pyinstxtractor.py脚本，并把这个.exe文件作为参数传入。
  
  输入完成后文件目录下会出现一个文件名_extracted文件夹
  
  `如图放到同一根目录下，再cmd中运行就可提取到一个文件夹`
  
  
  
  https://img.cdn1.vip/i/693aabc746742_1765452743.webp
  
  

## 3.3 直接反编译

（使用方法均是把文件放到工具的根目录下）

- 方法1：直接用`uncompyle6`
  
      uncompyle6 -o output_dir example.pyc
  
  输出的`.py`文件可能可以直接使用

- 方法2：使用`pycdc`
  
      pycdc example.pyc > output.py

## 3.4 根据反编译代码就可以分析了



https://img.cdn1.vip/i/693ab54205d3c_1765455170.webp

- 在这里就可以看到真正的主函数是mypy，然后我们就可以在解包出来的文件中找到这段函数放入ida中去逆向分析

在ida中f12定位cheak函数

https://img.cdn1.vip/i/693ab6deac4bc_1765455582.webp

- 通过两个运算函数`sub_36F4D1430 & sub_36F4D149C`可以得知这是一个RC4加密

https://img.cdn1.vip/i/693aba9e0e38e_1765456542.webp



- 在将密文和密钥直接带入解密函数
  
  https://img.cdn1.vip/i/693aba28bef6b_1765456424.webp

- 接着运行就可得到flag
  
  https://img.cdn1.vip/i/693abaee5d6af_1765456622.png

- 当然这属于简单题，下面是其他情况

## 3.5 无法直接反编译的情况

- 情况1：魔改字节
  
  - 使用 `marshal` 解析原始数据：
    
    ```
    import marshal
    
    with open('example.pyc', 'rb') as f:
        f.read(16)  # 跳过头部
        code_obj = marshal.load(f)
        print(code_obj)
    ```
    
    这里运用了py中的 `marshal`模块
+ 情况2：动态加密
  
  - 这里需要结合`pycdas` 进行动态分析
  
  - 在执行时注入调试钩子或打印关键变量
  
  - （具体还没实践，最近暂时先放一放）

### 3.5.1经过修改后运行

- 若需要动态修改字节码逻辑，可以直接将字节码导出为 `.py` 文件后重新生成 `.pyc` 文件
  
  ```
  python -m py_compile modified.py
  ```



# 关于py中数据的序列化和反序列化模块

- [ ] | `模块` | 功能特点 | 兼容性 | 适用场景 |
  | ---- | ---- | --- | ---- |

- [ ] | `marshal` | 速度快，主要用于 Python 内部数据处理 | 不保证跨 Python 版本兼容，主要服务于 `.pyc` 文件 | Python 内部字节码存储、临时数据的快速读写 |
  | --------- | ---------------------- | -------------------------------- | ------------------------ |

- [ ] | `pickle` | 能处理更广泛的 Python 对象类型，支持自定义序列化行为 | 可通过选择合适协议实现一定程度的跨版本兼容 | 通用的对象持久化和网络传输，需要处理复杂对象和自定义序列化逻辑 |
  | -------- | ------------------------------ | --------------------- | ------------------------------- |

- [ ] | `json` | 数据以文本形式存储，具有良好的可读性和跨语言兼容性 | 跨语言支持好，但只支持 Python 内置类型的子集 | 数据需要在不同语言或系统之间交换的场景 |
  | ------ | ------------------------- | -------------------------- | ------------------- |

 Python `marshal` 模块：序列化 Python 字节码与安全隐患的参考文献

```
https://www.zyxy.net/archives/11198
```









# <font style="color:rgb(38, 38, 38);">下周待做事项</font>

# <font style="color:rgb(38, 38, 38);">本周学习的知识分享</font>

# <font style="color:rgb(38, 38, 38);">本周学习总结</font>

# <font style="color:rgb(38, 38, 38);">杂项</font>
