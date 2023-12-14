---
title: Go语言基础
date: 2023-11-08 08:35:32
tags: Go
mathjax: true
---

# Go语言基础

## 入门

### 代码结构

```go
package main
import "fmt"
func main(){
    fmt.Print("...");
    fmt.Println("...");
    return;
}
```

### 语句

```go
var i int;
i=300;
fmt.Print(i);
```

### 代码块

```go
if a>0{
    //...
}else{
    /*...*/
}
```

## 运算符

### 基础运算符

```go
package main;
import(
    "fmt"
)
func main(){
    var m,n int;
    fmt.Scan(&m,&n);
    r1:=m+n;//不需var声明直接使用
    fmt.Printf("%d+%d=%d\n",m,n,r1);
    return;
};
```

### 指数运算

```go
result:=math.Pow(5,3);
fmt.Printf("%d\n",int(result));
result=math.Pow10(4);
fmt.Printf("%d\n",int(result));
result:=math.Pow(81,0.5);
fmt.Printf("%d\n",int(result));
```

### 比较运算符

```go
var num=30000;
var p1 *int-&num;
var p2 *int=&num
result=p1==p2;
fmt.Printf("%t\n",result);//true
```

### 空接口

```go
var k1,k2 interface{};
k1=50;
k2=50;
result=k1==k2;
fmt.Printf("%t\n",result);
```

### 自定义结构体

```go
type test struct{
    fd01 int8;
    fd02 float64;
    fd03 int16;
};
var obj1,obj2 test;
obj1=test{
    fd01:2,
    fd02:0.00075,
    fd03:809,
};
obj2=test{
    fd01:2,
    fd02:0.00075,
    fd03:809,
};
result=obj1==obj2;
fmt.Printf("%t\n",result);
```

### 接口类型

```go
type get interface{
    GetName() string;
};
type cat struct{
    name string;
};
func(c cat) GetName() string{
    return c.name;
};
type dog struct{
    name string;
};
func(d dog) GetName() string{
    return d.name;
};
var(
    pet1 pet=cat{name:"Jack"};
    pet2 pet=dog{name:"Tim"};
    pet3 pet=pet2;
);
result=pet1==pet2;//false
result=pet2==pet3;//true
```

### 特殊位运算符

```go
var n uint8=27;
var r=^n;//228

var a int8;
a=7;
res=^a;//-8 取7的补码

var a int16=29156;
var r=a<<7;
fmt.Printf("%[1]d(%016[1]b)<<5:%[2]d(%016[2]b)",a,r);
//[1][2]表示第一、二个参数，016保留16位二进制数。

var k uint8=0b_1101_1111;//或0b_11011111
var r =k&^0b_00000111;//最右边三位变为0
//八进制：0o 十六进制：0x
```

有符号整数按位取反公式：$c=-(n+1)$。

### 取地址

```go
type point struct{
    x float32;
    y float32;
};
func clean(p *point){
    p.x=0.0;
    p.y=0.0;
};
var pt point;
pt.x=10.5;
pt.y=32.35;
clean(&pt);
```

## 包管理

### 包命名规则

一个目录下所有文件必须为同一个package。编译器默认从GOPATH中找需要的库，系统库默认从GOROOT中找。

### 初始化函数

```go
import _ "test";//仅调用init函数初始化，而不导入
```

### 成员可访问性

当成员的首字母大写时才可被其他包代码访问。

### 匿名变量

```go
a,b,_:="abc","lmn","opq";
```

### 常量

```go
const Val1 int=0;
```

### 批量声明

```go
var(
    k=0.0001;
    j=0.0021;
    m int16=5530;
);
const(
    //...
);
```

### iota

```go
const(
    S=17;
    T=9;
    U=iota;//2
    V;//3
    W=iota+3;//7
    X;//8
    Y;//9
    Z;//10
);
```



## 字符与字符串

### rune

```go
var x1 rune='f';//英文、中文字符、标点、特殊、数字
```

### string

```go
var st string="zyx";
st=`
	多行字符串内容
`;
```

### 数值类型

int8 uint8 int16 uint16 int32 uint32 int64 uint64 int uint byte float32 float64 complex64 complex128

