## 本周重点
### 1.任务进展

- shctf结束
- ntactf结束
- 继续学习sql注入
### 2.知识分享
1.http请求头伪造（Geek Challenge 2023）
打开题目看到
![c634b126a4201af14f9133b43bdb155c.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1698570128811-85c8bf3e-6631-4121-8b11-6bcbfe4995b7.png#averageHue=%23eeebe9&clientId=ucbe19d06-950e-4&from=paste&height=36&id=u0b9cf281&originHeight=45&originWidth=446&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=2952&status=done&style=none&taskId=ua39c4df9-47ef-4064-b15f-e034ba09fa0&title=&width=356.8)
![e7d291fc7f5cce7ab13e44c7daebd366.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1698570137329-5206d3d0-c6bc-4398-8415-1afb7024790b.png#averageHue=%23faf8ec&clientId=ucbe19d06-950e-4&from=paste&height=20&id=ue5ed4975&originHeight=25&originWidth=561&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=8528&status=done&style=none&taskId=uf28181fb-de46-4e9b-843f-6321470fb68&title=&width=448.8)
根据上周的web信息收集内容，可知爬虫即在URL/robots.txt
然后看到
![e37e79143e9b82fdb77c8569983b92a2.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1698570234583-445654fd-d0c8-4053-bf3f-b782b96378e5.png#averageHue=%23fbfaf9&clientId=ucbe19d06-950e-4&from=paste&height=71&id=u3c99aeb0&originHeight=89&originWidth=495&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=2701&status=done&style=none&taskId=ueafcf605-28f6-4c34-8b50-a0948c84d8a&title=&width=396)
进入后得到username和password
![c3922ca99d3859a85eb852c8d33e026a.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1698570261341-c3bae7bf-e335-4702-ad50-a0e7fd468139.png#averageHue=%23f8f6f4&clientId=ucbe19d06-950e-4&from=paste&height=51&id=u71cc01f9&originHeight=64&originWidth=293&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=2483&status=done&style=none&taskId=u42aa8cbf-2843-44f7-8ca8-cc67693026b&title=&width=234.4)
post传参后开始http请求头伪造环节
![816b016818bd99906443e79248b4ccfa.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1698570354258-ad13552a-d9fc-4de5-8c71-5700f7baf7a0.png#averageHue=%23fbfaf9&clientId=ucbe19d06-950e-4&from=paste&height=114&id=uc3f23c71&originHeight=143&originWidth=717&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=11726&status=done&style=none&taskId=u5c6e13ab-1a65-4956-9fd2-8935383d261&title=&width=573.6)
![958226a293a9b7f14ea1fb6b69ef8cb9.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1698570361832-0d26db81-10bf-4a56-ac66-356cb65457b6.png#averageHue=%23f8f6f5&clientId=ucbe19d06-950e-4&from=paste&height=131&id=ubb05536e&originHeight=164&originWidth=309&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=4061&status=done&style=none&taskId=u55cb5cda-b18a-4e84-b299-7cf89c9eed6&title=&width=247.2)
第一关来源，即伪造来源头referer
Referer是header的一部分，当浏览器向web服务器发送请求的时候，一般会带上Referer，告诉服务器该网页是从哪个页面链接过来的  
![17b7e00792c233a3c6a668bce25ef94e.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1698570594825-36e47b9f-d313-4385-8fd9-b8659ee1105f.png#averageHue=%23f4f3f2&clientId=ucbe19d06-950e-4&from=paste&height=39&id=u81bf76d3&originHeight=49&originWidth=178&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=1936&status=done&style=none&taskId=u2103e06e-6765-4737-8a21-ea57ec8daa9&title=&width=142.4)
进入第二关
![c67ce3271a0f405c551cd67e35c03319.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1698570602744-356311d4-e93c-4597-be58-b3a79a1cd9c7.png#averageHue=%23f6f4f2&clientId=ucbe19d06-950e-4&from=paste&height=126&id=uaa9114b4&originHeight=157&originWidth=265&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=3940&status=done&style=none&taskId=u3db6b002-7c32-4d54-9baf-823078af6b3&title=&width=212)
伪造浏览器信息
 User-Agent头是HTTP客户端（例如Web浏览器）发送的请求头，它包含有关客户端的信息。这些信息可以包括浏览器的名称和版本、操作系统的名称和版本以及其他相关信息。  
![3ef098d84ce0004822ce309486a5d196.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1698570733407-d3addce4-d088-43f4-af90-cbae063cb1a5.png#averageHue=%23f6f5f4&clientId=ucbe19d06-950e-4&from=paste&height=46&id=u8854a430&originHeight=58&originWidth=162&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=1682&status=done&style=none&taskId=ua3c371d2-1b1e-48ae-b406-c5e3d94c2c6&title=&width=129.6)
进入第三层
![7aa02115a32d60b37d22ae831739d58c.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1698570761437-5d002a28-2827-4539-88e6-3627f6a91b2e.png#averageHue=%23f5f3f2&clientId=ucbe19d06-950e-4&from=paste&height=122&id=u0077e862&originHeight=153&originWidth=228&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=3379&status=done&style=none&taskId=u775d8079-8752-4b6c-b370-7745b1caa6f&title=&width=182.4)
伪造IP
 X-Forwarded-For（XFF）是用来识别通过HTTP代理或负载均衡方式连接到Web服务器的客户端最原始的IP地址的HTTP请求头字段。  
![ca4599c26319c547b15962a4567438eb.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1698570876532-4e7fb1f2-2c93-49f8-b955-9984dacd8622.png#averageHue=%23f6f5f4&clientId=ucbe19d06-950e-4&from=paste&height=42&id=u0da4b1f1&originHeight=52&originWidth=331&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=2930&status=done&style=none&taskId=ud208be5c-0049-45f7-b7d4-cb280bd8cef&title=&width=264.8)
进入下一关
![d8b4163f943458dc4f75a04732bcc8e2.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1698570898862-a8f825bd-c996-40b3-8477-facad1308138.png#averageHue=%23f3f1ef&clientId=ucbe19d06-950e-4&from=paste&height=114&id=u0864711e&originHeight=143&originWidth=212&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=3414&status=done&style=none&taskId=uf2775faf-cd0f-4d5c-9798-0a7d80f5f63&title=&width=169.6)
伪造代理
Via头通知中间网关或代理服务器地址，通信协议。
![bbeeac72fda98295a5d64ddaead94ec4.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1698571294129-953654ac-5ce7-41b8-a878-2358d4d1dce9.png#averageHue=%23fefdfd&clientId=ucbe19d06-950e-4&from=paste&height=147&id=ua9eca527&originHeight=184&originWidth=478&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=8474&status=done&style=none&taskId=uaf04e78f-40c3-41d4-b50d-50b52dd0d78&title=&width=382.4)
最后是个预定义http头
![38069cb6af3771bc489fa7057cea97ff.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1698571360687-e49ec31a-e736-4058-8cf4-613de719c465.png#averageHue=%23f6f4f3&clientId=ucbe19d06-950e-4&from=paste&height=46&id=u8ffb1ab7&originHeight=57&originWidth=283&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=3192&status=done&style=none&taskId=uc5c72afe-d3cc-4cc3-99dc-0018b4e402c&title=&width=226.4)
得到flag
![72b192206f1433188b3b602268365cd2.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1698571374014-82984cc7-efb3-4e8e-baec-0c84d4d4cad6.png#averageHue=%23f5f3f1&clientId=ucbe19d06-950e-4&from=paste&height=38&id=u71086bf7&originHeight=48&originWidth=279&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=1638&status=done&style=none&taskId=u15d46eaf-ab5a-4b54-a854-b14939734cc&title=&width=223.2)
2.kali sqlmap
打开靶场
![2b9826c4175b95ad2ca84a8620cd11c8.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1698571838082-68eafdc6-afd2-4a83-bd9a-d8805eeedc3f.png#averageHue=%231d1c1b&clientId=ucbe19d06-950e-4&from=paste&height=292&id=u70107104&originHeight=365&originWidth=1245&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=122290&status=done&style=none&taskId=u2866a7a8-d4d1-4750-a137-8607faf925f&title=&width=996)
尝试id=1注入成功可以用sqlmap
![fec556dc9274ca8f6518da5a809d8961.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1698571923908-a88acc9b-0f65-485d-8e67-3c79ebbbd3a4.png#averageHue=%238e9c33&clientId=ucbe19d06-950e-4&from=paste&height=338&id=ue1b6bb9a&originHeight=422&originWidth=1261&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=128210&status=done&style=none&taskId=udeddf56c-c0c9-4d1a-89a5-60732ca1f78&title=&width=1008.8)
打开shell使用
`sqlmap -u "url" --dbs`
爆库名，获得所有数据库
![f7b9981b5810815dd712bb1c82ba6227.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1698572147766-06dce9ec-156e-4c00-921e-091406cceba7.png#averageHue=%23252934&clientId=ucbe19d06-950e-4&from=paste&height=316&id=u10698509&originHeight=395&originWidth=612&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=96299&status=done&style=none&taskId=u690de85c-711b-4568-bf5a-0c47b192b44&title=&width=489.6)
`sqlmap -u "url" --current-db`
爆当前站点所在库名
![5cf1611e8b33f7f1c62d1630f2e73272.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1698572271859-3b652ece-e7fc-4c82-b8d3-e53b42cd7834.png#averageHue=%23252a35&clientId=ucbe19d06-950e-4&from=paste&height=294&id=u21620506&originHeight=367&originWidth=640&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=97973&status=done&style=none&taskId=u1099c4e1-38b9-4c60-a943-d3e10de0b51&title=&width=512)
然后爆表名
`sqlmap -u "url" -D 数据库 --tables`
![126f5dabfe8310a74bf055b35ad0b406.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1698572392508-4d85b97d-8aac-4f1d-be64-03de62eb3859.png#averageHue=%23242832&clientId=ucbe19d06-950e-4&from=paste&height=303&id=ud39d856f&originHeight=379&originWidth=644&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=78564&status=done&style=none&taskId=u99e1eb6f-fc53-4677-b132-0cf8451a757&title=&width=515.2)
然后爆字段
`sqlmap -u "url" -D 数据库 -T 数据表 --columns`
![67d6197e64f285e38363b358634d34a4.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1698572539440-b6e16ffb-0983-47ad-8471-998f9d749520.png#averageHue=%23242832&clientId=ucbe19d06-950e-4&from=paste&height=197&id=u5de7f5f4&originHeight=246&originWidth=641&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=46040&status=done&style=none&taskId=uf1c4562d-2f80-4206-b8b9-f43e3e7c235&title=&width=512.8)
爆字段内容
`sqlmap -u "url" -D 数据库 -T 数据表 -C 字段 --dump`
![c8d782ad542283f6406aa7d97ba7a7a8.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1698572681073-2ee2992c-6fa6-4bed-8b62-5fb8c5c49c55.png#averageHue=%23272a35&clientId=ucbe19d06-950e-4&from=paste&height=195&id=u4a122bd7&originHeight=244&originWidth=614&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=56788&status=done&style=none&taskId=u2d3f2c37-c82b-4a45-b44e-d7dc68763c3&title=&width=491.2)
`sqlmap -u "url" -D 数据库 -T 数据表 --dump`
直接看表内内容
![851f56e28f1fd57095f622cb9601840b.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1698572756729-eb0e39fb-36c6-4fdc-9bd3-47a915f0e979.png#averageHue=%23262a35&clientId=ucbe19d06-950e-4&from=paste&height=218&id=u0678bcff&originHeight=272&originWidth=631&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=65357&status=done&style=none&taskId=ud86b6921-6886-46dd-8d54-0afbd2af603&title=&width=504.8)
## 下周计划

- 鹏程杯初赛
- 极客大挑战
## 总结
这周活动有一点多，各种体育比赛，和文化艺术节，疯狂赚学分，早日把课外把学费赚完，以后就不用管这些事了。然后又一次了解了kali，kali里总有意想不到的工具。每次学一种题型总会看到本工具kali自带，哈哈。

