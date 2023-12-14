---
title: Python笔记
date: 2023-10-15 20:48:07
tags: Python
mathjax: true
---

# Python笔记

```python
#https://www.runoob.com/python3/python3-os-file-methods.html
#C:\Users\Administrator\AppData\Roaming\Python\Python37\site-packages

# 命令行
# pyinstaller -f -w *.ico *.py #生成.exe，加上-w表示去掉控制台
# pyinstaller --paths 第三方模块路径 -F -w --icon=*.ico *.py
# 资源要放在.exe目录下

#生成.whl:python *.py bdist_wheel
```

```python
print():
print('abc'+abc)
print('abc',end='')
print('abc','def')
print('abc','def',sep=',')
print('asdf'+\
      'asdf')
print('''asdfasdf
asdfasdf
asdf''')

#asdf
"""asdf
asdf
"""

input():
abc=input()

len():
len(abc)

str():
print('abc'+str(1)+'abc')

int():
int('42')
int(1.99)

float():
float('3.14')

type(...)

id(...)

if name=='alice':
    print(...)
else:
    print(...)

if name=='alice':
    print('abc')
elif age<12
    print('abc')

break

continue

for i in range(5):
for i in range(12,16):
for i in range(0,10,2):
for i in range(5,-1,-1):

def abc(a):
    ...

try:
    ...
except ZeroDivisionError:
    ...

TypeError
NameError
SyntaxError
UnboundLocalError
ZeroDivisionError 被0除
KeyboardInterrupt Ctrl-C
IndexError 列表
AttributeError
KeyError 字典

spam=[['cat','bat'],[10,20,30,40,50]]
spam[0] #['cat','bat']
spam=['cat','bat','rat','elephant']
spam[-1] #'elephant'
spam[1:3] #['bat','rat']
spam[0:-1] #['cat','bat','rat']
spam[:2] #['cat','bat']
spam[1:] #['bat','rat','elephant']
spam[:]==spam
len(spam)==4
[1,2,3]+['A','B','C']=[1,2,3,'A','B','C']
del spam[2] #['cat','bat','elephant']
spam.index('cat')==1
spam.append(...)
spam.insert(1,'chicken')
spam.remove('cat')
spam.sort() #ASCII
spam.sort(key=str.lower) #字典序
spam.reverse()
list([...])

tuple((...))

mycat={'size':'fat','color':'gray','disposition':'loud'}
mycat=dict(size='fat',color='gray',disposition='loud')
mycat['size'] #'fat'
list(mycat) #['size','color','disposition']
for v in spam.values():
for k in spam.keys():
for i in spam.items():
for k,v in spam.items():
spam.get('cups',0) #第二个参数表示找不到时返回的参数
spam.setdefault('color','black')

spam="asdf'asdf"
'abc%s asdf%s asdf'%(name,age)
f'asdf{name}asdf{age+1}'
spam=spam.upper()
spam=spam.lower()
spam.isupper()
spam.islower()
spam.isalpha()#字母非空
spam.isalnum()#字母数字非空
spam.isdecimal()#数字非空
spam.isspace()#空格制表符换行符非空
spam.istitle()#大写字母开头 后面都是小写字母数字空格
spam.startswith()
spam.endswith()
'abc'.join(['1','2','3','4'])#1abc2abc3abc4
'1abc2abc3abc4'.split('abc')#['1','2','3','4']
'abcdefghij'.partition('f')#('abcde','f','ghij')
'abcdefghij'.partition('z')#('abcdefghij','','')
'Hello'.ljust/rjust/center(10)
'Hello'.ljust/rjust/center(20,'=')
'   Hello       '.strip/lstrip/rstrip()
ord()
chr()

helloFile=open('...','r',encoding='utf-8') #'r'可省略 其他：写入覆盖'w' 添加'a'
"""
    详细说明：
    文件必须存在：
        r 只读，指针在开头
        rb 二进制只读，指针在开头
        r+ 可读，可从头覆盖
        rb+ 二进制读写，指针在开头
    文件存在则覆盖，不存在则创建：
        w 只写
        wb 二进制只写
        w+ 清空后读写
        wb+ 二进制读写
    文件存在则指针在末尾，否则创建新文件：
        a 追加
        ab 二进制追加
        a+ 读写
        ab+ 二进制追加
"""
"""string""" helloFile.read()
"""list""" helloFile.readlines()#以\n结束
helloFile.write(...)
helloFile.close()

try:
    #...
    raise Exception('...')
except Exception as err:
    print('...'+str(err))

assert ...#boolean表达式 False时引发AssertionError

folder_name=os.path.dirname(__file__) #返回.py文件所在全路径，报错可使用inspect
```

