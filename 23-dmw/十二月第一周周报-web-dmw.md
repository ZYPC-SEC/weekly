# 本周重点
## 1.fuzz
```
<?php
/*
Read /flaggggggg.txt
Hint: 你需要学会fuzz，看着键盘一个一个对是没有灵魂的
知识补充：curl命令也可以用来读取文件哦，如curl file:///etc/passwd
*/
error_reporting(0);
header('Content-Type: text/html; charset=utf-8');
highlight_file(__FILE__);
$file = 'file:///etc/passwd';
if(preg_match("/\`|\~|\!|\@|\#|\\$|\%|\^|\&|\*|\(|\)|\_|\+|\=|\\\\|\'|\"|\;|\<|\>|\,|\?|jay/i", $_GET['file'])){
    die('你需要fuzz一下哦~');
}
if(!preg_match("/fi|le|flag/i", $_GET['file'])){
    $file = $_GET['file'];
}
system('curl '.$file); 
```
写脚本查正则匹配未过滤的字符
![eb0f939ff5c6b18e7b986dd11f3e97b7.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1701602411052-c62bb1dd-9a77-43bf-aa73-6c0348f44147.png#averageHue=%231e1d1d&clientId=u5ee13b2b-6ceb-4&from=paste&height=275&id=ua6601db9&originHeight=344&originWidth=1173&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=25449&status=done&style=none&taskId=u52a4700b-fe98-4465-8503-f279ce0942c&title=&width=938.4)
看到[]{}./|没有过滤，直接命令执行||左边的curl显然无法执行，则会执行右边的代码，然后通过[a-z]绕过正则匹配得到flag
![5bcfc2538508bbe1b5252d0e0c998439.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1701602481273-2a15cee5-b25d-418c-885a-16f12aa3bee7.png#averageHue=%23fbfaf8&clientId=u5ee13b2b-6ceb-4&from=paste&height=383&id=u2e3d5308&originHeight=479&originWidth=1689&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=95772&status=done&style=none&taskId=u7a4879a1-2336-40bb-ade2-8282ea9248d&title=&width=1351.2)
## 2.webinclude
打开题目看到
![6e2df07d974bcb3c80eb30f610f39acc.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1701604493499-47f6dba8-634a-40c2-b2a3-eedd2898338a.png#averageHue=%23f9f8f8&clientId=u5ee13b2b-6ceb-4&from=paste&height=103&id=u3d00c5cf&originHeight=129&originWidth=530&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=2991&status=done&style=none&taskId=ue12d96e3-b5a7-42f1-99b4-957e75cefc9&title=&width=424)
告诉我你的参数!!错误的参数!找参数的意思，然后用dirsearch扫出两个目录
![9b696ede072b3438c234e6a93a82ad8c.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1701605112645-701be4b6-f34c-42e4-90ee-f660cb78f6bf.png#averageHue=%23111111&clientId=u5ee13b2b-6ceb-4&from=paste&height=330&id=u2dd8fbd1&originHeight=412&originWidth=1379&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=37337&status=done&style=none&taskId=ub604b9c9-84bd-4702-be55-d31f029e5c0&title=&width=1103.2)
然后下载index.bak
```
 function string_to_int_array(str){
        const intArr = [];

        for(let i=0;i<str.length;i++){
          const charcode = str.charCodeAt(i);

          const partA = Math.floor(charcode / 26);
          const partB = charcode % 26;

          intArr.push(partA);
          intArr.push(partB);
        }

        return intArr;
      }

      function int_array_to_text(int_array){
        let txt = '';

        for(let i=0;i<int_array.length;i++){
          txt += String.fromCharCode(97 + int_array[i]);
        }

        return txt;
      }


const hash = int_array_to_text(string_to_int_array(int_array_to_text(string_to_int_array(parameter))));
if(hash === 'dxdydxdudxdtdxeadxekdxea'){
            window.location = 'flag.html';
          }else {
            document.getElementById('fail').style.display = '';
          }

```
为js加密代码，解密得到参数mihoyo
![51fbf311b0f97ff15d6b6c3b1381b584.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1701605645005-60b8035c-0418-43cb-a1fc-5b9f1356ae14.png#averageHue=%231f1f1e&clientId=u5ee13b2b-6ceb-4&from=paste&height=276&id=u8ca5844a&originHeight=345&originWidth=914&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=25171&status=done&style=none&taskId=u8a08659d-7cc6-40c1-9946-202c9660aad&title=&width=731.2)
然后给mihoyo传入命令发现他是include函数
![ee5af5e844b57c6ae1e4ade23da7b241.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1701605767193-16cca68c-195d-4ad3-9ed8-635d9b4b8947.png#averageHue=%23f1efee&clientId=u5ee13b2b-6ceb-4&from=paste&height=57&id=u69415b34&originHeight=71&originWidth=1210&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=10567&status=done&style=none&taskId=ub114b625-1205-45c5-b1ed-a52f1629d2e&title=&width=968)
直接传伪协议得到flag
![d557b1cc509e8ddcaa0bc071d50f8082.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1701605817537-72b1ad06-0c77-4014-9ba7-d44081a7e2f0.png#averageHue=%23b2f8f7&clientId=u5ee13b2b-6ceb-4&from=paste&height=124&id=u0f7f5a98&originHeight=155&originWidth=1337&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=29488&status=done&style=none&taskId=u3f017bd5-4896-455a-9f8f-1d0e5f17053&title=&width=1069.6)
![4d22b99d9b0b13204183e47bd11c26de.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1701605825168-83d29c8f-0e13-4c83-b476-850888acc7ea.png#averageHue=%23f5f2c1&clientId=u5ee13b2b-6ceb-4&from=paste&height=180&id=u2769c9ad&originHeight=225&originWidth=858&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=11684&status=done&style=none&taskId=uaaed396a-0915-47ca-a21d-a1e5eb2a290&title=&width=686.4)
## 3.尝试xss
发现现在题一直再考各种注入攻击，之前浅学了些sql，现在打算尝试一下xss，打的是xss-lab靶场
### 1.level1
![238e2ce2e57f1577855caac84f10d785.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1701606359707-62445da6-f2bc-4677-8ef8-a2e76fb17475.png#averageHue=%23dadada&clientId=u5ee13b2b-6ceb-4&from=paste&height=586&id=u9a9c5d96&originHeight=733&originWidth=705&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=140293&status=done&style=none&taskId=u7729f4f5-c305-4369-a925-7e9fd54ad3c&title=&width=564)
首先可以看到是给name进行get传参
![991120245ffdb82052c5b87986892844.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1701606421071-59642e66-576f-4a6a-b7ce-f15bd04a4a68.png#averageHue=%23eaeaee&clientId=u5ee13b2b-6ceb-4&from=paste&height=34&id=ucce3a52b&originHeight=43&originWidth=220&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=1109&status=done&style=none&taskId=u0649b737-203c-4f5b-a505-269dabe27af&title=&width=176)
然后看到标志性的xss <center>尝试反射型
![833fed8dc994fd13f99d5afa5dc70ddb.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1701606485156-86edf691-5855-452f-80c3-876253cb1f5f.png#averageHue=%23fffae4&clientId=u5ee13b2b-6ceb-4&from=paste&height=54&id=u856c916f&originHeight=67&originWidth=347&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=2072&status=done&style=none&taskId=u47ec721f-2400-43bf-bd78-e827c0a1d07&title=&width=277.6)
直接输入payload：
![e24b6c994246f00d9b55346b9770bc33.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1701606699428-10955637-ba18-4739-b157-53bb76a72408.png#averageHue=%23ebecf1&clientId=u5ee13b2b-6ceb-4&from=paste&height=33&id=u72fefa84&originHeight=41&originWidth=484&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=2427&status=done&style=none&taskId=u7829db51-363f-4c51-bcd6-c4c495621a7&title=&width=387.2)
过关
![b17a15f5f86acbcaeccb0b28ebb910b1.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1701606718328-9cc1dcbc-83dc-4f47-81c1-fa44eae59be2.png#averageHue=%23cacbcf&clientId=u5ee13b2b-6ceb-4&from=paste&height=164&id=ud74f9321&originHeight=205&originWidth=581&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=28464&status=done&style=none&taskId=u07f69e86-777c-45ff-8f04-d1da4b2ebbe&title=&width=464.8)
### 2.level2
![90e174557151c175c945c48635e66aef.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1701606751915-7255869c-3c76-42ef-8f73-1993b9c91d40.png#averageHue=%23efeeed&clientId=u5ee13b2b-6ceb-4&from=paste&height=502&id=u24ddfda9&originHeight=628&originWidth=481&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=61310&status=done&style=none&taskId=ua960f341-335b-43f0-9d9a-5c92bd3af14&title=&width=384.8)
看源码
![4d287f675d390d834fc99e252d685503.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1701606795397-2a100054-8759-419e-b58b-44ea1ad1be05.png#averageHue=%23fefefe&clientId=u5ee13b2b-6ceb-4&from=paste&height=231&id=udeb7929f&originHeight=289&originWidth=469&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=13015&status=done&style=none&taskId=u959543d5-c19b-426f-bb00-0609b553f49&title=&width=375.2)
尝试注入
![8890001b1b73d37256d6e03659deb19d.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1701606858694-aea4250b-daee-4d18-9ada-e35e141aedcb.png#averageHue=%23f7e6c7&clientId=u5ee13b2b-6ceb-4&from=paste&height=134&id=ua3911136&originHeight=167&originWidth=592&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=8293&status=done&style=none&taskId=u44e65bfc-29dd-4cd2-9318-674f2e244f3&title=&width=473.6)
可以看到注入值在center中间，我们构造一波前闭合，过关
![88e61049b27e4b3f135da8ac047c0f6d.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1701606947218-3391fb91-4c6d-4735-83bc-3754d5b8d173.png#averageHue=%231e66c1&clientId=u5ee13b2b-6ceb-4&from=paste&height=359&id=u088d5646&originHeight=449&originWidth=601&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=36028&status=done&style=none&taskId=ua4993fcf-fffa-4f87-ae2a-d7c23574b19&title=&width=480.8)
### 3.level3
![image.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1701607047452-02d7a648-7af9-4e99-bbed-cffa582864af.png#averageHue=%23e4e2e2&clientId=u5ee13b2b-6ceb-4&from=paste&height=475&id=u72cc1ad1&originHeight=594&originWidth=836&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=63335&status=done&style=none&taskId=u5bf4be0b-86e7-45c1-bc9e-7bd4be7b2a0&title=&width=668.8)
直接注入后看源码
![408d5940cb6cdc97e3577db3853f89e0.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1701607187937-39bfb884-c23b-424f-9016-b35be9716390.png#averageHue=%23fefdfc&clientId=u5ee13b2b-6ceb-4&from=paste&height=178&id=u0c21deba&originHeight=223&originWidth=652&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=13181&status=done&style=none&taskId=u58738334-7181-4652-9255-59e87ff202f&title=&width=521.6)
构造闭合，还是不行
![71b8f1dc1b7793751c37617c2b7fa8b2.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1701607291030-9d586907-daeb-4bb2-b3c8-d86d2c78ba49.png#averageHue=%23fefefd&clientId=u5ee13b2b-6ceb-4&from=paste&height=109&id=u99369fe5&originHeight=136&originWidth=674&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=10249&status=done&style=none&taskId=uda6cb5c7-ac99-4305-bd85-7dfe8e81f71&title=&width=539.2)
用网上payload过关了
![ca3422c20c3735dd2b0c76c4c42161e6.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1701607701145-7d951b77-16ed-4c74-82f0-27d57d574474.png#averageHue=%236b88ae&clientId=u5ee13b2b-6ceb-4&from=paste&height=369&id=uc65c3f45&originHeight=461&originWidth=846&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=48356&status=done&style=none&taskId=ua46de1cd-8155-43f0-b4d9-3a439d8d02d&title=&width=676.8)
# 下周计划

- is等大佬把复现靶场完成后继续复现
- 学学注入
# 总结
isctf是一次非常好的团队合作体验，虽然没有misc手，但大家合作想办法，写脚本将misc几乎ak，然后web方面要么会做的直接出，要么不会就坐牢，实力还是差很多，需要后期继续复现之前比赛和刷题积累，本周还尝试了awd比赛，第一次打awd，比赛方式，怎么找自己漏洞，怎么修漏洞，怎么攻击别人漏洞，还有怎么得分算是开启新大陆了。

