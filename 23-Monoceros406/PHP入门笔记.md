---
title: PHP入门笔记
date: 2023-12-02 15:22:07
tags: PHP
mathjax: true
---

# PHP入门笔记

## 语言基础

### 数据类型

```php
<?php
    $name="...";
    echo "xxx".$name."xxx";//.为字符串连接
?>
```

### 类型转换

```php
<?php
    $num='3.1415926r*r';
    echo (int)num;
    $result=settype($num,'integer')
?>
```

### 类型检测

```php
<?php
    $boo="043112345678"
    if(is_numberic($boo)){
        echo "xxx";
    }else{
        echo "xxx";
    }
    if(is_null($boo)){
        echo "xxx";
    }else{
        echo "xxx";
    }
?>
//其他函数：is_bool is_string is_float is_double is_integer is_int is_null is_array is object is_numeric
```

### 定义常量

```php
<?php
    define("MESSAGE","xxx");//区分大小写
    echo MESSAGE;
?>
/*
	默认常量：
	__FILE__ 程序文件名
	__LINE__ 程序行数
	PHP_VERSION 版本 如：php6.0.0-dev
	PHP_OS 操作系统名称 如Windows
	TRUE
	FALSE
	NULL
	E_ERROR
	E_WARNING
	E_PARSE
	E_NOTICE
*/
```

### 指针（引用赋值）

```php
<?php
    $i="book";
    $j=&$i;
    $i="bccd";
    echo $j;//book
    echo "<br>";
    echo $i;
?>
```

### 预定义变量

```php
<?php
    $_SERVER['SERVER_ADDR'] //当前服务器IP
    $_SERVER['SERVER_NAME'] //当前主机名
    $_SERVER['REQUEST_METHOD'] //请求方法
    $_SERVER['REMOTE_ADDR'] //用户IP
    $_SERVER['REMOTE_HOST'] //用户主机名
    $_SERVER['REMOTE_PORT'] //连接服务器的端口
    $_SERVER['SCRIPT_FILENAME'] //执行脚本的绝对路径名
    $_SERVER['SERVER_PORT'] //服务器使用的端口
    $_SERVER['SERVER_SIGNATURE'] //服务器版本、虚拟主机名
    $_SERVER['DOCUMENT_ROOT'] //当前脚本所在根目录
    $_COOKIE //HTTPCookie传到脚本的信息
    $_SESSION //与所有会话变量有关的信息
    $_POST
    $_GET
    $GLOBALS //所有已定义全局变量组成的数组
?>
```

### 字符串

```php
<?php
    $i="xxx";
    echo "$i";//xxx
    echo '$i'//$i
?>
```

### 函数

```php
<?php
    function example($num){
        echo "$num*$num=".$num*$num;
    	return $num*$num;
    }
    $sum=example(10);
?>
```

## 流程控制

### 条件控制

```php
<?php
    $num=rand(1,20);
    if($num%2==0){
        echo "...";
    }else{
        echo "...";
    }
?>
    
<?php
    $num=rand(1,20);
    if($num%2==0){
        echo "...";
    }elseif($num%3==0){
        echo "...";
    }else{
        echo "...";
    }
?>
```

### 日期

```php
<?php
    date_default_timezone_set("Asia/Shanghai");
    $month=date("n");
    $today=date("j");
?>
```

### switch

```php
<?php
    $type=isset($_GET['type'])?$_GET['type']:'';
    switch($type){
        case 'qq':
            echo "...";
            break;
        default:
            echo "...";
    }
?>
```

### for

```php
<?php
    $sum=1;
    for($i=1;$i<=100;$i++){
        $sum*=$i;
    }
    echo "xxx".$sum;
?>
```

### while

```php
<?php
    $num=1;
    $str="xxx";
    while($num<=10){
        if($num%2==0){
            $str.=$num."";
        }
        $num++;
    }
    echo $str;
?>
```

### do...while

```php
<?php
    $num=1;
    do{
        echo "xxx";
    }while($num!=1);
?>
```

