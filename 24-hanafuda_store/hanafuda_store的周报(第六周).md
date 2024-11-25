# hanafuda_store的周报(第六周)
为了更好地记录自己每周学习的内容并更好地监督自己，从这周开始我的周报将按照每一天完成的内容来记录。
## Sunday
1. 完成上一周的的周报
2. 经过几次比赛的考验，我发现不能仅仅专注于自己学习方向的题目，将自己的路走得太窄，还是应该对其他方向的内容有所涉及，故这天晚上我还尝试做了几道Web和PWN方向的题目：
### [SWPUCTF 2021 新生赛]gift_F12
签到题，按F12查看源代码即出答案
![](https://a1.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SWh3FYvrkm4kDMYkrnTbYUff59PlATqhrcaJZSiGXRmIZjQ6wMXvk13.PMoQQ0iFGIDfV7YWWzyHiLoRVxBCp74!/c&ek=1&kp=1&pt=0&bo=KgQrASoEKwEDFzI!&tl=1&vuin=934483106&tm=1732460400&dis_t=1732463434&dis_k=b636bdcce537b067a6b0ff0c0befc644&sce=60-2-2&rf=0-0)
### [SWPUCTF 2021 新生赛]jicao
考察post和get方式传参，阅读源代码发现输出flag的条件是接收到一个post方式传的参数id并使其等于wllmNB且接收到一个get方式传的参数json使其等于{"x":"wllm"}，则使用hackbar进行传参即可得到flag。
![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*Sf.KC6JqNGNeXI39fOyQacFJXhg68jehrGz36TbSNbDBYR9LfIm1Ef3nTncY2awKYcXlEXwmNU7TVSSqIWVjzFU!/b&bo=vwPDAr8DwwIDFzI!&rf=viewer_4)
### [SWPUCTF 2021 新生赛]easy_md5
阅读源代码发现是要使传入的name和password参数的值本身不相等，但是MD5值却相等。在网上查找可知满足这种条件的字符串有QNKCDZO和240610708，这样传入参数即可完成绕过得到flag。
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SbqlJrVRTX57z0LnChsWCZhGK7oEfuhfZnSMHSC0hf8uq6HWMJlHT60KGpgCzR*YAFfTiZl37UIL30b6fw4Jboc!/b&bo=1gOkA9YDpAMDFzI!&rf=viewer_4)
### [SWPUCTF 2021 新生赛]include
打开环境后提示传入一个file，那就以get或post方式传入一个file参数，阅读此时显示的代码可知有一个名为flag.php的文件，然后最下方的include_once函数(在脚本执行期间包含并运行指定文件)可执行参数file中的内容，然后构造伪协议http://1.14.71.254:28689/?file=php://filter/convert.base64-encode/resource=flag.php，使flag.php中的内容以base64编码的方式打印出来(这里不能使file直接等于flag.php的原因是include_once函数是执行对应语句，而flag.php中不一定含有echo输出语句，而只是给flag变量赋了个值)
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SbqlJrVRTX57z0LnChsWCZhGK7oEfuhfZnSMHSC0hf8uq6HWMJlHT60KGpgCzR*YAFfTiZl37UIL30b6fw4Jboc!/b&bo=1gOkA9YDpAMDFzI!&rf=viewer_4)
使用base64解码后即可得到flag
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SYlxO.He*fOJ2ceP7jbP8kmC5wF5yDt2YUT.ML*H3x5cykzxOV0UiBWOvcRvs1CzhrDg*PH.nXrZQCIvrzZYwEU!/b&bo=nAK6AJwCugADFzI!&rf=viewer_4)
### [HGAME 2023 week1]test_nc
nc签到，在linux虚拟机终端上使用nc指令打开对应靶场后使用ls指令扫一下目录即可看到“flag”，使用cat指令使flag输出即可。
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SXf34zuSQko7oj4YvNSTQGXGOBS78GCsHGgEGuemTc9J8aug.pmx.BZVP6f*tqPQGGTrQmpf9w3sL*f21U0AUvQ!/b&bo=LgMeAi4DHgIDFzI!&rf=viewer_4)
## Monday
这周的主要工作是学习动态调试，先从VisualStudio这种IDE动态调试自己编写的软件着手吧。

