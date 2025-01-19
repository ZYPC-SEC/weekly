# hanafuda_store的周报（第九周 1.12-1.19）
## 重建个人博客
由于之前创建个人博客时时间较为紧张，故当时的成果较为简陋。进入时间较为充裕的寒假我便重建了自己的博客，并配置了`butterfly`主题以及一些个性化设置，具体成果可点击[链接](hanafudastore.github.io)查看。

## 编写博文
在重建博客后上线了`《汇编语言》总结`和`逆向工程常见密码总结`两篇文章，分别总结了王爽的《汇编语言》中的各种指令、寄存器的使用和逆向中常见的`RC4`、`TEA`、`XTEA`、`XXTEA`等算法的加密与解密原理及其C语言实现，可在上文的链接处查看文章。

## 刷题
保留节目
### [HDCTF 2023]enc
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SdpT1uyoNKFZuL10*6uj4rUjrF0yC5XVe.v5QbJ4eXxbxNMeL4lYMdcB8ZgTqqut2*53VDb0sCYr*A4YAN9KXlQ!/b&bo=fgMHA34DBwMDFzI!&rf=viewer_4)
进入main_0函数，经分析可知`"input key"`阶段进行的是`TEA`加密，并给出了key秘钥的内容(此处笔误写成了RC4)
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SeyNA17lQ5yA8f2xNSSO*p.3nNHyhfQ7iFC9d*a9RgPXYTFJ*3eGdqSrdEHQ8JTt3hxxB37RmjUrhSQiC0R0kXM!/b&bo=BAMiAgQDIgIDFzI!&rf=viewer_4)
查看栈段的调用发现v7和v8是连着的
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SeDN2qEH3OFeAARBvZZiz1ksWHV7qSW5JNIM9ZDQAQbaA5qJX1we.3H0WtDpC4wM80p4Zf02kG2nO2nF87NGXFA!/b&bo=dAYIAXQGCAEDByI!&rf=viewer_4)
传入RC4加密函数是v7的地址，根据后面if中的条件中对v7和v8的判断得出密文，可用TEA解密代码得出
```c
#include <stdio.h>
#include <stdint.h>
void decrypt(uint32_t* temp, uint32_t* key) // 解密函数
{  
    uint32_t v0 = temp[0], v1 = temp[1];
    int sum = 0xC6EF3720;    // 初始sum值，注意此处要修改为delta的32倍
    uint32_t delta = 0x9e3779b9;  // 和加密函数一致的delta常量
    for (int i = 0; i < 32; i++) {
        v1 -= ((v0 << 4) + key[2]) ^ (v0 + sum) ^ ((v0 >> 5) + key[3]);// 不要修改算式！
        v0 -= ((v1 << 4) + key[0]) ^ (v1 + sum) ^ ((v1 >> 5) + key[1]);
        sum -= delta;
    }
    temp[0] = v0;
    temp[1] = v1;
}

int main() {
    uint32_t key[4] = 
    {
        0x12,0x34,0x56,0x78
    };  
    uint32_t temp[2];  // 存储每组密文
        temp[0] = 0x60FCDEF7;
        temp[1] = 0x236DBEC;
        decrypt(temp, key);// 调用解密函数
        for (int j = 0; j < 2; j++) // 输出解密后的数据
        {
            for (int m = 0; m < 4; m++) 
            {
                printf("%d", temp[j] & 0xff);  // 按字节输出，恢复原始字符
                temp[j] >>= 8;
            }
        }
    return 0;
}
```
得出解密结果为00030004（要以整数输出），即key为3