### break continue

略。

## 字符串

### 定界符

```php
<?php
    $i="aaaa";
    echo <<<EOT
        这行内容可被输出$i
    EOT;//aaaa
?>
```

### trim

```php
<?php
    $keyword="   (:@_@xxx@_@:)   ";
    $keyword=trim($keyword);//如果不设置字符范围，默认\0 \t \n \x0B \r " "
    $keyword=ltrim($keyword,"(:@_@");
    $keyword=rtrim($keyword,"@_@:)");
?>
```

### strlen

一个汉字在GBK/GB2312中占2个字节，在UTF-8/unicode中占3（或2~4）个字节。

`mb_strlen`的第二个参数如果未设定则默认为内部编码，可由`mb_insternal_encoding`得到。

使用`mb_strlen()`时应确保在php.ini中`extension=php_mbstring.dll`存在且没有被注释掉。

```php
<?php
    $str="啊啊啊啊xxx";
    echo "xxx".strlen($str);//中文字符3字节 15
    echo "xxx".mb_strlen($str,'UTF-8');//7
?>
```

### substr

```php
<?php
    $str="xxxxxxxxxxxxxxx";
    echo substr($str,0);//从第1个字符开始截取
    echo "<br>";
    echo substr($str,4,14);//从第5个字符开始截取14个字符
    echo "<br>";
    echo substr($str,-4,4);//从倒数第4个开始截取4个字符
    echo "<br>";
    echo substr($str,0,-4);//从第1个字符到倒数第4个字符为止
    echo "<br>";

    $str="啊啊啊啊啊啊啊";
    echo substr($str,0,15,"UTF-8");
?>
```

### strstr

```php
<?php
    $string="啊啊啊八八八八";
    echo strstr($string,"八");//八八八八
    echo strstr($string,"八",true);//啊啊啊
    //不区分大小写使用stristr()
    //strrchr()从字符串倒序位置开始检索字符串
?>
```

### strpos

```php
<?php
    $string="xxxx";
    echo strpos($string,"xx",0);//从起始位置开始首次出现的位置，0可选，表示从0开始检索
	//不区分大小写用stripos()函数
?>
```

### str_replace

```php
<?php
    echo str_replace($str2,$str1,$str,$count);//输出str字符串中str2被str1替换后的字符串
    echo "<br>";
    echo $count;//替换个数
?>
```

### sub_replace

```php
<?php
    echo substr_replace($username1_phone,$replace,3,4);//username1_phone字符串中第3+1个字符开始的四个字符替换为replace字符串
?>
```

### explode

```php
<?php
    $array=explode(' ',$string);//将字符串string以空格为分隔符分割到数组array中
    for($i=0;$i<3;$i++){
        echo trim($array[$i],'@')."<br>";
    }
?>
```

### implode

```php
<?php
    $string=implode("@",$str_arr);//将str_arr中的元素用@组合成字符串
?>
```

## 正则表达式

### 基本元素

```
行定位符
^tm 以tm开头
tm$ 以tm结尾

元字符
. 除换行符外任意字符
\w 字母、数字、_、汉字
\s 任意空白符
\d 数字
\b 单词开始或结束
^ 字符串开始
$ 字符串结束
例如：\bmr\w*\b

限定符
? 一次或零次
+ 一次或多次
* 零次或多次
{n} n次
{n,} 最少n次
{n,m} 最少n次，最多m次

字符类、排除字符
[^a-zA-Z]

选择字符、转义字符、分组
```

### preg_match

```php
<?php
    if(preg_match('/1[34578]\d{9}$/',$mobile)){
        //...
    }else{
        //...
    }
	//preg_match_all()全局正则表达式匹配
?>
```

## 数组

### 数组声明

```php
<?php
    $array=array("asp","php","jsp");
    $array=["asp","php","jsp"];
    print_r($array)
    echo $array[1];//php

    $array=array("1"=>"a","2"=>"b","3"=>"c","4"=>"d");
    $array=array("1"=>"a","b","c","d");
    echo $array[1];//a

    $newarray=array("first"=>1,"second"=>2,"third"=>3);
    echo $newarray["second"];
    $newarray["third"]=8;
?>
```

