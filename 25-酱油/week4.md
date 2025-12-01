# <font style="color:rgb(38, 438, 38);">完成事项</font>

+ 这周主要搞了动调和c语言
  
  # 动态调试：
  
  动态调试的话可以用ida或者是64ollydbg来分析，dbg我还不会，先整ida。
  
  # 1-调用未引用函数
  
  不考虑脱壳，关于暂且命名为，隐藏函数（自己编的自己好归类），就是并没有再主函数中被调用的函数，而flag就可能藏在其中，为了调用这个函数，我们可以通过ida修改eip来跳转到ques函数，以下为步骤；
  1.先记下你要调用的函数地址（以下是例子）
  ![eaf08257-db89-4d41-b1d6-9efbccf7b8ed](file:///C:/Users/1/Pictures/Typedown/eaf08257-db89-4d41-b1d6-9efbccf7b8ed.png)
  记下ques的引用地址  这里是0x00401520；
  2.之后再主函数运行的途中随便下一个断点：
  ![20057d17-f7f5-4adb-b29b-911b33b36f5f](file:///C:/Users/1/Pictures/Typedown/20057d17-f7f5-4adb-b29b-911b33b36f5f.png)
  3.然后在调试器中进行调试
  ![04f21d2d-b92e-43d1-9bcb-cbc46f636168](file:///C:/Users/1/Pictures/Typedown/04f21d2d-b92e-43d1-9bcb-cbc46f636168.png)
  之后能看到main函数的EIP地址为0x00401761，之后我们需要双击这串地址就可以将其修改为我们要运行的函数的地址。
  ![46360291-30cf-4652-b241-cd37e30ff40e](file:///C:/Users/1/Pictures/Typedown/46360291-30cf-4652-b241-cd37e30ff40e.png)
  然后再运行一下就能看到这串没有被引用的函数在干嘛了
  ![d97ecdd2-d21d-4e71-8017-9e4c3599f035](file:///C:/Users/1/Pictures/Typedown/d97ecdd2-d21d-4e71-8017-9e4c3599f035.png)
  
  # 2-获取内容数据
  
  在过往的一道迷宫图中半天拿不出地图，这时候动态就排上用场了，当发现题目中涉及到的程序内部值无法查看和获取时，可以通过动调获取内容数值。
  1.迷宫先找迷宫
  
  <img title="" src="file:///C:/Users/1/Pictures/Typedown/8ce1f759-a2c9-461e-8c9a-3a1a2e41e2ab.png" alt="8ce1f759-a2c9-461e-8c9a-3a1a2e41e2ab" style="zoom:67%;">
  
  <img src="file:///C:/Users/1/Pictures/Typedown/6cae87e8-6db7-456f-b3ab-3ac69fbdcd47.png" title="" alt="6cae87e8-6db7-456f-b3ab-3ac69fbdcd47" style="zoom:80%;">
  
  ![ba0f082c-8cf5-4019-9e85-2284bb12861e](file:///C:/Users/1/Pictures/Typedown/ba0f082c-8cf5-4019-9e85-2284bb12861e.png)
  依次点击光标所在位置的有关map函数，直到最后跳转出map的地址函数。如图中是0000000000407040但是再点进去会发现看不到地图
  ![bb7c385f-820c-490e-a8d1-ab302fccc2cd](file:///C:/Users/1/Pictures/Typedown/bb7c385f-820c-490e-a8d1-ab302fccc2cd.png)
  2.接下来我们需要再地图函数中下断点。
  
  <img title="" src="file:///C:/Users/1/Pictures/Typedown/a65f35dd-a7bc-4aee-bbc2-2cee125cb633.png" alt="a65f35dd-a7bc-4aee-bbc2-2cee125cb633" style="zoom:67%;">
  
   运行后结果
  
  <img title="" src="file:///C:/Users/1/Pictures/Typedown/59407058-e582-4685-b582-bfbba2ca0157.png" alt="59407058-e582-4685-b582-bfbba2ca0157" style="zoom:67%;">
  
  在任务栏处随便输入点什么
  ![14f5cf7f-ddfb-438b-a416-4f107ff242c7](file:///C:/Users/1/Pictures/Typedown/14f5cf7f-ddfb-438b-a416-4f107ff242c7.png)
  然后再找到map函数点进去就能看到地图了。
  
  # 3-匹配绕过
  
  1.通常就是在有比较的时候，通过在比较的地方下断点，然后运行就可以看到匹配值是多少。
  ![ad38b989-80a2-457f-9145-e963f305b3ca](file:///C:/Users/1/Pictures/Typedown/ad38b989-80a2-457f-9145-e963f305b3ca.png)
  在这里有一个cmp像是对比函数的地方，故可以尝试在对比结束的地方下断点，而上面的string1和2就有可能是密码和输入值。
  ![b592ee50-a4ea-4ce9-953a-21f6c0282f78](file:///C:/Users/1/Pictures/Typedown/b592ee50-a4ea-4ce9-953a-21f6c0282f78.png)
  在比较函数结尾下断点然后运行
  ![73ca5567-b1d5-4473-8785-691e9255f4ea](file:///C:/Users/1/Pictures/Typedown/73ca5567-b1d5-4473-8785-691e9255f4ea.png)
  然后再在输入栏处随便输入什么提交，在这里用户名给了提示，然后第二行随便输，但是要长度符合他限制，然后再接着运行就能看到结果，但是在这题里面最后并没有直接输出flag，我看了下其他人的也并没有说明flag，有点不懂。

# 4-修改判断函数跳转值

 像很多game类型的题目会将目标值设到非常高，大佬硬打也不是没有，正常就需要修改类似gat flag函数然后跳过拿高分阶段直接拿到flag

这个还有待修正





# 汇编

寄存器

因为 CPU 的运算的速度远高于内存的读写速度，为了避免被内存的读写速度拖慢，CPU 自带缓存，但是 CPU 缓存还是不够快，所以出现了更快的寄存器

CPU 自带寄存器，用于储存最常用的数据

CPU 优先读写寄存器，再由寄存器跟内存交换数据

### 通用寄存器

通用寄存器是一种通用型的寄存器，用于传送和暂存数据，也可以参与算数逻辑运算，并保存运算结果

所说的 32 位 CPU、64 位 CPU 中的 ”位“，指的是寄存器的大小，32 位 CPU 的寄存器大小为 4 个字节，64 位 CPU 的寄存器大小为 8 字节

| 32 位通用寄存器 | 通用寄存器的作用                                      |
| --------- | --------------------------------------------- |
| EAX       | 累加器，在乘法和除法指令中被自动使用<br>返回值，在 Win32 中一般用作函数的返回值 |
| EBX       | 基地址寄存器，在内存寻址时存放基地址                            |
| ECX       | 计数器，CPU 自动使用 ECX 作为循环计数器，在字符串和循环操作中常用         |
| EDX       | 数据寄存器，常用来放整数除法产生的余数                           |
| ESP       | 堆栈指针计数器，指向上个栈帧的栈顶，ESP 一般不参与算数运算，而是用来寻址堆栈上的数据  |
| EBP       | 指向最上面一个栈帧的地步，EBP 由高级语言用来引用参数和局部变量             |
| EIP       | 存放下一条要执行的指令地址                                 |
| ESI       | 一般在字符串操作时指向源串                                 |
| EDI       | 一般在字符串操作时指向目标串                                |

16 位通用寄存器为

* AX
* BX
* CX
* DX
* SI
* DI
* BP
* SP

其中，前四个 16 位通用寄存器还可以分为高 8 位和低 8 位两个独立的寄存器

# <font style="color:rgb(38, 38, 38);">下周待做事项</font>

+ 

# <font style="color:rgb(38, 38, 38);">本周学习的知识分享</font>

# <font style="color:rgb(38, 38, 38);">本周学习总结</font>

# <font style="color:rgb(38, 38, 38);">杂项</font>


