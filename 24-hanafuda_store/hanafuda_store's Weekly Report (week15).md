# hanafuda_store's Weekly Report (week15)
## 初识反调试
1. `IsDebuggerPresent()`函数

包含在`debugapi.h`头文件中，函数原型：
```c
BOOL IsDebuggerPresent();   //未在调试器中运行时返回值为零，否则为非零值
```
该函数允许程序确定是否正在调试它，以便可以修改其行为

2. `PEB->BeingDebugged`

FS标志段寄存器总是指向TEB（当前的线程环境块），其中包含一个指针指向当前PEB（进程环境块），该结构体包含一个成员BeingDebugged，它是一个标志位，用于标识当前进程是否正在被调试

![](https://a1.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*ScWUasj8l6FTRnRDvQp8TIpYjRifnw2KruccXACmMh.zN9k8dike5SuOW2x*8g.kyg8R2UDe5UuCg6Z3CMrPL6o!/b&ek=1&kp=1&pt=0&bo=kQcwBJEHMAQDJwI!&tl=1&vuin=934483106&tm=1742738400&dis_t=1742740099&dis_k=a21c9396998d681cc9165ecbb06e0d5e&sce=60-2-2&rf=viewer_4)

3. `NtQueryInformationProcess`函数

包含在`ntdll.h`头文件中，语法如下：
```cpp
__kernel_entry NTSTATUS NtQueryInformationProcess(
  [in]            HANDLE           ProcessHandle,
  [in]            PROCESSINFOCLASS ProcessInformationClass,
  [out]           PVOID            ProcessInformation,
  [in]            ULONG            ProcessInformationLength,
  [out, optional] PULONG           ReturnLength
);
```

其检索一个WORD_PTR值，该值是进程的调试器端口号。非零值指示进程正在环3调试器的控制下运行，如果进程没有调试器，则返回零
4. EPROCESS_DebugPort
获取系统内核中标记进程信息的结构体EPROCESS，通过EPROCESS结构体中的DebugPort成员判断进程是否正在被调试，一般无法使用普通方法实现，需要内核调试

![](https://a1.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SSFNJvhTG0z*jfoUPNVVQqDZRkS8JITKydM7rfseX6SuCsM1uG37ORUHbsqFIaWP7USKLo5x7U1P.7St7WMB5sU!/b&ek=1&kp=1&pt=0&bo=oAh3BKAIdwQDJwI!&tl=1&vuin=934483106&tm=1742738400&dis_t=1742741532&dis_k=7a8ab9647b6de2a88bf0fe8e237dc5aa&sce=60-2-2&rf=viewer_4)

5. 异常处理检测

处理异常时，正常运行过程会将信息发给Windows的SEH异常捕获流程，而进行调试时则会发给调试器

![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SbqgYDX6PeFhKznn5*BNwXZAriEdT8Sfr0KSuWIbypVroHFiP8zGVQ.a5iLWbTDOjNcyUcglVCKA9iXNYdO8PNY!/b&bo=DgjAAw4IwAMDByI!&rf=viewer_4)

6. 断点检测

函数断点体现为0xCC，可通过对比内存数据中的指令数据与磁盘内文件的数据进行对比，如发现存在不同，则说明有断点，即程序被调试

![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*Scyi7cExO23Hp.x1*TjFLtXqbO17DZXFvDMlSmdJjEKYUaw5MaIRrSpmq0D*8mUBZ58OguGqH7EUY*G08BkrfwA!/b&bo=HQKRAx0CkQMDByI!&rf=viewer_4)

7. 检测调试器进程

通过枚举进程，判断进程名是否为调试器进程名，如果是，则说明程序正在被调试
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SSNTwaMYsBPht0aslnMAkqjzX5vszhkBeJIgdvr2RKDO6UnQz7bsfpzBfIeStJa4MP2WCiF5x3WgPpmH2BhbASY!/b&bo=4weoBOMHqAQDByI!&rf=viewer_4)

还可通过查看是否存在调试器的窗口，判断程序是否正在被调试。可使用VC++中附带的Spy++查找窗口名

![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SYTphlDnllGnUpzo2tgEM4v8UY22GVurmPl6jDXD*84OIAqrUV6jtPuLQGo2RVkYWXZ00rcjfep7cSkCmBO1Buc!/b&bo=awYBA2sGAQMDR2I!&rf=viewer_4)

8. 时间检测

![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SRjP01XHhp.RJeU1Xb*KIMfkXBiGMQHf9j5uwhhnRwcGXBFbjWaRQRHbvd5OrLhSOKl8WRRM5vVppSp0K9aNC6g!/b&bo=4wYXBOMGFwQDByI!&rf=viewer_4)

程序运行时，如果被调试，则由于会出现单步运行等过程，程序运行速度会变慢，因此可通过检测程序运行时间，判断程序是否正在被调试

## 刷题
### ADCTF{Android_startup_here!}
程序输出界面：
```bash
物品的重量和价值为:
-------------------------------------
| 物品编号 | 重量 | 价值 |
-------------------------------------
|    1    |   2   |   8   |
|    2    |   5   |   1   |
|    3    |   10   |   5   |
|    4    |   9   |   9   |
|    5    |   3   |   5   |
|    6    |   6   |   6   |
|    7    |   2   |   8   |
|    8    |   2   |   2   |
|    9    |   6   |   3   |
|    10    |   8   |   7   |
|    11    |   2   |   5   |
|    12    |   3   |   4   |
|    13    |   3   |   3   |
|    14    |   2   |   7   |
|    15    |   9   |   6   |
|    16    |   8   |   7   |
|    17    |   2   |   9   |
|    18    |   10   |   3   |
|    19    |   8   |   10   |
|    20    |   6   |   5   |
|    21    |   4   |   2   |
|    22    |   3   |   4   |
|    23    |   4   |   5   |
|    24    |   2   |   2   |
|    25    |   4   |   9   |
|    26    |   8   |   5   |
|    27    |   3   |   8   |
|    28    |   8   |   10   |
|    29    |   4   |   2   |
|    30    |   10   |   9   |
|    31    |   7   |   6   |
|    32    |   1   |   3   |
|    33    |   9   |   7   |
|    34    |   1   |   3   |
|    35    |   5   |   9   |
|    36    |   7   |   6   |
|    37    |   1   |   10   |
|    38    |   1   |   1   |
|    39    |   7   |   2   |
|    40    |   4   |   9   |
-------------------------------------
HDCTF淘宝店今天开业啦,你来到了淘宝店看到了琳琅满目的商品,这么多商品你都想要,怎么办鸭??
不知道要咋办惹,你只的背包只有50的容量,但你想买到价值最高的商品
你必须在50的容量内买到价值最大的商品
商品的编号从小到大排列即为flag
注意！每个商品只能拿一次!!
请输入你选择的物品编号
```
0-1背包问题，可使用动态规划求解，具体代码如下：
```python
def knapsack(W, wt, val, n):
    # 创建动态规划表格
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    
    # 填充DP表
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], 
                             dp[i-1][w - wt[i-1]] + val[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    
    # 回溯查找选中的物品
    res = dp[n][W]
    w = W
    selected = []
    
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == dp[i-1][w]:
            continue
        else:
            # 当前物品被选中
            selected.append(i-1)  # 记录数组索引（0-based）
            res -= val[i-1]
            w -= wt[i-1]
    
    # 将索引转换为物品编号（1-based）
    selected_items = sorted([x + 1 for x in selected])
    return dp[n][W], selected_items

# 输入数据（直接从问题描述中粘贴）
weights = [2,5,10,9,3,6,2,2,6,8,2,3,3,2,9,8,2,10,8,6,4,3,4,2,4,8,3,8,4,10,7,1,9,1,5,7,1,1,7,4]
values = [8,1,5,9,5,6,8,2,3,7,5,4,3,7,6,7,9,3,10,5,2,4,5,2,9,5,8,10,2,9,6,3,7,3,9,6,10,1,2,9]

# 执行算法
max_value, selected = knapsack(50, weights, values, 40)

# 验证结果
total_weight = sum(weights[i-1] for i in selected)
total_value = sum(values[i-1] for i in selected)

# 输出flag
print(f"最大价值: {max_value}")
print(f"总重量: {total_weight} (<= 50)")
print(f"选中物品编号: {selected}")
print(f"flag{{{'_'.join(map(str, selected))}}}")
#NSSCTF{0 4 6 10 11 13 16 18 21 22 24 26 31 33 34 36 39}
```
### [GXYCTF 2019]luck_guy
除去部分对话输出，核心代码如下
```c
unsigned __int64 get_flag()
{
  unsigned int v0; // eax
  int i; // [rsp+4h] [rbp-3Ch]
  int j; // [rsp+8h] [rbp-38h]
  __int64 s; // [rsp+10h] [rbp-30h] BYREF
  char v5; // [rsp+18h] [rbp-28h]
  unsigned __int64 v6; // [rsp+38h] [rbp-8h]

  v6 = __readfsqword(0x28u);
  v0 = time(0LL);
  srand(v0);
  for ( i = 0; i <= 4; ++i )
  {
    switch ( rand() % 200 )
    {
      case 1:
        puts("OK, it's flag:");
        memset(&s, 0, 0x28uLL);                 // 拼接
        strcat((char *)&s, f1);
        strcat((char *)&s, &f2);
        printf("%s", (const char *)&s);
        break;
      case 2:
        printf("Solar not like you");
        break;
      case 3:
        printf("Solar want a girlfriend");
        break;
      case 4:
        s = 0x7F666F6067756369LL;
        v5 = 0;
        strcat(&f2, (const char *)&s);
        break;
      case 5:
        for ( j = 0; j <= 7; ++j )
        {
          if ( j % 2 == 1 )
            *(&f2 + j) -= 2;
          else
            --*(&f2 + j);
        }
        break;
      default:
        puts("emmm,you can't find flag 23333");
        break;
    }
  }
  return __readfsqword(0x28u) ^ v6;
}
```
观察可得正确得到flag的执行顺序应为case4》5》1，但由于使用随机数，无法按想要的顺序执行，即可自行编写代码解密:
```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<string.h>
int main()
{
    char f1[] = "GXY{do_not_";
    char f2[16] = { 0 };
    long long s_val = 0x7F666F6067756369LL;
    // 将s_val的字节按小端序转为字符串
    for (int i = 0; i < 8; i++) {
        f2[i] = ((char*)&s_val)[i];
        // 调整字符
        if (i % 2) f2[i] -= 2;
        else f2[i] -= 1;
    }
    f2[8] = '\0'; // 确保终止符
    char result[64];
    strcpy(result, f1);
    strcat(result, f2);
    puts(result);
    //GXY{do_not_hate_me}
}
```
### [SWPUCTF 2023 秋季新生赛]base64
base64水题
### [FSCTF 2023]Xor
异或水题
### [HNCTF 2022 WEEK2]Easy_Android
```java
package com.example.crackme;

import android.app.Activity;
import android.os.Bundle;
import android.view.Menu;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

/* loaded from: classes.dex */
public class MainActivity extends Activity {
    private Button btn_register;
    private EditText edit_sn;
    String edit_userName;

    @Override // android.app.Activity
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        setTitle(R.string.unregister);
        this.edit_userName = "Tenshine";
        this.edit_sn = (EditText) findViewById(R.id.edit_sn);
        this.btn_register = (Button) findViewById(R.id.button_register);
        this.btn_register.setOnClickListener(new View.OnClickListener() { // from class: com.example.crackme.MainActivity.1
            @Override // android.view.View.OnClickListener
            public void onClick(View v) {
                if (!MainActivity.this.checkSN(MainActivity.this.edit_userName.trim(), MainActivity.this.edit_sn.getText().toString().trim())) {
                    Toast.makeText(MainActivity.this, R.string.unsuccessed, 0).show();
                    return;
                }
                Toast.makeText(MainActivity.this, R.string.successed, 0).show();
                MainActivity.this.btn_register.setEnabled(false);
                MainActivity.this.setTitle(R.string.registered);
            }
        });
    }

    @Override // android.app.Activity
    public boolean onCreateOptionsMenu(Menu menu) {
        getMenuInflater().inflate(R.menu.activity_main, menu);
        return true;
    }

    /* JADX INFO: Access modifiers changed from: private */
    public boolean checkSN(String userName, String sn) {
        if (userName == null) {
            return false;
        }
        try {
            if (userName.length() == 0 || sn == null || sn.length() != 22) {
                return false;
            }
            MessageDigest digest = MessageDigest.getInstance("MD5");
            digest.reset();
            digest.update(userName.getBytes());
            byte[] bytes = digest.digest();
            String hexstr = toHexString(bytes, "");
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < hexstr.length(); i += 2) {
                sb.append(hexstr.charAt(i));
            }
            String userSN = sb.toString();
            return new StringBuilder().append("flag{").append(userSN).append("}").toString().equalsIgnoreCase(sn);
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
            return false;
        }
    }

    private static String toHexString(byte[] bytes, String separator) {
        StringBuilder hexString = new StringBuilder();
        for (byte b : bytes) {
            String hex = Integer.toHexString(b & 255);
            if (hex.length() == 1) {
                hexString.append('0');
            }
            hexString.append(hex).append(separator);
        }
        return hexString.toString();
    }
}
```
该题的逻辑是对Tenshine进行MD5计算，获取哈希值后，取其每一个偶数位组成字符串，最后拼接上“flag{”和“}”即可得到flag。
```python
char='b9c77224ff234f27ac6badf83b855c76'
for i in range(0,16):
    print(char[2*i])
#flag{bc72f242a6af3857}
```
### [LitCTF 2023]For Aiur
Python打包exe游戏，解包获得如下代码
```python
# Source Generated with Decompyle++
# File: Probee.pyc (Python 3.8)

from cv2 import imread, imshow, namedWindow, WINDOW_NORMAL, FONT_HERSHEY_SIMPLEX, getTickCount, getTickFrequency, putText, LINE_AA, waitKey, getTextSize, resize, moveWindow, IMREAD_UNCHANGED, destroyAllWindows
from numpy import uint8, zeros
from ch import check
Mineral = 100
Pylonnum = 0

def buildPylon():
    global Mineral, Pylonnum
    if Mineral < 100:
        warn_img = imread('source/warn1.png')
        imshow('warning', warn_img)
        return None
    None -= 100
    img1 = imread('source/warpin.png')
    namedWindow('Pylon' + str(Pylonnum), WINDOW_NORMAL)
    imshow('Pylon' + str(Pylonnum), img1)
    font = FONT_HERSHEY_SIMPLEX
    pos = (img1.shape[1] - 300, 50)
    color = (0, 0, 0)
    thickness = 2
    timer = getTickCount() + 18 * getTickFrequency()
    if getTickCount() < timer:
        img1_copy = img1.copy()
        time_left = int((timer - getTickCount()) / getTickFrequency())
        text = 'Time left: {}s'.format(time_left)
        putText(img1_copy, text, pos, font, 1, color, thickness, LINE_AA)
        imshow('Pylon' + str(Pylonnum), img1_copy)
        if waitKey(1) & 255 == ord('q'):
            pass

    img2 = imread('source/Pylon.png')
    imshow('Pylon' + str(Pylonnum), img2)
    waitKey(1)
    Pylonnum += 1


def gather():
    global Mineral
    digit_value = Mineral
    icon_img = imread('source/jingtikuang.png', IMREAD_UNCHANGED)
    icon_img = resize(icon_img, (120, 120))
    bg_img = zeros(icon_img.shape, uint8, **('dtype',))
    bg_img[(0:icon_img.shape[0], 0:icon_img.shape[1], :)] = icon_img
    digit_text = str(digit_value)
    digit_size = getTextSize(digit_text, FONT_HERSHEY_SIMPLEX, 1, 2)[0]
    digit_x = bg_img.shape[1] - digit_size[0]
    digit_y = digit_size[1] + 10
    putText(bg_img, digit_text, (digit_x, digit_y), FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    imshow('Mineral', bg_img)
    moveWindow('Mineral', 1200, 100)
    Mineral += 5

img = imread('source/Probe.png')
(new_width, new_height) = (200, 200)
img = resize(img, (new_width, new_height))
(screen_width, screen_height) = (800, 120)
(x, y) = (600, 100)
(dx, dy) = (0, 5)
namedWindow('Probe', WINDOW_NORMAL)
imshow('Probe', img)
check(Pylonnum) #此处为核心代码，调用ch.py中的check函数
imshow('Probe', img)
if y < screen_height:
    dy = 5
if y > screen_height:
    dy = -5
x = x + dx
y = y + dy
moveWindow('Probe', x, y)
if waitKey(50) & 255 == ord('g'):
    gather()
if waitKey(50) & 255 == ord('b'):
    buildPylon()
if waitKey(50) & 255 == ord('e'):
    pass

destroyAllWindows()
```
核心代码在check函数中，调用ch.py中的check函数，在解包的文件夹中找到ch.pyc文件，反汇编后得到如下内容
```python
# Source Generated with Decompyle++
# File: ch.pyc (Python 3.8)

enc = [
    98,
    77,
    94,
    91,
    92,
    107,
    125,
    66,
    87,
    70,
    113,
    92,
    83,
    70,
    85,
    81,
    19,
    21,
    109,
    99,
    87,
    107,
    127,
    65,
    65,
    64,
    109,
    87,
    93,
    90,
    65,
    64,
    64,
    65,
    81,
    3,
    109,
    85,
    86,
    80,
    91,
    64,
    91,
    91,
    92,
    0,
    94,
    107,
    66,
    77,
    94,
    91,
    92,
    71]
lis = []

def check(num):
    flag = 'LitCTF{'
    if num % 2 == 0 and num % 4 == 0 and num % 6 == 0 and num % 8 == 0 and num % 12 == 0 and num % 13 == 11:
        k = str(num)
        for i in range(len(enc)):
            flag += chr(ord(k[i % len(k)]) ^ enc[i])
            lis.append(ord(k[i % len(k)]) ^ enc[i])
        flag += '}'
        imread = imread
        imshow = imshow
        namedWindow = namedWindow
        WINDOW_NORMAL = WINDOW_NORMAL
        FONT_HERSHEY_SIMPLEX = FONT_HERSHEY_SIMPLEX
        getTickCount = getTickCount
        getTickFrequency = getTickFrequency
        putText = putText
        LINE_AA = LINE_AA
        waitKey = waitKey
        getTextSize = getTextSize
        resize = resize
        moveWindow = moveWindow
        IMREAD_UNCHANGED = IMREAD_UNCHANGED
        destroyAllWindows = destroyAllWindows
        import cv2
        uint8 = uint8
        zeros = zeros
        import numpy
        img = zeros((200, 20000, 3), uint8)
        img.fill(255)
        text = flag
        font = FONT_HERSHEY_SIMPLEX
        pos = (50, 120)
        color = (0, 0, 0)
        thickness = 2
        putText(img, text, pos, font, 1, color, thickness, LINE_AA)
        imshow('flag', img)
        waitKey(0)
        destroyAllWindows()
```
由此输出flag的核心代码即可写出解密代码
```python
enc = [
    98, 77, 94, 91, 92, 107, 125, 66, 87, 70, 113, 92, 83, 70, 85, 81, 19, 21,
    109, 99, 87, 107, 127, 65, 65, 64, 109, 87, 93, 90, 65, 64, 64, 65, 81, 3,
    109, 85, 86, 80, 91, 64, 91, 91, 92, 0, 94, 107, 66, 77, 94, 91, 92, 71
]

def find_valid_num():
    num = 24  # 最小的 24 的倍数
    while True:
        if num % 13 == 11:  # 需满足 num % 13 == 11
            return num
        num += 24  # 递增 24 继续查找

def decrypt(enc, num):
    flag = "LitCTF{"
    k = str(num)
    for i in range(len(enc)):
        flag += chr(ord(k[i % len(k)]) ^ enc[i])
    flag += "}"
    return flag

num = find_valid_num()
flag = decrypt(enc, num)
print("解密后的 flag:", flag)
# LitCTF{Pylon_OverCharge!!_We_Must_construc7_addition4l_pylons}
```

### [NSSCTF Round#28 Team]动态调试
```c
int __cdecl main_0(int argc, const char **argv, const char **envp)
{
  char v4; // [esp+0h] [ebp-F0h]
  char v5; // [esp+0h] [ebp-F0h]
  int j; // [esp+D0h] [ebp-20h]
  int i; // [esp+E8h] [ebp-8h]

  __CheckForDebuggerJustMyCode(&unk_86D038);
  printf((char *)&prompt_output, v4);
  scanf("%s", (char)input);
  while ( input[k] )
    ++k;                                        // 统计输入长度
  for ( i = 0; i < k; ++i )
    input[i] ^= rand();
  for ( j = 0; j < k; ++j )
  {
    if ( input[j] != enc[j] )
    {
      printf((char *)&wrong, v5);
      exit(0);
    }
  }
  printf((char *)&Right, v5);
  return 0;
}
```
使用了rand随机数，但是没有看到srand函数，用1作种子无法解出，故尝试其他方法。

点击rand函数查看函数导入表，观察到srand函数的存在
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SXpycXaiSWtCU9cpujkPjpipRcCDTPR5KWbamVa1v*WUx2PMKz602Zwzn0CxIlKlWdpnLdq2BDLnQbLY4WDXMig!/b&bo=sgPxALID8QADByI!&rf=viewer_4)