```go
t1:=35.25e6;
var ca complex128=50+2i;
```

## 时间日期

### time包

```go
import "time";
func main(){
    var n=time.Now();
    fmt.Print(n);
    return;
};
```

### Month/Weekday

```go
var date=time.Date(2007,time.June,14,0,0,0,0,time.Local);
var weekday=date.Weekday();
var wdStr string;
switch weekday{
    case time.Sunday:
    	wdStr="星期天";
    //...
	default:
    	//...
};
```

### Duration

```go
import "time";
func main(){
    var dr=24*time.Hour;
    fmt.Printf("%d\n",int64(dr.Minutes()));
    fmt.Printf("%d\n",int64(dr.Seconds()));
    fmt.Printf("%d\n",dr.Milliseconds());
    fmt.Printf("%d\n",dr.Microseconds());
    fmt.Printf("%d\n",dr.Nanoseconds());
    return;
}
```

### Time

```go
var ct=time.Now();
year,month,day:=ct.Date();
hour,minute,second=ct.Clock();

var newTime1=ct.Add(30*time.Hour);
var newTime2=ct.Add(-4*24*time.Hour);//4天前
```

### Sleep

```go
time.Println(3*time.Second);
```

## 函数

### 可变个数的参数

```go
func test(args...float32){
    n:=len(args);
    fmt.Printf("%d\n",n);
    if(n>0){
        for _,val:=range args{
            fmt.Printf("%f",val);
        }
    }
    return;
}
```

### 匿名函数

```go
var myfun=func(x,y int)int{
    return x*x+y*y;
};
res:=myfun(2,4);
```

### 协程

```go
func main(){
    var ch=make(chan byte);
    go func(){
        //...
        ch<-1;
    };
    <-ch;
    //...
    return;
};
```

### 函数作为参数传递

```go
func printElements(fn func(int),items...int){
    if(len(items)==0||fn==nil){
        return;
    };
    for _,n:=range items{
        fn(n);
    };
    return;
};
var pf1=func(i int){
    fmt.Printf("%d\n",i);
};
printElements(pf1,5,8,12);//5 8 12
```

## 流程控制

### 输入

```go
var input int;
fmt.Scan(&input);
```

### switch

与C语言不同，只会找一个case语句执行。

```go
switch(n){
	case 1,3,5,7,9:
    	//...
	case 0,2,4,6,8:
    	//...
};

switch{
	case i%3==0:
    	//...
	case i%5==0:
    	//...
    //...
};

var t interface{}=0.0000012;
switch t.(type){
	case int:
    	//...
    //...
};

var number=200;
switch(number){
    case 200:
    	//...
    	fallthrough;
    case 400:
    	//...
};
```

### for

```go
var q=1;
for q<10{
    //...
    q++;
};

for i:=0;i<12;i+=2{
    fmt.Print(i," ");
};

var str string="春江水暖鸭先知";
for i,x:=range str{
    fmt.Printf("%2d-->%c\n",i,x);
};

var m=map[rune]string{'a':"at",'b':"bee",'c':'cut'}
for key,value:=range m{
    fmt.Printf("[%c]:%s\n",key,value);
};

var ch=make(chan int);
go func(){
    defer close(ch);
    ch<-1;
    ch<-2;
    ch<-3;
    ch<-4;
    ch<-5;
    ch<-6;
}();
for v:=range ch{
    fmt.Printf("%d\n",v);
};
```

### continue/break

略。

### goto

略。

## 加密解密

### Base64

字符串形式：

```go
package main;
import(
	"fmt";
	"encoding/base64"
);
func main(){
	var testData="This is my DATA!!!";
	var encodeStr=base64.StdEncoding.EncodeToString([]byte(testData));
	fmt.Printf("%s\n",encodeStr);
	var decodeData,err=base64.StdEncoding.DecodeString(encodeStr);
	if(err!=nil){
	    fmt.Println("Eroor!\n",err);
	    return;
	};
	fmt.Printf("%s\n",string(decodeData));
	return;
};
```

换表：

