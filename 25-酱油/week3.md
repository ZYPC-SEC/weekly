# <font style="color:rgb(38, 238, 38);">完成事项</font>

+ [HNCTF 2022 Week1]贝斯是什么乐器啊？
  这题先找到main函数之后f5看伪代码
  
  ```
  _main();
   puts("please input your flag:");
   scanf("%s", Str);
   for ( i = 0; i < strlen(Str); ++i )
     Str[i] -= i;
   base64_encode((__int64)Str2, Str);
   if ( !strcmp(enc, Str2) )
     printf("yes!");
   else
     printf("error");
   return 0;
  ```
  
  - 先是有第一部分的加密（？）运算
  
  ```
  for ( i = 0; i < strlen(Str); ++i )
     Str[i] -= i;
  ```
  
  便利Str数组中的每一个数，然后取出将他的ASCII减掉对应索引的值
  
  - 然后就是base64加密
  
  ```
  base64_encode((__int64)Str2, Str);
  ```
  
  在点到函数内部
  
  ```
    v3 = strlen(a2);
    if ( v3 % 3 )
      v6 = 4 * (v3 / 3 + 1);
    else
      v6 = 4 * (v3 / 3);
    *(_BYTE *)(v6 + a1) = 0;
    v5 = 0;
    v4 = 0;
    while ( v6 - 2 > v5 )
    {
      *(_BYTE *)(a1 + v5) = aAbcdefghijklmn[(unsigned __int8)a2[v4] >> 2];
      *(_BYTE *)(a1 + v5 + 1LL) = aAbcdefghijklmn[(16 * (a2[v4] & 3)) | ((unsigned __int8)a2[v4 + 1] >> 4)];
      *(_BYTE *)(a1 + v5 + 2LL) = aAbcdefghijklmn[(4 * (a2[v4 + 1] & 0xF)) | ((unsigned __int8)a2[v4 + 2] >> 6)];
      *(_BYTE *)(a1 + v5 + 3LL) = aAbcdefghijklmn[a2[v4 + 2] & 0x3F];
      v4 += 3;
      v5 += 4;
    }
    if ( v3 % 3 == 1 )
    {
      *(_BYTE *)(v5 - 2LL + a1) = 61;
      *(_BYTE *)(v5 - 1LL + a1) = 61;
    }
    else if ( v3 % 3 == 2 )
    {
      *(_BYTE *)(v5 - 1LL + a1) = 61;
    }
    return putchar(10);
  ```
  
  在点aAbcdefghijklmn可以看base对应的码表是否有被魔改，这里没有，找到密文直接解密就可以
  密文在比较函数中可以找到
  
  ```if
  if ( !strcmp(enc, Str2) )
      printf("yes!");
  ```
  
  在其中的enc中就可以找到密文
  之后再逆推就可以，先解密64，再跑解密代码。
  
  ```
  #include<stdio.h>
  
  int main() {
      char a[22] = "NRQ@PAu;8j[+(R:2806.i";
      char b[22];
      char c;
      for (int i = 0; i < 21; i++) 
      {
          printf("%c\n", a[i]);
          printf("%c", a[i] += i);
      }
  }
  ```
- [SWPUCTF 2022 新生赛]base64-2
  
  - 大致步骤一样找对应密文啥的就不说了，说不一样的
  
  - ```
    v6[v2] = off_4018[(unsigned __int8)a1[v3] >> 2];
      v6[v2 + 1] = off_4018[(16 * a1[v3]) & 0x30 | ((unsigned __int8)a1[v3 + 1] >> 4)];
      v6[v2 + 2] = off_4018[(4 * a1[v3 + 1]) & 0x3C | ((unsigned __int8)a1[v3 + 2] >> 6)];
      v6[v2 + 3] = off_4018[a1[v3 + 2] & 0x3F];
    ```
  
  - 打开off_4018之后可以看到aNopqrstuvwxyza继续点可以看到码表
  
  - 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm0123456789+/'
  
  - ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/（正常base64码表，显然不大一样，在代码里面改。）
  
  - 同样密文在对比函数中的s2就能找到了，然后塞到自己程序里面就行
  
  ```
  aGyagd1etr3acgk db 'GyAGD1ETr3AcGKNkZ19PLKAyAwEsAIELHx1nFSH2IwyGsD==',0
  ```
  
  GyAGD1ETr3AcGKNkZ19PLKAyAwEsAIELHx1nFSH2IwyGsD==            密文
  直接换表然后解码就行，但是我自己的代码解码完是一堆乱码，一直没成功，改用锤子解码了。。。。。。