## inspect

```python
import inspect,os
file_name=inspect.getframeinfo(inspect.currentframe()).filename
folder_name=os.path.dirname(os.path.abspath(file_name)) #替代__file__作用
```

## random

```python
import random
from random import *
random.randint(1,10)
random.choice(list)
random.shuffle(list)
"""list""" random.sample(list,k) #选k个
```

## sys

```python
import sys
sys.exit()
if len(sys.argv)<2:
    ... #第一项：字符串包含文件名 第二项：第一个命令行参数
sys.platform
```

## pprint

```python
import pprint
pprint.pprint(dict)
print(pprint.pformat(dict))
abc=[{'a':'1','b':'2'},{'c':'3','d':'4'}]
fileObj=open('abc.py','w')
fileObj.write('abc='+pprint.pformat(abc)+'\n')
fileObj.close()
import abc
abc.abc abc.abc[0] abc.abc[0]['a']
```

## pyperclip

```python
import pyperclip
pyperclip.copy('...')
pyperclip.paste()#...
```

## traceback

```python
"""string""" traceback.format_exc() #异常的回溯信息
```

## zombiedice

```python
import zombiedice
class MyZombie:
    def __init__(self,name):
        self.name=name
    def turn(self,gameState):
        diceRollResults=zombiedice.roll() 
        brains=0
        while diceRollResults is not None:
            brains+=diceRollResults['brains']
            if brains<2:
                diceRollResults=zombiedice.roll()
            else:
                break
"""
    可能的 roll() 返回值：
    {'brains':1,'footsteps':1,'shotgun':1,'rolls':[('yellow','brains'),('red','footsteps'),('green','shotgun')]}
"""
zombies=(
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns',minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotguns',minShotguns=1),
    MyZombie(name='My Zombie Bot')
)
#zombiedice.runWebGui(zombies=zombies,numGames=10) #CLI模式
zombiedice.runTournament(zombies=zombies,numGames=10) #Web GUI模式
```

## re

```python
import re
"""Regex""" phoneNumRegex=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
"""Match""" mo=phoneNumRegex.search('...415-555-4242...')
mo.group(1) #'415'
mo.group(2) #'555-4242'
mo.group(0) mo.group() #'415-555-4242'
mo.groups() #('415','555-4242')
'\. \^ \$ \* \+ \? \{ \} \[ \] \\ \| \( \)'
r'a|b' #a或b
r'a(b|c|d)' #ab|ac|ad
r'a(b)?c' #abc|ac
r'a(b)*c' #b不存在或一次或重复多次
r'a(b)+c' #b一次或存在多次
r'(a){3}' #匹配固定次数
r'(a){3,5}' #匹配3到5次，3、5可不写，贪心：尽可能长
r'(a){3,5}?' #同上，非贪心：尽可能短
"""list""" re.complie('...').findall('...') #[(分组),(分组)]
"""
    /d 数字=[0-9]
    /D 非数字=[^0-9]
    \w 字母=[a-zA-Z]、数字、_（单词）
    \W 非\w
    \s 空格、制表符、换行（空白）
    \S 非\s
"""
r'[a-zA-Z0-9._%+-]'
r'[^...]' #在被查找文本开始处
r'[...$]' #同上，结束处
r'.at' #匹配*at，通配字符：(.*)表示任意文本 除换行，贪心
r'.*?' #非贪心
re.compile('.*',re.DOTALL) #使通配包括换行
"""
    参数：用|连接
    re.DOTALL 使通配字符匹配换行符
    re.IGNORECASE或re.I 不区分大小写
    re.VERBOSE 忽略多行中注释
"""
re.compile(...).sub('替换','被替换')#替换中 /1 /2 /3代替分组1、2、3
```

## pyinputplus

