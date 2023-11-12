## 本周重点
### 1.任务进展

- shctf week3
- n1CTF坐牢
- 开始学习sql注入
### 2.知识分享
1.web信息搜集（一）（ctfshow）

- 源码泄露

![bf4aa78ef6eb4dc3ec15ca4a313ea4fc.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1697901487770-3c4acbcc-9c9c-4eca-88f1-3a96b66e6d5d.png#averageHue=%23faf9f9&clientId=ua4b38011-a7b0-4&from=paste&height=124&id=u05bb1522&originHeight=155&originWidth=405&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=4082&status=done&style=none&taskId=u86c7ec52-f2f4-4bb7-a9ea-bc460be6565&title=&width=324)
直接右键查看源码得到flag
![4d325c7cb521db5c78e4d006bc59567e.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1697901539589-408e65b0-1357-4e7e-8976-5a8fda30b68b.png#averageHue=%23fefefd&clientId=ua4b38011-a7b0-4&from=paste&height=499&id=u7706561e&originHeight=624&originWidth=788&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=58054&status=done&style=none&taskId=ufa528033-23b5-4721-8af9-9129314e052&title=&width=630.4)

- 前端js绕过

![00fd05dd6518ea20a17a50e972c12674.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1697901666576-fec39f65-2a98-4387-a96f-9754d1dde15a.png#averageHue=%23f4f3f2&clientId=ua4b38011-a7b0-4&from=paste&height=88&id=u4f8f0f65&originHeight=110&originWidth=312&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=3709&status=done&style=none&taskId=u299540ae-930c-49f8-b390-f6b64a9e033&title=&width=249.6)
无法右键查看源码
这里我说下查看源码的几种姿势
1.Ctrl+U
2.在URL前添加 view-source:  
3.F12--->查看器/调试器/网络 均可查看
![f7a8f162c0faf30e07ac682ef9c50d10.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1697902063072-996deb3d-4c00-484d-b680-458fef62627e.png#averageHue=%23fefdfc&clientId=ua4b38011-a7b0-4&from=paste&height=521&id=u5ff47811&originHeight=651&originWidth=1089&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=73356&status=done&style=none&taskId=uca5a447c-610c-4197-ad01-fdf0c80718d&title=&width=871.2)

- 协议头信息泄露

![a3e75cd040e5d3b8ae1112757d1b1e73.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1697902774650-78b58b17-7295-4705-aa87-1b11b083580d.png#averageHue=%23faf9f9&clientId=ua4b38011-a7b0-4&from=paste&height=76&id=u41817938&originHeight=95&originWidth=325&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=1717&status=done&style=none&taskId=u56cffc13-9d81-4dc4-a83b-2cdcfc83fbc&title=&width=260)
抓包看协议
![4dd3aeb46d815b7ec9ebd78c53086caf.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1697902800862-6a457ca9-43a2-45f4-bd3b-9dfabb51fedd.png#averageHue=%23dfb581&clientId=ua4b38011-a7b0-4&from=paste&height=174&id=u1ec4df80&originHeight=218&originWidth=583&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=15122&status=done&style=none&taskId=u11b047b6-a0f9-4fa6-bca8-0f5e029a0c7&title=&width=466.4)

- robots后台泄露

![1b1b1a65ee3f33dbc8bcb702fea95511.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1697903069430-bcc8831e-6a85-4468-b645-8eead4b192b1.png#averageHue=%23f9f8f7&clientId=ua4b38011-a7b0-4&from=paste&height=78&id=u12be887c&originHeight=98&originWidth=264&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=1708&status=done&style=none&taskId=ud0c42fb7-3cc8-4a5b-b1f0-8cba0303c4d&title=&width=211.2)
URL/robots.txt查看robots文件
![dc92a9bad499446ffb2e7970f8b9a957.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1697903102294-0d423c89-fbff-43bf-81f3-7dc823917cb3.png#averageHue=%23fbf9f8&clientId=ua4b38011-a7b0-4&from=paste&height=67&id=udf555997&originHeight=84&originWidth=310&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=1782&status=done&style=none&taskId=u6fded06f-4fb1-46ca-a222-309c752a05e&title=&width=248)![e4c04bec4a06b255ebc75ebaaea224ad.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1697903115119-89eb6458-aa25-4fad-858c-7968d1f4c29f.png#averageHue=%23f8f6f4&clientId=ua4b38011-a7b0-4&from=paste&height=35&id=ub802b5ca&originHeight=44&originWidth=471&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=2124&status=done&style=none&taskId=u9846e275-8915-47c9-af68-03efa1d20a4&title=&width=376.8)

- phps源码泄露

![467dc2c94658a0360e615b31485c8011.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1697903459791-6992fead-c75e-4890-b2df-c7ed33b834a9.png#averageHue=%23f9f7f7&clientId=ua4b38011-a7b0-4&from=paste&height=66&id=uec4b7059&originHeight=82&originWidth=283&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=1661&status=done&style=none&taskId=ueb13ab63-c303-4c31-9f48-b1780db701f&title=&width=226.4)
phps文件就是php源代码文件 URL/index.phps
![286e158d0821767ae0bf553e734dc634.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1697903492782-d0d1e46c-22cd-4a21-9400-a2bcd3a7b044.png#averageHue=%23f4f2f2&clientId=ua4b38011-a7b0-4&from=paste&height=382&id=u99f34ae1&originHeight=478&originWidth=550&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=17163&status=done&style=none&taskId=u29285f82-0b0b-40e5-aeac-ac4df6c2a5c&title=&width=440)

- 源码压缩包泄露

成因：网站修改时，存有备份文件，访问备份文件不需要权限，可以直接被下载，并且可以被任意使用修改
可能的后缀名：.rar .zip .7z .tar.gz .bak .swp .txt，例如www.zip
2.php preg_replace /e 模式 漏洞（shctf）
preg_replace函数基本形式
```php
mixed preg_replace ( mixed $pattern , mixed $replacement , mixed $subject )
```
shctf的题目：
```
<?php
error_reporting(0);
if(isset($_GET['code']) && isset($_POST['pattern']))
{
    $pattern=$_POST['pattern'];
    if(!preg_match("/flag|system|pass|cat|chr|ls|[0-9]|tac|nl|od|ini_set|eval|exec|dir|\.|\`|read*|show|file|\<|popen|pcntl|var_dump|print|var_export|echo|implode|print_r|getcwd|head|more|less|tail|vi|sort|uniq|sh|include|require|scandir|\/| |\?|mv|cp|next|show_source|highlight_file|glob|\~|\^|\||\&|\*|\%/i",$code))
    {
        $code=$_GET['code'];
        preg_replace('/(' . $pattern . ')/ei','print_r("\\1")', $code);
        echo "you are smart";
    }else{
        die("try again");
    }
}else{
    die("it is begin");
}
?> 
```
先简单展示preg_replace函数的作用
```
    <?php
    $str = "wo shi da shuai ge";
    echo $str;
    echo "\n";
    $ste = preg_replace('/shi/','bu shi',$str);
    echo $ste;
    ?>
```
 这个代码就是在str字符串中搜索"shi"这个字符串，然后将它替换为"bu shi"；运行结果：  
```
    wo shi da shuai ge
    wo bu shi da shuai ge
```
然后我再讲下这个/e模式，在这个模式下replacement参数可以作php代码执行（前提该参数为合法的PHP代码字符串）
而在上周周报可知php代码中“”中间的的变量会进行命令执行
所以preg_replace函数/e模式加“”组合就是该漏洞出题形式
(.*)则是一个捕获组可以匹配所有字符{注：get传参.会变成_而POST不会，本题为post传参没有bug，当遇到get传参时可以用\S来代替空白非打印字符，即可代替.}
然后就可以构造payloadle
![clip_image002.jpg](https://cdn.nlark.com/yuque/0/2023/jpeg/39174886/1697962909573-5b8d4cf4-c462-4390-966f-5395b5f74963.jpeg#averageHue=%23fbfbfb&clientId=u017abcbe-2ae3-4&from=drop&id=u5bf95a69&originHeight=321&originWidth=692&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=17039&status=done&style=none&taskId=ufa83c04f-8fb6-4466-9582-9c8b62d2580&title=)
即可输出结果
## 下周计划

- ntactf
- 继续学习积累
- 打完青少年CTF的sql靶场，总结sql注入
## 思考
有了规划后做事就顺很多了，至少大部分要干的事有时间概念，课内学习方面除了英语其他目前还没感到压力，比赛方面本来以为n1ctf可以看佬们乱杀，没想到在我交了misc签到后就开始集体坐牢，梦回高二第一次打强网杯，太难了，还是自己见识太浅，网络安全漏洞出题日益更新，就像之前的windows截图漏洞，实在是很惊叹，开眼，所以更要好好学习。