按F9可在光标所在的行打下一个断点，只有程序以调试模式运行时打下的断点才有效，想要在非调试模式下运行，需要按ctrl+F5，调试模式只按下F5即可。

在程序运行后停在断点处时可以进行按步执行来观察程序运行时的细节，使用方法：单步步入(F10)进入被调用函数后再停下；单步步过(F11)跳过被调用的函数。

若要以更细致的汇编指令按步执行的话可通过调试-窗口-反汇编查看汇编指令，可以逐指令进行。还可打开寄存器窗口、内存窗口、调用堆栈窗口(可查看函数调用过程与关系，可用堆栈指针寄存器sp中储存的值输入内存查询窗口查看堆栈)、监视窗口(查看各个变量的值)等帮助分析程序运行过程。
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SSpjeL7azqyZeevZhQzfuQo8AKbFbBOYBuJ.1WjNPWwPTo6TubhD5cQaJo66IlRhx0tKwGUlXs1g4ShKxdrgfTk!/b&bo=JAmiBCQJogQDJwI!&rf=viewer_4)
在学习完VS的动调后，我们便可类比着展开对OllyDBG的学习。注：OD只支持X86程序的调试而不支持X64的程序。

打开OD的界面可看到左侧反汇编窗口、右侧的寄存器窗口以及底部的16进制内存窗口。查看选项卡可打开和VS相似的很多窗口帮助分析程序；调试选项卡可以开始/停下调试的过程，也可以选择单步步入(F7)和单步步过(F8)；插件选项卡可以打开许多使用的功能，如查找字符串等。

那么接下来就通过实践展示实际用法
### [BJDCTF 2020]Easy
先在IDA中静态分析，发现main函数中并没有我们需要的信息，根据提示"Can you find me"找到有输出的_ques函数，但是该函数没有被调用，所以得想办法让其运行起来。

用OD打开，使用查找字符串的功能，找到了检查输入的的内容，定位到反汇编界面，修改下图所示中call指令所调用的函数地址，将其修改为_ques函数的地址，再重新开始调试就可以看到输出的flag了
![](https://a1.qpic.cn/psc?/V11300AO0tdWfu/LiySpxowE0yeWXwBdXN*SfOovbFbvsE3CQMbj4EiTAKyG5QJt1GP3RApBDLV*Bfovoj3u08m9QQVvbXKI6txd9g12DQZnLcsoiCrxVZv0*I!/c&ek=1&kp=1&pt=0&bo=VAkWBVQJFgUWECA!&t=5&tl=3&vuin=934483106&tm=1732460400&dis_t=1732463710&dis_k=7d395137146ad0be7c1f2e091921f728&sce=60-2-2&rf=0-0)
## Tuesday
继续刷题
### [HNCTF 2022 Week1]你知道什么是Py嘛？
简单的python逆向
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SbQmGU8FVcQkFdINP.edgd5XEvXlNyFsVls4AkT*QPE2JMJp7kZejDNcaafgLbLPBnQQ.s*rQafZp5i2CFj7Cqc!/b&bo=.AY0A*gGNAMDFzI!&rf=viewer_4)
### [SWPUCTF 2021 新生赛]easyapp
安桌逆向，将附件用JADX打开附件，找到关键函数后可写出解密代码
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SQwuB03a2IUTrLDJ1PcfEED0ZAh.pkI6xuZv6uCuHc7CivAehe6wm46X32Pfi8Kql3.KFbVQ0G2lt1YAxZ*MGwc!/b&bo=cgPOAXIDzgEDFzI!&rf=viewer_4)
注意：此处与0xFF进行按位与运算是为了防止计算所得的值过大，导致超出Unicode的范围
### [HGAME 2023 week1]test your IDA
简单的签到题
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*Saj8wIPC0yj57yPKPyUea.xc1AfQY6QSyOXQPsWO1WTMUP1T5Vs6mQhdhP5truxSC81aIEgWIfUdsVuWrnNDKxo!/b&bo=PgPbAD4D2wADFzI!&rf=viewer_4)
### [SWPUCTF 2022 新生赛]py2
python解包逆向，但是有特殊解
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SYB.d*D35So3Di34jtYaGG.Obw8.qYljekViBckgBIffEH*c0dj7k*xjEYccZtc0XNZ5e7USayE4QaTLHUgKZkY!/b&bo=BAbbAQQG2wEDFzI!&rf=viewer_4)
直接在010Editor的界面看到被Base64加密的flag
## Wednesday
### [第五空间 2021]签到题
如题，直接看答案
### [HGAME 2022 week1]easyasm
汇编代码分析，阅读代码可分析出以下内容：
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SQOf0fcmJnx3B4ogLLR95f7DqLpJGOppL33JCqQes0oKlJNhtGyjPLY6V4KrlT33J9WbZ6.WTt*hGEXBaPynvrE!/b&bo=QwPTA0MD0wMDR2I!&rf=viewer_4)
由此可分析得出解密代码
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SQaC99mYPgVnDg0AyO2QGLWNckKvn*6IIpF3nmXSAo.hOePb*KAIdWnQP8I7VoV0sQVJ5zYVoTVBKvExymzHiCs!/b&bo=9AOhAvQDoQIDFzI!&rf=viewer_4)
## Tursday
### [HUBUCTF 2022 新生赛]help
迷宫题，但是这一题比较特殊的是该迷宫的地图不是静态储存的，而是动态生成的，所以需要使用动态调试来得到迷宫地图。

