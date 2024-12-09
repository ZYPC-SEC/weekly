# hanafuda_store的周报(第五周)
## 学习Python逆向
这是本周工作的重点，下面先记录这种题目的一般做法：
#### 1.将exe文件解包
这种题目本质上就是像编译C语言源文件那样将Python文件编译为一个可执行文件，可使其在没有Python环境的情况下也能独立运行。判断这种题目的特征有exe文件的图标，以及用ExeinfoPE查壳所得到的文件类型提示。

我们拿到题目附件后需要先将exe文件解包，这一步需要使用`pyinstxtractor.py`，将其和要解密的文件放在一个目录下，然后在命令行使用如下指令
```
python pyinstxtractor.py <要解包的文件名>.exe
```
然后会生成一个名为`<要解包的文件名>.exe_extracted`的文件夹
#### 2.修补魔法字节MagicNumber
此时进入文件夹，找到目标文件对应的源码pyc文件（版本低的运行后的结果pyc文件需要自己补上后缀名，该文件名称一般与原exe文件名称有关），用`010Editor`打开查看文件首行是否含有魔法字节（一个 4 字节的magic number，用于标识其格式和兼容的 Python 版本），若没有，则需要手动补齐。打开刚刚那个文件夹中的另一个文件夹，可以看到很多其他的pyc文件，这些都带有魔法字节，可以复制下来使用。补充魔法字节时要注意后面12个字节留空，这是文件头的格式。
![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SenYsSF1xc*DZkm*xttiahHP6hUTWzHeD*lKyhhi*xEk1AnY4SoQ63J.wjXlE9PksnFtGsjwIfZwjWS3ifi61fQ!/b&bo=IARlAQAAAAADB2I!&rf=viewer_4)
#### 3.反汇编得到Python源文件
此时的pyc文件已经可以进行反汇编了，这里可以使用的工具有两种，第一个是`uncompyle6.exe`，需要拖至和目标pyc文件所在目录，然后使用指令
```
uncompyle6 文件名.pyc > 文件名.py
```
也可使用`pycdc.exe`，需要拖至和目标pyc文件所在目录，然后使用指令
```
pycdc 文件名.pyc
```
此时已获得了反编译的Python文件，进行分析即可
PS：有时会遇到前面两种工具都无法反编译的情况，此时需要使用`pycads.exe`获取汇编指令进行分析，所需指令为
```
pycdas 文件名.pyc
```
## 练习题目
学习后的练习还是必不可少的，直接上题
### [ZYPC-Newstar2024 Week3]压轴-PyAndTEA
~~当时新生赛时没做出来的题，离AK就差一点点啊~~