```go
var encodeStr="...";//表 必须64字节 不能出现\n \r
custEncoding:=base64.NewEncoding(encodeStr);
testData:="...";//要被加密的信息
var ecStr=custEncoding.EncodeToString([]byte(testData));
fmt.Printf("%s\n",ecStr);

var decodeData,_=custEncoding.DecodeString(ecStr);
fmt.Printf("%s\n",decodeData);
```

字节形式：

```go
var data=[]byte("...");
n:=base64.StdEncoding.EncodedLen(len(data));//编码后字节数
encodeData:=make([]byte,n);
base64.StdEncoding.Encode(encodeData,data);
fmt.Printf("%#x\n",encodeData);

n=base64.StdEncoding.DecodedLen(len(encodeData));
decodeData:=make([]byte,n);
base64.StdEncoding.Decode(decodeData,encodeData);
fmt.Printf("%#x\n",decodeData);
```

流形式：

```go
file,err:=os.Create("encode.bin");
if err!=nil{
    fmt.Println(err);
    return;
};
var b64Writer=base64.NewEncoder(base64.StdEncoding,file);
b64Writer.Write([]byte("..."));
b64Writer.Write([]byte("..."));
b64Writer.Write([]byte("..."));
//...
b64Writer.Close();
file.Close();

file,err=os.Open("encode.bin");
if err!=nil{
    fmt.Println(err);
    return;
};
var decoder=base64.NewDecoder(base64.StdEncoding.file);
io.Copy(os.Stdout,decoder);
file.Close();
```

### DES/AES(Block)

```go
import("crypto/des";"crypto/cipher");//AES为crypto/aes
var key=[]byte{//密钥长度为8字节 aes为16/24/32字节
    0x2D,//...
};
block,err:=des.NewCipher(key);
if(err!=nil){
    fmt.Println(err);
    return;
};
var test=[]byte{//密文 多出8字节的不参与计算
    0x26,//...
};
/*
	var test=make([]byte,aes.BlockSize);
	copy(srcData,[]byte("你好，世界"));
*/
var enc=make([]byte,len(test));
block.Encrypt(enc,test);
var dec=make([]byte,len(test));
block.Decrypt(dec,enc);
```

### DES/AES(BlockMode)

```go
dt:=[]byte("密文");
var n int;
//确定密文为8/16整数倍：
if(len(dt)<=des.BlockSize){
    n=1;
}else{
    n=len(dt)/des.BlockSize;
    if(len(dt)%des.BlockSize>0){
        n++;
    };
};
srcdata:=make([]byte,des.BlockSize*n);
copy(srcdata,dt);
var key=[]byte{
    0x02,//...
};
var iv=make([]byte,des.BlockSize);
rand.Read(iv);//iv随机生成
block,err:=des.NewCipher(key);
if(err!=nil){
    fmt.Println(err);
    return;
};
encBlockmode:=cipher.NewCBCEncrypter(block,iv);
var out=make([]byte,len(srcdata));
encBlockmode.CryptBlocks(out,srcdata);
desBlockmode:=cipher.NewCBCDecrypter(block,iv);
var dec=make([]byte,len(out));
desBlockmode.CryptBlocks(dec,out);
```

### DES/AES(Stream)

文件加密：

```go
var srcFilename="*.jpg";
var outFilename="*.bin";
var key=[]byte{
    0x18,//...
};
var iv=make([]byte,aes.BlockSize);
rand.Read(iv);
srcFile,err:=os.Open(srcFilename);
if(err!=nil){
    fmt.Printfln(err);
    return;
};
defer srcFile.Close();
outFile,err:=os.Create(outFilename);
if(err!=nil){
    fmt.Println(err);
    return;
};
defer outFile.Close();
block,err:=aes.NewCipher(key);
if(err!=nil){
    fmt.Println(err);
    return;
};
outFile.Write(iv);
var stream=cipher.NewOFB(block,iv);
strWriter:=cipher.StreamWriter{
    S:stream,
    W:outFile,
};
defer strWriter.Close();
io.Copy(strWriter,srcFile);//加密、写入文件
```

文件解密：

