---
title: Python-Pandas
date: 2023-10-15 20:47:39
tags: Pandas
mathjax: true
---

# Python-pandas

```python
import pandas
```

## 文件读写通用

```python
folder_name=os.path.dirname(__file__)
file_name=os.path.join(folder_name,'*.txt')
```

## 读写.csv文件

```python
df=pandas.read_csv(file_name,encoding='GBK')
"""
    read_csv常用参数：
    index_col:设置索引，如：
        index_col=0 第1列
        index_col='orderDate'
        index_col=[0,1]
        index_col=['orderDate','itemNo']
    sep或delimiter:二选一
        sep='\t' 设置分隔符
        delimiter='\t' 设置备用界定符
    header:指定第几行为表头，跳过此前数据
        header=3 从第4行为表头开始
"""
print(df)
csv_default=os.path.join(folder_name,'*.csv')
df.to_csv(csv_default) #出现中文乱码
csv_GBK=os.path.join(folder_name,'*.csv')
df.to_csv(csv_GBK,encoding='GBK',index=False)
```

## 读写Excel

```python
df=pandas.read_excel(file_name)
print(df)
df=pandas.read_excel(
    file_name,
    converters={
        '表头1':str,
        '表头2':float,
        ...
    }
)
print(df)
```

### 读取复杂表头Excel

```python
pandas.set_option('display.max_columns',None)
"""
    常用参数：
    display.max_columns/display.min_columns 最多/少显示列数 None无限制
    display.max_colwidth 最大显示列宽 默认50 None无限制
    display.max_rows/display.min_rows 最多/少显示行数 None无限制
    display.precision 浮点精度（小数点后位数） 默认6 38以上不使用科学计数法
"""
df=pandas.read_excel(file_name,sheet_name=1,header=None,usecols='A:P',nrows=7,skiprows=2,names=['新表头1','新表头2',...])
"""
    常用参数（索引从0开始）：
    skiprows=2 跳过前2行
    skiprows=[1,4] 跳过第2行和第5行
    sheet_name=1 读取第2个工作表
    sheet_name='流失率' 读取指定名称工作表
    sheet_name=[0,1] 读取第1~2个工作表，返回字典形式DataFrame，df[0]为第一个工作表
    header=None 默认第一行为表头名称
    header=1 指定第二行为表头名称，重复名称出现.1之类后缀，空值出现Unnamed:2之类
    names=['地区','3月存量','3月流失量'] 设置各列字段名，与列数对应
    usecols='A:B,E:E' 读取A:B和E:E列
    usecols=[0,1,4] 读取第1、2和5列
    nrows=6 读取6行数据，不含跳过的行
"""
df.to_excel(result_file,sheet_name='...',index=False)
"""
	常用参数：
	sheet_name='流失率' 设置工作表名，不指定则自动分配Sheet1
	index=False 不输出索引，表头被重新定义
"""
```

## JSON文件读写

### txt转JSON

```python
folder_name=os.path.dirname(__file__)
file_name=os.path.join(folder_name,'test.txt')
df=pandas.read_csv(file_name,encoding='GBK')
ascii_json=os.path.join(folder_name,'ascii.json')
df.to_json(ascii_json,force_ascii=False) #防中文字符被强制转为Unicode
df_json=pandas.read_json(ascii_json)
print(df_json)
```

