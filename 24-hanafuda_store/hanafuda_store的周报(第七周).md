# hanafuda_store的周报(第七周)
## Sunday
1. 完成上一周的周报
2. 参加了强网杯青少赛，但是结果并不理想，在自己Re方向的题目上并无建树，说明自己还是应该再精进自己的实力，不能停滞不前。做出的题目思路如下：
### whitepic
下载附件后发现没有后缀名，用010Editor打开发现其为一张gif动图，补上后缀名后打开发现其为一张白色图片。
![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*Sbl14QclTteAoV6j39r4scVAMWJuGsjGRvC*SCQkiNeN.PmIN8tuo1oucnSRamVuYfkZNyd0wpd096C1wffAK0w!/b&bo=yQWtAckFrQEDFzI!&rf=viewer_4)
尝试用Stegsolve工具进行分析，由于是动图，于是尝试使用逐帧查看，然后发现该动图有两帧，第二帧写着flag的内容
![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SXX4j75jTunBZc9snfAX8DTnhidvSDAYQLnvbwnZrAXvRL8o23mrgVVORT9kL0fX61Cr8eFSbs7I5ArV3ibqC.w!/b&bo=7QRLA.0ESwMHFzY!&rf=viewer_4https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SXX4j75jTunBZc9snfAX8DTnhidvSDAYQLnvbwnZrAXvRL8o23mrgVVORT9kL0fX61Cr8eFSbs7I5ArV3ibqC.w!/b&bo=7QRLA.0ESwMHFzY!&rf=viewer_4)
### AliceAES
根据提示发现本题是要对“Hello，Bob”这句话进行CBC模式的AES加密后进行输入检验。获取到key和iv的内容后在在线网站上完成加密步骤
![](https://a1.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SeDY41LHqAJqNsHYQXVm6ouFX1NlXB29sJkF.X0HaEq*PxOGPcV3CmGoJ1qUOJFbHsnSl.aM8dm7aQXaBOQb2PQ!/b&ek=1&kp=1&pt=0&bo=Mgb8AjIG*AIDFzI!&tl=1&vuin=934483106&tm=1732442400&dis_t=1732443347&dis_k=d7cc3e02729a2455ea12602993fd7ccc&sce=60-2-2&rf=viewer_4)
然后将结果输入框中即可获得flag
![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*STajq4GZ1Daqzp*VoJDd1Ovjs*Ks*WHHHrl6jCflhpj7OM2LBrbMrEJvCh5xZhLF4r9DH8CPH.uiogkfqC4s*Yk!/b&bo=RASDAkQEgwIDFzI!&rf=viewer_4)
## Monday
还是做题呗
### [WUSTCTF 2020]level3
用IDA分析可知该程序用的是Base64，而且贴脸给了密文，但是解密发现不对，但Base64加密函数却又是正常的。于是从别的函数中发现问题：找到了一个名为`O_OLookAtYou`的函数，内容如下：
![](https://m.qpic.cn/psc?/V11300AO0tdWfu/LiySpxowE0yeWXwBdXN*SbysCzE4KSxyC9VCsUJSKmxpmZIE3BXqSHuHawbFqu7FUOUIl1j1EKNRZdjvPr6Axm2CAPy0JMsbHLoH3m81bJY!/b&bo=NwR7ATcEewEDByI!&rf=viewer_4)
由此可知它修改了 base64_table 中的字符顺序。具体来说，O_OLookAtYou 会交换 base64_table 的前 10 个字符和后 10 个字符的位置，所以用换表Base64解密即可
![](http://m.qpic.cn/psc?/V11300AO0tdWfu/LiySpxowE0yeWXwBdXN*Sd.wv8yogHy3MGV64zA7zMwT58*KMAt3jVdXWaQqFv.9MxE6tQRoAh2*N99jJ**wxyksOjG14W7kEACesT0On3Q!/b&bo=zAflAswH5QIDFzI!&rf=viewer_4)
### [MoeCTF 2022]Base
简单的换表Base64
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SSNLAsdkYD0zhmGWNBb1xCX0HVg7rO.CBch5s4woJ5q8BkjxzzTSc9yZGyBbm7Qi*Cl5rfQ*qRvy92aC4LUQPyk!/b&bo=4gK6AeICugEDFzI!&rf=viewer_4)
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*ScTKYs1mfG.hiF46h6RXOYq5NWKofs*tRa2hj4Pj5YRUNCj1iIxhDvQTmn71pQUC9TLAmE6rrhmshB.oA0WDKaY!/b&bo=kgMwApIDMAIDFzI!&rf=viewer_4)
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SWU6o3m6eS3cb68ClRHPd0PPgdMSiBlszgiCFdkK*Y2U4B35TEUqfuZwQ2wGaEIU09BxlBiI0QZQUPsJyn3BtyE!/b&bo=2ARoANgEaAADFzI!&rf=viewer_4)
### [HNCTF 2022 WEEK2]Packet
怎么捅了Base64窝？？？
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SQ.FtBOj3u..5SvAqwVSkfP*Kqxo7jbdkPgwKwqrytJ9yUQMmNqkUzBjV7pJBHIgad6S29AqcddnWso2FCxN0CU!/b&bo=MAXYADAF2AADFzI!&rf=viewer_4)
## Tuseday
### [HGAME 2023 week2]before_main
用IDA分析，阅读代码可知该程序是在对输入的内容的前`4bit`和后`4bit`进行拆分后储存在数组`v4`中，然后`v4`再与`dword_403000`中的数据一一比较
```C
int __cdecl main(int argc, const char **argv, const char **envp)
{
  int v4[100]; // [esp+0h] [ebp-1CCh] BYREF
  char v5[52]; // [esp+190h] [ebp-3Ch] BYREF
  int j; // [esp+1C4h] [ebp-8h]
  int i; // [esp+1C8h] [ebp-4h]

  memset(v5, 0, 0x32u);
  memset(v4, 0, sizeof(v4));
  scanf(a50s, (char)v5);
  for ( i = 0; i < 50; ++i )
  {
    v4[2 * i] = v5[i] & 0xF;
    v4[2 * i + 1] = (v5[i] >> 4) & 0xF;
  }
  for ( j = 0; j < 100; ++j )
  {
    if ( v4[j] != dword_403000[j] )
    {
      printf(Format, v4[0]);
      return 0;
    }
  }
  printf(aYesYouAreRight, v4[0]);
  return 0;
}
```
由于是`dword_403000`本身是双字型的数据（`int`为4字节），但是定义该数据时却使用的是`db`的伪指令，所以这里实际的有效数据每相隔3个0出现一个
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SV4Vg*Rxm0PAxpPtZx3iVhZhlRtBcyNAfy0deF914RWvseIQJ6VdMbFR9dFU9JlZ6YotfSQCJWIIMYcEp7YrOAI!/b&bo=oANyAaADcgEDFzI!&rf=viewer_4)
```C
#include<stdio.h>
int main()
{
    unsigned char dword_403000[400] =
    {
      0x08, 0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x00, 0x07, 0x00,
      0x00, 0x00, 0x06, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00,
      0x06, 0x00, 0x00, 0x00, 0x0D, 0x00, 0x00, 0x00, 0x06, 0x00,
     //其他数据.......
      0x05, 0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x00, 0x05, 0x00,
      0x00, 0x00, 0x06, 0x00, 0x00, 0x00, 0x02, 0x00, 0x00, 0x00,
      0x07, 0x00, 0x00, 0x00, 0x0D, 0x00, 0x00, 0x00, 0x07, 0x00,
      0x00, 0x00
    };
    char v5[100] = "";
    int i,j;
    for (i = 0;i<100;i++)
    {
        j = 2 * i;
        v5[i] = (dword_403000[4 * (j+ 1)] << 4) | dword_403000[4 * j];
    
    }
    printf("%s", v5);
    return 0;
}//结果为：hgame{encode_is_easy_for_a_reverse_engineer}
```
### [HDCTF 2023]easy_asm
经过分析可得到以下内容
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SezmuBrUTfLJj*w2FrES9NtHvu6kiEx6LjCK54p3bXg8z4WJh9WpA*YHvVg.ZIUBj7GOnUhyYKrSM.Er*bqJ17M!/b&bo=ggTvA4IE7wMDByI!&rf=viewer_4)
密文在这里
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SV9c3z3VDNZ7kSzzKYqbIw8ahAz2P55rx79yL.RN8aS5hnsK1zkWGO2jSxS3iDiY1XPyAHnk1cr3kmOE*PP2fv8!/b&bo=LgQXAS4EFwEDByI!&rf=viewer_4)