### 高维数组

```php
<?php
    $str=array(
        "xxx"=>array(
            "xxx"=>array('xxx','xxx'),
            "xxx"=>array('xxx')
        ),
        "xxx"=>array(
            "m"=>"xxx",
            "n"=>"xxx"
        ),
        "xxx"=>array(
            "xxx",
            8=>"xxx",
            "xxx"
        )
    );
    print_r($str);
?>
```

### foreach

```php
<?php
    $url=array('PHP官网'=>'www.PHP.net',
               'xxx'=>'xxx');
    foreach($url as $key=>$link){
        echo $key.":".$link.'<br>';
    }
?>
```

### count

```php
<?php
    echo count($array);//数组元素个数
	echo count($array,COUNT_RECURSIVE);//递归统计数组元素个数
?>
```

### array_search

```php
<?php
    $key=array_search($book_name,$books);//找到返回索引，找不到返回false
    if($key){
        echo $price[$key];
    }else{
        echo "未知";
    }
?>
```

### array_pop

```php
<?php
    $arr=array("ASP","Java","Java Web","PHP","VB");
    $array=array_pop($arr);//VB
    echo "$array <br/>";
    print_r($arr);//不存在VB
?>
```

### array_push

```php
<?php
    $arr=array("ASP","Java","Java Web","PHP","VB");
    array_push($array_push,"xxx","xxx");//同上，压入元素
    print_r($array_push);
?>
```

### array_unique

```php
<?php
    $result=array_unique($array);
	print_r($result);
?>
```

### sort

```php
<?php
    function arraySortByKey($array=array(),$key="",$asc=true){
        $result=array();
        foreach($array as $k=>$v){
            $values[$k]=isset($v[$key])?$v[$key]:"";
        }
        unset($v);
        $asc:asort($values):arsort($values);//按照键值排序
        foreach($values as $k=>$v){
            $result[$k]=$array[$k];
        }
        return $result;
    }
    $data=array(
        array('post_id'=>1,'title'=>'xxx','reply_num'=>582),
        //...
    );
    $new_array=arraySortByKey($data,'reply_num',false);
    echo "<pre>";
    print_r($new_array);

	sort() //从低到高排序，不保持索引关系
    rsort() //同上，逆序
    asort() //保持索引关系
    arsort() //同上，逆序
    ksort() //按键名排序
    krsort() //同上，逆序
    natsort() //“自然排序”算法排序
    natcasesort() //同上，不区分大小写
?>
```

### array

```php
<?php
    $result=array_intersect($brand,$color);//取两数组交集

	array_sum() //数组所有值的和
    array_merge() //合并多个数组
    array_diff() //差集
    array_diff_assoc() //带索引检查计算差集
    array_intersect() //交集
    array_intersect_assoc() //带索引检查计算交集
?>
```

## 面向对象

### 基础

```php
<?php
    interface Mpurview{
        function playBasketball();
    }
    interface Mpopedom{
        function showMe();
    }
    class SportObject implements Mpurview,Mpopedom{
        const BOOK_TYPE='xxx';
        public $name,$height;
        const NAME='aaa';
        private $aaa='xxx';
        protected $bbb='xxx';
        static $ccc=0;
        public function __construct($name,$height){
            $this->name=$name;
            $this->height=$height;
            echo SportObject::NAME."<br>";
        }
        public function playBasketball($name,$height){
            $this->name=$name;
            $this->height=$height;
            //...
            return "xxx";
        }
        abstract function showMe();//不会被执行，抽象类不能被实例化
        function __destruct(){
            //析构函数
        }
    }
    final class WeightLifting extends SportObject{//final修饰表示不能被继承
        public $weight;
        const NAME='bbb';
        function __construct($name,$weight){
            $this->weight=$weight;
            $this->name=$name;
            echo self::NAME."<br>";
            echo $this->bbb;//子类可以操作父类的protected型变量
        }
        function showMe(){//重写showMe方法
            if($this->weight<85){
                return $this->name."xxx"."<br>";
            }else{
                return "xxx";
            }
        }
    }
    $sport=new SportObject();
    echo $sport->playBasketball('xxx','xxx');
    echo SportObject::BOOK_TYPE;
    $weightlifting=new WeightLifting()
    if($weightlifting instanceof SportObject)
        echo "weightlifting属于SportObject类";
    echo SportObject::$aaa;//非法，不能读取私有变量
?>
```

