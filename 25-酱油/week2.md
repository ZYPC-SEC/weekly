# <font style="color:rgb(138, 38, 38);">完成事项</font>

+ 
  
  # <font style="color:rgb(238, 38, 38);">下周待做事项</font>

+ 

# <font style="color:rgb(38, 638, 38);">本周学习的知识分享</font>

## 1.《P   plus》中p101的5.3中：

其中对++n的使用

```
nextnum = (y + n++)*6    #y=2 n=3
nextnum = 30 (结果)
```

书中提到 在n++的使用中<font style="color:rgb(238, 38, 38);">n的值只有在被使用过才进行递增</font>也就是只有当整体的计算式读出结果并赋值给目标数时，n的值才进行递增（++n则相反）

## 2.对re迷宫题的基础类型认识：（例题攻防世界-reverse_re3）

- 一，先是判断有没有加壳（在buuctf中出现了很像花指令的东西，需要先nop掉反调试的指令（由于没在自己的ida上找到该函数对应地址故还没做出那题）才能看到迷宫所需要的移动函数）

- 二，f5，看看伪代码中有什么信息。——通常在main函数中会存在几个函数，我们需要一个个去查看。

- 三，较简单题目像这道例题中可以很轻松的在函数中看到“wasd”（一般以ascii码的方式存在直接选中摁r就能变成字符了）但是我猜正常题目应该都是要通过对其函数进行分析才能知具体按键

```例题中“d”执行的函数
__int64 sub_E23()
{
  if ( dword_202AB8 != 14 )
  {
    if ( dword_202020[225 * dword_202AB0 + 1 + 15 * dword_202AB4 + dword_202AB8] == 1 )
    {
      dword_202020[225 * dword_202AB0 + 1 + 15 * dword_202AB4 + dword_202AB8] = 3;
      dword_202020[225 * dword_202AB0 + 15 * dword_202AB4 + dword_202AB8] = 1;
    }
    else if ( dword_202020[225 * dword_202AB0 + 1 + 15 * dword_202AB4 + dword_202AB8] == 4 )
    {
      return 1LL;
    }
  }
  return 0LL;
}
```

```“s”的
__int64 sub_C5A()
{
  if ( dword_202AB4 != 14 )
  {
    if ( dword_202020[225 * dword_202AB0 + 15 + 15 * dword_202AB4 + dword_202AB8] == 1 )
    {
      dword_202020[225 * dword_202AB0 + 15 + 15 * dword_202AB4 + dword_202AB8] = 3;
      dword_202020[225 * dword_202AB0 + 15 * dword_202AB4 + dword_202AB8] = 1;
    }
    else if ( dword_202020[225 * dword_202AB0 + 15 + 15 * dword_202AB4 + dword_202AB8] == 4 )
    {
      return 1LL;
    }
  }
  return 0LL;
}
```

```w
__int64 sub_A92()
{
  if ( dword_202AB4 )
  {
    if ( dword_202020[225 * dword_202AB0 - 15 + 15 * dword_202AB4 + dword_202AB8] == 1 )
    {
      dword_202020[225 * dword_202AB0 - 15 + 15 * dword_202AB4 + dword_202AB8] = 3;
      dword_202020[225 * dword_202AB0 + 15 * dword_202AB4 + dword_202AB8] = 1;
    }
    else if ( dword_202020[225 * dword_202AB0 - 15 + 15 * dword_202AB4 + dword_202AB8] == 4 )
    {
      return 1LL;
    }
  }
  return 0LL;
}
```

```a
__int64 sub_FEC()
{
  if ( dword_202AB8 )
  {
    if ( dword_202020[225 * dword_202AB0 - 1 + 15 * dword_202AB4 + dword_202AB8] == 1 )
    {
      dword_202020[225 * dword_202AB0 - 1 + 15 * dword_202AB4 + dword_202AB8] = 3;
      dword_202020[225 * dword_202AB0 + 15 * dword_202AB4 + dword_202AB8] = 1;
    }
    else if ( dword_202020[225 * dword_202AB0 - 1 + 15 * dword_202AB4 + dword_202AB8] == 4 )
    {
      return 1LL;
    }
  }
  return 0LL;
}
```

这段是对，要是代码中没有给明位移字符的含义，需要对函数进行分析才能得出具体哪个字符代表什么。但是我其实也不知道到底有没有这种出题方式，只是借这样的方法对此类题目有一个更深的理解。

上述代码中大部分内容其实是一样的，唯一出现的位移点就是在对迷宫变量的第一次运用中。















迷宫地图函数（例题）：