点开最后处理v6的sub_411302函数
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SYQf.YG9d1xiC7L6IWdqCMlWzSEZNn3pERa3CUZzKuUCKTC9nz2hETQV1ljJP8tFwbCJyoIOQVQKWOy97VZi4*M!/b&bo=mQF*AJkBfwADFzI!&rf=viewer_4)
发现是一堆未识别出的数据
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SRuYK9tHmpRptdA4uj87rBQnMYRONBPe.WbAMtkuB2FWGaPDwHNun5i017UJFL.VUSycoed201i0ZduPaPYc*sk!/b&bo=XARaAlwEWgIDFzI!&rf=viewer_4)
打断点进入调试模式
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SYZ5bdC.41uxUZW8MHaLp6*7Qjjwwt9M6KXwYkbXvShbp84nOBttue3K7K50HYYGfqh6ICoWBOdypYCOKz7SMmc!/b&bo=zASxA8wEsQMDByI!&rf=viewer_4)
步进运行程序将loc_0041D000地址的数据分析为指令，再在`loc_0041D000`处按P将其分析为函数，分析伪代码可知该函数为RC4加密
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SYT3kV3681GuMZTtdjih.2oh*ERLml6z*e2FHOgxp43yRTHNgi9fYjV7yNUVGMb45WPTxvioDuTmIJx4dA0novM!/b&bo=6QSOA.kEjgMDFzI!&rf=viewer_4)
```c
#include <stdio.h>
#include <stdlib.h>
void swap(unsigned char* a, unsigned char* b) {
    // 交换两个字节
    unsigned char temp = *a;
    *a = *b;
    *b = temp;
}
void RC4_dec(unsigned char* ciphertext, int length, const char* key) {
    // RC4解密函数
    int i, j;
    unsigned char* S;
    unsigned char k[256];
    int keylen = 0;
    while (key[keylen] != '\0') {
        keylen++;
    }
    for (i = 0; i < 256; i++) {    // 初始化密钥数组k
        k[i] = key[i % keylen];
    }
    S = (unsigned char*)malloc(256 * sizeof(unsigned char));    // 初始化S盒
    for (i = 0; i < 256; i++) {
        S[i] = i;
    }
    j = 0;
    for (i = 0; i < 256; i++) {
        j = (j + S[i] + k[i]) % 256;
        swap(&S[i], &S[j]);
    }
    i = 0;
    j = 0;
    for (int n = 0; n < length; n++) {
        i = (i + 1) % 256;
        j = (j + S[i]) % 256;
        swap(&S[i], &S[j]);
        int t = (S[i] + S[j]) % 256;
        ciphertext[n] ^= S[t];
    }
    free(S);
}
int main() {
    unsigned char res[] = {
    0x0F, 0x94, 0xAE, 0xF2, 0xC0, 0x57, 0xC2, 0xE0,
    0x9A, 0x45, 0x37, 0x50, 0xF5, 0xA0, 0x5E, 0xCB,
    0x2C, 0x16, 0x28, 0x29, 0xFE, 0xFF, 0x33, 0x46,
    0x0E, 0x57, 0x82, 0x22, 0x52, 0x26, 0x2B, 0x6E,
    0xE4, 0x82, 0x24
    };//此处为密文
    const char key[] = "you_are_master";//此处为秘钥
    RC4_dec(res, sizeof(res), key);
    for (int i = 0; i < sizeof(res); i++)
        printf("%c", res[i]);
    return 0;
}
```
用RC4代码解密即可
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SdgnuCzSIxEJFJU2I1YKDuBkO1ELpZ2Z1unfjQoTT2OJBqT8ki7FyfnVJ7KBZgsr6OhWeY5kBOnrmkkHDX8NhvU!/b&bo=tQISA7UCEgMDJwI!&rf=viewer_4)
### [SWPUCTF 2022 新生赛]pypy
pyc反编译+RC4,AI直接秒
```python
def reverse_get_flag():
    # 已知密文
    cipher_text = [
        84, 91, 254, 48, 129, 210, 135, 132, 112, 234, 208, 15, 213, 39, 108, 253, 
        86, 118, 248
    ]
    
    # 密钥
    Key = 'abcdefg'
    
    # 初始化 S 和 T 数组
    S = list(range(256))
    T = [ord(Key[i % len(Key)]) for i in range(256)]
    
    # 交换 S 数组
    j = 0
    for i in range(256):
        j = (j + S[i] + T[i]) % 256
        S[i], S[j] = S[j], S[i]
    
    # 生成密钥流
    KeyStream = []
    j = 0
    for i in range(len(cipher_text)):
        i = i % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        t = (S[i] + S[j]) % 256
        KeyStream.append(S[t])
    
    # 使用密钥流反向推导 flag
    flag = ''.join(chr(c ^ KeyStream[i]) for i, c in enumerate(cipher_text))
    
    return flag

# 调用函数并打印 flag
flag = reverse_get_flag()
print(flag)
#NSSCTF{this_is_rc4}
```
### [HNCTF 2022 WEEK4]checker
这是一个 HTML 页面，涉及用户名和密码验证，并在验证成功时展示一个 flag。代码通过以下步骤工作：

用户名和密码验证：

用户名必须是 "Admin"。
密码必须经过 Base64 解码后等于 "goldenticket"。如果条件符合，执行解密过程并显示 flag。
解密流程：

