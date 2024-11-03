# Solidity-LearnNotes

> 本笔记仅代表作者视角的个人见解,所出现任何观点均为所写时的主观见解,不保证其客观正确性

教材:
1. [Bilibili:崔棉大师玩转Web3]https://www.bilibili.com/video/BV1oZ4y1B7WS
2. WTFsolidity基础入门

***谨以此文,记录我Solidity的学习过程,那是一段充满折磨的痛苦时光***

## 变量

Solidity里的变量有些奇特,我个人认为他偏向C一些,因为他的整型变量是有不同大小的,如int8,对应了C里的char,int(int256)对应了C里的int,而不像python那样定了就走

- int(int8/int16/int32/int64/int128/int256) 约等于C语言中的int
- uint(uint8/uint16/uint32/uint64/uint128/uint256) 约等于C语言中的un.. int,只有正数
- byte
- address 地址变量,智能合约的特有变量,可以用来存储地址,用来交易,调用合约

Solidity 中含有三种变量类型

- 状态变量,在合约中定义,可以被函数 更改/读取
- 局部变量,在函数中定义
- 全局变量,不定义也有的变量

## 函数

Solidity里的函数感觉比C和Python都要抽象复杂不少
```Solidity
    function add (int a, int b) external pure returns (int){
        int sult = a + b;
        return sult;
    }
```
如这样一个举例代码 **↑**
function 是定义函数用的,如C中的int和Python中的def
add 是函数名
括号里是喜闻乐见的参数类型
external 就有些抽象了,他的中文意思是外部的,意思是该函数只能从外部访问???
pure 中文意思 纯 ,代表该函数不对区块链上的函数进行读写,也就是说你每次调用函数都得自己传入参数
  view 代表仅读取链上函数但不修改
  defult 可读可改
returns 就比较有意思了,他提前规定了返回的数据类型,但我个人不是很懂这个有什么用

## 变量的储存位置

- 变量存储的位置有两种
  * storage
  * momery
- 前者是存储在链上
- 后者则是运行时临时起用完即丢

当 storage 赋值给 storage 时,两者之间是引用关系,修改一个**会影响**另一个
当 storage 赋值给 memory 时,两者间为副本关系,修改一个**不会影响**另一个(memory赋值给storage同理)
当 memory 赋值给 memory 时

## 函数修改器

定义词:modifier 译:修饰词

类似于函数中的常亮,可以将重复的代码语句集成到一个控制器里,需要时可以直接调用
个人感觉是模块化神器

```Solidity
modifier [Name](unit x,xxxx){
    // code 需要重复执行的语句
    _;// 不同于函数修改器的语句
    // code 需要重复执行的语句
}
```


## 报错语句

Solidity共有三种报错语句

- Require 判断某个条件是否成立,如果不成立,输出报错语句
- revert 需要If语句作前置启动,直接输出报错语句
- assert 判断一个变量是否等于一个设定值,如果不等于则报错

```Solidity
contrack Error {
  function testRequire(uint _i) public pure {
    require(_i <= 10, "i > 10(报错语句)");
  }

  function testRevert(uint _i) public pure {
    if (_i > 10) {
      revert("i > 10 (报错语句)");
    }
  }

  uint public num = 123;

  function testAssert() public view {
    assert(num == 123);
  }
}
```
<!-- ![alt text](报错.png) -->

* 自定义报错语句
* 可以节约 Gas

```Solidity
error Myerror(address caller,...)
if(i > 10){
  revert Myerror(msg.sender,...);
}
```


## 构造函数
> 一次性函数

一种特殊的函数,仅在合约部署时执行一次

定义关键字:construckor

## 函数返回值的使用

可以用一行语句给多个变量赋值函数的返回值
```Solidity
(uint x,uint y,uint z) = TestFuc()
```
如返回值不全需要,可以仅赋值部分以节省GAS,仅需将不需要的变量空掉即可,但应保留 ',' 让合约知道应该给他赋第几个值
```Solidity
(uint x,,uint z) = TestFuc()
```

## 数组 `24/03/17`

Solidity有**定长**和**不定长**两种数组
```Solidity
uint[] public num;  // 定义个一个不定长数组

uint[3] public num2;// 定义一个长度固定为 3 的数组
```

定长数组可以随时通过pop/push来弹出/压入数字,也就是可以随时减少/增加数组长度,但是只能弹出/压入最后的数字
不定长数组则无法通过pop/push来弹出/压入数字
```Solidity
uint[] public num = [1,2,3];  // 定义个一个不定长数组

function pushtest{
  num.push(4);  // 向 num 数组中压入 4 ,使其由[1,2,3] >> [1,2,3,4]
}

function poptest{
  num.pop();  // 将 num 数组的最后一个数字弹出,使其由[1,2,3] >> [1,2]
}

uint len = num.length;  // 获取 num 数组的长度并赋值给 len
```