- [SWPUCTF 2022 新生赛]upx
  1.先拉die里面看看，其实直接拉upx也行毕竟他都写了
  然后能直接脱壳，无魔改
  2，再放到ida里面看main
  
  ```
  qmemcpy(v4, "LQQAVDyWRZ]3q]zmpf]uc{]vm]glap{rv]dnce", sizeof(v4));
    v5 = 127;
    for ( i = 0; i <= 38; ++i )
    {
      if ( (v6[i] ^ 2) != v4[i] )
      {
        printf_0("\nwrong flag");
        return 0;
      }
    }
    printf_0("\nflag is right");
  ```
  
  上面代码就能看出，把v4里的每一个字符与2亦或就能得到flag。
  
  ```
  #include<stdio.h>
  
  int main()
  {
      char Str[39] = "LQQAVDyWRZ]3q]zmpf]uc{]vm]glap{rv]dnce";
      char* p = Str;
      printf("与0异或：");
      while (*p != '\0')
      {
          putchar((*p) ^ 2);
          ++p;
      }
  }
  
  ```

- [MoeCTF 2022]ezTea
  本体把delta值改了一下，然后就是把tea加密算法顺序调换，加改成减，把加密程序翻一下就行
  然后k他已经给了就1，2，3，4不用改，最后把他给的pdf里面有正确flag的输出值，直接套tea就能出flag。