## 尝试使用IDA金星Linux远程动态调试
参考资料：[IDA 远程调试展示 https://www.bilibili.com/video/BV15E411Q7wx/?spm_id_from=333.999.0.0&vd_source=f68ecadd2591bdcc41975d6c695dc214](https://www.bilibili.com/video/BV15E411Q7wx/?spm_id_from=333.999.0.0&vd_source=f68ecadd2591bdcc41975d6c695dc214)

[ELF64文件逆向分析知识—[0]搭建动态调试环境https://blog.csdn.net/txx_683/article/details/53454139](https://blog.csdn.net/txx_683/article/details/53454139)

在IDA的`安装目录/dbgsrv`找到`linux_server`或`linux_serverx64`这两个文件，具体选择哪个文件需要视待分析的ELF文件的编译信息而定(64bit/32bit)，把待分析的可执行文件和`linux_serverx64`一起拷贝到装好的Linux虚拟机中。然后在终端运行`linux_serverx64`，这样就在Linux中开启了远程调试端口。

接下来的任务就是在IDA这边进行配置：正常启动IDA打开【Debugger】-【Run】-【Remote Linux debugger】来设置调试
其中，填入信息如下：
| 选项 | 应填入的信息 |
| ---- |  ---- |
| Application |待调试文件在Linux上的路径（包括带调试文件）|
| Director |调试文件所在的文件夹路径|
| Parameters |运行参数，例如运行可执行文件时传递到main函数的命令参数|
| Hostname | Linux的IP地址|
| Port |Linux的端口，这里默认即可，和Linux上运行的linux_serverx64开启的端口一致|
| Password | Linux登陆密码  |

根据Linux终端显示的内容填写内容，然后即可开始调试，其余操作基本与Windows本地动态调试一致。
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SeJgXOfUDYUBU0DyTKyg3cDa3mbzXpdhBQeVnGh7aUFE8kaZjiiwdSxXkxTgvitwte*xmWGMziXg4a5tFemodk8!/b&bo=*wkABf8JAAUDV3I!&rf=viewer_4)
## Wednesday
### [GDOUCTF 2023]Tea
tips：IDA里可选中10进制的数据按h可以将其转换为16进制的数据
本题是Tea加密，解密代码如下：
```C
#include <stdio.h>
void decrypt(unsigned int* value, int* key, int block_count, int delta) {
    int wheel, i;
    int sum;

    for (i = block_count - 2; i >= 0; i--) { // 倒序遍历数据块
        wheel = 33;
        sum = delta * (i + wheel);
        while (wheel--) {
            sum -= delta;
            value[i + 1] -= (sum + key[(sum >> 11) & 3]) ^
                (value[i] + ((value[i] >> 5) ^ (16 * value[i])));
            value[i] -= sum ^ (value[i + 1] + ((value[i + 1] >> 5) ^ (16 * value[i + 1]))) ^
                (sum + key[sum & 3]);
        }
    }
}

int main() {
    int key[] = { 2233, 4455, 6677, 8899 };
    unsigned int value[] = { 0x1A800BDA, 0xF7A6219B, 0x491811D8, 0xF2013328,
                            0x156C365B, 0x3C6EAAD8, 0x84D4BF28, 0xF11A7EE7,
                            0x3313B252, 0xDD9FE279 };
    int delta = 0xF462900;
    int block_count = sizeof(value) / sizeof(value[0]);

    decrypt(value, key, block_count, delta);

    for (int i = 0; i < block_count; i++) {
        printf("%08X ", value[i]);
    }
    printf("\n");

    return 0;
}
```
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SeJg1r1NKCR4DxjZgFe03Ak2xuO8nSZJGumA1H80DHoaHb0OgBGALX6yl77JrwDvqbbcPW6Xl7oLLvzrIkKxXWA!/b&bo=gwOJAYMDiQEDFzI!&rf=viewer_4)
### 学习UPX加壳原理
UPX本质上其实是一种压缩文件的方式，它通过压缩可执行文件的内容从而达到使文件本身变小，便于传输目的，同时也可保护程序无法被IDA等反汇编软件分析。具体方法是先扫描文件，识别如代码段、文件头等数据的不同段（此时会记录程序执行的起始地址），然后将原本的数据进行压缩，最后在程序开头补充一段解压的代码，并将最后的地址指向之前记录的原序执行的起始地址。

