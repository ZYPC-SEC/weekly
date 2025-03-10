# hanafuda_store's Weekly Report (week13)
## GHCTF
这场比赛知识点还是偏向新生赛水平，但是综合性很强，所以难度也不低。我做出了两道密码方向有关RSA的题目，但是在自己本职的逆向方向并没有什么突出的建树，只做了一个16位汇编的签到(ASM?Signin!)，然后另外的两道题都只做了一半。FishingKit这题用z3库解了个多元方程，解了个RC4然后得到了个fakeflag……后来使用动态调试找到了一些藏的比较深的函数，疑似使用了多个TEA加密，但是由于实在过于复杂最后没能做出来。
```c
__int64 __fastcall sub_7FF636021CE0(_BYTE *a1, unsigned __int8 *a2)
{
  unsigned int v3; // [rsp+20h] [rbp-108h]
  unsigned int v4; // [rsp+20h] [rbp-108h]
  unsigned int v5; // [rsp+20h] [rbp-108h]
  unsigned int v6; // [rsp+24h] [rbp-104h]
  unsigned int v7; // [rsp+24h] [rbp-104h]
  unsigned int v8; // [rsp+24h] [rbp-104h]
  unsigned int v9; // [rsp+28h] [rbp-100h]
  unsigned int v10; // [rsp+28h] [rbp-100h]
  unsigned int v11; // [rsp+28h] [rbp-100h]
  char v12; // [rsp+2Ch] [rbp-FCh]
  int i; // [rsp+30h] [rbp-F8h]
  int j; // [rsp+34h] [rbp-F4h]
  int ii; // [rsp+38h] [rbp-F0h]
  int jj; // [rsp+3Ch] [rbp-ECh]
  int kk; // [rsp+40h] [rbp-E8h]
  int mm; // [rsp+44h] [rbp-E4h]
  int nn; // [rsp+48h] [rbp-E0h]
  int v20; // [rsp+4Ch] [rbp-DCh]
  int k; // [rsp+50h] [rbp-D8h]
  int m; // [rsp+54h] [rbp-D4h]
  int n; // [rsp+58h] [rbp-D0h]
  HMODULE hModule; // [rsp+60h] [rbp-C8h]
  FARPROC ProcAddress; // [rsp+68h] [rbp-C0h]
  CHAR LibFileName[16]; // [rsp+70h] [rbp-B8h] BYREF
  CHAR ProcName[16]; // [rsp+80h] [rbp-A8h] BYREF
  char v28[3]; // [rsp+90h] [rbp-98h] BYREF
  char v29[11]; // [rsp+93h] [rbp-95h] BYREF
  char v30[8]; // [rsp+9Eh] [rbp-8Ah] BYREF
  char v31[32]; // [rsp+A8h] [rbp-80h] BYREF
  int v32[6]; // [rsp+C8h] [rbp-60h] BYREF
  int v33[14]; // [rsp+E0h] [rbp-48h] BYREF
  _BYTE *v34; // [rsp+130h] [rbp+8h]

  v34 = a1;
  memset(v32, 0, 0x14ui64);
  memset(v33, 0, 0x32ui64);
  for ( i = 0; i < 20; ++i )
    *((_BYTE *)v32 + i) = a1[i - 80];
  for ( j = 0; j < 50; ++j )
    *((_BYTE *)v33 + j) = a1[j - 56];
  v3 = 0;
  v6 = v33[0];
  v9 = v33[1];
  for ( k = 0; k < 24; ++k )
  {
    v6 += (v32[v3 & 3] + v3) ^ (v9 + ((v9 >> 5) ^ (16 * v9)));
    v3 += 1719109785;
    v9 += (v32[(v3 >> 11) & 3] + v3) ^ (v6 + ((v6 >> 5) ^ (16 * v6)));
  }
  v33[0] = v6;
  v33[1] = v9;
  v4 = 0;
  v7 = v33[2];
  v10 = v33[3];
  for ( m = 0; m < 24; ++m )
  {
    v7 += (v32[v4 & 3] + v4) ^ (v10 + ((v10 >> 5) ^ (16 * v10)));
    v4 += 1719109785;
    v10 += (v32[(v4 >> 11) & 3] + v4) ^ (v7 + ((v7 >> 5) ^ (16 * v7)));
  }
  v33[2] = v7;
  v33[3] = v10;
  v5 = 0;
  v8 = v33[4];
  v11 = v33[5];
  for ( n = 0; n < 24; ++n )
  {
    v8 += (v32[v5 & 3] + v5) ^ (v11 + ((v11 >> 5) ^ (16 * v11)));
    v5 += 1719109785;
    v11 += (v32[(v5 >> 11) & 3] + v5) ^ (v8 + ((v8 >> 5) ^ (16 * v8)));
  }
  v33[4] = v8;
  v33[5] = v11;
  v12 = 1;
  for ( ii = 0; ii < 24; ++ii )
  {
    if ( write[ii] != *((unsigned __int8 *)v33 + ii) )
    {
      v12 = 0;
      break;
    }
  }
  if ( v12 )
  {
    strcpy(LibFileName, "dbtc\"#?u}}");
    for ( jj = 0; jj < 10; ++jj )
      LibFileName[jj] ^= 0x11u;
    hModule = LoadLibraryA(LibFileName);
    strcpy(ProcName, "\\tbbpvtS~iP");
    for ( kk = 0; kk < 11; ++kk )
      ProcName[kk] ^= 0x11u;
    ProcAddress = GetProcAddress(hModule, ProcName);
    strcpy(v31, "H~d6gt1rpdvye1p1sxv1wxby0");
    for ( mm = 0; mm < 25; ++mm )
      v31[mm] ^= 0x11u;
    qmemcpy(v28, "R~", 2);
    v28[2] = 127;
    qmemcpy(v29, "vcped}pex~", 10);
    v29[10] = 127;
    strcpy(v30, "000");
    for ( nn = 0; nn < 17; ++nn )
      v28[nn] ^= 0x11u;
    ((void (__fastcall *)(_QWORD, char *, char *, _QWORD))ProcAddress)(0i64, v31, v28, 0i64);
  }
  while ( 1 )
  {
    v20 = (unsigned __int8)*v34 - *a2;
    if ( v20 || !*v34 )
      break;
    ++v34;
    ++a2;
  }
  if ( v20 > 0 )
    return 1i64;
  if ( v20 >= 0 )
    return 0i64;
  return 0xFFFFFFFFi64;
}
```
Mio？Ryo？Soyo？这题是Python解包，比普通题复杂的一点是，这题由于定义了多个函数，所以解包时要提取多个pyc文件进行反编译，否则会出现调用的函数没有定义的情况(可由pyc文件的名称得知需要提取哪些文件)，然后可以得到下面的内容。长崎素世是在进行类似凯撒加密的位移操作，山田凉是Base45编码，秋山澪是Base85编码，然后连续互相套娃调用了几次。
```python
# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: program.py
from Secret import *
if __name__ == "__main__":
    print("输入:", end="")
    aaaaaaaaaaaaa = input()
    wwwwwwwwwww = l(aaaaaaaaaaaaa)
    if sssssssssssss == wwwwwwwwwww.encode():
        print("哦，对的。")
    else:
        print("哎，并非。")
    input()

# okay decompiling program.pyc

# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: Secret.py
from SecretEncrypt import *
sssssssssssss = bytes([57, 118, 33, 114, 68, 56, 117, 115, 34, 52, 52, 95, 78, 40, 49, 59,
 95, 85, 63, 122, 54, 33, 77, 110, 49, 54, 34, 109, 106, 122, 60,
 92, 108, 91, 61, 51, 42, 62, 35, 38, 52, 67, 62, 122, 116, 48,
 76, 50, 67, 51, 59, 41, 122, 45, 45, 51, 90])

def l(_: str):
    return SSSooooyyooo(MMMMiiiiiio.MMMMiiooooooo(SSSooooyyooo(RRRRyyooo.RRRRRRRyyyyooooo(_.encode()), 7).encode()), 9)

# okay decompiling Secret.pyc

import math

class MMMMiiiiiio:
    MMiiiiiiooo = "".join([chr(Miiooooooooo) for Miiooooooooo in range(33, 118)])

    @staticmethod
    def MMMMiiooooooo(MMMMMMMMMiiiooo: bytes) -> str:
        MMMMiiiiioooooooooo = ""
        MMMMMMMiiiiioo = (4 - len(MMMMMMMMMiiiooo) % 4) % 4
        MMMMMMMMMiiiooo += b'\x00' * MMMMMMMiiiiioo
        for MMMMMMiiiiiio in range(0, len(MMMMMMMMMiiiooo), 4):
            MMMMiiiiiiooooo = MMMMMMMMMiiiooo[MMMMMMiiiiiio[:MMMMMMiiiiiio + 4]]
            MMMMMMiiioooooo = int.from_bytes(MMMMiiiiiiooooo, "big")
            MMMMMMMiiooooooooo = ""
            for _ in range(5):
                MMMMMMMiiooooooooo = MMMMiiiiiio.MMiiiiiiooo[MMMMMMiiioooooo % 85] + MMMMMMMiiooooooooo
                MMMMMMiiioooooo //= 85
            else:
                MMMMiiiiioooooooooo += MMMMMMMiiooooooooo

        else:
            if MMMMMMMiiiiioo:
                MMMMiiiiioooooooooo = MMMMiiiiioooooooooo[None[:-MMMMMMMiiiiioo]]
            return MMMMiiiiioooooooooo


class RRRRyyooo:
    RRRRyooooooo = "".join([chr(RRRRRRRyyyyyoooo) for RRRRRRRyyyyyoooo in range(48, 93)])

    @staticmethod
    def RRRRRRRyyyyooooo(RRRRRRyyyoooooo: bytes) -> str:
        RRRRyyyyyooo = []
        RRyyyyyyyyyoooooo = 0
        while RRyyyyyyyyyoooooo < len(RRRRRRyyyoooooo):
            if RRyyyyyyyyyoooooo + 1 < len(RRRRRRyyyoooooo):
                RRRRRRRRRyyo = RRRRRRyyyoooooo[RRyyyyyyyyyoooooo] << 8 | RRRRRRyyyoooooo[RRyyyyyyyyyoooooo + 1]
                RRRRyyyyyooo.append(RRRRyyooo.RRRRyooooooo[RRRRRRRRRyyo % 45])
                RRRRRRRRRyyo //= 45
                RRRRyyyyyooo.append(RRRRyyooo.RRRRyooooooo[RRRRRRRRRyyo % 45])
                RRRRRRRRRyyo //= 45
                RRRRyyyyyooo.append(RRRRyyooo.RRRRyooooooo[RRRRRRRRRyyo])
                RRyyyyyyyyyoooooo += 2
            else:
                RRRRRRRRRyyo = RRRRRRyyyoooooo[RRyyyyyyyyyoooooo]
                RRRRyyyyyooo.append(RRRRyyooo.RRRRyooooooo[RRRRRRRRRyyo % 45])
                RRRRRRRRRyyo //= 45
                RRRRyyyyyooo.append(RRRRyyooo.RRRRyooooooo[RRRRRRRRRyyo])
                RRyyyyyyyyyoooooo += 1

        return "".join(RRRRyyyyyooo)


def SSSooooyyooo(SSSSooyoooooo, SSSSSoyyooooo):
    SSoooooyyyyyyoo = []
    for SSSSSSSSSoyooo in SSSSooyoooooo:
        if "a" <= SSSSSSSSSoyooo <= "z":
            SSSSoooyooooooo = (ord(SSSSSSSSSoyooo) - ord("a") + SSSSSoyyooooo) % 26
            SSoooooyyyyyyoo.append(chr(ord("a") + SSSSoooyooooooo))
        elif "0" <= SSSSSSSSSoyooo <= "9":
            SSSSoooyooooooo = (ord(SSSSSSSSSoyooo) - ord("0") - SSSSSoyyooooo) % 10
            SSoooooyyyyyyoo.append(chr(ord("0") + SSSSoooyooooooo))
        else:
            SSoooooyyyyyyoo.append(SSSSSSSSSoyooo)
    else:
        return "".join(SSoooooyyyyyyoo)

# okay decompiling SecretEncrypt.pyc
```
但是由于我编程能力还是太差，没能顺利解出，可见我近期又疏忽了代码的学习，得恶补了……

然后由于班里面后面几天忙了起来，所以没时间继续做新上的题，就搁置了。
## 出题
准备ADCTF，出了四道题。一个签到，一个Linux平台的ELF文件，用的RC4加密，一个换表Base64，一个Python打包的贪吃蛇游戏，里面隐藏了一个TEA加密的流程。头一次自己出CTF的题所以虽然是偏简单的题，但是也遇到了不少麻烦，耽搁了一些时间。

## 其他
非常抱歉的一点是，这周由于时间分配的不合理，导致我没能完成对AES和DES算法的总结，虽然之前有了解过，但是转化为实际的代码还是不轻松的，我会尽快在下一周补上。

总之，这一周状态比较差，学习内容完成的成果不好，我对此深表歉意。下一周我会痛定思痛，争取填补空缺。