```python
import pyinputplus
pyinputplus.inputStr() #类似input()
pyinputplus.inputNum() #int或float
pyinputplus.inputChoise() #?
pyinputplus.inputMenu() #?
pyinputplus.inputDatetime() #日期时间?
pyinputplus.inputYesNo() #yes或no y或n
pyinputplus.inputBool() #True或False
pyinputplus.inputEmail() #有效E-mail地址
pyinputplus.inputFilepath() #有效文件路径文件名，检查是否存在文件?
pyinputplus.inputPassword() #输入时显示*
response=pyinputplus.inputInt(prompt='...')
response=pyinputplus.inputNum('...',min=...或max=...或greaterThan=...或lessThan=...)
response=pyinputplus.inputNum('...',blank=True) #可选
response=pyinputplus.inputNum('...',limit=...,default='...') #次数 无输入默认
    #异常：pyinputplus.TimeoutException
response=pyinputplus.inputNum('...',timeout=...) #限时
    #异常：pyinputplus.RetryLimitException
response=pyinputplus.inputNum(allowRegexes=[r'...',r'...',...],blockRegexes=[r'...',r'...',...]) #allow允许 block拒绝 允许优先

def addsUpToTen(numbers):
    numbersList=list(numbers)
    for i,digit in enumerage(numbersList):
        numbersList[i]=int(digit)
    if sum(numbersList)!=10:
        raise Exception('...')
    return int(numbers)
response=pyinputplus.inputCustom(addsUpToTen)
```

## time

```python
import time
time.sleep(...)
```

## turtle

```python
import turtle #挖坑待填
```

## os

```python
import os
os.chdir('...') #改变cwd
os.makedirs('...') #需要\\ 可创建必要中间文件夹
os.makedirs('...',exist_ok=true) #已存在不抛出异常
os.rename('重命名前','重命名后')
os.remove('...') #删除文件
a=os.stat('...') #获取属性
"""
    返回对象常用属性：
    a.st_mode 保护模式
    a.st_ino 索引号
    a.st_nlink 硬链接号
    a.st_size 文件大小 单位字节
    a.st_mtime 最后一次修改事件
    a.st_dev 设备名
    a.st_uid 用户ID
    a.st_gid 组ID
    a.st_atime 最后一次访问事件
    a.st_ctime 最后一次状态变化事件（Windows下文件创建时间）
"""
os.path.abspath('...') #相对转绝对
bool os.path.isabs('...')
os.path.relpath(path,start) #start到path的相对路径
string os.path.basename('...')
string os.path.dirname('...')
tuple(dirname,basename)=os.path.split('...')
"""int""" os.path.getsize('...')
"""list""" os.listdir('...')
os.unlink(path)#删path处文件
os.rmdir(path)#删path处空文件夹
os.path.exists('...') #判断目录是否存在，有True 没有False
#遍历文件树
    import os
    for folderName,subfolders,filenames in os.walk('...')
        print('Current folder:'+folderName)
        for subfolder in subfolders:
            print('Subfolder'+subfolder)
        for filename in filenames:
            print('File'+filename)
        print('')
```

## pathlib

```python
import pathlib
# spam/bacon/eggs:
pathlib.Path('spam','bacon','eggs')
pathlib.Path('spam')/'bacon'/'eggs'
pathlib.Path('spam')/pathlib.Path('bacon/eggs')
pathlib.Path.cwd() #当前工作目录
pathlib.Path.home() #主目录 C:\Users
pathlib.Path(r'...').mkdir() #不需要\\ 不可创建多个必要中间文件夹
p=pathlib.Path('...')或pathlib.Path.cwd()等
bool p.is_absolute()
string p.anchor #锚点 
string p.name #文件名
string p.stem #主干名
string p.suffix #后缀名
string p.drive #驱动器 C:
pathlib.Path p.parent #祖先文件夹
p.parents[0] #C:/a/b/c
p.parents[1] #C:/a/b
p.parents[2] #C:/a
p.parents[3] #C:/
list(p.glob('*')) #[WindowsPath('...),...]
    #*.txt project?.docx ?只一个字符
"""bool""" p.exists()#存在
"""bool""" p.is_dir()#存在是文件
"""bool""" p.is_file()#存在是文件夹
"""int""" p.write_text('...') #返回字符数
"""string""" p.read_text()
```