```go
var encFilename="*.bin";
var decFilename="*.jpg";
var key=[]byte{
    0x18,//...
};
encFile,err:=os.Open(encFilename);
if(err!=nil){
    fmt.Println(err);
    return;
};
decFile,err:=os.Create(decFilename);
if(err!=nil){
    fmt.Println(err);
    return;
};
defer encFile.Close();//跳出当前代码范围时执行
defer decFile.Close();
block,err:=aes.NewCipher(key);
if(err!=nil){
    fmt.Println(err);
    return;
};
var iv=make([]byte,aes.BlockSize);
encFile.Read(iv);
stream:=cipher.NewOFB(block,iv);
strReader:=cipher.StreamReader{
    S:stream,
    R:encFile,
};
io.Copy(decFile,strReader);
```

### Hash

法一：

```go
import(
    "crypto";
    _ "crypto/md5";
    _ "crypto/sha1";
    _ "crypto/sha256";
    "fmt"
);
func main(){
    var msg="...";
    md5:=crypto.MD5.New();
    sha1:=crypto.SHA1.New();
    sha256:=crypto.SHA256.New();
    var data=[]byte(msg);
    md5.Write(data);
    sha1.Write(data);
    sha256.Write(data);
    fmt.Printf("%x\n",md5.Sum(nil));
    fmt.Printf("%x\n",sha1.Sum(nil));
    fmt.Printf("%x\n",sha256.Sum(nil));
};
```

法二：

```go
var src=[]byte("...");
var(
    sha1Sum=sha1.Sum(src);
    sha256Sum=sha256.Sum256(src);
    sha384Sum=sha512.Sum384(src);
    sha512Sum=sha5112.Sum512(src)
);
fmt.Printf("%x\n",sha256Sum);
```

### 文件Hash

```go
var fileName="*.bin";
sha1:=sha1.New();
inputFile,_:=os.Open(fileName);
io.Copy(sha1,inputFile);
inputFile.Close();
result:=sha1.Sum(nil);
fmt.Printf("%x\n",result);
```

### HMAC

```go
import "cyrpto/hamc";
var Key[]byte=make([]byte,64);
func init(){
    rand.Seed(time.Now().Unix());
    rand.Read(Key);//随机密钥
};
func ComputeHMAC(msg string)[]byte{
    var buf=[]byte(msg);
    mHmac:=hmac.New(sha256.New,Key);
    mHmac.Write(buf);
    return mHmac.Sum(nil);
};
var msg01 string;
fmt.Scanln(&msg01);
var hash01=ComputeHMAC(msg01);
var msg02 string;
fmt.Scanln(&msg02);
var hash02=ComputeHMAC(msg02);
res:=hmac.Equal(hash01,hash02);
if(res){
    //两条消息一致
}else{
    //不一致
};
```

### RSA

PKCS#1 v1.5标准：

```go
import "crypto/rsa";
var prvKey,_=rsa.GenerateKey(rand.Reader,512);
var pubKey=&prvkey.PublicKey;
var msg="...";\
var cipherText,_=rsa.EncryptPKCS1v15(rand.Reader,pubkey,[]byte(msg));
var decText,_=rsa.DecryptPKCS1v15(rand.Reader,prvKey,cipherText);
```

OAEP标准：

```go
import "crypto/rsa";
var prvKey,_=rsa.GenerateKey(rand.Reader,1024);
var pubKey=&prvKey.PublicKey;
var msg="...";
var cipherText,_=rsa.EncryptOAEP(sha256.New(),rand.Reader,pubKey,[]byte(msg),nil);
var decText,_=rsa.DecryptOAEP(sha256.New(),rand.Reader,prvKey,cipherText,nil);
```

### 存储密钥

```go
import "crypto/x509";
var prvkey,_=rsa.GenerateKey(rand.Reader,512);
var pubkey=&prvkey.PublicKey;
keydata:=x509.MarshalPKCS1PrivateKey(prvkey);
ioutil.WriteFile("myPrvkey",keydata,0600);//写入文件
var testmsg="测试消息";
var cipherdata,_=rsa.EncryptPKCS1v15(rand.Reader,pubkey,[]byte(testmsg));
indata,err:=ioutil.ReadFile("myPrvkey");
if(err!=nil){
	fmt.Println(err);
	return;
};
loadKey,err:=x509.ParsePKCS1PrivateKey(indata);
if(err!=nil){
	fmt.Println(err);
	return;
};
decrdata,err:=rsa.DecryptPKCS1v15(rand.Reader,loadKey,cipherdata);
if(err!=nil){
	fmt.Println(err);
	return;
};
fmt.Printf("%s\n",decrdata);
```

