---
title: Rust语言基础
date: 2023-11-11 13:34:01
tags: Rust
mathjax: true
---

# Rust语言基础

## 命令行

### 输出

```rust
fn main(){
    let a=12;
    println!("a is {0}, a again is {0}",a);
    println!("{{}}");//输出大括号
}
```

### 详细输出

```rust
#[derive(Debug)]
struct Rectangle{
    width:u32,
    height:u32,
}
fn main(){
    let rect1=Rectangle{width:30,height:50};
    println!("rect1 is {:?}",rect1);//替换为{:#?}时输出带格式的输出
}
```

### 命令行输入

```rust
use std::io::stdin;
fn main(){
    let mut str_buf=String::new();
    stdin().read_line(&mut str_buff).unwrap();
    printfln!("{}",str_buf);
}
```

## 基础语法

### 变量

```rust
let a=123;//不可变变量
let a:i32=123;
let mut a=123;//可变变量

//可以声明后赋初始值
let a;
a=456;

//重影机制
let x=5;
let x=x+1;
let x=x*2;
```

### 静态变量

```rust
static a:i32=123;
fn main(){
    println!("{}",a);
}
```

直接修改静态变量的值：

```rust
static mut VAR:i32=123;
fn main(){
    unsafe{
        VAR=456;
        println!("{}",VAR);
    }
}
```

## 数据类型

### 整数型 浮点型 布尔型 字符型

```rust
i8 u8
i16 u16
i32 u32
i64 u64
i128 u128
isize usize

f64 f32

bool

char
```

### 字符串

String

```rust
let string=String::from("Some string");
//追加
let mut string=String::from("");
string.push('A');
string.push_str("QWER");
//长度
String::from("Hello你好").len();//11 字符编码UTF-8 一个中文字符3
//比较
let a=String::from("...");
let b=String::from("...");
let result=a.eq(&b);//true
String::from("...").eq("...");
String::from("...").eq(String::from("...").as_str());
//截取
let s:String=String::from("RUNOOB");
let ch:char=s.chars().nth(2).unwrap();//N
let sub:&str=&s[0..3];//RUN
```

其实&str比String好使：

```rust
fn main(){
    let s:&str="RUNOOB";
    println!("{}{}{}{}",s.len(),s.eq("RUNOOB"),s.chars().nth(2).unwarp(),&s[0..3]);
}
```

### 元组

```rust
let tup=(500,6.4,1);
let tup:(i32,f64,i32)=(500,6.4,1);

fn main(){
    let tup:(i32,f64,i32)=(500,6.4,1);
    println!("{}",tup.0);
    let (x,y,z)=tup;
    println!("{}",x);
}
```

### 数组

```rust
let a=[1,2,3,4,5];
let length=a.len();
let b=["January","Febrary","March"];
let c:[i32;5]=[1,2,3,4,5];
let d=[3;5];//d=[3,3,3,3,3];
let first=a[0];
let mut a=[1,2,3,4,5]
a[0]=0;
```

## 函数

### 声明

```rust
fn addition(a:i32,b:i32)->i32{
    return a+b;
}
fn main(){
    let sum=addition(100,23);
    println!("{}",sum);
}
```

### 函数表达式

```rust
fn main(){
    let x=4;
    let y={
        let a=x*x*x;
        let b=2*x*x;
        a+b+3
    };
    println!("{}",y);
}
```

### 函数对象

```rust
fn function_one(){
    println!("Funtion1");
}
fn function_two(){
    println!("Function2");
}
fn main(){
    let mut fun:fn();
    fun=function_one;
    fun();
    fun=function_two;
    fun();
}
```

### 闭包/Lambda表达式/匿名函数

```rust
fn main(){
    let fun=|x:i32|->i32{
        return x+1;
    };
    println!("{}",fun(1));
}
```

## 条件语句

### if-else

```rust
fn main(){
    let number=3;
    if number<5 {//必须为bool型，否则违法
        println!("{}",number);
    }else{
        println!("{}",number);
    }
}

fn main(){
    let score=100;
    if score>90 {
        println!("...");
    }else if score>60{
        println!("...");
    }
}
```

### 三元运算符

```rust
fn main(){
    let a=3;
    let number=if a>0 {!} else {-1};
}

fn main(){
    let score=86;
    let branch=if score>90{
        "..."
    }else if score>80{
        ",,,"
    }else{
        "..."
    };
}
```

### match

```rust
fn main(){
    let op=1;
    match op{
        0=>{
            println!("op=0");
        },
        1|2|3|4|5=>{
            println!("...");
        },
        _=>{
            println!("default");
        }
    }
}
```

## 循环结构

### while

```rust
fn main(){
    let mut number=1;
    while number<4{
        number+=1;
    }
}
```

### for

```rust
fn main(){
    for i in 1..5{
        println!("{}",i);
    }
}

fn main(){
    let a=[10,20,30,40,50];
    for i in a.iter(){
        println!("{}",i);
    }
}

fn main(){
    let a=[10,20,30,40,50];
    for i in 0..a.len(){
        println!("a[{}]={}",i,a[i]);
    }
}
```

### loop

```rust
fn main(){
    let s=['R','U','N','O','O','B'];
    let mut i=0;
    loop{
        let ch=s[i];
        if ch=='O'{
            break;//loop内没有break时不会通过编译
        }
        print!("{}",ch);
        i+=1;
    }
}
fn main(){
    let s=['R','U','N','O','O','B'];
    let mut i=0;
    let location=loop{//唯一支持函数表达式的循环
        let ch=s[i];
        if ch=='O'{
            break i;//返回下标
        }
        i+=1;
    };
    println!("{}",location);
}
```