## shelve

```python
import shelve
shelfFile=shelve.open('...')
abc=['a','b','c']
shelfFile['abc']=abc
shelfFile['abc']#['a','b','c']
list(shelfFile.keys())#['abc']
list(shelfFile.values())#[['a','b','c']]
shelfFile.close()
```

## shutil

```python
import shutil #以下方法各层级目录必须已经存在
shutil.copy(source,destination)#把source文件拷贝到destionation目录，若destination为文件名则重命名
shutil.copytree(source,destination)#复制文件夹、子文件夹、文件
shutil.move(source,destination)#移动文件同copy
shutil.rmtree(path)#删除path文件夹、包含的所有文件、文件夹
```

## send2trash

```python
import send2trash
send2trash.send2trash('...')#将文件送到回收站
```

## zipfile

```python
import zipfile
exampleZip=zipfile.ZipFile('...')
exampleZip.namelist()#ZIP中包含所有文件文件夹
spamInfo=exampleZip.getinfo('...')
spamInfo.file_size#原来大小
spamInfo.compress_size#压缩后大小
exampleZip.extractall('...')#参数不填则当前工作目录 不存在则创建
exampleZip.extract('...','...')#解压单个文件 可选：第二个参数指定文件夹 不存在则创建
#新建ZIP并写入文件
    newZip=zipfile.Zipfile('...','w') #添加文件改为'a'
    newZip.write('...',compress_type=zipfile.ZIP_DEFLATED)
exampleZip.close()
```

## logging

```python
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')
logging.basicConfig(filename='...',同上)#写入文件
    #logging.DEBUG表示显示DEBUG级别及以上 例如logging.ERROR只显示ERROR和CRITICAL
logging.disable(logging.CRITICAL)#禁止日志：禁止CRITICAL及更低级别
logging.debug('...')
logging.info('...')
logging.warning('...')
logging.error('...')
logging.critical('...')
```

## webbrowser

```python
import webbrowser
webbrowser.open('http://...') #浏览器打开
```

## requests

```python
import requests
res=requests.get('...')
res.encoding='utf-8' #中文需要
try:
    res.raise_for_status() #连接状态
except Exception as exc:
    print('...:%s'%(exc))
res.status_code==requests.codes.ok #一切都好 200
print(res.text[:250])
playFile=open('*.txt','wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()
```

## bs4

```python
import bs4
#法1
import requests,bs4
res=requests.get('http://...')
res.raise_for_status()
exampleSoup=bs4.BeautifulSoup(res.text,'html.parser')
#法2
exampleFile=open('*.html')
exampleSoup=bs4.BeautifulSoup(exampleFile,'html.parser')

elems=exampleSoup.select('#author') #CSS选择器，找不到返回None
len(elems) #匹配数
str(elems[0]) #'<span id="author">...</span>'
elems[0].getText() #'...'
elems[0].attrs #{'id':'author'}
elems[0].get('id') #'author'
```

## selenium

```python
from selenium import webdriver
browser=webdriver.Firefox()
browser.get('https://...')
browser.back() #返回
browser.forward() #前进
browser.refresh() #刷新
browser.quit() #关闭窗口

elem=browser.find_element_by_class_name(...)
elem=browser.find_element_by_css_selector(...)
elem=browser.find_element_by_id(...)
elem=browser.find_element_by_link_text(...) #完全匹配
elem=browser.find_element_by_partial_link_text(...) #包含提供的
elem=browser.find_element_by_name(...)
elem=browser.find_element_by_tag_name(...) #大小写不敏感
elem=browser.find_elements_by_class_name(...)
elem=browser.find_elements_by_css_selector(...)
elem=browser.find_elements_by_id(...)
elem=browser.find_elements_by_link_text(...)
elem=browser.find_elements_by_partial_link_text(...)
elem=browser.find_elements_by_name(...)
elem=browser.find_elements_by_tag_name(...)

elem.tag_name
elem.get_attribute(...)
elem.text
elem.clear() #清除输入的文本
elem.is_displayed() #可见返回True
elem.is_enabled() #输入元素启用返回True
elem.is_selected() #复选框、单选被勾选返回True
elem.location #dict类型 包含在页面上位置'x' 'y'

elem.click() #模拟鼠标单击
elem.send_keys('...') #提交表单
elem.submit()
from selenium.webdriver.common.keys import Keys
# Keys.DOWN Keys.UP Keys.LEFT Keys.RIGHT
# Keys.ENTER Keys.RETURN Keys.TAB
# Keys.HOME Keys.END
# Keys.PAGE_DOWN Keys.PAGE_UP
# Keys.ESCAPE Keys.BACK_SPACE Keys.DELETE
# Keys.F1,...,Keys.F12
elem.send_keys(Keys.END)
```

