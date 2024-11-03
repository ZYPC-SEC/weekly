# Solidity-LearnNope

> 本笔记仅代表作者视角的个人见解,所出现任何观点均为所写时的主观见解,不保证其客观正确性

谨以此文,记录我Solidity的学习过程,那是一段充满折磨的痛苦时光

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
    * Storng
    * momery
- 前者是存储在链上
- 后者则是运行时临时起用完即丢

## 函数修改器

定义词:modifier 译:修饰词

类似于函数中的常亮,可以将重复的代码语句集成到一个控制器里,需要时可以直接调用
个人感觉是模块化神器

Example:
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

eample:
```Solidity
contrack Error {
  function testRequire(uint _i) public pure {
    require(_i <= 10, "i > 10(报错语句)");
  }

  funciton testRevert(uint _i) public pure {
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