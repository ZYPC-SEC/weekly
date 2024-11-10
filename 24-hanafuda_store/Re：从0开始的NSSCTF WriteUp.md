# Re：从0开始的CTF WriteUp
### 1.[SWPUCTF 2021 新生赛]re1
下载附件后用IDA打开按F5即可看到反汇编后的代码如下
![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SUEHC54yXqqSL8U5KysHXKQxNDqPnk7C2siilefnlhnLm3v9Xh8TrODW2qq8gqGf8Vxy4rXObe.E9abSmfXa7XM!/b&bo=EQNvAgAAAAADF00!&rf=viewer_4)
这里的代码表示在遍历Str1中的每一个元素，当遇到a(ASCII码值为97)或e(ASCII码值为101)时将它们分别替换为3和4(ASCII码值分别为51和52)，然后于于Str2比较。由此可逆向推导出flag为{easy_reverse},加上NSSCTF头提交即可

### 2.[SWPUCTF 2021 新生赛]简简单单的逻辑
打开附件中的python文件，该程序遍历一个数字列表，对每个列表元素进行位操作以计算出一个key，然后将flag变量的每个字符与这个key进行异或运算。result变量会累加异或运算的十六进制值并转为字符串。最终打印输出result
可根据这样的思路解出flag：
1.将 result 中的每对十六进制字符转换为整数
2.计算对应的key
3.反向执行异或操作以获取 flag 中每个字符的原始 ASCII 值
4.使用从列表计算出的 key 来解码原始信息
由此可写出解密代码：
![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SQm5mAI1Z.9TnF7byUBGHD1WnxKuTdhw.kqKKQoYa*wSf2Lo5pfes0WAQuR1NM7Vtggkzke*dhGdVfn*.zQzTNQ!/b&bo=nwTVAgAAAAADF34!&rf=viewer_4)
说明：int()可进行强制类型转换，得到整型数据，要转换的数据后还可加上一个用逗号隔开的数字表示这是几进制的数据；str()可强制转换为字符串类型；对字符串进行操作时，+=进行的是字符串的拼接而不是相加！！！