## openpyxl

```python
import openpyxl
wb=openpyxl.load_workbook('*.xlsx') #打开.xlsx
"""list""" wb.sheetnames #表单名
sheet=wb['Sheet3']
sheet=wb.active #活动表单
sheet.title='...' #表单名
sheet['A1'].value #单元格值
sheet.cell(row=1,column=2).value
sheet['A1'].row 
sheet['A1'].column
sheet['A1'].coordinate #坐标
sheet.max_row #行数
sheet.max_column #列数
from openpyxl.utils import get_column_letter,column_index_from_string
get_column_letter(1) #'A'
column_index_from_string('A') #1
for rowOfCellObjects in sheet['A1':'C3']:
    for cellObj in rowOfCellObjects:
        print(cellObj.coordinate,cellObj.value)
for cellObj in list(sheet.columns)[1]:
    print(cellObj.value)
wb=openpyxl.Workbook()
wb.create_sheet(index=0,title='...') #创建
del wb['Sheet'] #删除
wb.save('*.xlsx') #保存
from openpyxl.styles import Font
sheet['A1'].font=Font(size=24,italic=True) #修改字体
sheet.row_dimensions[1].height=70 #0~409点 1点=0.35mm 默认12.75
sheet.column_dimensions['B'].width=20 #0~225 默认11点字体大小可显示字符数 默认8.43
sheet.merge_cells('A1:D3')
sheet.unmerge_cells('A1:D3')
sheet.freeze_panes='A2' #A2左、上方行列冻结 填'A1'或None为没有冻结窗格
#图表
refObj=openpyxl.chart.Reference(sheet,min_col=1,min_row=1,max_col=1,max_row=10) #数据源A1:A10
seriesObj=openpyxl.chart.Series(refObj.title='...') #类名
chartObj=openpyxl.chart.BarChart() #还有openpyxl.chart.LineChart() openpyxl.chart.ScatterChart() openpyxl.chart.PieChart()
chartObj.title=' ' #图标名
charObj.append(seriesObj)
sheet.add_chart(chartObj,'C5') #图表左上角定位在C5
```

## PyPDF2

```python
import PyPDF2
pdfFileObj=open('*.pdf','rb')
pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.isEncrypted #布尔 是否已加密
pdfReader.decrypt('***') #密码，错误返回0 未解密时调用getPage()失败，需要重新打开文件
pdfReader.numPages #页数
pageObj=pdfReader.getPage(0)
pageObj.extractText() #获取文字
pdfFileObj.close()
pdfWriter=PyPDF2.PdfFileWriter()
pdfWriter.addPage(pageObj)
pdfWriter.encrypt('***') #保存前加密
pdfOutputFile=open('*.pdf','wb')
pdfWriter.write(pdfOutputFile) #保存
pageObj.rotateClockwise(90) #90 180 270
pageObj.rotateCounterClockwise(90) #90 180 270
pageObj.mergePage(pdfWatermarkReader.getPage(0)) #水印
```

## docx