此时运行可执行文件，当操作系统加载加壳后的可执行文件时，UPX 的壳程序会首先获得控制权。它会先对压缩和加密的部分进行解压和解密操作，将文件恢复到原始的可执行状态（或者接近原始状态，在一些经过优化的情况下），然后再将控制权交给原始的程序入口点，使得程序能够正常运行。这一过程对于用户来说是透明的，就好像在运行一个没有加壳的普通可执行文件一样
## Tursday
昨天那道Tea加密的题是AI帮忙写的解密代码，还是得自己弄懂Tea加密的原理啊
参考资料：[【动画密码学】TEA(Tiny Encryption Algorithm)|分组加密](https://www.bilibili.com/video/BV1Nu411E7wX/?spm_id_from=333.999.0.0&vd_source=f68ecadd2591bdcc41975d6c695dc214)
自行编写TEA解密代码
```C
#include<stdio.h>

int main()
{
    unsigned int key[] = { 0x01234567, 0x89ABCDEF, 0xFEDCBA98, 0x76543210 }; 
    unsigned int data[] = { 0xD4AB3FFF, 0x1DD13825 }; 
    const unsigned int delta = 0x9E3779B9;
    unsigned int a = delta * 32; 
    int i;

    for (i = 0; i < 32; i++) 
    {
        data[1] -= ((data[0] << 4) + key[2]) ^ (data[0] + a) ^ ((data[0] >> 5) + key[3]);   
        data[0] -= ((data[1] << 4) + key[0]) ^ (data[1] + a) ^ ((data[1] >> 5) + key[1]);
        a -= delta;
    }

    printf("%X %X", data[0], data[1]); 
    return 0;
}
```
昨天题目自己手搓解密代码
```C
#include<stdio.h>
int main()
{
    unsigned int key[4] = {2233,4455,6677,8899};
    unsigned int data[10] = { 0x1a800bda,0xf7a6219b,0x491811d8,0xf2013328,0x156c365b,0x3c6eaad8,0x84d4bf28,0xf11a7ee7,0x3313b252,0xdd9fe279 };
    for (int i = 8; i >= 0; --i)
    {
        const unsigned int delta = 256256256;
        unsigned int sum = delta * (33+i);//原程序中这句sum = 256256256 * i的逻辑说明sum的值与循环次数有关！！！
        for (int j = 33; j > 0; --j)
        {
            sum -= delta;
            data[i+1] -= (sum + key[(sum >> 11) & 3]) ^ (data[i]+((data[i] >> 5) ^ (16 * data[i])));
            data[i] -= sum ^ (data[i+1] + ((data[i+1] >> 5) ^ (16 * data[i+1]))) ^ (sum + key[sum & 3]);
        }
    }
    printf("%X %X %X %X %X %X %X %X %X %X", data[0], data[1],data[2], data[3],data[4], data[5],data[6], data[7],data[8], data[9]);
    return 0;
}
```
### [WUSTCTF 2020]level1
tips：
为什么 (i & 1) != 0 能判断奇偶性？
(i & 1)：
取出 i 的最低位，如果为 1 则是奇数，为 0 则是偶数。
(i & 1) != 0：
判断最低位是否非零，非零说明是奇数。
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SXKAtTJeTDfAzIgjhjlTwyCzYF8rbdqy1CkYhmet.LzQM6bNj2vYCFG7RZw53P5Hb9Z0t7YxjgwE0Iha5ekLWAE!/b&bo=XgTUAV4E1AEDFzI!&rf=viewer_4)
由此写出解密代码
```C
#include<stdio.h>
int main()
{
    int enc[19] = { 198,232,816,200,1536,300,6144,984,51200,570,92160,1200,565248,756,1474560,800,6291456,1782,65536000 };
    for (int i = 1; i <= 19;i++)
    {
        if (i & 1 != 0)
            enc[i - 1] = enc[i - 1] >> i;
        else
            enc[i - 1] = enc[i - 1] / i;
    }
    for(int i = 0; i < 19; i++)
        printf("%c", enc[i]);
    return 0;
    //结果：ctf2020{d9-dE6-20c}
}
```

