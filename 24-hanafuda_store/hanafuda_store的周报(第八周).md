# hanafuda_store的周报(第八周)
由于期末周将近，所以本周的部分精力分配在了校内课程的学习上
## [HNCTF 2022 Week1]给阿姨倒一杯Jvav
.class文件反编译，可使用JD-GUI 编辑工具将其反编译为java文件，也可使用[在线网站](https://www.shenmeapp.com/zh-CN/decompiler)进行反编译
得到以下内容
![](http://m.qpic.cn/psc?/V11300AO0tdWfu/LiySpxowE0yeWXwBdXN*SemSeAWLOdNX9F.x.k9RQfKaOHss8abV6as6XM8qM0waVNc1fOL9Y897HyBGVm0kLyezyRKjRBllsNlHExCg18g!/b&bo=JQevBCUHrwQDJwI!&rf=viewer_4)
虽然不太懂java的语法，但也能看懂一二，是输入的字符加上'@'的ASCII码后再与32异或得到的，所以由此我们可以写出解密代码
```C
#include<stdio.h>
#include<string.h>
int main()
{
    //printf("hello world!");
    //return 0;
    int key[] = {180, 136, 137, 147, 191, 137, 147, 191, 148, 136, 133, 191, 134, 140, 129, 135, 191, 65};
    int len = sizeof(key) / sizeof(key[0]);
    for (int i=0; i < len; i++)
    {
        key[i] ^= 32;
        key[i] -= '@';
        printf("%d ", key[i]);
    }
    return 0;
}
//结果：This_is_the_flag_!
```
## [GDOUCTF 2023]Check_Your_Luck
Python解方程，原始C++程序为根据5个方程检验vwxyz五个变量的值是否符合要求

使用z3-solver求解器，安装指令：
```
pip install z3-solver
```
然后编写Python解密脚本：
```Python
from z3 import *

v,w,x,y,z=Reals('v w x y z')
solve(v * 23 + w * -32 + x * 98 + y * 55 + z * 90 == 333322,
      v * 123 + w * -322 + x * 68 + y * 67 + z * 32 == 707724,
      v * 266 + w * -34 + x * 43 + y * 8 + z * 32 == 1272529,
      v * 343 + w * -352 + x * 58 + y * 65 + z * 5 == 1672457,
      v * 231 + w * -321 + x * 938 + y * 555 + z * 970 == 3372367)
#输出结果：[z = 777, y = 1754, x = 677, w = 123, v = 4544]
#故flag为NSSCTF{4544_123_677_1754_777}
```

##  [HNCTF 2022 WEEK2]Try2Bebug_Plus
动态调试+patch修改指令
IDA打开程序，发现一下内容
![](https://a1.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*Sa5mY9KIq2xG.fBzRxAnFcUK.PYmHbcUu1mNzCpseX65YO7iraME1nBGqD5k5uUSKNaS8yuFFpFMV7DASjqVRFk!/b&ek=1&kp=1&pt=0&bo=MQOsATEDrAEDFzI!&tl=1&vuin=934483106&tm=1733641200&dis_t=1733643590&dis_k=39d81c8cfc73d709e32d0cd85cb3d761&sce=60-2-2&rf=viewer_4)
发现sleep函数会让程序中断，故需要patch掉这个指令

先配置远程Linux虚拟机，然后在调试状态下进行patch（因为如果是在静态调试模式下修改指令，只会修改.idb或.i64那个文件，而不会修改exe文件本身，所以要调起来再修改），将sleep函数改为nop空指令。
![](https://a1.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*STOpnVm2Jm9LbwsrAsM0LLC9TWGwETyzdB73AWZVMg8*CgYyRlAZZVBqxH7mNGe5JXr5gScJj4AcJl6bNdB.aKs!/b&ek=1&kp=1&pt=0&bo=YAewA2AHsAMDNxI!&tl=1&vuin=934483106&tm=1733641200&dis_t=1733644307&dis_k=3c39e8d5e328d35a6c3260ebf6407586&sce=60-2-2&rf=viewer_4)
然后进行动态调试，可在栈区储存的`v3`看到flag

## [suctf 2019]signin
逆向+RSA

e、n、密文已知，使用在线质数分解网站分解n得到p、q
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SdHDXesL5DmBwZIQwO6E01uYjx26z1cvGnXg7wMtgXuppeVrMN6r.*XUsDTsQIgxGymlc4edn24ne3KeOj9P3aE!/b&bo=3wggAt8IIAIDFzI!&rf=viewer_4)
然后解密16进制转ASCII码即可得到flag

## [MoeCTF 2022]D_flat
C#逆向，要用到dnSpyex反编译.net文件

按照如图的配置即可反编译得到C#源码（感谢Auto指点）
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SRF7PUy533gvaIR8DBWqHffe3i6zeHTefJ.2UHzGenm28S8FM81QeinFee*uoyLj.Gn4lNXM1IbS*PoVHdrZ9jY!/b&bo=*wkHBv8JBwYDByI!&rf=viewer_4)
可执行选dll 宿主选exe 然后中断在入口点

反编译出的C#代码如下
```C#
using System;
using System.Text;

// Token: 0x02000002 RID: 2
internal class D_flate
{
    // Token: 0x06000001 RID: 1 RVA: 0x00002050 File Offset: 0x00000250
    private static void Main()
    {
        int f = 0;
        int[] flag = new int[]
        {
            109, 111, 101, 99, 116, 102, 123, 68, 95, 102,
            108, 97, 116, 101, 95, 105, 115, 95, 67, 95,
            115, 104, 97, 114, 112, 33, 125
        };
        Console.WriteLine("In music theory, there is a note that has the same pitch as D flat.");
        Console.WriteLine("Do you know it?\nNow plz input your flag:");
        string input = Console.ReadLine();
        byte[] byteArray = Encoding.ASCII.GetBytes(input);
        for (int i = 0; i < input.Length; i++)
        {
            if (flag[i] == (int)byteArray[i])
            {
                f++;
            }
        }
        if (f == flag.Length)
        {
            Console.WriteLine("TTTTTQQQQQQLLLLLLL!!! This is your flag!");
            return;
        }
        Console.WriteLine("QwQ, plz try again.");
    }
}
```
可知只需转为ASCII输出即可
## [SWPUCTF 2023 秋季新生赛]Easy SMC
Linux动调+自修改代码

先调起来，然后单步步进执行，直到出现此提示时
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*Sa3WYkVxSwjTNi4fZZ*JfnxCdWaU6VZDu9RJjODTLHMmtMXNwpXEd9gel5ybbqKqj7IryrZOJqzt5MHC*cZMrMQ!/b&bo=wAJbAcACWwEDByI!&rf=viewer_4)
将其后面的数据按U未定义一下，然后将其直到最下方return处的部分分析为代码，即可得到实际运行的代码。
```C
#include <stdio.h>
int main() {
    unsigned char enc[] = 
    {
        0x4E, 0x52, 0x51, 0x40, 0x50, 0x41, 0x75, 0x61, 0x2B, 0x2C, 0x4F,
        0x25, 0x6A, 0x5C, 0x34, 0x5D, 0x31, 0x65, 0x3A, 0x22, 0x4B, 0x1C,
        0x58, 0x5D, 0x1B, 0x59, 0x4B, 0x1A, 0x58, 0x4C, 0x50, 0x48, 0x3F,
        0x52, 0x11, 0x0E, 0x42, 0x3A, 0x47, 0x09, 0x3C, 0x08, 0x3C, 0x4E,
        0x33, 0x36, 0x02, 0x35, 0x03, 0x2E, 0xFF, 0x05, 0x23, 0x1E, 0x12,
        0x0D, 0x1E, 0xFA, 0x3B, 0xFC, 0x33, 0x06, 0x16, 0x3E,
    };
    int i=0; 
    // 修复循环条件
    for (i = 0; i < 64; i++)
    {
        enc[i] = enc[i]+i;
    }
    printf("%s\n", enc);
    return 0;
}
//NSSCTF{h35Y0viBlAvL5_1nt3re5ting_s31f_m0d1fy_c0d3_18WSHDV3u7oCT}
```
由此即可写出解密代码
## 复习C语言字符串函数
这里的内容经常在逆向分析的题目中出现，但是对于这里的众多字符串函数我之前没能分辨清楚它们的函数原型和功能，导致经常需要回头去查资料，这周末我自己进行了专门的学习，能对后续逆向分析有一定的帮助


部分学习成果展示：
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*Se*.6uqwbhtcELTz6kSqNs7p8j.2RySJqvmZoUx60mYrrbYIAlzoYJcw8maOJ8PtnL9usR4UX*jPzd5kqZa4ync!/b&bo=QAZVCNALwA8HNxk!&rf=viewer_4)