```python
import docx #python-docx
doc=docx.Document('*.docx')
len(doc.paragraphs) #paragraph数
doc.paragraphs[0].text
len(doc.paragraphs[0].runs) #一个paragraph中的run数
doc.paragraphs[0].runs[0].text
paragraphObj.style='Quote'
runObj.style='QuoteChar'
    #默认样式：
    #Normal、Quote、Intense Quote、List Paragraph、MarcoText、No Spacing、Caption、Subtitle、TOC Heading、Title
    #Body Text ~2
    #Heading 1~9
    #List ~3、List Bullet ~3、List Continue ~3 、List Number ~3
doc.paragraphs[0].runs[0].underline=True #True
    #其他属性：
    #bold italic strike double_strike all_caps shadow outline rtl imprint emboss
doc.paragraphs[0].run[0].add_break(docx.enum.text.WD_BREAK.PAGE) #换页符
paraObj=doc.add_paragraph('文本','标题')
paraObj.add_run('...')
doc.add_heading('...',0) #0~4
doc.add_picture('*.png',width=docx.shared.Inches(1),height=docx.shared.Cm(4)) #添加图像，
doc.save('*.docx')
#Word创建PDF
    import win32com.client
    import docx
    wordFilename='*.docx'
    pdfFilename='*.pdf'
    doc=docx.Document()
    #...
    doc.save(wordFilename)
    wdFormatPDF=17
    wordObj=win32com.client.Dispatch('Word.Application')
    docObj=wordObj.Documents.Open(wordFilename)
    docObj.SaveAs(pdfFilename,FileFormat=wdFormatPDF
    docObj.close()
    wordObj.Quit()
```

## csv

```python
import csv
exampleFile=open('example.csv')
exampleReader=csv.reader(exampleFile)
exampleData=list(exampleReader)
exampleData[row][col]
for row in exampleReader: #只能循环一次，需要再用csv.reader(...)读取一次
    print(str(exampleReader.line_num)+' '+str(row))
outputFile=open('*.csv','w',newline='')
outputWriter=csv.writer(outputFile)
outputWriter=csv.writer(outputFile,delimiter='\t',lineterminator='\n\n') #制表符代替逗号，两倍行距
outputWriter.writerow([...,...])
outputFile.close()
#DictReader DictWriter对象
exampleDictReader=csv.DictReader(exampleFile)
#默认第一行为表头Timestamp Fruit Quantity，如果没有规定表头，可人为设置：
    exampleDictReader=csv.DictReader(exampleFile,['Timestamp','Fruit','Quantity'])
for row in exampleDictReader:
    print(row['Timestamp'],row['Fruit'],row['Quantity'])
outputDictWriter=csv.DictWriter(outputFile,['Name','Pet','Phone'])
outputDictWriter.writeheader() #标题行
outputDictWriter.writerow({'Name':'Alice','Pet':'cat','Phone':'555-1234'})#顺序无所谓，没有可不填
```

## json

```python
import json
stringOfJsonData='...' #JSON数据
jsonDataAsPythonValue=json.loads(stringOfJsonData) #json转dict
stringOfJsonData=json.dumps(pythonValue) #dict转json
```

## time

```python
import time
time.time() #UTC
time.ctime() #人类可读
time.ctime(time.time()) #同上
time.sleep(1) #暂停 单位s
round(time.time(),4) #四舍五入小数点后4位
```

## datetime

```python
import datetime
dt=datetime.datetime.now()
dt=datetime.datetime(2019,10,21,16,29,0) #可比较，晚的大 可加减乘除
dt.year dt.month dt.day dt.hour dt.minute dt.second
dt.strftime('%Y/%m/%d %H:%M:%S')
    # %Y 年份'2014' %y 年份'00'~'99'(1970~2069) %m 月份'01'~'12' %B 月份'November'
    # %b 月份'Nov' %d 一个月中第几天'01'~'31' %j 一年中第几天 '001'~'366' %w 一周中第几天 ‘0’~‘6’ 周日~六
    # %A 周几'Monday' %a 周几 'Mon' %H 小时'00'~'23' %I 小时'01'~'12'
    # %M 分'00'~'59' %S 秒 '00'~'59' %p 'AM'或'PM' %% 字符'%'
dt=datetime.datetime.strptime('October 21,2019','%B %d,%Y')
datetime.datetime.fromtimestamp(1000000) #UNIX纪元时间戳转datetime
delta=datetime.timedelta(days=11,hours=10,minutes=9,second=8) #可加减乘除
delta.days delta.seconds delta.microseconds
delta.total_seconds()
str(delta) #可读
```

## threading