### PEM编码

编码与解码：

```go
var content="...";
var block pem.Block;
block.Type="DEMO";
block.Bytes=[]byte(content);
var encodeData=pem.EncodeToMemory(&block);
var decblock,_=pem.Decode(encodeData);
fmt.Printf("%s\n%s\n",decblock.Type,decblock.Bytes);//消息类型、消息正文
```

解码后保留数据：

```go
var pemData=`
-----BEGIN MY NAME------
546L5aSn5bGx
-----END MY NAME------
Hello, Jim`
var msgblock,other=pem.Decode([]byte(pemData));
fmt.Printf("%s\n%s\n%s\n",msgblock.Type,msgblock.Bytes,other);
```

消息头：

```go
var msg="...";
var headers=map[string]string{
	"ver":"1.0",
	"sender":"Jack",
	"copyto":"Tom",
};
block:=pem.Block{
	Type:"EMSG",
	Bytes:[]byte(msg),
	Headers:headers,
};
pem.Encode(os.Stdout,&block);
```

## 接口与结构体

### 结构体

```go
type person struct{
    name string;//首字母为小写的只能在当前包中访问
    age uint8;
    weight,height float32;
    gender uint8;
};
var g=person{
    name:"...",
    //...
};
var pc *person=&person{
    "...",
    //...
};
```

结构体方法：在结构体外部定义

```go
type test struct{
    //...
};
func(o test)doSomething()string{
    test.data=1;
    return "dosomething";
};
```

### 接口的实现

```go
type Locker interface{
	Lock() uint16;
	Unlock(id uint16);
};
type interLocker struct{
	lockID uint16;
};
func(l *interLocker)Lock()uint16{
	l.lockID++;
	return l.lockID;
};
func(l *interLocker)Unlock(id uint16){
	if(id!=l.lockID){
		return;
	};
};
func main(){
	var lk Locker;
	lk=&interLocker{};//interLocker实现了Locker
	id:=lk.Lock();
	lk.Unlock(id);
	return;
};
```

### 空接口

```go
var obj interface{};
obj=12345;
obj="xyz";
//...
```

### 类型嵌套

```go
type base struct{
	code uint;
	line uint64;
	label string;
};
type dev struct{
	base;
	size float32;
	publisher string;
};
var x dev
//一种正确的写法
x.base.code=1001;
x.base.line=1;
x.base.label="F7";
//另一种正确的写法
x.code=1001;
x.line=1;
x.label="F7";
var y=dev{
	base:base{1002,1,"D6"},//或：base{1002,1,"D6"},
	size:0.12,
	publisher:"Dick"
};
```

### 类型断言

```go
var x interface{}=float64(0.00123);
y,ok:=x.(float64);
if(ok){
    fmt.Printf("%T\n",y);//float64
}else{
    //断言失败
};
```

## 数组与切片

### 数组

```go
var f=[5]uint32{18};//第一个值18，后面的默认0
s:=[3]interface{}{"abc",887,'H'};
r:=[...]int32{800,500,1600,2400,900,700};//自动计算长度为6
n:=len(r);
var b=[5][4][3]int32;
```

### 切片

```go
s:=x[2:4];//[2,4)
s3:=a[:];//全部
```

### 追加

```go
var sf=[]float32{0.001,0.0007};
sf=append(sf,0.0008,0.1205);//添加2个元素
```

## 映射与链表

### 映射的初始化

```go
//只有以下方法初始化才能继续添加元素
//法一
var m1=make(map[uint16]string);
//法二
var m2=map[rune]float64{};
//法三
var m3=map[string]uint64{
	"item1":8150,
	//...
};
```

### 映射的枚举

