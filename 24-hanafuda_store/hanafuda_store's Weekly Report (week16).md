# hanafuda_store's Weekly Report (week16)
## 刷题
### [CISCN 2021初赛]babybc
经查资料得知，`.bc`后缀名文件是LLVM编译器基础设施生成的 ​中间表示（IR）字节码文件。它类似于传统编译器的汇编代码，但与机器无关，用于跨平台优化和代码分析。

于是我们将附件拖入Linux虚拟将bc文件继续编译为ELF文件，使用命令：
```BASH
clang baby.bc -o baby
```
将得到的ELF文件拖入IDA分析，得到如下核心代码：
```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  unsigned __int64 v4; // [rsp+8h] [rbp-20h]
  size_t input_len; // [rsp+10h] [rbp-18h]
  unsigned __int64 i; // [rsp+18h] [rbp-10h]

  scanf(&unk_2004, input, envp);
  if ( (unsigned int)strlen(input) == 25 )      // 输入长度为25
  {
    if ( input[0] )
    {
      if ( (unsigned __int8)(input[0] - 48) > 5u )// 检查输入的第一位，只能为字符1~5，否则程序退出（字符‘0’的ASCII值为48）
        return 0;
      input_len = strlen(input);
      for ( i = 1LL; ; ++i )
      {
        v4 = i;
        if ( i >= input_len )
          break;
        if ( (unsigned __int8)(input[v4] - 48) > 5u )// 检查输入的其他位，只能为字符1~5，否则程序退出
          return 0;
      }
    }
    if ( (fill_number(input) & 1) != 0 && (docheck() & 1) != 0 )
      printf("CISCN{MD5(%s)}", input);
  }
  return 0;
}
//
__int64 __fastcall fill_number(__int64 input)
{
  unsigned __int8 *v2; // [rsp+0h] [rbp-70h]
  char v3; // [rsp+Fh] [rbp-61h]
  unsigned __int8 *v4; // [rsp+10h] [rbp-60h]
  char v5; // [rsp+1Fh] [rbp-51h]
  unsigned __int8 *v6; // [rsp+20h] [rbp-50h]
  char v7; // [rsp+2Fh] [rbp-41h]
  unsigned __int8 *v8; // [rsp+30h] [rbp-40h]
  char v9; // [rsp+3Eh] [rbp-32h]
  char v10; // [rsp+3Fh] [rbp-31h]
  __int64 v11; // [rsp+40h] [rbp-30h]
  __int64 v12; // [rsp+48h] [rbp-28h]
  char v13; // [rsp+5Fh] [rbp-11h]
  __int64 v14; // [rsp+68h] [rbp-8h]

  v14 = 0LL;
  do
  {
    v11 = v14;                                  // v11：列
    v12 = 5 * v14;                              // v12：行
    v13 = *(_BYTE *)(input + 5 * v14);          // v13是当前处理的输入格中的数据
    if ( map[5 * v14] )                         // 如果地图当前处理行的首列元素不是0
    {
      v10 = 0;                                  // 则令v10=0
      if ( v13 != 48 )                          // 当前输入格中的数据若不为0
        return v10 & 1;                         // 返回0
    }
    else                                        // 地图上是0
    {
      map[5 * v14] = v13 - 48;                  // 修改地图上对应位置的数据为当前处理的输入格
    }
    v8 = &map[5 * v14 + 1];                     // 对应行第二列
    v9 = *(_BYTE *)(input + v12 + 1);           // 对应输入元素
    if ( *v8 )
    {
      v10 = 0;
      if ( v9 != 48 )
        return v10 & 1;                         // &1用于判断奇偶性
    }
    else
    {
      *v8 = v9 - 48;
    }
    v6 = &map[5 * v14 + 2];                     // 对应行第三列
    v7 = *(_BYTE *)(input + v12 + 2);
    if ( *v6 )
    {
      v10 = 0;
      if ( v7 != 48 )
        return v10 & 1;
    }
    else
    {
      *v6 = v7 - 48;
    }
    v4 = &map[5 * v14 + 3];                     // 对应行第四列
    v5 = *(_BYTE *)(input + v12 + 3);
    if ( *v4 )
    {
      v10 = 0;
      if ( v5 != 48 )
        return v10 & 1;
    }
    else
    {
      *v4 = v5 - 48;
    }
    v2 = &map[5 * v14 + 4];                     // 对应行第五列
    v3 = *(_BYTE *)(input + v12 + 4);
    if ( *v2 )
    {
      v10 = 0;
      if ( v3 != 48 )
        return v10 & 1;
    }
    else
    {
      *v2 = v3 - 48;
    }
    ++v14;                                      // 更新列
    v10 = 1;
  }
  while ( v11 + 1 < 5 );                        // 循环退出条件：处理完5列
  return v10 & 1;                               // 若读取无误，则返回1
}
__int64 docheck()
{
  char *v1; // [rsp+0h] [rbp-C8h]
  char *v2; // [rsp+8h] [rbp-C0h]
  char *v3; // [rsp+10h] [rbp-B8h]
  char *v4; // [rsp+18h] [rbp-B0h]
  char v5; // [rsp+21h] [rbp-A7h]
  char v6; // [rsp+22h] [rbp-A6h]
  char v7; // [rsp+23h] [rbp-A5h]
  char v8; // [rsp+24h] [rbp-A4h]
  char v9; // [rsp+25h] [rbp-A3h]
  char v10; // [rsp+26h] [rbp-A2h]
  char v11; // [rsp+27h] [rbp-A1h]
  __int64 v12; // [rsp+28h] [rbp-A0h]
  __int64 v13; // [rsp+38h] [rbp-90h]
  char v14; // [rsp+46h] [rbp-82h]
  char v15; // [rsp+47h] [rbp-81h]
  __int64 v16; // [rsp+48h] [rbp-80h]
  __int64 v17; // [rsp+50h] [rbp-78h]
  char v18; // [rsp+5Fh] [rbp-69h]
  char *v19; // [rsp+60h] [rbp-68h]
  __int64 v20; // [rsp+68h] [rbp-60h]
  char *v21; // [rsp+70h] [rbp-58h]
  char v22; // [rsp+7Fh] [rbp-49h]
  char *v23; // [rsp+80h] [rbp-48h]
  __int64 v24; // [rsp+88h] [rbp-40h]
  char *v25; // [rsp+90h] [rbp-38h]
  __int64 v26; // [rsp+A0h] [rbp-28h]
  __int64 v27; // [rsp+B0h] [rbp-18h]
  char v28[6]; // [rsp+BCh] [rbp-Ch] BYREF
  char v29[6]; // [rsp+C2h] [rbp-6h] BYREF

  v27 = 0LL;                                    // 行索引
  do
  {
    v24 = v27;                                  // v24行标
    memset(v29, 0, sizeof(v29));
    v25 = &v29[map[5 * v27]];                   // map中元素只能为1~5,此处将其中对应的元素取出作为v29的索引，从而标记此处数字已经出现过
    if ( *v25
      || (*v25 = 1, v23 = &v29[map[5 * v27 + 1]], *v23)// 标记第一个元素并检查第二个元素
      || (*v23 = 1, v2 = &v29[map[5 * v27 + 2]], *v2)// 检查v29中储存的标记值，以检查该行是否有重复元素
      || (*v2 = 1, v1 = &v29[map[5 * v27 + 3]], *v1)
      || (*v1 = 1, v29[map[5 * v27 + 4]]) )
    {                                           // PS：逗号运算符依次执行表达式，返回最后一个表达式的值
      v22 = 0;
      return v22 & 1;                           // 若同行元素有重复则返回0
    }
    ++v27;
  }
  while ( v24 + 1 < 5 );                        // 行唯一性检查
  v26 = 0LL;
  while ( 1 )
  {
    v20 = v26;
    memset(v28, 0, sizeof(v28));                // 初始化v28作为储存检查列重复标志（类似v29）
    v21 = &v28[map[v26]];
    if ( *v21 )
      break;
    *v21 = 1;
    v19 = &v28[map[v26 + 5]];
    if ( *v19 )
      break;
    *v19 = 1;
    v4 = &v28[map[v26 + 10]];
    if ( *v4 )
      break;
    *v4 = 1;
    v3 = &v28[map[v26 + 15]];
    if ( *v3 )
      break;
    *v3 = 1;
    if ( v28[map[v26 + 20]] )
      break;
    ++v26;
    if ( v20 + 1 >= 5 )                         // 检查完列中全部元素才跳出循环，说明未出现重复
    {
      v16 = 0LL;
      while ( 1 )
      {
        v17 = v16;
        v18 = row[4 * v16];                     // 检查row数组的标记情况
        if ( v18 == 1 )                         // 若为1
        {
          if ( map[5 * v16] < map[5 * v16 + 1] )// 则此处对应元素必须大于其右侧元素，否则
            goto LABEL_27;
        }
        else if ( v18 == 2 && map[5 * v16] > map[5 * v16 + 1] )// 若为2，则此处对应元素必须小于其右侧元素
        {
LABEL_27:                                       // 返回0
          v22 = 0;
          return v22 & 1;
        }
        v15 = row[4 * v16 + 1];
        if ( v15 == 1 )
        {
          if ( map[5 * v16 + 1] < map[5 * v16 + 2] )
            goto LABEL_27;
        }
        else if ( v15 == 2 && map[5 * v16 + 1] > map[5 * v16 + 2] )
        {
          goto LABEL_27;
        }
        v6 = row[4 * v16 + 2];
        if ( v6 == 1 )
        {
          if ( map[5 * v16 + 2] < map[5 * v16 + 3] )
            goto LABEL_27;
        }
        else if ( v6 == 2 && map[5 * v16 + 2] > map[5 * v16 + 3] )
        {
          goto LABEL_27;
        }
        v5 = row[4 * v16 + 3];
        if ( v5 == 1 )
        {
          if ( map[5 * v16 + 3] < map[5 * v16 + 4] )
            goto LABEL_27;
        }
        else if ( v5 == 2 && map[5 * v16 + 3] > map[5 * v16 + 4] )
        {
          goto LABEL_27;
        }                                       // 处理对应行其他列的元素，效果与上文相同
        ++v16;
        if ( v17 + 1 >= 5 )
        {
          v12 = 0LL;
          while ( 1 )
          {
            v13 = v12 + 1;
            v14 = col[5 * v12];
            if ( v14 == 1 )
            {
              v11 = 0;
              if ( map[5 * v12] > map[5 * v13] )
                goto LABEL_26;
            }
            else if ( v14 == 2 )
            {
              v11 = 0;
              if ( map[5 * v12] < map[5 * v13] )
              {
LABEL_26:
                v22 = v11;
                return v22 & 1;                 // 返回0
              }
            }
            v10 = col[5 * v12 + 1];             // 检查row数组的标记情况
            if ( v10 == 1 )                     // 标志为1
            {
              v11 = 0;
              if ( map[5 * v12 + 1] > map[5 * v13 + 1] )// 该元素必须小于对应其下方的元素，否则
                goto LABEL_26;
            }
            else if ( v10 == 2 )                // 标志为2
            {
              v11 = 0;
              if ( map[5 * v12 + 1] < map[5 * v13 + 1] )// 该元素必须大于对应其下方的元素，否则
                goto LABEL_26;
            }
            v9 = col[5 * v12 + 2];
            if ( v9 == 1 )
            {
              v11 = 0;
              if ( map[5 * v12 + 2] > map[5 * v13 + 2] )
                goto LABEL_26;
            }
            else if ( v9 == 2 )
            {
              v11 = 0;
              if ( map[5 * v12 + 2] < map[5 * v13 + 2] )
                goto LABEL_26;
            }
            v8 = col[5 * v12 + 3];
            if ( v8 == 1 )
            {
              v11 = 0;
              if ( map[5 * v12 + 3] > map[5 * v13 + 3] )
                goto LABEL_26;
            }
            else if ( v8 == 2 )
            {
              v11 = 0;
              if ( map[5 * v12 + 3] < map[5 * v13 + 3] )
                goto LABEL_26;
            }
            v7 = col[5 * v12 + 4];
            if ( v7 == 1 )
            {
              v11 = 0;
              if ( map[5 * v12 + 4] > map[5 * v13 + 4] )
                goto LABEL_26;
            }
            else if ( v7 == 2 )
            {
              v11 = 0;
              if ( map[5 * v12 + 4] < map[5 * v13 + 4] )
                goto LABEL_26;
            }
            ++v12;
            v11 = 1;
            if ( v13 >= 4 )
              goto LABEL_26;
          }
        }
      }
    }
  }
  v22 = 0;
  return v22 & 1;
}
```
分析可知该程序执行一个数独游戏，按照要求完成数独如下：
![](http://m.qpic.cn/psc?/V11300AO0tdWfu/LiySpxowE0yeWXwBdXN*SeNL1YvrpIeKt4ZcrH9quQPbYJ*JKcY9zouYhwdTs4ecuWpTMYKZ8dEozyZ8.FhUFRGaZownfNvEYEHqraS6AI4!/b&bo=VAg*BmYITQYHB2Y!&rf=viewer_4)
按照要求用md5加密并包上flag头即可
### [FSCTF 2023]Tea_apk
jadx分析apk，得到以下关键代码：
```java
package com.tutdroid;

import java.io.UnsupportedEncodingException;

/* loaded from: classes.dex */
public final class FlagChecker {
    static final /* synthetic */ boolean $assertionsDisabled = false;
    private static final int DELTA = -1640531527;

    private static int MX(int i, int i2, int i3, int i4, int i5, int[] iArr) {
        return ((i ^ i2) + (iArr[(i4 & 3) ^ i5] ^ i3)) ^ (((i3 >>> 5) ^ (i2 << 2)) + ((i2 >>> 3) ^ (i3 << 4)));
    }

    private FlagChecker() {
    }

    public static final byte[] encrypt(byte[] bArr, byte[] bArr2) {
        return bArr.length == 0 ? bArr : toByteArray(encrypt(toIntArray(bArr, true), toIntArray(fixKey(bArr2), false)), false);
    }

    public static final byte[] encrypt(String str, String str2) {
        try {
            return encrypt(str.getBytes("UTF-8"), str2.getBytes("UTF-8"));
        } catch (UnsupportedEncodingException unused) {
            return null;
        }
    }

    public static final String encryptToBase64String(String str, String str2) {
        byte[] encrypt = encrypt(str, str2);
        if (encrypt == null) {
            return null;
        }
        return Base64.encode(encrypt);
    }

    private static int[] encrypt(int[] iArr, int[] iArr2) {
        int length = iArr.length - 1;
        if (length < 1) {
            return iArr;
        }
        int i = (52 / (length + 1)) + 6;
        int i2 = iArr[length];
        int i3 = 0;
        while (true) {
            int i4 = i - 1;
            if (i <= 0) {
                return iArr;
            }
            i3 += DELTA;
            int i5 = (i3 >>> 2) & 3;
            int i6 = i2;
            int i7 = 0;
            while (i7 < length) {
                int i8 = i7 + 1;
                i6 = iArr[i7] + MX(i3, iArr[i8], i6, i7, i5, iArr2);
                iArr[i7] = i6;
                i7 = i8;
            }
            i2 = MX(i3, iArr[0], i6, i7, i5, iArr2) + iArr[length];
            iArr[length] = i2;
            i = i4;
        }
    }

    private static byte[] fixKey(byte[] bArr) {
        if (bArr.length == 16) {
            return bArr;
        }
        byte[] bArr2 = new byte[16];
        if (bArr.length < 16) {
            System.arraycopy(bArr, 0, bArr2, 0, bArr.length);
        } else {
            System.arraycopy(bArr, 0, bArr2, 0, 16);
        }
        return bArr2;
    }

    private static int[] toIntArray(byte[] bArr, boolean z) {
        int[] iArr;
        int length = (bArr.length & 3) == 0 ? bArr.length >>> 2 : (bArr.length >>> 2) + 1;
        if (z) {
            iArr = new int[length + 1];
            iArr[length] = bArr.length;
        } else {
            iArr = new int[length];
        }
        int length2 = bArr.length;
        for (int i = 0; i < length2; i++) {
            int i2 = i >>> 2;
            iArr[i2] = iArr[i2] | ((bArr[i] & 255) << ((i & 3) << 3));
        }
        return iArr;
    }

    private static byte[] toByteArray(int[] iArr, boolean z) {
        int length = iArr.length << 2;
        if (z) {
            int i = iArr[iArr.length - 1];
            int i2 = length - 4;
            if (i < i2 - 3 || i > i2) {
                return null;
            }
            length = i;
        }
        byte[] bArr = new byte[length];
        for (int i3 = 0; i3 < length; i3++) {
            bArr[i3] = (byte) (iArr[i3 >>> 2] >>> ((i3 & 3) << 3));
        }
        return bArr;
    }

    public static boolean check(String str) {
        return encryptToBase64String(str, "ABvWW7hqwNvHUhfP").equals("vlgg9nNjUcYuWzBSSOwKxbMD2rhFgf4zuiyMpLxpNkM=");
    }
}
```
在MainActivity中查找到FlagChecker.check函数，点击查看发现XXTEA加密算法

用密码学工具箱秒出
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SSz*1rOkUhLom4jEE*wl5MuVGLbkW0OHAZTrgvrIzUv9YjtsCy*3ZkHA4TZwL7sfiuF4Dvg3u4.Opf7YGb3QQMI!/b&bo=JgQYAiYEGAIDByI!&rf=viewer_4)