- [FSCTF 2023]EZRC4
  在main函数中直接给出密钥了和密文了(  strcpy(key, "wanyuanshenwande");  )函数名字就直接是rc4_crypt。
  (偷懒可以直接动调，在return函数之前在加密函数之后f9打断点，然后直接运行看到几个地址
  ![50399135-67a2-414e-b068-6a1c5fb80321](file:///C:/Users/1/Pictures/Typedown/50399135-67a2-414e-b068-6a1c5fb80321.png)
  最上面那个就有flag
  ![e59632e9-911d-4e96-8c59-34be96ba9910](file:///C:/Users/1/Pictures/Typedown/e59632e9-911d-4e96-8c59-34be96ba9910.png)
  )
  写脚本的话这题给的信息比较全，key和data都在main里面

- *[LitCTF 2023]enbase64

自己做的时候一头雾水...看了解析应该是有一段改码表的加密basechange(Source)作为该表程序但是他并未直接给出换码后的表，所以要是想拿到码表就只用复制一下加密函数，之后再把result printf一下就能拿到改过的码表，然后接下来的就是老套路找密文了，拿到密文和加密的码表后，直接带入解码函数就行。这题的主要就是看出加密base64原码表的加密函数然后通过加上输出加密函数结果的程序跑一边，拿到加密后的码表。

# <font style="color:rgb(238, 38, 38);">下周待做事项</font>

+ 
  
  # <font style="color:rgb(38, 838, 38);">本周学习的知识分享</font>

# <font style="color:rgb(438, 38, 38);">本周学习总结</font>

## 1.UPderX如何识别？如何脱壳？如何加壳？

- upx在die中可以直接识别。（在不考虑手脱的情况下）一般将要脱壳程序放到upx目录下，然后再目录中打开cmd。若魔改了upx头需要先拖到010 editor中改回upx头否则upx检查不到加壳

- 在cmd中输入upx -d （把文件脱进来）回车绿色就托克成功。

- 查看其他指令 upx -h

- upx -1 要加壳的程序名.exe       （更快

- upx -9 要加壳的程序名.exe       （更好的压缩率    

- 加壳 将文件放到upx根目录下----cmd----upx （把文件拖进来） 完成加壳

## 2.Base64编码的特征？不用工具怎么解？逆向程序时如何识别？有什么变体？

### 特征

- ==代替空字符（通常在结尾至于异常情况还没考虑），（一个字符二进制化为8为---3个为一组为24位-----分成4组一组6位-----每6位按照十进制化为数值----根据base64表提出字符=---得到结果）根据加密过程可得知最后的结果一定是4的倍数。

### 不用工具

- 跑代码（有时候能跑出有时候是乱码，还没整明白）

### 识别：

- 实操经验不多，主要看比较函数中的码表，或者看看是否有将字符三组三组分的函数。

### 变体：

- 可以改码表

- 为了避免在URL中出现     +  和 / 字符，可以将它们分别替换为  .  和__。
  
  

## 3. RC4、TEA算法的实现过程？逆向中如何识别？

- # TEA

- tea算法的主要特征表现在 sum 和 delta 变量，以及 3行核心加密 中出现的 右移4左移5 ，两行各有3个小括号互相异或在题目中看到这些特征时就应该警醒这是tea

- 加密

- ```加密
  void tea_enc(uint32_t* v, uint32_t* k) {
      uint32_t v0 = v[0], v1 = v[1];  // v0、v1分别是明文的左、右半部分
      uint32_t sum = 0;               // sum用作加密过程中的一个累加变量
      uint32_t delta = 0xd33b470;     //作为sum每次累加的变化值，题目中往往会修改此值
      for (int i = 0; i < 32; i++) {  // tea加密进行32轮
          //以下3行是核心加密过程，题目中往往会对部分细节做出修改（但由于异或的对称性质，根本不需要记，写解密函数时照抄就行了）
          sum += delta;
          v0 += ((v1 << 4) + k[0]) ^ (v1 + sum) ^ ((v1 >> 5) + k[1]);
          v1 += ((v0 << 4) + k[2]) ^ (v0 + sum) ^ ((v0 >> 5) + k[3]);
      }
      // v0和v1只是加密的临时变量，因此加密后的内容要还给v数组
      v[0] = v0;
      v[1] = v1;
  }
  ```

- 解密

```
void tea_dec(uint32_t* v, uint32_t* k) {
    uint32_t v0 = v[0], v1 = v[1];  // v0、v1分别是密文的左、右半部分
    uint32_t delta = 0xd33b470;     //作为sum每次累加的变化值，题目中往往会修改此值
    uint32_t sum = 32 * delta;      //此处需要分析32轮加密结束后sum的值与delta的变化, 以此处加密为例子，32轮每次sum+=delta，因此最后sum=32*delta
    for (int i = 0; i < 32; i++) {  // tea加密进行32轮
        //根据加密时的顺序颠倒下面3行的顺序，将加法改为减法（异或部分都是整体，不用管），就是逆向解密过程
        v1 -= ((v0 << 4) + k[2]) ^ (v0 + sum) ^ ((v0 >> 5) + k[3]);
        v0 -= ((v1 << 4) + k[0]) ^ (v1 + sum) ^ ((v1 >> 5) + k[1]);
        sum -= delta;
    }
    // 因此解密后的内容要还给v数组
    v[0] = v0;
    v[1] = v1;
}
```

**无论明文是什么形式、有多长，解密时一定是每次传入两个uint32_t（32位无符号整数）**



# RC4

- RC4是一种流加密算法，其工作原理可以分为两个主要部分：密钥调度算法KSA和伪随机生成算法PRGA

1.KSA(密钥调度算法):



2.PRGA(伪随机生成算法):



来自某位知名学长的代码

```
#include <stdio.h>  
#include <stdlib.h>  

void swap(unsigned char* a, unsigned char* b) // 交换两个字节  
{  
    unsigned char temp = *a;  
    *a = *b;  
    *b = temp;  
}  

void RC4_enc(unsigned char* plaintext, int length, const char* key)  // RC4加密函数  
{  
    int i, j;  
    unsigned char* S;  
    unsigned char k[256];  
    int keylen = 0;  

    while (key[keylen] != '\0')   
    {  
        keylen++;  
    }// 计算密钥长度  

    for (i = 0; i < 256; i++)   
    {      
        k[i] = key[i % keylen];  
    }    // 初始化密钥数组k  

    S = (unsigned char*)malloc(256 * sizeof(unsigned char));      
    for (i = 0; i < 256; i++) {  
        S[i] = i;  
    }// 初始化S盒  

    j = 0;  
    for (i = 0; i < 256; i++) {  
        j = (j + S[i] + k[i]) % 256;  
        swap(&S[i], &S[j]);  
    }// 打乱S盒  

    i = 0;  
    j = 0;  
    for (int n = 0; n < length; n++) {  
        i = (i + 1) % 256;  
        j = (j + S[i]) % 256;  
        swap(&S[i], &S[j]);  
        int t = (S[i] + S[j]) % 256;  
        plaintext[n] ^= S[t];  
    }// 进行加密  

    free(S);  
}  

int main() {  
    unsigned char plaintext[] =   
    {  
        0x11,0x45,0x14  
    };//此处为密文  
    const char key[] = "Key";  //此处为秘钥  
    RC4_enc(plaintext, sizeof(plaintext), key);  

    for (int i = 0; i < sizeof(plaintext); i++)  
        printf("%02X ", plaintext[i]);  
    printf("\n");    // 输出加密后的密文  

    return 0;  
}  

```

### 什么是 RC4？

RC4 是一种对称流密码算法，特点是使用简单且高效的密钥流生成机制。RC4 的核心思想是将密钥扩展成伪随机字节流（称为密钥流），并通过按位异或操作（XOR）实现加解密。

### RC4 的工作原理

<img title="" src="file:///C:/Users/1/Pictures/Typedown/4c790962-6176-4da5-a510-f2b231457e39.png" alt="4c790962-6176-4da5-a510-f2b231457e39" style="zoom:50%;">

RC4 算法分为两个阶段： 

-  **密钥调度算法（Key Scheduling Algorithm, KSA）** 
  KSA 用于初始化 256 字节的 S 数组，并根据用户提供的密钥对 S 数组进行置换。

- **伪随机数生成算法（Pseudo-Random Generation Algorithm, PRGA）** 
  PRGA 基于 S 数组生成伪随机字节流，供加解密使用。

### 密钥调度算法（KSA）

   1-初始化一个长度为 256 的数组 S ，值为 S[i] = i ，其中 i 是索引。

   2-根据密钥对数组 S 进行置换: `j=(j+S[i%len(K)])`交换 S[i] 和 S[j] 。

### 伪随机数生成算法（PRGA）

- 初始化两个索引变量 i, j = 0 。

- 根据 S 数组生成伪随机字节流：

- <img src="file:///C:/Users/1/Pictures/Typedown/784d1c1d-722a-48cf-91d8-34b3c83adaf0.png" title="" alt="784d1c1d-722a-48cf-91d8-34b3c83adaf0" style="zoom:67%;">

识别的话较长度为256的数组，三个关键变量S-Box，密钥K char key[256]，临时向量k 长度也为256

# <font style="color:rgb(38, 438, 38);">杂项</font>

# 面试题

# base64

这题的c语言有几个问题导致运行不了

1.#include "stdio.c"这个头文件的书写应该是  <stdio.h>

2.

# 04题

分段来看

共用体

``` 
union zypc {
    int z;      // 4字节（32/64位系统一致）
    char y;     // 1字节
    short p;    // 2字节
    float c;    // 4字节（32/64位系统一致）
};
```

这一组是共用体，所有成员共享内存，内存大小由 最大的成员 决定。本组中 int 和 float都是四字节



结构体

```
struct hello {
    int* z;     // 指针：32位=4字节，64位=8字节
    double y;   // 8字节（32/64位系统一致）
    char p;     // 1字节
    float c;    // 4字节（32/64位系统一致）
};
```

结构体成员按声明顺序分配，需考虑内存对齐，要分 32 位和 64 位系统分析

先看64吧：

**指针 = 8 字节，对齐系数默认 = 成员大小**

* 成员 1：`int* z`（8 字节）→ 起始地址 0，占用 [0-7]（满足 8 字节对齐）。
* 成员 2：`double y`（8 字节，对齐系数 8）→ 起始地址 8（8 是 8 的倍数），占用 [8-15]（无填充）。
* 成员 3：`char p`（1 字节）→ 起始地址 16，占用 [16-16]（满足 1 字节对齐）。
* 成员 4：`float c`（4 字节，对齐系数 4）→ 起始地址 17，需对齐到 4 的倍数（18→20？不，16 是 4 的倍数，`p` 占用 16 后，`c` 从 17 开始，需填充 [17-19]（3 字节），`c` 占用 [20-23]。
* 总大小 24（24 是最大对齐系数 8 的整数倍）→ 因此 `sizeof(h)=24`（64 位）。
* 总而言之就是需要按原本字符的字节大小倍数位填充，如果距离下一个倍数不满足，（比如 上述 float c）则自动补完不足的位置从下一个倍数位置开始加入。

计算zh大小

```
typedef struct hello_zypc {
	hello h;
	zypc z;

}
```

根据内存对齐原则，最大对齐系数，`struct hello` 中的 `double`（8 字节），因此 `struct hello_zypc` 总大小需是 8 的整数倍（这里还没有特别清楚，迟点再整整）

就24 + 4 =28，但是28并不是8的倍数，所以自动填充到下一个8的为主也就是32

所以输出结果就是 24  4  32.





# 05

<img src="file:///C:/Users/1/Pictures/Typedown/b4c95233-2efc-497c-8f40-38e16f39793e.png" title="" alt="b4c95233-2efc-497c-8f40-38e16f39793e" style="zoom:67%;">

这题核心就是     **C 语言中二维数组的内存布局、数组名与指针的关系**

- a[3][3]的二维数组，a是一个三个元素的数组，每个元素是又包含3个数组，a[0]，a[1],a[2],都是数组。

- 4个printf的输出分析：
  
  ##### 1. `printf("%ld\n", sizeof(a[0]))` → 输出 12

计算a[0]的元素所占内存，4*3

##### 2. `printf("%ld\n", sizeof(*(a+1)))` → 输出 12

数组名 `a` 本质是「指向数组首元素的指针」，`a` 的类型是 `int(*)[3]`（指向 “包含 3 个 int 的数组” 的指针，简称「数组指针」）。

指针加法 `a+1` 表示 “跳过一个一维数组的大小”（即跳过 3 个 `int`，偏移 12 字节），指向二维数组的第二行（`a[1]`）

就是指计算a中跳过一个一维的数组，计算第二个一维数组大小

##### 3.`printf("%ld\n", sizeof(*(&a[0])))` → 输出 12

1.因为`a[0]` 是一维数组，`&a[0]`就是取`a[0]` 的地址，然后前面加上*就是从新把他当成指针，也就是  *和&相互抵消，最后计算的依旧是a[0]--就是12

##### 4. `printf("%ld\n", sizeof(&a))` → 64 位输出 8，32 位输出 4

* `&a`：对二维数组整体取地址，得到的是「指向整个二维数组的指针」，类型为 `int(*)[3][3]`（指向 “3 行 3 列 int 数组” 的指针）。

* 64 位系统：指针大小为 8 字节；
* 32 位系统：指针大小为 4 字节。



- 后面就是循环输出通过两个循环i负责外部j负责内部全部遍历就能打印出所有元素







- 汇编，有所搁置：

- 基本语法
汇编程序可以分为三个段-
data段
bss 段
text段
- data段就是用于初始化数据或者常数，可以在这里定义各种值，文件名或者缓冲区大小等
- bss 段是用来声明变量
- text段被用于保持实际的代码该段必须以全局声明_start开头，该声明告诉内核程序从何处开始执行。

- 注释——汇编语言注释以分号（;）开头。它可以包含任何可打印字符，包括空格。
