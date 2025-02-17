# hanafuda_store's Weekly Report (week11)
## 刷题
### [SWPUCTF 2021 新生赛]easyapp
安卓程序，用jadx打开
![]()
在MainActivity中找到关键代码，即可编写exp
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
### [HNCTF 2022 WEEK3]Double
用IDA反汇编程序可以看到如下代码
```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  int buf; // [rsp+0h] [rbp-70h] BYREF
  int i; // [rsp+4h] [rbp-6Ch]
  int j; // [rsp+8h] [rbp-68h]
  int v8; // [rsp+10h] [rbp-60h]
  int v9; // [rsp+14h] [rbp-5Ch]
  int pipedes[2]; // [rsp+18h] [rbp-58h] BYREF
  char input[56]; // [rsp+20h] [rbp-50h] BYREF
  unsigned __int64 v12; // [rsp+58h] [rbp-18h]

  v12 = __readfsqword(0x28u);
  pipe(pipedes);
  if ( fork() )
  {
    puts("i'm parent");
    close(pipedes[1]);
    for ( i = 0; i <= 29; ++i )
    {
      read(pipedes[0], &buf, 1uLL);
      v9 = i ^ buf;
      if ( arr[i ^ buf] != enc[i] )
      {
        puts("error!");
        exit(0);
      }
    }
    puts("you are right!");
    close(pipedes[0]);
    return 0;
  }
  else
  {
    puts("i am child");
    close(pipedes[0]);
    puts("please input your flag!");
    __isoc99_scanf("%s", input);
    for ( j = 0; j < strlen(input); ++j )
    {
      v8 = j;
      write(pipedes[1], &input[j], 1uLL);
    }
    close(pipedes[1]);
    return 0;
  }
}
```
该程序是输入的flag与i异或（parent算法）后作为索引从arr中取出数据与enc中的数据比较（child算法）。按顺序在arr中找到enc的元素，再把被找到元素的下标经过和i的异或即可得到flag。
exp:
```python
35756, 22784, 12417, 19994, 22941, 23523, 23625, 62779, 65498, 47727, 15965, 10168, 23377, 35376,10768]
table=[15374, 50828, 20199, 31702, 49944, 53123, 60189, 12367, 65280, 11322, 26221, 26520, 53269, 7766, 22058,\
    35457, 23701, 30880, 24813, 4372, 44507, 29484, 20880, 4405, 58195, 59849, 2735, 10264, 9782, 39718,
    15625, 6335, 10852, 20285, 44639, 19994, 18794, 56196, 9411, 65498, 14219, 8030, 53361, 35953, 1582,
    55001, 36724, 59478, 59973, 48836, 1158, 61760, 29338, 32765, 45037, 24376, 1788, 19389, 13090, 25822,
    17807, 35376, 29972, 35756, 46468, 47345, 29372, 49634, 45232, 23625, 43967, 21403, 56272, 3500, 60168,
    23523, 15154, 54581, 8108, 64355, 3608, 14230, 20369, 26180, 38824, 3590, 64409, 43136, 51586, 34971,
    20361, 16356, 61054, 3047, 35533, 12808, 10768, 25394, 10966, 976, 62779, 22784, 366, 63784, 23377,
    10168, 48879, 9019, 382, 25584, 49189, 58653, 15684, 28470, 5881, 12417, 28767, 46966, 22941, 20188,
    25943, 48662, 36622, 47727, 15965, 29552, 5958, 27660, 28971, 23739, 25433, 36015, 20183, 44744, 64423,
    29885, 58289, 23863, 19790, 33028, 46096, 34390, 8566, 9147, 9310, 43310, 44314, 58672, 55164, 57411,
    37142, 60892, 43794, 3431, 30341, 15545, 49102, 23083, 14841, 37003, 65086, 48408, 56148, 3243, 15446,
    65139, 55668, 3848, 23432, 41202, 15752, 40420, 2357, 21172, 41792, 60040, 48754, 28110, 27179, 12614,
    856, 3919, 64096, 9707, 56007, 1898, 15719, 17392, 40860, 23398, 29027, 36667, 32443, 1489, 25284,
    40853, 7686, 23896, 59780, 30131, 3423, 61016, 9104, 64401, 10410, 34781, 62954, 17468, 26434, 6553,
    35049, 64782, 51389, 22008, 47881, 27664, 32872, 52692, 10662, 56735, 52931, 25111, 48680, 15994,
    59166, 50547, 1067, 56838, 51508, 13777, 61257, 25507, 61583, 9953, 58910, 10000, 46771, 4320, 48438,
    18844, 33862, 46612, 59681, 56109, 19128, 19595, 53672, 27291, 55319, 62281, 52882, 32653, 19558,
    53056, 37225]
flag=""
for i in range(30):
    index=table.index(a[i])
    flag+=str(chr(index^i))
print(flag)
```
### [CISCN 2022 东北]crackme_Android
用JADX打开apk文件，在此处找到反编译出来的源码
![]()
```java
package com.example.crackme1;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;

/* loaded from: classes3.dex */
public class MainActivity extends AppCompatActivity {
    public String md5(String info) {
        try {
            MessageDigest md5 = MessageDigest.getInstance("MD5");
            md5.update(info.getBytes(StandardCharsets.UTF_8));
            byte[] encryption = md5.digest();
            StringBuilder stringBuffer = new StringBuilder();
            for (byte b : encryption) {
                if (Integer.toHexString(b & 255).length() == 1) {
                    stringBuffer.append("0");
                    stringBuffer.append(Integer.toHexString(b & 255));
                } else {
                    stringBuffer.append(Integer.toHexString(b & 255));
                }
            }
            return stringBuffer.toString();
        } catch (Exception e) {
            return "";
        }
    }

    public boolean check(CharSequence flag) {
        if (flag.length() != 38 || !flag.subSequence(0, 5).toString().equals("flag{") || flag.charAt(flag.length() - 1) != '}') {
            return false;
        }
        CharSequence data = flag.subSequence(5, flag.length() - 1);
        StringBuilder sumval = new StringBuilder();
        for (int i = 0; i < data.length(); i += 4) {
            sumval.append(md5(data.subSequence(i, i + 4).toString()));
        }
        return sumval.toString().equals("8393931a16db5a00f464a24abe24b17a9040b57d9cb2cbfa6bdc61d12e9b51f2789e8a8ae9406c969118e75e9bc65c4327fbc7c3accdf2c54675b0ddf3e0a6099b1b81046d525495e3a14ff6eae76eddfa1740cd6bd483da0f7684b2e4ec84b371f07bf95f0113eefab12552181dd832af8d1eb220186400c494db7091e402b0");
    }

    @Override // androidx.fragment.app.FragmentActivity, androidx.activity.ComponentActivity, androidx.core.app.ComponentActivity, android.app.Activity
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Button button = (Button) findViewById(R.id.button);
        final EditText flagInput = (EditText) findViewById(R.id.flagInput);
        button.setOnClickListener(new View.OnClickListener() { // from class: com.example.crackme1.MainActivity.1
            @Override // android.view.View.OnClickListener
            public void onClick(View view) {
                CharSequence flag = flagInput.getText();
                if (MainActivity.this.check(flag)) {
                    Toast.makeText(MainActivity.this, "Right!", 0).show();
                } else {
                    Toast.makeText(MainActivity.this, "Wrong!", 0).show();
                }
            }
        });
    }
}
```
这段代码来自一个 Android 应用的 MainActivity 类，主要功能是检查用户输入的 flag 是否与预定义的字符串匹配，具体通过 MD5 哈希运算来进行校验。
可以通过MD5哈希值查询网站 https://www.cmd5.com/ 按位查询出flag
### [HDCTF 2023]enc
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
### [强网杯 2022]GameMaster
C#纸牌程序，用dnspy打开，查看反编译代码gamemessage文件的操作，提取出关键部分编写exp的第一部分：
```python
from Crypto.Cipher import AES

# 定义AES加密算法的密钥和块大小
key = b'Brainstorming!!!'
block_size = 16

# 创建AES加密算法对象
cipher = AES.new(key, AES.MODE_ECB)

# 打开待解密的文件
with open('D:\\桌面\\gamemessage', 'rb') as f:
    ciphertext = f.read()

# 对读取的数据进行异或操作
ciphertext = bytes([byte ^ 34 for byte in ciphertext])

# 对密文进行解密
plaintext = cipher.decrypt(ciphertext)

# 将解密后的明文写入到新文件中
with open('D:\\桌面\\gamemessage2', 'wb') as f:
    f.write(plaintext)
```
的到新的gamemessge2文件，用010Editor查看找到PE文件的头，删掉前面的内容，改为dll文件再次拖入dnspy中分析，核心内容如下
```c#
using System;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace T1Class
{
	// Token: 0x02000002 RID: 2
	public class T1
	{
		// Token: 0x06000001 RID: 1 RVA: 0x00002050 File Offset: 0x00000250
		private static void Check1(ulong x, ulong y, ulong z, byte[] KeyStream)
		{
			int num = -1;
			for (int i = 0; i < 320; i++)
			{
				x = (((x >> 29) ^ (x >> 28) ^ (x >> 25) ^ (x >> 23)) & 1UL) | (x << 1);
				y = (((y >> 30) ^ (y >> 27)) & 1UL) | (y << 1);
				z = (((z >> 31) ^ (z >> 30) ^ (z >> 29) ^ (z >> 28) ^ (z >> 26) ^ (z >> 24)) & 1UL) | (z << 1);
				bool flag = i % 8 == 0;
				if (flag)
				{
					num++;
				}
				KeyStream[num] = (byte)((long)((long)KeyStream[num] << 1) | (long)((ulong)((uint)(((z >> 32) & 1UL & ((x >> 30) & 1UL)) ^ ((((z >> 32) & 1UL) ^ 1UL) & ((y >> 31) & 1UL))))));
			}
		}

		// Token: 0x06000002 RID: 2 RVA: 0x00002110 File Offset: 0x00000310
		private static void ParseKey(ulong[] L, byte[] Key)
		{
			for (int i = 0; i < 3; i++)
			{
				for (int j = 0; j < 4; j++)
				{
					Key[i * 4 + j] = (byte)((L[i] >> j * 8) & 255UL);
				}
			}
		}

		// Token: 0x06000003 RID: 3 RVA: 0x0000215C File Offset: 0x0000035C
		public T1()
		{
			try
			{
				string environmentVariable = Environment.GetEnvironmentVariable("AchivePoint1");
				string environmentVariable2 = Environment.GetEnvironmentVariable("AchivePoint2");
				string environmentVariable3 = Environment.GetEnvironmentVariable("AchivePoint3");
				bool flag = environmentVariable == null || environmentVariable2 == null || environmentVariable3 == null;
				if (!flag)
				{
					ulong num = ulong.Parse(environmentVariable);
					ulong num2 = ulong.Parse(environmentVariable2);
					ulong num3 = ulong.Parse(environmentVariable3);
					ulong[] array = new ulong[3];
					byte[] array2 = new byte[40];
					byte[] array3 = new byte[40];
					byte[] array4 = new byte[12];
					byte[] array5 = new byte[]
					{
						101, 5, 80, 213, 163, 26, 59, 38, 19, 6,
						173, 189, 198, 166, 140, 183, 42, 247, 223, 24,
						106, 20, 145, 37, 24, 7, 22, 191, 110, 179,
						227, 5, 62, 9, 13, 17, 65, 22, 37, 5
					};
					byte[] array6 = new byte[]
					{
						60, 100, 36, 86, 51, 251, 167, 108, 116, 245,
						207, 223, 40, 103, 34, 62, 22, 251, 227
					};
					array[0] = num;
					array[1] = num2;
					array[2] = num3;
					T1.Check1(array[0], array[1], array[2], array2);
					bool flag2 = array5.SequenceEqual(array2);
					if (flag2)
					{
						T1.ParseKey(array, array4);
						for (int i = 0; i < array6.Length; i++)
						{
							array6[i] ^= array4[i % array4.Length];
						}
						MessageBox.Show("flag{" + Encoding.Default.GetString(array6) + "}", "Congratulations!", MessageBoxButtons.OK);
					}
				}
			}
			catch (Exception)
			{
			}
		}
	}
}
```
由此可写出exp：
```python
from z3 import *

# 定义环境变量
AchivePoint1 = BitVec('AchivePoint1', 64)
AchivePoint2 = BitVec('AchivePoint2', 64)
AchivePoint3 = BitVec('AchivePoint3', 64)

# 定义密钥流比较的目标
array5 = [
    101, 5, 80, 213, 163, 26, 59, 38, 19, 6,
    173, 189, 198, 166, 140, 183, 42, 247, 223, 24,
    106, 20, 145, 37, 24, 7, 22, 191, 110, 179,
    227, 5, 62, 9, 13, 17, 65, 22, 37, 5
]

array6 = [
    60, 100, 36, 86, 51, 251, 167, 108, 116, 245,
    207, 223, 40, 103, 34, 62, 22, 251, 227
]

# 定义位移函数
def bit_shift_operations(x, y, z):
    x = ((x >> 29) ^ (x >> 28) ^ (x >> 25) ^ (x >> 23)) & 1 | (x << 1)
    y = ((y >> 30) ^ (y >> 27)) & 1 | (y << 1)
    z = ((z >> 31) ^ (z >> 30) ^ (z >> 29) ^ (z >> 28) ^ (z >> 26) ^ (z >> 24)) & 1 | (z << 1)
    return x, y, z

# 构建位流生成的约束条件
def check_key_stream(AchivePoint1, AchivePoint2, AchivePoint3):
    key_stream = [0] * 40
    x, y, z = AchivePoint1, AchivePoint2, AchivePoint3

    for i in range(320):
        x, y, z = bit_shift_operations(x, y, z)

        num = i // 8  # 每8次迭代，更新一次key_stream
        key_stream[num] = (key_stream[num] << 1) | (((z >> 32) & 1) & ((x >> 30) & 1)) ^ (((z >> 32) & 1) ^ 1) & ((y >> 31) & 1)

    # 构造每个byte的约束条件
    key_constraints = []
    for i in range(40):
        key_constraints.append(key_stream[i] == array5[i])

    return key_constraints

# 使用Z3求解
solver = Solver()

# 添加约束
solver.add(check_key_stream(AchivePoint1, AchivePoint2, AchivePoint3))

# 求解
if solver.check() == sat:
    model = solver.model()
    x_val = model[AchivePoint1].as_long()
    y_val = model[AchivePoint2].as_long()
    z_val = model[AchivePoint3].as_long()
    
    # 输出求解得到的 AchivePoint1, AchivePoint2, AchivePoint3 的值
    print(f"AchivePoint1: {x_val}")
    print(f"AchivePoint2: {y_val}")
    print(f"AchivePoint3: {z_val}")
    
    # 使用求解得到的值生成密钥流
    def generate_key_stream(x, y, z):
        key_stream = [0] * 40
        for i in range(320):
            x, y, z = bit_shift_operations(x, y, z)

            num = i // 8  # 每8次迭代，更新一次key_stream
            key_stream[num] = (key_stream[num] << 1) | (((z >> 32) & 1) & ((x >> 30) & 1)) ^ (((z >> 32) & 1) ^ 1) & ((y >> 31) & 1)

        return key_stream

    # 生成 array4（密钥）
    array4 = []
    array4 += ulong_to_bytes_le(x)  # 分解 x 为 4 字节
    array4 += ulong_to_bytes_le(y)  # 分解 y 为 4 字节
    array4 += ulong_to_bytes_le(z)  # 分解 z 为 4 字节

    # 预定义的密文 array6
    array6 = bytes([
        60, 100, 36, 86, 51, 251, 167, 108, 116, 245,
    207, 223, 40, 103, 34, 62, 22, 251, 227
    ])

# 异或解密
flag_bytes = bytes([array6[i] ^ array4[i % len(array4)] for i in range(len(array6))])

# 转换为字符串（使用 latin-1 编码确保所有字节可解码）
flag = flag_bytes.decode("latin-1")

print(f"flag{{{flag}}}")
```
## 密码学
学习了DES、三重DES、AES的加密算法，掌握了其算法。
## Python
在复习和巩固前面学过内容的基础上，我进一步学习了字典、结构化数据以及字符串的有关操作，提升了我相应的编程能力有助于我在以后的CTF题目中写exp的阶段更便捷地使用Python而不是C语言编写。
## C++
了解了C++与C语言的不同之处，明晰了面向对象编程和泛型编程思想，掌握了一些基础语法，重点学习了操作符重载用于输入与输出、enum枚举类型以及C++中的对象与C语言中结构体的区别，这有助于我后续对C++程序的逆向分析。
## 调整工具
工欲善其事，必先利其器。我解决了自己所下版本x64dbg没有scylla插件的问题；然后给自己的IDA换了喜欢的VScode风格深色主题，安装了一些有用的插件，解决了lazyIDA插件无法正常使用的问题；下载了雷电模拟器用于安卓逆向分析。
## Linux C
开始看这本书了，但是还没怎么深入，大体浏览得知了AuTo✌️指定我们学习的部分并非编程方法，而是程序内存分配管理、进程与线程及其间通信等程序运行有关的内容，这部分内容我之前也看过相关课程粗略了解过，后期我深入学习也能更加得心应手地展开。