```go
myMap:=map[string]int{
	"task-01":1000,
	//...
};
for key,val:=range myMap{
	fmt.Printf("%s\n%d\n",key,val);
};
```

### 映射的存在性检验

```go
var m=map[string]int{};
xv:=m["c3"];//该值如果不存在，返回默认值0
xv,ok:=m["c3"];
if ok{
    //存在
}else{
    //不存在
};
```

## 字符串

### Fprint

```go
file,err:=os.Create("*.txt");
if(err!=nil){
	fmt.Println(err);
	return;
};
fmt.Fprintln(file,"...");
```

### uint32转字符串

```go
var h uint32=55660;
hs:=strconv.FormatUint(uint64(h),10);
fmt.Println("%s\n",hs);
```

### 特殊格式控制符

```
%t 布尔
%T 对象的类型
%v 默认格式打印值
%+v 对于结构体对象只打印值
%#v 打印出来的是一个有效的Go语言表达式
%#b 带前缀二进制
%#o 带前缀八进制
%#x 带前缀十六进制
%#X 带前缀大写字母十六进制
```

### 参数索引

```go
fmt.Printf("%[2]s:%[1]d",120,"item");
```

### 文件中读入文本

```go
fileName:="data.txt";
var file,err=os.Open(fileName);
if(err!=nil){
	fmt.Println("%v\n",err);
	return;
};
defer file.Close();
err=nil;
var line string;
var lineNo uint;
for{
	_,err=fmt.Fscanln(file,&line);
	lineNo++;
	if(err==io.EOF){
		break;
	};
	fmt.Printf("%-4d%s\n",lineNo,line);
};
```

### Stringer接口

```go
type Stringer interface{
	String() string;
};
type Product struct{
	Pid uint;
	ProdName string;
	ProdDate string;
	ProdColor string
};
func (p Product)String()string{
	return fmt.Sprintf("...");//自定义输出格式
};
var vp=Product{
	Pid:41920014,
	ProdName:"xxx",
	ProdColor:"xxx",
	ProdDate:"...",
};
fmt.Println(vp);//以下三行输出结果相同，均为自定义输出格式
fmt.Println("%v",vp);
fmt.Println("%s",vp);
```

### Join

```go
var s="xx"+"xx";

var strs=[]string{"xxx","xxx",...};
var out=strings.Join(strs,"#");//用#将strs连接起来
```

### Replace

```go
var a="xxx";
var b=strings.Replace(a,"a","b",2);//将字符串a中字符a替换为b，最多替换2次，0次可省略表示不限次数
```

### Split

```go
var res=strings.Split(s,"#");//以#为分隔符切分字符串s，数组保存到res
var res=strings.SplitN(s,"#",2);//同上，只切分为2份
var res=strings.SplitAfter(s,"#");//在#后分割（保留分隔符）
var res=strings.SplitAfterN(s,"#",2);//同上，只切分为2份
```

### HasPrefix、HasSuffix

```go
res:=strings.HasPrefix(s,"st");//字符串s是否以st为前缀，返回bool
res:=strings.HasSuffix(s,"st");//同上，后缀
```

### Index、LastIndex

```go
index1:=strings.Index(text,"xxx");//text中第一次出现xxx的字节位置，找不到-1
index2:=strings.LastIndex(text,"xxx");//同上，最后一次

func runeIndexOf(src string,byteIndex int)int{//真实位置方法
	if(byteIndex<=0){
		return byteIndex;
	};
	theBuffer:=[]byte(src)[:byteIndex];
	str:=string(theBuffer);
	rs:=[]rune(str);
	return len(rs);
};
```

### TrimPrefix、TrimSuffix、TrimSpace、Trim、TrimLeft、TrimRight

```go
var str2=strings.TrimPrefix(str,"ftp://");//去除前缀
var str2=strings.TrimSuffix(str,".xct");//去除后缀
var str2=strings.TrimSpace(str);//去除首尾空格
var str2=strings.Trim(s,"abcd");//当字符串s首尾出现abcd之一任意则删除，直到首尾字符都不为abcd任一字符
var str2=strings.TrimLeft(s,"abcd");//同上，只首
var str2=strings.TrimRight(s,"abcd");//同上，只尾
```