点击跳转到调用处
```asm
.text:00862A36     loc_862A36:                             ; CODE XREF: sub_8629E0+53↑j
.text:00862A36 0E4                 pop     eax
.text:00862A37 0E0                 mov     esi, esp
.text:00862A39 0E0                 push    114514h ; <suspicious> ; Seed
.text:00862A3E 0E4                 call    ds:srand
.text:00862A44 0E4                 add     esp, 4
.text:00862A47 0E0                 cmp     esi, esp
.text:00862A49 0E0                 call    j___RTC_CheckEsp
.text:00862A4E 0E0                 mov     eax, [ebp+var_8]
.text:00862A51 0E0                 pop     edi
.text:00862A52 0DC                 pop     esi
.text:00862A53 0D8                 pop     ebx
.text:00862A54 0D4                 add     esp, 0CCh
.text:00862A5A 008                 cmp     ebp, esp
.text:00862A5C 008                 call    j___RTC_CheckEsp
.text:00862A61 008                 mov     esp, ebp
.text:00862A63 004                 pop     ebp
.text:00862A64 000                 retn
```
发现调用srand前将114514h压入栈中，故将114514h作为种子即可解出flag
```c
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int main()
{

	srand(0x114514);
	char input[] = { 0xC6, 0xD0, 0xF0, 0x3D, 0xBE, 0xE7, 0xC1, 0x72, 0x17, 0x83, 0x7E, 0x01, 0x34, 0x35, 0x48, 0x04, 0x9C, 0x30, 0xA6, 0x7C, 0xD8, 0x3A, 0xE7, 0x3D, 0x36, 0x19, 0xDF, 0x0E, 0x06, 0x21, 0x64, 0xF4, 0x50, 0x4D, 0x14,0x0 };
	for (int i = 0; i < strlen(input); ++i)
	{
		input[i] ^= rand();
		printf("%c", input[i]);
	}
}
```