页面包含了一个 Base64 编码的字符串 FGFqMA4BLT8lES01UEEJRDIBZjE/FCIqKCYCDRRTMVV7Tw==。
成功登录后，页面会根据用户输入的密码通过异或（XOR）操作与 Base64 解码后的密钥生成 flag。
encoded_key 是一个 Base64 编码的字符串，在解密后它会被逐字符与密码的字符异或，生成 flag。
总结：
用户输入 "Admin" 作为用户名，密码 "goldenticket" 后，密钥通过 Base64 解码并与密码异或生成 flag。
如果用户名和密码正确，最终的 flag 会显示在页面上。
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SbcoVOztF25XvRbq8Y.0SefrdJMxwj9zUsjB8uOj0XwIybc0gDa0FCXZrMRYMTvxSlFfg7BOA8EQVrM9bEKOVeQ!/b&bo=WwO7AVsDuwEDByI!&rf=viewer_4)
### [SWPUCTF 2022 新生赛]贪吃蛇
跟着程序运行顺序走，在`gameMainLoop()`函数里找到关键函数`decode_flag()`和密文地址`&t_flag`
```c
int __cdecl decode_flag(int a1)
{
  int result; // eax
  int i; // [esp+Ch] [ebp-4h]

  for ( i = 0; i <= 30; ++i )
  {
    result = i + a1;
    *(_BYTE *)(i + a1) ^= 0x52u;
  }
  return result;
}
```
直接写出exp
```python
encoded_data = [
    0x1C, 0x01, 0x01, 0x11, 0x06, 0x14, 0x29, 0x0B, 0x3D, 0x27, 0x20, 0x13,
    0x20, 0x37, 0x06, 0x3A, 0x37, 0x1F, 0x33, 0x21, 0x26, 0x37, 0x20, 0x1D,
    0x34, 0x15, 0x33, 0x3F, 0x37, 0x73, 0x2F
]

decoded_data = [byte ^ 0x52 for byte in encoded_data]
decoded_string = ''.join(chr(byte) for byte in decoded_data)
print(decoded_string)
#NSSCTF{YourAreTheMasterOfGame!}
```
[HNCTF 2022 WEEK2]来解个方程?
```python
from z3 import *
s = Solver()
v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23 = Ints("v2 v3 v4 v5 v6 v7 v8 v9 v10 v11 v12 v13 v14 v15 v16 v17 v18 v19 v20 v21 v22 v23")
s.add(245 * v6 + 395 * v5 + 3541 * v4 + 2051 * v3 + 3201 * v2 + 1345 * v7 == 855009)
s.add(3270 * v6 + 3759 * v5 + 3900 * v4 + 3963 * v3 + 1546 * v2 + 3082 * v7 == 1515490)
s.add(526 * v6 + 2283 * v5 + 3349 * v4 + 2458 * v3 + 2012 * v2 + 268 * v7 == 854822)
s.add(3208 * v6 + 2021 * v5 + 3146 * v4 + 1571 * v3 + 2569 * v2 + 1395 * v7 == 1094422)
s.add(3136 * v6 + 3553 * v5 + 2997 * v4 + 1824 * v3 + 1575 * v2 + 1599 * v7 == 1136398)
s.add(2300 * v6 + 1349 * v5 + 86 * v4 + 3672 * v3 + 2908 * v2 + 1681 * v7 == 939991)
s.add(212 * v22 + 153 * v21 + 342 * v20 + 490 * v12 + 325 * v11 + 485 * v10 + 56 * v9 + 202 * v8 + 191 * v23 == 245940)
s.add(348 * v22 + 185 * v21 + 134 * v20 + 153 * v12 + 460 * v9 + 207 * v8 + 22 * v10 + 24 * v11 + 22 * v23 == 146392)
s.add(177 * v22 + 231 * v21 + 489 * v20 + 339 * v12 + 433 * v11 + 311 * v10 + 164 * v9 + 154 * v8 + 100 * v23 == 239438)
s.add(68 * v20 + 466 * v12 + 470 * v11 + 22 * v10 + 270 * v9 + 360 * v8 + 337 * v21 + 257 * v22 + 82 * v23 == 233887)
s.add(246 * v22 + 235 * v21 + 468 * v20 + 91 * v12 + 151 * v11 + 197 * v8 + 92 * v9 + 73 * v10 + 54 * v23 == 152663)
s.add(241 * v22 + 377 * v21 + 131 * v20 + 243 * v12 + 233 * v11 + 55 * v10 + 376 * v9 + 242 * v8 + 343 * v23 == 228375)
s.add(356 * v22 + 200 * v21 + 136 * v11 + 301 * v10 + 284 * v9 + 364 * v8 + 458 * v12 + 5 * v20 + 61 * v23 == 211183)
s.add(154 * v22 + 55 * v21 + 406 * v20 + 107 * v12 + 80 * v10 + 66 * v8 + 71 * v9 + 17 * v11 + 71 * v23 == 96788)
s.add(335 * v22 + 201 * v21 + 197 * v11 + 280 * v10 + 409 * v9 + 56 * v8 + 494 * v12 + 63 * v20 + 99 * v23 == 204625)
s.add(428 * v18 + 1266 * v17 + 1326 * v16 + 1967 * v15 + 3001 * v14 + 81 * v13 + 2439 * v19 == 1109296)
s.add(2585 * v18 + 4027 * v17 + 141 * v16 + 2539 * v15 + 3073 * v14 + 164 * v13 + 1556 * v19 == 1368547)
s.add(2080 * v18 + 358 * v17 + 1317 * v16 + 1341 * v15 + 3681 * v14 + 2197 * v13 + 1205 * v19 == 1320274)
s.add(840 * v18 + 1494 * v17 + 2353 * v16 + 235 * v15 + 3843 * v14 + 1496 * v13 + 1302 * v19 == 1206735)
s.add(101 * v18 + 2025 * v17 + 2842 * v16 + 1559 * v15 + 2143 * v14 + 3008 * v13 + 981 * v19 == 1306983)
s.add(1290 * v18 + 3822 * v17 + 1733 * v16 + 292 * v15 + 816 * v14 + 1017 * v13 + 3199 * v19 == 1160573)
s.add(186 * v18 + 2712 * v17 + 2136 * v16 + 98 * v13 + 138 * v14 + 3584 * v15 + 1173 * v19 == 1005746)
flag=[]
if s.check() == sat:
    ans=s.model()
    flag.append(ans[v2])
    flag.append(ans[v3])
    flag.append(ans[v4])
    flag.append(ans[v5])
    flag.append(ans[v6])
    flag.append(ans[v7])
    flag.append(ans[v8])
    flag.append(ans[v9])
    flag.append(ans[v10])
    flag.append(ans[v11])
    flag.append(ans[v12])
    flag.append(ans[v13])
    flag.append(ans[v14])
    flag.append(ans[v15])
    flag.append(ans[v16])
    flag.append(ans[v17])
    flag.append(ans[v18])
    flag.append(ans[v19])
    flag.append(ans[v20])
    flag.append(ans[v21])
    flag.append(ans[v22])
    flag.append(ans[v23])
for x in flag:
    print(x,end=",")
#NSSCTF{pip_inst@ll_Z3}
```
`z3`解方程组脚本
### [HNCTF 2022 Week1]Little Endian
小端序存储问题
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SSpKDTPZdtP0XXUGgoKfo9HycOGbXhaOfDrz*r3U1bqYosS.LbRnoV.8FRJ*BTPJsp6IuN1OsWM2HgZPIKRnQic!/b&bo=6gPlAuoD5QIDByI!&rf=viewer_4)
exp:
```c
#include<stdio.h>
int main()
{
    unsigned int enc[] = {
        0x36056751, 0x2C104F5E, 0x1122407E, 0x4B09717C, 0x1C3F557C, 0x16385A6F
    };
    int flag[100];
    for (int i = 0; i <= 5; ++i)
    {
        flag[i] = enc[i] ^ 0x78563412;
    }
    for (int i = 0; i <= 5; ++i)
    {
        printf("%x ", flag[i]);
    }
    return 0;
}
//4e535343 54467b4c 6974746c 335f456e 6469616e 6e6e6e7d
```
转ASCII得NSSCTF{Littl3_Endiannnn}
### [LitCTF 2023]程序和人有一个能跑就行了
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SQWwgV.Bzz6Ou1Daqzli4UZhTjZRtEQF87LUeJSOSJJ3Izd3kpFks*m4l.cnhREo1H6ryIrKglwgVESGreQtcz8!/b&bo=3ATuA9wE7gMDByI!&rf=viewer_4)
动调发现实际运行时设置密文时在执行的是loc_475B85的内容，F5的反汇编代码中的内容实际最后被修改，要多观察反汇编代码的实际逻辑
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SQ91HA7n0jiOzqcdEIbnj8gxfbqjhuLmeNOPLp364v5ljG26zbnjoP2UerVT4AzcbcSZUPyp1*Yk0d46a5cacaU!/b&bo=WAFrAVgBawEDByI!&rf=viewer_4)
左假右真

还是用RC4即可解出LitCTF{welcome_to_the_litctf}

还有一些比较杂的题就不总结了
## 学习反汇编
学习之前在校期间由于时间紧张导致进度落下的《C++反汇编与逆向分析技术揭秘》一书，大体把要求的范围搞定了，下周进行最后的收尾工作。通过这里的学习，我熟悉了高级语言与汇编代码之间的联系，了解到了计算机编译程序的许多细节以及32位和64位环境下的汇编，提升了逆向分析能力。

## 学科目一
考驾照也很重要，分配了部分精力在科目一的学习上。