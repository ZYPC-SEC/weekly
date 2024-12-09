# hanafuda_store的周报(第四周)
## 1.搭建个人博客
这是学长们这周布置的任务，个人感觉有一定难度，难点在于选择合适的图床以及进行相关的设置，使图片正常显示，以及在git中各种指令的使用。搭建过程已作为博客里的第一篇文章上传。可点击这里的链接查看[我的博客](https://nintendo-hanafudastore.github.io/)
## 2.刷题
例行公事了，还是得通过练习才能达到“无他，唯手熟尔”的程度，新做的题目中有值得参考的经验的已补充在下面；同时，也参加了ISCTF的比赛，感觉较为正式的比赛的难度还是不小的，做出的题并不多，还是得继续努力积累经验
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
## 3.C语言Remake
C语言作为最基础的编程语言，在我所学习的逆向工程方向也是发挥着巨大作用。由于我长时间没有专门赶C语言的进度，导致目前部分知识点有遗忘。这周我便专门抽出时间来进行复习和学习新知识，以后每周也要专门规划一部分时间继续深入学习C语言，提升自己代码审计的能力