### [广东强网杯 2021 个人组]goodpy
python字节码逆向
```python
enc = [56, 92, 6, 1, 47, 4, 2, 62, 129, 84, 97, 100, 5, 100, 87, 89, 
       60, 11, 84, 87, 244, 103, 118, 247, 47, 96, 47, 244, 98, 127, 81, 102]
a=32
for i in range(a):
    if i % 7 != 1:
        '''            
        541 COMPARE_OP               2 (==)
        544 POP_JUMP_IF_FALSE      553
        由于“FALSE"，所以判断条件应该是不相等时进行异或操作
        '''
        enc[i] = enc[i] ^ 119
tmp3=enc[0]
tmp2=enc[1]
tmp1=enc[2]
for i in range(a - 3):
    enc[i] = enc[i+3]
enc[a-3] = tmp1
enc[a-2] = tmp2
enc[a-1] = tmp3

for i in range(a):
    enc[i] = enc[i] - 8
for i in range(a):
    enc[i] = enc[i] ^ 51
for i in range(a):
    enc[i] = enc[i] + 9
for i in range(a):
    print(chr(enc[i]), end='')
#flag{S1FAbA4kyP14QDfTlElQGM6Ccp}
```
### [HGAME 2023 week1]a_cup_of_tea
关键代码:
```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  int _bool; // eax
  char *out; // rcx
  __m128i si128; // [rsp+20h] [rbp-19h] BYREF
  int enc[8]; // [rsp+30h] [rbp-9h] BYREF
  __int16 v8; // [rsp+50h] [rbp+17h]
  __int128 input; // [rsp+58h] [rbp+1Fh] BYREF
  __int128 v10[2]; // [rsp+68h] [rbp+2Fh] BYREF
  __int16 v11; // [rsp+88h] [rbp+4Fh]

  enc[0] = 0x2E63829D;
  input = 0i64;
  memset(v10, 0, sizeof(v10));
  v11 = 0;
  enc[1] = -1051836401;
  si128 = _mm_load_si128((const __m128i *)&xmmword_7FF7ABD222B0);
  enc[2] = 0x9B39BFB9;
  enc[3] = 0x5A1F8B14;
  enc[4] = 0x61886DDE;
  enc[5] = 0x6565C6CF;
  enc[6] = 0x9F064F64;
  enc[7] = 0x236A43F6;
  v8 = 0x7D6B;
  printf("nice tea!\n> ");
  scanf("%50s", &input);
  tea_enc((unsigned int *)&input, si128.m128i_i32);
  tea_enc((unsigned int *)&input + 2, si128.m128i_i32);
  tea_enc((unsigned int *)v10, si128.m128i_i32);
  tea_enc((unsigned int *)v10 + 2, si128.m128i_i32);
  _bool = memcmp(&input, enc, 0x22ui64);
  out = "wrong...";
  if ( !_bool )
    out = "Congratulations!";
  printf(out);
  return 0;
}
__int64 __fastcall tea_enc(unsigned int *enc, int *key)
{
  int key1; // ebx
  int sum; // r11d
  int key2; // edi
  int key3; // esi
  int key4; // ebp
  unsigned int enc1; // r9d
  __int64 i; // rdx
  unsigned int enc2; // r10d
  __int64 result; // rax

  key1 = *key;
  sum = 0;
  key2 = key[1];
  key3 = key[2];
  key4 = key[3];
  enc1 = *enc;
  i = 32i64;
  enc2 = enc[1];
  do
  {
    sum -= 0x543210DD;
    enc1 += (sum + enc2) ^ (key1 + 16 * enc2) ^ (key2 + (enc2 >> 5));
    result = sum + enc1;
    enc2 += result ^ (key3 + 16 * enc1) ^ (key4 + (enc1 >> 5));
    --i;
  }
  while ( i );
  *enc = enc1;
  enc[1] = enc2;
  return result;
}
```
exp:
```c
#include<stdio.h>
#include<string.h>
#include<stdint.h>
int main()
{
    unsigned int key1 = 0x12345678;
    unsigned int key2 = 0x23456789;
    unsigned int key3 = 0x34567890;
    unsigned int key4 = 0x45678901;
    unsigned int sum = 0x79bde460;
    int i = 32;
    unsigned int enc1 = 0x9F064F64;
    unsigned int enc2 = 0x236A43F6;//一定要注意把数据设置为无符号类型！！！
    int enc[2] = { 0 };
    do
    {
        enc2 -= (sum + enc1) ^ (key3 + 16 * enc1) ^ (key4 + (enc1 >> 5));
        enc1 -= (sum + enc2) ^ (key1 + 16 * enc2) ^ (key2 + (enc2 >> 5));
        sum -= -1412567261;
        --i;
    } while (i);
    *enc = enc1;
    enc[1] = enc2;
    for (int j = 0; j < 2; j++) // 输出解密后的数据
    {
        for (int m = 0; m < 4; m++)
        {
            printf("%c", enc[j] );  // 按字节输出，恢复原始字符
            enc[j] >>= 8;
        }
    }
    printf("%c%c", 0x6b, 0x7d);
    return 0;


    //第一轮：hgame{Te
    //第二轮：a_15_4_v
    //第三轮：3ry_h3a1
    //第四轮：thy_drln
    //补充后缀：k}
    //hgame{Tea_15_4_v3ry_h3a1thy_drlnk}
}
```
注意在原程序的密文定义中v8紧跟在enc数组的栈内地址后面，其没有进行tea加密，而是以明文形式存储着密文的最后两位内容
### [SWPUCTF 2023 秋季新生赛]Junk Code
花指令，E9全部patch为90即可