```python
import threading
def takeANap():
    ...
threadObj=threading.Thread(target=takeANap)
treadObj=threading.Thread(target=print,args=['Cats','Dogs','Frogs'],kwargs={'sep':'&'})
threadObj.start()
threadObj.join() #阻塞主线程，完成后继续主线程
```

## subprocess

```python
import subprocess
paintProc=subprocess.Popen('...') #windows用\\分割符 Ubuntu Linux用/
paintProc=subprocess.Popen(['...','参数',...])
paintProc=subprocess.Popen(['start','参数',...],shell=True) #windows下用默认软件打开
paintProc.poll() #正在运行返回None 已终止则返回退出代码
paintProc.wait() #阻塞主程序，终止后返回
```

## pillow

```python
from PIL import ImageColor #pillow
ImageColor.getcolor('red','RGBA') #返回(255,0,0,255)
from PIL import Image
catIm=Image.open('*.png') # *.jpg *.gif *.png
catIm.size #(816,1088)
catIm.filename #'*.png'
catIm.format #'PNG'
catIm.format_description #'Portable network graphics'
catIm.save('*.jpg')
im=Image.new('RGBA',(100,200),'purple') #100px宽 200px高 紫色背景，省略默认不可见黑(0,0,0,0)
croppedIm=catIm.crop((335,345,565,560)) #裁剪
catCopyIm=catIm.copy()
catCopyIm.paste(croppedIm,(400,500))
catCopyIm.paste(croppedIm,(400,500),croppedIm) #跳过透明像素，否则粘贴黑色
svelteIm=catIm.resize((宽,高))
rotateIm=catIm.rotate(90) #逆时针 windows用黑色背景填补 macOS用透明
rotateIm=catIm.rotate(6,expand=True) #扩大图像尺寸
flipIm=catIm.transpose(Image.FLIP_LFET_RIGHT) #镜像翻转
flipIm=catIm.transpose(Image.FLIP_TOP_BOTTOM)
im.getpixel((0,0)) #(0,0,0,0)
im.putpixel((x,y),(210,210,210)) #改单个像素
from PIL import ImageDraw
draw=ImageDraw.Draw(im)
#以下方法fill填充颜色和outline轮廓颜色可选
#   point(xy,fill) 单个像素，xy为[(x,y),(x,y),...]或[x1,y1,x2,y2,...]
#   line(xy,fill,width) 一条线或一系列线，xy为[(x,y),(x,y),...]或[x1,y1,x2,y2,...]，width为线宽
#   rectangle(xy,fill,outline) 矩形，xy为(左上x,左上y,右下x,右下y)
#   ellipse(xy,fill,outline) 椭圆，xy为(左上x,左上y,右下x,右下y)
#   polygon(xy,fill,outline) 多边形，xy为[(x,y),(x,y),...]或[x1,y1,x2,y2,...]
draw.line([(0,0),(199,0),(199,199),(0,199),(0,0)],fill='black')
from PIL import ImageFont
arialFont=ImageFont.truetype(os.path.join(fontsFolder,'arial.ttf'),32) #32点 1点=1/72英寸 PNG默认72px/英寸
draw.text((20,150),'Hello',fill='purple',font=arialFont) #在(20,150)绘制
```



## pyautogui