可以用用 delete 删除数组索引对应数,将其重置为默认值 (0)
delete 不会改变数组长度,仅会重置数据
```Solidity
uint[] public num = [1,2,3];
delete num[2]; // [1,2,3] >> [1,2,0]
```

## 映射 `24/03/19`

定义关键字:mapping

这应该类似于 python 中的字典

可以将两个值关联起来,而且可以多层嵌套
```Solidity
mapping (string => uint) public [Name];
Name[Luotianyi] = 120712; // 将映射表中 Luotianyi 的值设置为 120712
```

多层嵌套映射:
```Solidity
mapping(string =>mapping(string => uint)) public VJIA;

VJIA[Vocaloid][Luotianyi] = 120712;
VJIA[Vocaloid][Yuezengling] = 150412;
VJIA[Vocaloid][Yanhe] = 130711;

VJIA[SV][Xingchen] = 160812;
```

## 迭代映射 `24/03/19`

通过 **数组 & 映射** 结合
据说是可以`遍历映射`(但我不知道有什么具体作用)

抄课程的示例代码: 
```Solidity
mapping(address => uint) public balances;
mapping(address => bool) public inserted;
address[] public keys;

function set(address _key, uint _val) external {
  balances[_key] = _val;

// 判断传入的地址是否已经在数组里,如果不在,创造一个
  if(!inserted){
    inserted[_key] = true;
    keys.push[_key];
  }
}

// 查看数组的长度
function getSize() external view returns (uint) {
  return keys.length;
}

// 查看数组中第一个地址的余额
function first() external view returns (uint) {
  return balances[keys[0]];
}

// 查看数组中最后一个地址的余额
function last() external view returns (uint) {
  return balances[keys[keys.length - 1]];
}

// 查看数组中第 I 个地址的余额
function get(uint _i) external view returns (uint) {
  return balances[keys[_i]];
}
```

## 结构体 `24/03/19`

和其他语言的结构体基本一样,不再赘述
```Solidity

struct VSinger{
  string Name;
  uint BirthDay;
  string Coclor;
  string engine;
}


// 定义一个叫 vsinger 的 VSinger 结构体
VSinger public vsinger;

// 定义一个 Vsinger 结构体数组
VSinger[] public VSingers;

function STRUCTest() external{
  // 第一种定义方式
  VSinger memory Luotianyi = VSinger("LuoTianyi",120712,"66CCFF","VOCALOID");

  // 第二种定义方式 因为加入了各参数的名字,所以可以乱序输入
  VSinger memory Yuezhengling = VSinger({engine:"VOCALOID",BirthDay:150412,Name:"YuezhengLing",Coclor:"EE0000"});

  // 第三种定义方式,可以先定义再给各个参数逐一赋值
  VSinger memory Miku;
  Miku.Name = "MIKU";
  Miku.Coclor = "39C5BB";
  Miku.BirthDay = 20070831;
  Miku.engine = "VOCALOID";

  // 将赋值完的结构体变量压入结构体数组
  VSingers.push(Luotianyi);
  VSingers.push(Yuezhengling);
  VSingers.push(Miku);

  // 第四种定义方式
  VSingers.push(VSinger("XingChen",160812,"9999FF","SV"));

  // 可以通过定义 Storage 创造引用来修改结构体数组中结构体变量的参数
  VSinger storage _Vsinger = VSingers[3];
  _Vsinger.Coclor = "FFFF00";
}

function Delete() external {
  // 可以通过 delete 来删除结构体数组中结构体变量的参数值
  VSinger storage Vsinger2 = VSingers[2];
  // 让初音未来消失
  delete Vsinger2.Name;
}
```




## 枚举 `24/03/20`

一个很神奇的玩意

因为不管是WTF的读物还是崔棉老师的课我都没咋听懂
就感觉听着有些懵,勉强就目前的理解用自己的话总结一下
众所周知: Bool 值有 Ture 和 Flase 两种,如事有对错,人分善恶,道分阴阳
但世界不是二极管,常用数字也不是只有0和1,所以一件事可以有多种状态,人能作恶也能为善,道自阴阳生四相,四相又衍生八卦,所以一个事物也呢有多种状态
如我们网购一件商品,有已下单,已付款,未发货,已发货,运输中,待签收,已签收等数个状态,这是仅有01的Bool值就远远不够用的了,所以我们需要更多的状态的可能性,而枚举就可以实现这一点

```Solidity
// 定义枚举类型
enum Status{
  None,
  Pending,
  Shipped,
  Completed,
  Rejected,
  Canceled
}

// 用Status类型定义一个变量
Status public status;

// 结构体联动枚举
struct Order {
  address buyer;
  Status status;
}

Order[] public orders;

// 查询状态
function get() view external returns(Status) {
  return status;
}

// 根据输入设置状态
function set(Status _status) external {
  status = _status;
}

// 设置状态为 Shipped
function ship() external {
  status = Status.Shipped;
}

// delete 可以将状态重置为默认值(即第一个值)
function reset() external {
  delete status;
}
```

## 