exp:
```c
#include<stdio.h>
#include<string.h>
#include<stdint.h>
int main()
{
    char* enc = "NRQ@PC}Vdn4tHV4Yi9cd#\\}jsXz3LMuaaY0}nj]`4a5&WoB4glB7~u";
    char dec[100] = { 0 };
    for (int i = 0; i < strlen(enc); ++i)
    {
        dec[i]=enc[i] ^ (i % 9);
        putchar(dec[i]);
    }
    //NSSCTF{Qln5vKR1_n1ce!_you_r3MOved_7unk_c0d3!_oC6dhG1y}
}
```
### [XYCTF2025]WARMUP
搜索VBS相关知识可得：
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SRo1g94E5iJgY8ac7d32sCkCe9m.fi819M9xvUUhRrTL41ZBf.AkaSeQv7Y9CI2N3GpxX7CbsQj2PU707xX.KP4!/b&bo=QQanAUEGpwEDFzI!&rf=viewer_4)
修改后运行得到以下内容：
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SZ9yLXeLCoO7EFD7tYHYVSc9szgvLEWmbP*heMe2heRNuXQDp99X74i1eGHeRl46rKNH*ZahvUgQLc59XQfUt*0!/b&bo=NgZmBTYGZgUDNxI!&rf=viewer_4)
一眼RC4
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SXwpPbb.jtO9l4hFl4JsiySTRuwlJ4txLd58opeeQ26sbJAplHSGG*ZItzb2JOEMMePwVtMrNZCV0HIwb04bSkI!/b&bo=tgZ2ArYGdgIDFzI!&rf=viewer_4)
### [XYCTF2025]Dragon
MASM风格的汇编代码，但是编译不出来，让AI帮忙还原
```c
#include <cstdint>
#include <cstdio>
#include <cstring>