### [MoeCTF 2022]Hex
misc打过来了？？？
### [MoeCTF 2022]checkin
签到
### [SWPUCTF 2021 新生赛]astJS
ChatGPT一眼丁真直接连结果都生成出来了，实则是json文件逆向
```
npm install -g optionator
```
用指令安装对应工具后，使用如下指令esgenerate 附件.json，还原出JavaScript源代码
```
npm i escodegen -g
```
虽然js还是不太懂，但是可读性更高了，能看得出来是密文在和11异或
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SXPUbdMQaiF76emhpotny3XI4jhBBdM5Q1jwMmLx2ZWgyCj*W82Ew*7IiHPG8s*ZwxBffcI.qWxbPD68hwAcnqg!/b&bo=cwM1AXMDNQEDByI!&rf=viewer_4)
## Friday
休息
## Saturday
### [HZNUCTF 2023 final]signin
UPX头修正+动调+RC4
学习了UPX头的知识后用010Editor将三处要修改的地方改为UPX
动调得到密文
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SYZZHXbpNX5HNCMu4wFO52VnXC6lSFvNkEVqTT*agcnGo1v5lcMJMR7b.EfFeXAcndJji7DUlm5u30KETakjRmI!/b&bo=9AQ6A*QEOgMDByI!&rf=viewer_4)
由反汇编代码直接可以看到秘钥为justfortest

用RC4解密脚本解密
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SQlvHIULoaMbKG29SomWLQ6i3*Iowsp2Sw8eO4fEzgFMChi8ZTpIa*Rt7CcHU4MHoNpXQ3Wuo0SW94gQv88kLrU!/b&bo=GgRAAhoEQAIDByI!&rf=viewer_4)