### [NSSCTF 2022 Spring Recruit]easy C
打开附件查看代码可知该程序在对输入的a字符串中的的数据每一项加1后与2异或后的值与b字符串进行比较。
![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*Scse83QiRWbFKxkHQhznFqvFbeiyAxgamWShNkwZO2oEdVk.79Yw6q4SoSAXsRTplKTAH9Fxyas8S94xtT42WQc!/b&bo=WgK2AwAAAAADF98!&rf=viewer_4)
由此可反向推理写出解密代码：
![](https://a1.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SUOL0JHwaJNHz2cPhx4k1dQct4Z.NmRZbCk8ocGVPrdwvW2HVy370ULEPwUVzSwTGHL8qk2N6x94XrUK5bkFgpU!/b&ek=1&kp=1&pt=0&bo=SQJPAgAAAAADFzQ!&tl=1&vuin=934483106&tm=1730379600&dis_t=1730380221&dis_k=12f05ed960fa8f001fe381158f17fe5a&sce=60-2-2&rf=viewer_4)
注意：逆向操作时要注意顺序和对应运算的逆运算！！！

### [LitCTF 2023]世界上最棒的程序员
下载附件后用IDA打开按F5即可看到反汇编后的代码如下
![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SZ2eWnJMqyarbnnqmpoyRzMcc0qV8EzxO6L0*9fWTg9Xvg7U4W1wPvJIl469Yu3VOyh3XbcH2Q0exkr5uqGhHCw!/b&bo=*wL0AAAAAAADBys!&rf=viewer_4)
点进start查看内容
![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SUSV1mULupMHNi3af.WeJiO7t7ThKFJkkTEB.xGsmfjl5qVXsKFMhDJy7*nzjTF8K9yFaZv06HsVOut0WDyhCcY!/b&bo=3QKVAQAAAAADB2k!&rf=viewer_4)
可直接看到flag
### [LitCTF 2023]enbase64
下载附件后用IDA打开按F5即可看到反汇编后的代码如下
![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*Seen9pnUcskVRvfVQUCRpz.4hy8XqvjxQxVnzOnq46HFjja89kUb3beKxqDCv05TERMDh95IzqhqTBswujKhiFE!/b&bo=OwX.AQAAAAADB.M!&rf=viewer_4)
由反汇编结果和题目提示可知进行的是Base64加密，但是用工具无法解密，推测其为换表的Base64.点开base64()函数继续分析
![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SRTN4pIqfdsfk2uovSGVcbXgnNaZsFlnBlfLHzIS11iD9X25QvV6OEO4vK2t13bgwYvbRHE5xQKhzkgQFCOM6d0!/b&bo=RgMXAgAAAAADF2I!&rf=viewer_4)
继续打开Basechange函数查看换表的过程

![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*STTpF1*UEVG6pr5H0DamErgjqslTtMZ1kulr*DXnEY5*yYdyRMnrvjDwArIfmAEbbEfmzNJbAxVfTXBjNsLWnJM!/b&bo=MgE8AAAAAAADFz0!&rf=viewer_4)这里初始化了一个v3数组，使其成员全部为0
![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SWFVhi6iCtTb82fyipwkwLNLrF9KSYePW92Po9fkj0Ijp05PnXv5LpIrVUeaZVOyGFh9DUpRC1GsJyv0erpWzBo!/b&bo=0QHdAQAAAAADFz4!&rf=viewer_4)
最后将元素按照相应的方式打乱48次

注意：![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SZ9.8vmHD1PqAnQbE5eUymOIf.tR5YatMGgLWM5m.FO4TCTQBN1.z3MhNjB9N0XXIZlcf8SSEUOys6xxaLMBT*g!/b&bo=rgByAAAAAAADF.4!&rf=viewer_4)

此处没有对v3操作的原因是其对应值为0，而所有元素为零的初始化设置在开头就已经说明，需特别注意
### [SICTF Round#4]Exc??
令人耳目一新的Excel表格题，通过逆向分析出表格中带有函数公式的数据是如何计算而来的，在AI和Python脚本的帮助下解出多个三元方程组即可
![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SfBLatgUwacg4XOrMe7jwP9lczKHhLNiwh26HlZsVLP4bAFge*16QBdlc0Zf9HLv9Q1JWoqh29TzTeh9K8rPlHU!/b&bo=*wmnAgAAAAADB3E!&rf=viewer_4)
点击发现有公式的单元格是左上方表格中output那一行、Factory工厂房子红色部分、grassland草地中的数据，我们已知flag的格式为SICTF{}，可知试出前两个格子，分别对应Factory工厂房子紫色部分、home房子、Astral星辰中的数据，由此可列出方程式，并使用Python脚本解出剩下格子中的内容
![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*ST6zYdJUqb0SRrvn3hINS.tbqNE3.Dr7QYVrHY*xdLL9jGo6HX5JGWsR9RZIHL8CiUq10hTeC2Prf7bwya3fA7s!/b&bo=.QL2AwAAAAADFzw!&rf=viewer_4)
最后将计算所得的ASCII码值转换为对应的字符即可
### [SICTF Round#4]派森
根据提示，先把附件加上.py的后缀名，再打开，发现其为一堆有类似于Python结构的汉字
![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SSE7jKrx4AyRAgDFu5du1ELeKk.6KRA5*9QGeKT*oQngpprAKQyYoze0Z03IxW3vVZP4EqzE5RcqlzmP7hDJVmQ!/b&bo=yQdTAQAAAAADF64!&rf=viewer_4)
在AI帮助下将其还原为正常的Python代码
![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SWwUl0vUQ*Ua67MGQmm5gvhrmKWHXDYpjbHFs3ppKZVcFnqikL.CEdU6DK38Sj1oitR1TUOVBjoEdkOVfCJksks!/b&bo=igefAQAAAAADFyE!&rf=viewer_4)
再写出逆向解密代码即可
![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SY5sRtQ*kqSXql*y.mQkvo.rxyMYPspafteN7RrZ8lCNMFGUPp.UFeOSCAwPYaGjWh5YwBn0pwUOXJxdToilBU4!/b&bo=FgjmAgAAAAADF8g!&rf=viewer_4)
### [SWPUCTF 2021 新生赛]简简单单的解密
Python逆向，阅读完代码发现这是在对flag字符串先进行RC4加密，再解密又加密Base64，最后进行URL编码
![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SdglCd4D1b*Aof7RTW4dk3nXyIWzEAoOoueJgHUnzaa.ho.PjeWjifTmcMQXWYehwL*LH8frQ*cBcErtKvN5eig!/b&bo=LwSwAgAAAAADF6s!&rf=viewer_4)
因为Base64部分是加密后又解密，所以不用考虑，将输出结果先后用URL和RC4解密一次就行
![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SSs7WQnoKKdPQbYP8xhXvSCHlwcAXUvRWzJto9Uyi1GdrE8arSVXhhLMdktv1402bQ.*sUoI17jrb3apxiXW7SQ!/b&bo=4ARWAwAAAAADB5M!&rf=viewer_4)
### [HGAME 2023 week1]easyasm
汇编代码阅读，这段代码是在通过循环，将一段字符串每个字符与0x33进行异或运算得到结果
![](https://a1.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SYYIaPv6YxR9*i6.AeORBSO5*.rSsUfh*pk3S5DANMZffjEGsoft6SN4VOUxK.2lQwODrXaCpqRMtEo01vBhqzo!/b&ek=1&kp=1&pt=0&bo=CwU4BAAAAAADNyA!&tl=1&vuin=934483106&tm=1730732400&dis_t=1730735231&dis_k=62391b1e95f4dd540b26610249f2275c&sce=60-2-2&rf=viewer_4)
所以根据异或运算的自反性，只需再异或一次即可
![](https://a1.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SRaGqMO9qjXaIDaUASR9a5OXd51eO7zkz7OFfiCqLfKUzcqJqcrIKqeD1yDLomUbJlLnw2I5c83X8f6oSm3MuP4!/b&ek=1&kp=1&pt=0&bo=CASNAQAAAAADF7I!&tl=1&vuin=934483106&tm=1730732400&dis_t=1730735240&dis_k=6fce45b96d90139d765e575627e0215d&sce=60-2-2&rf=viewer_4)
### [SWPUCTF 2021 新生赛]fakerandom
打开附件，发现是对flag用生成的随机数每位异或进行加密
![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SfAl.D0cwadNnsX*z0XO*tKJx7q7.VwYQ*5CBZhCJ4j*ZcCWdicxMesOfMRuL9iBTFMxGNXAj*.mPJzXifR9g5c!/b&bo=6wR1AQAAAAADF6k!&rf=viewer_4)
Python逆向，利用了伪随机数和异或运算的自反性。将原代码稍作修改就可以得到flag
![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SfAl.D0cwadNnsX*z0XO*tKJx7q7.VwYQ*5CBZhCJ4j*ZcCWdicxMesOfMRuL9iBTFMxGNXAj*.mPJzXifR9g5c!/b&bo=6wR1AQAAAAADF6k!&rf=viewer_4)
再将所得的异或数字结果转化为ASCII码即可得到flag
![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SWZZSemdrv536VvdqVNnrW8P5K7Swml3ILsjIlOevO3qsNwsdLSMDnJ30nyB6Ql0uDswoKYUuMLaUsnpU8EV82Q!/b&bo=igPJAgAAAAADF3A!&rf=viewer_4)
### [NISACTF 2022]string
附件是一个Linux的ELF文件，有一层壳，先用upx -d指令脱壳后拖入IDA分析
![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SecmGJrTS60ifcyNZs3.e4ZJqL2HNH3l3ngsT9uiXs77yY23bJ*qOuREn29ao6PYbDqObhr4Qi0CaszskTvr1vM!/b&bo=AwP*AAAAAAADF80!&rf=viewer_4)
main函数较为简单，接着查看较为显眼的flag函数
![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SXq7LaBgh5cUp0LYIhl7dYctlP7YAKPeHBpetb0ayK2oa9kRgtKg4lkIf.IZURtmvuU5L6pzkdUPIFmpqYdHi9o!/b&bo=VAMOBAAAAAADF28!&rf=viewer_4)
flag函数前面大段的内容都是在检查输入的内容是否符合标准(如该字符串长度为13等)，后面则是使用rand函数生成范围为1~8的随机数分别与输入的内容异或，最后按格式输出正确的flag。点开seed即可查看到该随机数生成过程中所用的种子为0x2766。
![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SbUZOFZp9CoC6ugqrEQGRe2FexDXod.sxGnD3d7Fky92KJYGA0WzTnL9gOecfwumDD39366vJ*Mpp0ee0CCUw3U!/b&bo=JwImAAAAAAADFzE!&rf=viewer_4)
由此即可写出解密代码。但是该文件是Linux上的可执行文件，由于Windows和Linux系统上生成伪随机数的数表不同，所以必须找一个Linux的环境下运行解密代码，可通过在线编译网站实现
![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SUsdkHW.ngBdVRPyIPDrpEkBr84GGsj9PxP8dP8sL0OJVyVxqEdM6he5eiibuTbbLLXTITEeooX*RzDUWbTFmhU!/b&bo=mwO.AQAAAAADFxU!&rf=viewer_4)
### [SWPUCTF 2022 新生赛]base64-2
简单的换表Base64，记录一下做题经验
![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SdYN6VvxkAO1Efvaqb6p4ud8sss6YcFbJyW8peTJf3jkin.J5KzdCX*LdqWi.aAdkUt0u3MDFMeAmxTm3efcpB0!/b&bo=2gN1AAAAAAADF54!&rf=viewer_4)
从主函数点进加密函数，再点开这个字符串
![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SQGg9J5BhuglHSwmafLvhaE9NB7F3ppOWemo1C885RkJu9PqAJqk1clwSD*4laWGxRmcRCkRzG4gBwK1T2PY6iQ!/b&bo=0QSmAAAAAAADF0E!&rf=viewer_4)
由于这里的s2和off_4018其实都是指向字符串的指针(旁边的注释也有在说明该指针实际指向内容的部分信息)，所以应该再点击一次才能打开这两段信息实际内容的位置
![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SYqMKi4broolaCJjBXNieJ8arqbsykU399*LXcC0HFpo6lhilMs1WedRflDO4yFqiV2mcIjv9RFYA7YoRe53mPs!/b&bo=BgXpAAAAAAADF9g!&rf=viewer_4)
这里才是密文和Base64码表实际所在的地方(也可使用查找字符串的窗口)