### 魔术方法

#### \_\_set、\_\_get

```php
<?php
    class Student{
        private $a;
        private $b=0;
        public $c;
        public $d=0;
        public function __get($name){//外部试图获取不存在或不可见变量
            return 123;
        }
        public function __set($name,$value){//外部试图修改不存在或不可见变量
            echo "this is a set function";
        }
    }
    $s=new Student();
    var_dump($s->a);//123
    var_dump($s->b);//123
    var_dump($s->c);//null
    var_dump($s->d);//0
    var_dump($s->e);//123
    $s->a=3;//输出this is a set function
    $s->c=3;//无输出
    $s->f=3;//输出this is a set function
?>
```

#### \_\_call

```php
<?php
    class SportObject{
        public function myDream(){
            //...
        }
        public function __call($method,$parameter){//外部调用不存在或不可见方法时
            echo $method;//mDream
            print_r($parameter);//参数数组
        }
    }
    $exam=new SportObject();
    $exam->myDream();
    $exam->mDream('how','what','why');
?>
```

#### \_\_toString

```php
<?php
    class SportObject{
        private $type='DIY';
        public function __toString(){//echo或print时对象转字符串
            return $this->type;
        }
    }
    $myComputer=new SportObject();
    echo $myComputer;
?>
```

#### \_\_autoload

```php
<?php
    //常规方法
    require('A.php');
    $a=new A();

    function __autoload($class_name){//当类不存在时自动加载
        $class_path=$class_name.'.php';
        if(file_exitsts($class_path)){
            include_once($class_path);
        }else{
            echo "xxx";
        }
    }
    $myBook=new StudyObject();
?>
//PHP 5.1.2引入spl_autoload_register()
```

## Web交互

### POST表单提交

```html
<form method="POST" action="*.php">
```

## PHP操作MySQL

### 基础操作

```php
<?php
    $host="localhost";
    $userName="root";
    $password="root";
    $dbName="database9";
	$link=mysqli_connect($host,$userName,$password,$dbName) or die("连接失败".mysqli_error());
	$result=mysqli_query($link,"insert into tb_member values('mrsoft','123','mrsoft@mrsoft.com)'");
	//select：成功返回结果集，否则false insert、delete、update：成功true，否则false
?>
```

本章暂时搁置

## Cookie与Session

### Cookie设置

```php
<?php
    date_default_timezone_set('PRC');
    if(!isset($_COOKIE["visittime"])){
        setcookie("visittime",date("Y-m-d H:i:s"));//永久有效
    }else{
        setcookie("visittime",date("Y-m-d H:i:s"),time()+60);//有效时间60秒
        echo $_COOKIE["visittime"];//上次访问时间
    }
    setcookie("xxx","",time()-1);//删除方法
?>
```

### Session设置

```php
<?php
    $path='./tmp/';
    session_save_path($path);//设置Session储存路径
    session_cache_limiter('private');
    $cache_limiter=session_cache_limiter();
    session_cache_expire(10);//设置缓存过期时间
    $cache_expire=session_cache_expire();
    session_start();
    $_SESSION['username']='xxx';
    if(!empty($_SESSION['username'])){
        $userName=$_SESSION['username'];
    }
    unset($_SESSION['username']);//删除对话
    $_SESSION=array();//删除所有会话
    session_destroy();//结束当前整个会话
?>
```

本章暂时搁置。