```
unsigned __int64 sub_86C()
{
  int i; // [rsp+0h] [rbp-10h]
  int j; // [rsp+4h] [rbp-Ch]
  unsigned __int64 v3; // [rsp+8h] [rbp-8h]

  v3 = __readfsqword(0x28u);
  for ( i = 0; i <= 14; ++i )
  {
    for ( j = 0; j <= 14; ++j )
    {
      if ( dword_202020[225 * dword_202AB0 + 15 * i + j] == 3 )
      {
        dword_202AB4 = i;
        dword_202AB8 = j;
        break;
      }
    }
  }
  return __readfsqword(0x28u) ^ v3;
}
```

地图函数一般出现在移动函数之前或者结尾可以放这两个地方着重关注一下



看上面函数中很明显出现了一个通过两个for循环嵌套的二维数组（出现类似二维数组就可以注意是否是迷宫地图）而在for函数中可以得到函数的长款，上述中就是一个15*15的地图大小



在上述地图函数中含有两个很明显的变量，dword_202020，dword_202AB0，dword_202AB4，dword_202AB8。

可以一个个点进去查看，基本出现一大串字符的就是迷宫地图

（而其他可能是行，或者列，又或者是多个迷宫下的迷宫序号）

dword_202020：其实就是题目给的地图，可以双击进去看看（shift+e 提取数据）

dword_202AB0：代表哪个迷宫，此题有3个迷宫（至于为什么后文会提及）

dword_202AB4：代表行（因为15*，说明可能是一行15个数字，大胆猜测！）

dword_202AB8：代表列

```(举个例子而已，不打全了)
dd 5 dup(1), 3 dup(0), 1, 6 dup(0), 5 dup(1), 3 dup(0)
.data:00000000002020F4                 dd 1, 6 dup(0), 5 dup(1), 3 dup(0), 5 dup(1), 2 dup(0)
.data:000000000020214C                 dd 5 dup(1), 7 dup(0), 1, 2 dup(0), 5 dup(1), 7 dup(0)
.data:00000000002021B8                 dd 1, 2 dup(0), 5 dup(1), 7 dup(0), 2 dup(1), 0, 5 dup(1)
.data:0000000000202214                 dd 8 dup(0), 1, 0, 5 dup(1), 8 dup(0), 4, 0, 4Dh dup(1)
.data:00000000002023AC                 dd 0Dh dup(0), 2 dup(1), 0, 3, 5 dup(1), 6 dup(0), 2 dup(1)
.data:0000000000202424                 dd 0, 2 dup(1), 3 dup(0), 1, 6 dup(0), 2 dup(1), 6 dup(0)
.data:0000000000202478                 dd 1, 6 dup(0), 2 dup(1), 0, 2 dup(1), 
```

当我们成功找到函数之后就可以导出地图了（通过shift+e就可以实现导出地图），然后再通过记事簿的ctrl+h唤出替换栏替换掉其他不需要的字符（回车键好像只能通过word中的/^p来替换）

但是！！！这还不是真正的迷宫。需要通过对应的脚本将这份原始数据转换为地图

```python
# 输入需要处理的字符串  
input_string = input("请输入需要处理的字符串：")  

# 将所有字符连起来，去掉换行符  
output_string = input_string.replace("\n", "")  
ZeK1D = output_string.replace(" ", "")    
​
def extract_chars(input_string):  
    # 将输入字符串分割为每四位  
    chunks = [input_string[i:i+4] for i in range(0, len(input_string), 4)]  

    # 提取每四位中的第一位字符  
    first_chars = [chunk[0] for chunk in chunks if chunk]  

    # 将字符连在一起并输出  
    output= ''.join(first_chars)  
    print(output)  


# 调用函数并输出结果  
extract_chars(ZeK1D)
```

而之后就需要通过最开始得到的迷宫大小（15*15）来划分迷宫。最后通过“wasd“或其他的字符来走出这个迷宫，然后输入的移动顺序就是flag（通常会用md5加密一下才是flag具体看函数要求）。



### 对xor （exclusive OR）：亦或程序初步了解：

- 在xor中，不考虑壳的情况下，先看看伪代码寻找是否有关键字这种特殊函数。

- 通常在伪代码中存在一个函数将输入量与global变量进行比对看是否相等，若相等则进入到下一步亦或。

- xor中的亦或操作通常是在global的数据中取前一位与后一位进行亦或，所以在解密中通常需要编写py或者c的脚本，将global中的数据提取出来，在看伪代码的函数写一段新的函数。

- 将取到的global以16进制导出，输入到py函数中，即可得到flag。











# <font style="color:rgb(38, 38, 438);">本周学习总结</font>

这周还是re题的浅浅认知和c，然后应为迷宫遇到需要nop了所以下周先把花指令和nop所需要的汇编顺带着看一下。

# <font style="color:rgb(198, 38, 38);">杂项</font>