在IDA中动态调试要现在Debugger选项卡中选择调试器，Windows程序调试就使用本地调试器即可
再检查输出结果的语句处打下断点开始调试
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SZfs*DqbCP0MF9puXLR*hnqHJsFtBZC7qOfdWKyfDEPGKVnKEsnX0IUhAh*H1Yux14MCD6l589rt2xQ9gKKLnq0!/b&bo=*wPZAf8D2QEDFzI!&rf=viewer_4)
在终端随便输入点内容，然后回车即可发现原本map数组处生成了正确的地图
![](https://a1.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SY2SUtqsNoPls3kaBQquedTC5ABLubShVXI92o6y.tgAjBCiKPw6QImVxH802GUyUDS7rN8DtSFO3bR06Ni.qYs!/c&ek=1&kp=1&pt=0&bo=xwTpAscE6QIDFzI!&tl=1&vuin=934483106&tm=1732460400&dis_t=1732463918&dis_k=91351faf31f8cde233f5dcbfac668bc7&sce=60-2-2&rf=0-0)
在得到地图后即可得到结果
![](https://a1.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SeMpEJphx.pdRsI7gepckAH41DDDoJGA27EyAjxO9qob5I7BCaNxK8k13MVjPx1zDXomWSHqe0duiqohev1mRXY!/b&ek=1&kp=1&pt=0&bo=RgRZA0YEWQMDR2I!&tl=1&vuin=934483106&tm=1732460400&dis_t=1732463918&dis_k=00e0f8c00276c0a27e70c4ab1d2c5c82&sce=60-4-3&rf=viewer_4)

迷宫题脚本法：

参考资料 [CTF-reverse二维四向迷宫路径求解](https://blog.csdn.net/liKeQing1027520/article/details/138583198?spm=1001.2014.3001.5501)

根据这篇文章套用脚本如下，即可得到flag
![](https://a1.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SeG5BjELbpNXS6s2K2*mTXuWfZyK6awza3w72F18BA6N.5Yn842xj816cXkuK1NRaCkQVQ6xSFD4BhJ68HF6JNg!/c&ek=1&kp=1&pt=0&bo=IwcIAyMHCAMDJwI!&tl=1&vuin=934483106&tm=1732464000&dis_t=1732464247&dis_k=a29ae651b4aebf2b4c31d2385fd628b3&sce=60-2-2&rf=0-0)
### [SWPUCTF 2021 新生赛]老鼠走迷宫
还是一道迷宫题，获取地图后走出即可
### [AFCTF 2018]欢迎光临
签到题
## Friday
休息
## Saturday
### [LitCTF 2023]snake
Python反汇编，反汇编后所得结果可知其为一个贪吃蛇小游戏，pyc反汇编后从源码中把输出flag的那一段代码扒下来，稍作修改运行输出即得flag
![](https://a1.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SZcRohnhr8kZ1ELyvyzUeHu4J*UtzRw0w2X0hMAkx9vrT4RZv7u3UXcjhcMZkV9nzsoKRz9DIvisMIHI2vcVUIE!/c&ek=1&kp=1&pt=0&bo=2gc*AdoHPwEDFzI!&tl=1&vuin=934483106&tm=1732464000&dis_t=1732464482&dis_k=820b1b77621866072b546423d89225bc&sce=60-2-2&rf=0-0)
### [羊城杯 2020]easyre
IDA反汇编后得到以下内容
![](http://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SQjlvAONM0oohzUXI1Y.vqs4S6Cg3RoMntgMgeClOwT*Smw7zJtMYJ8okVQ7hS2sVHOarq.HUyxGNNDk1NFnDyE!/b&bo=WwTMAlsEzAIDByI!&rf=viewer_4)
查看3个encode函数的内容可知第一个是在进行Base64加密，第二个函数按如下顺序对输入字符串的块进行重排：
原始字符串分为长度为 13 的 4 个块：
```
a1[0:13]  a1[13:26]  a1[26:39]  a1[39:52]
```
重排后，输出顺序为：
```
a3[0:13] = a1[26:39] a3[13:26] = a1[0:13] a3[26:39] = a1[39:52] a3[39:52] = a1[13:26]
```
第三个函数是含数字的凯撒加密

在AI帮助下生成解密代码
![](https://a1.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SUOd6QiYjcURLy6fC.GFTXs7AYUOIOq2slufyWn*hh0h6*BspjqSRzxjoJd4KsQnilxPELMYFDLDIfhxhQtMXio!/c&ek=1&kp=1&pt=0&bo=DgQiBQ4EIgUDJwI!&tl=1&vuin=934483106&tm=1732464000&dis_t=1732464771&dis_k=96985b46899093fb07ae9dc8bd321302&sce=60-2-2&rf=0-0)

### [NSSRound#3 Team]jump_by_jump_revenge
在非图形化反汇编界面中的_main_0函数中发现爆红的花指令
![](https://a1.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SQ6HBJbB9CiZ19M7N5V09SIz*SRLSkIYKNq7AKAG793*BcaC*kGD09Rdx9GafADzZgsZn6D5kV*nZUXjc1JpsjE!/c&ek=1&kp=1&pt=0&bo=DwTfAA8E3wADFzI!&tl=1&vuin=934483106&tm=1732464000&dis_t=1732464895&dis_k=43af4b813fbb824cc6fe416fbbd769c3&sce=60-2-2&rf=0-0)
将该处代码undefine，并将E9改为90（nop掉）然后再_main_0函数开头处按P重新解析函数再按F5就可以得到反汇编代码（不能只将nop掉的代码重新“code”分析为代码）
```C
int __cdecl main_0(int argc, const char **argv, const char **envp)
{
  int i; // [esp+D0h] [ebp-40h]
  char Str1[36]; // [esp+E8h] [ebp-28h] BYREF

  sub_411037("%s", (char)Str1);
  for ( i = 0; i < 29; ++i )
    Str1[i] = (Str1[i] + Str1[(i * i + 123) % 21]) % 96 + 32;
  if ( !j_strcmp(Str1, "~4G~M:=WV7iX,zlViGmu4?hJ0H-Q*") )
    puts("right!");
  else
    puts("nope!");
  return 0;
}
```
由此可逆向分析得到解密代码
```python
target = "~4G~M:=WV7iX,zlViGmu4?hJ0H-Q*"
Str1 = [0] * 36
for i in range(29):
    Str1[i] = ord(target[i])  # 转为ASCII值
# 反向推算，加入多解尝试机制
for i in range(28, -1, -1):
    idx = (i * i + 123) % 21
    for j in range(3):  # 尝试 j = 0, 1, 2
        s1 = Str1[i] - 32 + j * 96 - Str1[idx]
        if 33 <= s1 <= 126:  # 确保结果是合法ASCII字符
            Str1[i] = s1  # 更新当前字符
            break
original_input = ''.join(chr(c) for c in Str1[:29])
print("原始输入字符串:", original_input)
# NSSCTF{Jump_b9_jump!_r3V3n9e}
```