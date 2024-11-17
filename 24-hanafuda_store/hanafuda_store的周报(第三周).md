# hanafuda_store的周报(第三周)
## 1.学习汇编语言
这周的主要任务是完成了《**汇编语言**》这本书的学习，现在已经完成了学长分配内容的学习，已经能读懂一些16位下X86架构的汇编语言，也能自己用汇编语言编写一些简单的程序，这对于后期对32位和64位的汇编分析都是很重要的，我从此也收获很多，了解到不少关于计算机底层的知识与内容。从下周开始我也即将展开下一部分内容的学习，即学习C++中的反汇编与逆向分析，虽然C与C++较为相似，但仍有很多的区别曾困扰我，这方面还是很重要的。

部分学习成果展示:
![笔记](https://m.qpic.cn/psc?/V11300AO0tdWfu/LiySpxowE0yeWXwBdXN*Sf6Ju*3UQhYS1K2Lv7w7wwbC2iIJ*55UjUP4GgT100ZqJl897p98G1rt8RQd8O4Qy43FAvzCz4CVgIU48VXCnXY!/b&bo=VQhABsAP0AsHByk!&rf=viewer_4)

## 2.学习《IDA特训营》
这周我还用了部分时间来学习学长分享的《IDA特训营》课程。作为逆向分析中最长打交道的工具，IDA的使用在逆向学习中显得格外重要，现阶段我学习了许多方便的快捷键的使用，以及软件面板上各个功能键的使用，以及对函数/变量名称的更改，还有添加注释等功能，让我进一步熟悉了这个工具的使用，更加得心应手地应对逆向分析。
![学习截图](https://a1.qpic.cn/psc?/V11300AO0tdWfu/LiySpxowE0yeWXwBdXN*SQF8kf4LeyZV2mzKnsfzsi5eraoslUTTohzjkUrEsPN3NlrxMSkeTjsB3PwsJ8lUr7kXT2bdfHO3PH.m.GLe.Rw!/b&ek=1&kp=1&pt=0&bo=gwb5AwAAAAADN20!&tl=1&vuin=934483106&tm=1730620800&dis_t=1730621039&dis_k=ebb26a61ab4e4a89247dabe1a683ddd0&sce=60-1-1&rf=viewer_4)
## 3.NSSCTF刷题及WP编写
老样子，练习也是学习过程中必不可少的一个环节。在这周的联系中我发现在学习的过程中不断积累经验是很重要的，不然很多宝贵的经验教训就会被忘记，无法在下次实战中活用，所以记录自己的解题过程还是很重要的
### [SWPUCTF 2021 新生赛]re1
下载附件后用IDA打开按F5即可看到反汇编后的代码如下
![](https://m.qpic.cn/psc?/V52mtLJJ3HJION2p4keN1yJtcH3fCpcu/LiySpxowE0yeWXwBdXN*SUEHC54yXqqSL8U5KysHXKQxNDqPnk7C2siilefnlhnLm3v9Xh8TrODW2qq8gqGf8Vxy4rXObe.E9abSmfXa7XM!/b&bo=EQNvAgAAAAADF00!&rf=viewer_4)
这里的代码表示在遍历Str1中的每一个元素，当遇到a(ASCII码值为97)或e(ASCII码值为101)时将它们分别替换为3和4(ASCII码值分别为51和52)，然后于于Str2比较。由此可逆向推导出flag为{easy_reverse},加上NSSCTF头提交即可
### [SWPUCTF 2021 新生赛]简简单单的逻辑
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
## 4.参加SICTF比赛
这方面有些难以启齿，虽然曾努力尝试过解题，果然是实力上还有较大的缺陷，在比较大型的比赛中容易陷入一筹莫展的境地，部分知识点如动态调试、tea加密虽然已经大致搜索和了解过，但仍没有进行系统的学习，这也是下一周我要重点攻克的目标。

总之，这一周虽然学了不少知识，但也见识到了自己与“优秀”之间还有巨大的差距，在后面的学习是需要我去奋力追赶的目标。