### Repeat

```go
var str2=strings.Repeat(s,3);//字符串s重复3次
```

### ParseInt、ParseUint、ParseFloat

```go
var str="0xB20D8A";
var n,err=strconv.ParseInt(str,0,32);//将字符串str转化为指定进制数字
//这里转化为0进制数表示根据前缀自动判断进制
/*
	其他函数（用法同ParseInt）：
	ParseUint
	ParseFloat


	0 int uint
	8 int8 uint8
	16 int16 uint16
	32 int32 uint32 float32
	64 int64 uint64 float64
*/
if(err!=nil){
	fmt.Println(err);
	return;
};
fmt.Printf("%q-->%v\n",str,int32(n));
```

### ToUpper、ToLower

```go
var y=strings.ToLower(x);
var y=strings.ToUpper(x);
```

### Build

```go
var bd=new(strings.Builder);
bd.WriteString("aaa");
bd.WriteRune('\n');
fmt.Printf("%s\n",bd);
var str=bd.String();
```

## 数学函数

### 常用函数

```go
r1:=math.Abs(x1);//参数float64
r1:=math.Max(x1,x2);//参数浮点数
r1:=math.Min(x1,x2);//参数浮点数
r1:=math.Pi
r1:=math.Sin(r);
r1:=math.Cos(r);
var s,c=math.Sincos(r);
rad:=math.Atan2(y,x);//计算方位角
result:=math.Pow(bs,exp);
result:=math.Pow10(8);
r:=math.Sqrt(n);
r:=math.Cbrt(n);
```

### big

#### 加减操作

```go
var(
	num1="123456789";
	num2="123456789";
);
var bigInt1=new(bit.Int);
var bigInt2=new(bit.Int);
bigInt1.SetString(num1,10);
bigInt2.SetString(num2,10);
var res1=new(big.Int);
res1.Add(bigInt1,bigint2);
var res2=new(bit.Int);
res2.Sub(bigInt1,bigInt2);
fmt.Printf("%d,%d\n",res1,res2);
```

#### 阶乘

```go
var c=new(big.Int);
c.MulRange(1,30);//阶乘，求积范围为[1,30]
```

#### 大浮点数

```go
var strfloat="0.41646416489403";
var bigFloat=new(big.Float);
bigFloat.SetPrec(50);//精度
bigFloat.SetString(strfloat);
fmt.Printf("%.50f\n",bigFloat);
bigRes=new(big.Float);
bigRes.SetPrec(100);
bigRes.Add(bigFa,bigFb);
bigRes.Sub(bigFa,bigFb);
bigRes.Mul(bigFa,bigFb);
bigRes.Quo(bigFa,bigFb);
```

### 随机数

```go
import("math\rand");
n=rand.Float32();
n=rand.Float64();

n=rand.Int();
n=rand.Int31();
n=rand.Int63();
n=rand.Uint32();
n=rand.Uint64();

//以下函数指定范围最大值（不包含）
n=rand.Intn(100);
n=rand.Int31n(100);
n=rand.Int63n(100);

//设置随机数种子
timestamp:=time.Now().Unix();
rand.Seed(timestamp);
```

### 随机全排列

```go
var ints=rand.Perm(5);
for _,v:=range ints{
    fmt.Println(v);
};
```

### 洗牌

```go
var list=[]int{1,2,3,4,5,6,7};
var swap=func(i,j int){
    list[i],list[j]=list[j],list[i];
};
var ln=len(list);
rand.Shuffle(ln,swap);
```

### 随机字节序

```go
var file,err=os.Create("test.data");
if(err!=nil){
    fmt.Prinln(err);
    return;
};
rand.Seed(time.Now().Unix());
buffer:=make([]byte,100);
rand.Read(buffer);
file.Write(buffer);
file.Close();

//读取
fileToRead,err:=os.Open("test.data");
if(err!=nil){
    fmt.Println(err);
    return;
};
readBuf:=make([]byte,16);
for{
    n,err:=fileToRead.Read(readBuf);
    if(err!=io.EOF){
        break;
    };
    fmt.Printf("%x",readBuf[:n]);
};
```