// CRC64-ECMA 多项式
constexpr uint64_t CRC64_POLY = 0x42F0E1EBA9EA3693;

uint64_t calculate_crc64_direct(const uint8_t* data, size_t size) {
    uint64_t crc = ~0ULL; // 初始化为全1
    
    for (size_t i = 0; i < size; ++i) {
        // 处理每个字节
        crc ^= static_cast<uint64_t>(data[i]) << 56;
        
        // 处理每个bit
        for (int j = 0; j < 8; ++j) {
            const bool msb = (crc & (1ULL << 63)) != 0;
            crc <<= 1;
            if (msb) {
                crc ^= CRC64_POLY;
            }
        }
    }
    
    return crc ^ ~0ULL; // 最终取反
}

int main() {
    // 预计算的CRC64校验值数组
    const uint64_t enc[] = {
        0xdc63e34e419f7b47, 0x031ef8d4e7b2bfc6, 0x12d62fbc625fd89e,
        0x83e8b6e1cc5755e8, 0xfc7bb1eb2ab665cc, 0x9382ca1b2a62d96b,
        0xb1fff8a07673c387, 0x0da81627388e05e1, 0x9ef1e61ae8d0aab7,
        0x92783fd2e7f26145, 0x63c97ca1f56fe60b, 0x9bd3a8b043b73aab
    };

    char input[66] = {}; // 输入缓冲区
    
    printf("Input U flag:");
    scanf("%s", input);

    const size_t input_len = strlen(input);
    const size_t expected_chunks = sizeof(enc)/sizeof(enc[0]);

    // 每2个字符验证一个CRC
    bool valid = true;
    for (size_t i = 0, idx = 0; 
         i < input_len && idx < expected_chunks; 
         i += 2, ++idx) 
    {
        const uint64_t crc = calculate_crc64_direct(
            reinterpret_cast<const uint8_t*>(&input[i]), 2);
        
        if (crc != enc[idx]) {
            printf("Error!\n");
            valid = false;
            break;
        }
    }

    if (valid) {
        printf("Success\n");
    }

    return 0;
}
```
可知是CRC64校验值，直接用python脚本爆破即可
```python
def calculate_crc64_direct(data):
    crc = 0xFFFFFFFFFFFFFFFF
    for byte in data:
        crc ^= (byte << 56)
        crc &= 0xFFFFFFFFFFFFFFFF
        for _ in range(8):
            msb = crc & (1 << 63)
            crc = (crc << 1) & 0xFFFFFFFFFFFFFFFF
            if msb:
                crc ^= 0x42F0E1EBA9EA3693
    return crc ^ 0xFFFFFFFFFFFFFFFF