```python
import pyautogui
#急停：鼠标移向角落，抛出pyautogui.FailSafeException异常
wh=pyautogui.size() #(1920,1080)
pyautogui.moveTo(200,100,duration=0.25) #鼠标移向(200,100) 耗时0.25s pyautogui所有duration都可选
pyautogui.move(100,0,duration=0.25) #鼠标移动(右,下) 可负
    #其他相同用法：
    #pyautogui.dragTo() 鼠标拖动 macOS必须设置duration，否则不对
    #pyautogui.drag()
p=pyautogui.position() #(377,481)
pyautogui.click(100,150,button='left') #xy坐标 其他：middle right
    #其他相同用法：
    #pyautogui.mouseDown()
    #pyautogui.mouseUp()
    #pyautogui.doubleClick()
    #pyautogui.rightClick()
    #pyautogui.middleClick()
pyautogui.click((643,745,70,29))
pyautogui.click('*.png')
pyautogui.scroll(200) #鼠标当前位置向上滚动，单位不统一
pyautogui.mouseInfo()
Im=pyautogui.screenshot() #屏幕快照，pillow用法相同
pyautogui.pixel((50,200)) #rgb颜色 (130,135,144)
pyautogui.pixelMatchesColor(50,200,(255,135,144)) #True
b=pyautogui.locateOnScreen('*.png') #定位*.png出现在屏幕上位置
    #返回(左,上,宽度,高度) 即b.left b.top b.width b.height
    #需要屏幕分辨率保持不变
    #找不到返回None 引发ImageNotFoundException
b=pyautogui.locateAllOnScreen('*.png') #[(643,745,70,29),(1007,801,70,29)]
fw=pyautogui.getActiveWindow() #处于活动状态的窗口
    #fw.left fw.right fw.top fw.bottom 窗口边x y坐标
    #fw.topleft fw.topright fw.bottomleft fw.bottomright (x,y) 窗口角坐标
    #fw.mideleft fw.midright fw.midleft fw.midright (x,y) 窗口边中间
    #fw.width fw.height 窗口维度 单位px
    #fw.size (宽,高) 窗口大小
    #fw.area 窗口面积 单位px
    #fw.center (x,y) 窗口中心坐标
    #fw.centerx fw.centery
    #fw.box (左,上,宽度,高度)
    #fw.title 标题栏文本字符串
    #注意：修改以上值即为操纵窗口！
pyautogui.getAllWindows() #返回屏幕上所有可见窗口list
pyautogui.getWindowsAt(x,y) #返回所有包含点(x,y)的可见窗口list
pyautogui.getWindowsWithTitle(title) #返回所有标题栏包含字符串title的list
pyautogui.getAllTitles() #返回所有可见窗口字符串list
#判断窗口状态：fw.isMaximized fw.isMinimized fw.isActive
#改变窗口状态：
fw.maximize()
fw.minimize()
fw.active()
fw.restore() #撤销最大/小化操作
fw.close() #会跳过窗口退出前对话框等
pyautogui.write('...') #输入
pyautogui.write('...',0.25) #每个字符间暂停0.25s
pyautogui.write(['a','b','left','left','X','Y']) #模拟键盘按键
    #特殊键：
    #enter或return或\n
    #esc shiftleft shiftright altleft altright ctrlleft ctrlright tab或\t backspace delete pageup pagedown home end up down left right f1等
    #volumemute volumedown volumeup pause capslock numlock scrolllock insert printscreen
    #Windows特有：winleft winright
    #macOS特有：command option
pyautogui.keyDown('shift')
pyautogui.keypress('4')
pyautogui.keyUp('shift')
pyautogui.hotkey('ctrl','c')
pyautogui.sleep(3) #暂停3秒，与time.sleep()相同
pyautogui.countdown(10) #倒数十秒并显示
pyautogui.alert('...','标题') #返回'OK'
pyautogui.confirm('...') #返回'OK'或'Cancel'
pyautogui.prompt('...') #返回输入字符串
pyautogui.password('...') #返回输入密码
```

## 查缺补漏

```python
#is运算符：内存地址相同
colors1=['red','yellow','blue']
colors2=['red','yellow','blue'] #colors1==colors2
colors3=colors2 #colors2 is colors3

#函数可变参
def f(*args,**kwargs):
    print(args)
    print(kwargs)
f() #() {}
f(1,2) #(1,2) {}
f(a='a1',b='b1') #() {'a':'a1','b':'b1'}
f(1,2,a='a1',b='b1') #(1,2) {'a':'a1','b':'b1'}

#sorted
print(sorted(1,5,4,2,3));
print(sorted((1,5,4,2,3),reverse=True))

#filter
def divisible_by_24(x):
    if x%24==0:
        return True;
    return False;
l=filter(diviisible_by_24,range(1,101))
print(list(l))

#map
def multiplied_by_2(x):
    return x*2
l=map(multiplied_by_2,range(1,11))
print(list(l))
def multiply(x,y):
    return x*y
l=map(multiply,range(1,11),range(1,11))
print(list(l))#1,4,9,...

#lambda表达式
add2=lambda x,y:x+y
result=add2(1,2)
print(result)
result=(lambda x,y:x+y)(1,2)
print(result)
l=filer(lambda x:x%24==0,range(1,101))
print(list(l))
```