这题主要考察`Python解包`与`Tea加解密`，根据题目提示以及附件的图标可知该exe文件为打包编译后的Python文件，故进行解包。先用pyinstxtractor.py将exe文件转化为包含了Python源代码编译后的字节码的pyc文件，根据文件夹中的其他pyc文件补充pyc文件的魔法字节。然后使用pycdc将pyc文件反编译为Python源代码
![](https://a1.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SQ8YSVki4aAK8Z3Dcu3pIy7eWLOfKmVuJ8cS4pLLTH*1KnIWFPTq7rvqAD0KDGtcmhuLPz0iaGCNeUym6TLN8CU!/b&ek=1&kp=1&pt=0&bo=pgYUAwAAAAADF4U!&tl=1&vuin=934483106&tm=1731826800&dis_t=1731827895&dis_k=3ad0521ba0769e6cca973bf3e60b510b&sce=60-2-2&rf=viewer_4)
这里反编译出来的代码有一些问题，部分需要手动修改：
1. 有的数据显示为10进制，有的显示为16进制，需手动改为16进制（Tea加密就是将字符转换为16进制然后拼接在一起之后进行加密操作的
2. 有一句话是警告，应改为注释
3. `O00000O0OO0O0O000 = (None + ' ').encode()` 无法运行，`None + ' '` 不合法

结合AI帮助进行分析可知反编译出来的这部分代码是在对一段数据进行TEA加密，由此可写出解密代码：
```python
from ctypes import c_uint32

def decrypt(cipher, key):
    """解密 TEA 算法"""
    v0 = c_uint32(cipher[0])
    v1 = c_uint32(cipher[1])
    k0, k1, k2, k3 = key
    delta = 0xDEADC0DE
    sum = c_uint32(delta * 32)  # 初始 sum 为加密中 32 轮后的值

    for _ in range(32):
        v1.value -= ((v0.value << 4) + k2) ^ (v0.value + sum.value) ^ ((v0.value >> 5) + k3)
        v0.value -= ((v1.value << 4) + k0) ^ (v1.value + sum.value) ^ ((v1.value >> 5) + k1)
        sum.value -= delta

    return v0.value, v1.value

# 密钥
key = [0x7FE9D73C, 0xCE5D32FA, 0x0AD9AC89, 0x4455EC1D]
# 加密结果
cipher_blocks = [
    0x7C2236A0, 0x8C0EBB4A,
    0xA7CEABDC, 0xE3F2F84A,
    0xA7133D2F, 0xA537C331,
    0xE3F77866, 0xC6831FA1,
    0xE2C417FA, 0x9FF26C0C
]

# 解密每个块
plaintext = b""
for i in range(0, len(cipher_blocks), 2):
    block = cipher_blocks[i:i+2]
    decrypted = decrypt(block, key)
    # 将解密结果转换回字节
    plaintext += decrypted[0].to_bytes(4, 'big') + decrypted[1].to_bytes(4, 'big')

# 输出解密后的明文
print("Decrypted plaintext:", plaintext)
# 结果：ZYPC{390e95a8b53d0d8a1bef3594dd8c4c9d}
```

### [ISCTF 2024]《回忆安魂曲》--第三章：逃不出的黑墙
用IDA直接打开附件分析，找到main函数后进行分析，结果如下：
![](https://a1.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SRCr4lHzWCN8s9GX0SmXNtq9G2ULJvLgIAiaImAbA9wve7Gdy6V5iEmylPVwzW9L9.lI*xfrs3ALdrntscZHKjY!/c&ek=1&kp=1&pt=0&bo=2QL5AdkC.QEBFzA!&t=5&tl=3&vuin=934483106&tm=1731834000&dis_t=1731837253&dis_k=aaafe01e794b85333a14f8ac2e496116&sce=60-2-2&rf=0-0)
由此可推理出这是一个迷宫游戏，love作为方向键分别控制角色向上、下、左、右这四个方向移动，然后地图的数据储存在aP[]这个字符串中，井号代表墙，点代表路，为一个30*30的地图。编写代码打印出这个地图并得出步骤（注意，实际的起点和终点为P和E，C是一个假的终点！）
![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SSlyFwfLxGvix9eEjGWNViMkpSWFVJcPSczBAPpLNWagnUbPJyM6.LaQiiusaVFYbbnHUTkEvTYE5Cb9XV.b*84!/b&bo=YQNSAwAAAAADFwE!&rf=viewer_4)
走出迷宫后得到步骤为ooeeeeoooooovvoovvooeeooeelllleeooooeeeeooeeooeelleellllvvoovvlllleellvvvvllvvlleelllleeeeeeoovvvvooooeelleeooooooeelleeeeeeoooovvllvvoovvooooeeooeeoooovvooeeeeooeellllee
MD5 32位小写加密后包上ISCTF{}即可提交
### [ISCTF 2024]Ezre
用IDA直接打开附件分析，F12+Shift查看字符串窗口，看到类似于交互的语句和一段类似于flag的内容
![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SS4Bj3vtfnrfxkh4TvghmFbbEpHxgNV36c8ax*D5yhwZNKNeaJWabnk32eotYz*4htQQeXWOA9iB25SLqVqTOww!/b&bo=yAPtAAAAAAADFxQ!&rf=viewer_4)
点进去在反汇编界面分析，F5生成伪代码，可知该加密过程的主要过程在sub_1400112E9和sub_140011217中
![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SeewbYv907o0oZkMzdzvEvQbq600xKhMdRx34dIymkCOYofd68unlzt0yQpe.9bTKeSph*PSDhsfc*dAI.2Oi4w!/b&bo=wAR1AwAAAAADF4A!&rf=viewer_4)
接着点进去分别分析可看到以下代码
![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SbIOxEcfaIFEh0WqfZR0TmC.KM0FZFfdMEHq1oCcXvlAX1tFl0vlfilavX30NOgxifKnkwRkKcuAsiAZpZNboxE!/b&bo=YAPbAQAAAAADF4s!&rf=viewer_4)
![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*ScB03MMHelrhPnkf0GSKgO67mA9Xnu9sD7YS4cXB7Ns.mNbQmEMHj6G63Iu4cikx4iR.mmMEznibidUfQAvBbVU!/b&bo=YAMDAgAAAAADF1A!&rf=viewer_4)
加密逻辑：

循环遍历 input_flag 的每个字符：for (int i = 0; i < a2; ++a1)。
检查是否为大写字母：如果当前字符在 'A' 到 'Z' 之间，则将其与 a3 指向的字符（偏移为 i % 5）相加。

取模映射回大写字母：将计算的结果模 26，再加上 65，保持字符在 'A' 到 'Z' 范围内。
从以上分析可以看出，sub_1400117A0 使用 a3 指向的内容（即 encry_flag 的某些字符）对 input_flag 逐字符加密。因为 a3 是 "ISCTF"，这看起来像是一种基于 Vigenère 密码 的加密方式，使用密钥 "ISCTF" 对 input_flag 进行逐字母偏移。

由此我们即可写出解密的代码如下
```python
def decrypt_vigenere(encrypted_text, key):
    decrypted_text = []
    key_len = len(key)
    for i, char in enumerate(encrypted_text):
        if 'A' <= char <= 'Z':
            shift = ord(key[i % key_len]) - ord('A')
            decrypted_char = chr((ord(char) - ord('A') - shift + 26) % 26 + ord('A'))
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(char)  # 保留非大写字母的字符不变
    return ''.join(decrypted_text)

encry_flag = "QKEMK{7JB5_i5_W3SllD_3z_W3}"
key = "ISCTF"
original_flag = decrypt_vigenere(encry_flag, key)
print("Original flag:", original_flag)

```
由此即可得出flag
### [ISCTF]py不好，会被ban
Python解包，按上面的方法用pyinstxtractor.py解包，然后补充MagicNumber，之后进行反编译但是无法打开，考虑使用pycdas查看汇编指令，在AI的帮助下将汇编指令还原为Python源码，并进行分析，可写出解密代码
![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SbQxds0gHQf5*h5CIL9jiLIbdmf9F6f9ytWWDtNJ6ezbVcfbelOg6FLx38GEpbbPcUZMH0wGfgATtXp37iihTXs!/b&bo=9AY4BAAAAAADB.w!&rf=viewer_4)
当时没能做出该题的原因是AI和我都未能分析出该汇编指令中的reverse代表的是一个函数，将文本的内容倒序后再进行操作，比较遗憾
### [NISACTF 2022]string
附件是一个Linux的ELF文件，有一层壳，先用upx -d指令脱壳后拖入IDA分析
![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SecmGJrTS60ifcyNZs3.e4ZJqL2HNH3l3ngsT9uiXs77yY23bJ*qOuREn29ao6PYbDqObhr4Qi0CaszskTvr1vM!/b&bo=AwP*AAAAAAADF80!&rf=viewer_4)
main函数较为简单，接着查看较为显眼的flag函数
![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SXq7LaBgh5cUp0LYIhl7dYctlP7YAKPeHBpetb0ayK2oa9kRgtKg4lkIf.IZURtmvuU5L6pzkdUPIFmpqYdHi9o!/b&bo=VAMOBAAAAAADF28!&rf=viewer_4)
flag函数前面大段的内容都是在检查输入的内容是否符合标准(如该字符串长度为13等)，后面则是使用rand函数生成范围为1~8的随机数分别与输入的内容异或，最后按格式输出正确的flag。点开seed即可查看到该随机数生成过程中所用的种子为0x2766。
![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SbUZOFZp9CoC6ugqrEQGRe2FexDXod.sxGnD3d7Fky92KJYGA0WzTnL9gOecfwumDD39366vJ*Mpp0ee0CCUw3U!/b&bo=JwImAAAAAAADFzE!&rf=viewer_4)
由此即可写出解密代码。但是该文件是Linux上的可执行文件，由于Windows和Linux系统上生成伪随机数的数表不同，所以必须找一个Linux的环境下运行解密代码，可通过在线编译网站实现
![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SUsdkHW.ngBdVRPyIPDrpEkBr84GGsj9PxP8dP8sL0OJVyVxqEdM6he5eiibuTbbLLXTITEeooX*RzDUWbTFmhU!/b&bo=mwO.AQAAAAADFxU!&rf=viewer_4)
### [SWPUCTF 2021 新生赛]fakerandom
打开附件，发现是对flag用生成的随机数每位异或进行加密
![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SfAl.D0cwadNnsX*z0XO*tKJx7q7.VwYQ*5CBZhCJ4j*ZcCWdicxMesOfMRuL9iBTFMxGNXAj*.mPJzXifR9g5c!/b&bo=6wR1AQAAAAADF6k!&rf=viewer_4)
Python逆向，利用了伪随机数和异或运算的自反性。将原代码稍作修改就可以得到flag
![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SfAl.D0cwadNnsX*z0XO*tKJx7q7.VwYQ*5CBZhCJ4j*ZcCWdicxMesOfMRuL9iBTFMxGNXAj*.mPJzXifR9g5c!/b&bo=6wR1AQAAAAADF6k!&rf=viewer_4)
再将所得的异或数字结果转化为ASCII码即可得到flag
![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SWZZSemdrv536VvdqVNnrW8P5K7Swml3ILsjIlOevO3qsNwsdLSMDnJ30nyB6Ql0uDswoKYUuMLaUsnpU8EV82Q!/b&bo=igPJAgAAAAADF3A!&rf=viewer_4)
### [BJDCTF 2020]JustRE
shift+F12查看字符串，发现一个类似flag的字符串，但其中含有%d等转换说明
![](https://a1.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SUvcgehw54lJkWgXWMabY62smI7otorqIcEjl7IOkaZTLyd50LlN1R*v.HAK2MCezRcbSbJ9r5e5ddusCAc2*eE!/b&ek=1&kp=1&pt=0&bo=VAJVAAAAAAADFzE!&tl=1&vuin=934483106&tm=1731243600&dis_t=1731243830&dis_k=be1098132bd64c703b5184b6769eacf4&sce=60-3-3&rf=viewer_4)
点进去在反汇编窗口打开，通过旁边的注释链接到其所在的函数窗口
![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*STti1j1TcCy6m4p*y5fgStWLytVOpIuAAo8LnTva*Qf4GQhe2lEFl7X3J3H1tvBbsCmYJyjdgRZKemT*uXiblZI!/b&bo=uANlAAAAAAADF.w!&rf=viewer_4)
查看函数，原来是一个类似于printf的函数使用了转换说明，将19999和0替换flag中的%d，即可得到结果
![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SQ*JpJ6p5nsSp9oygDAMKA2AomWgsdiR2RHh7Imj2kfB6wknZGgNKx9ekFq2FW2.HUXz9Dfud9z8rFlbBzk2OTI!/b&bo=vgKqAAAAAAADFyQ!&rf=viewer_4)
### [SWPUCTF 2022 新生赛]base64-2
简单的换表Base64，记录一下做题经验
![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SdYN6VvxkAO1Efvaqb6p4ud8sss6YcFbJyW8peTJf3jkin.J5KzdCX*LdqWi.aAdkUt0u3MDFMeAmxTm3efcpB0!/b&bo=2gN1AAAAAAADF54!&rf=viewer_4)
从主函数点进加密函数，再点开这个字符串
![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SQGg9J5BhuglHSwmafLvhaE9NB7F3ppOWemo1C885RkJu9PqAJqk1clwSD*4laWGxRmcRCkRzG4gBwK1T2PY6iQ!/b&bo=0QSmAAAAAAADF0E!&rf=viewer_4)
由于这里的s2和off_4018其实都是指向字符串的指针(旁边的注释也有在说明该指针实际指向内容的部分信息)，所以应该再点击一次才能打开这两段信息实际内容的位置
![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SYqMKi4broolaCJjBXNieJ8arqbsykU399*LXcC0HFpo6lhilMs1WedRflDO4yFqiV2mcIjv9RFYA7YoRe53mPs!/b&bo=BgXpAAAAAAADF9g!&rf=viewer_4)
这里才是密文和Base64码表实际所在的地方(也可使用查找字符串的窗口)