enc = [
    0xdc63e34e419f7b47, 0x031ef8d4e7b2bfc6, 0x12d62fbc625fd89e,
    0x83e8b6e1cc5755e8, 0xfc7bb1eb2ab665cc, 0x9382ca1b2a62d96b,
    0xb1fff8a07673c387, 0x0da81627388e05e1, 0x9ef1e61ae8d0aab7,
    0x92783fd2e7f26145, 0x63c97ca1f56fe60b, 0x9bd3a8b043b73aab
]

flag = []
for target in enc:
    found = False
    for c1 in range(32, 127):
        for c2 in range(32, 127):
            if calculate_crc64_direct([c1, c2]) == target:
                flag.append(chr(c1) + chr(c2))
                found = True
                break
        if found:
            break
    if not found:
        print("Failed to find a valid pair")
        exit()

print("Flag:", ''.join(flag))
```
## 捕获文件babymaooer
“这是今天软件系统安全赛的唯一一道逆向题 也是个西北赛区零解题” “它会在某个目录释放一个文件 然后立即删掉” “你们俩下周有空搭配用api monitor和process monitor把那个释放的文件搞出来 写进周报里叭”

先搭Win10虚拟机

运行附件程序后使用Process Monitor进行监控，按照如下内容设置过滤器，即可得到程序运行进行文件操作相关的进程，但是并没有见到删除文件的操作
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SWQoqLgMJjzSwd7fzWmNQ6DRzYQeZRC7CFog.*hxhWOzPLWk9zrHoKd5gA2PeaGeKLhss6DEKy4cqHHldCINN7A!/b&bo=9wmiA*cJogMDByI!&rf=viewer_4)

实际是使用了一个函数标记位设置了删除属性，重新筛选文件操作列表
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SQaHx9TbxxA*y2GmldriJq3fql6RL5H66NqSG9UDEo8wXZMSfVx5YWWWjGALITSFOR8tRWVgxP13YiqbjBoXOQ0!/b&bo=HAiFBBwIhQQDNxI!&rf=viewer_4)
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SeqIbDu9On8EHKX594B.gxQTGR*FEbPlqNURbbK62UV6SKyXIEieZm9ee4jsaUIVieU1JmckDCdP5vNs4WJAKDg!/b&bo=HgkPAx4JDwMDByI!&rf=viewer_4)

用APIMonitor把ntdll的api全勾上，其他全不勾，只选中文件操作那几个api，跑起来然后一个个api断下来，断到这个api前就能找到文件了
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SR**WRJcdJSEFC5TrNjQO7oIDkPezusHG.MU80vs9Oi3iBduNFo0tDNNYcr.kLQN0RVroR6XGNmNVbtnMs9D6k4!/b&bo=hQfwBIUH8AQDJwI!&rf=viewer_4)