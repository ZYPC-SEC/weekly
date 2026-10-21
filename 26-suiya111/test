# git基础

## 存档

先`cd`进入目的文件夹

把当前目录初始化为一个**git仓库**:

```bash
git init
```

如下:
![[Pasted image 20261020192216.png]]

查看**状态**：

```bash
git status
```

Git仓库分为几个区域:
**1)工作区** 在电脑上的文件,在这里对文件进行修改===>`已修改`
**2)暂存区** 记录文件快照,存放在`.git/index`文件中==>`已暂存`
**3)本地仓库** `.git`目录,保存了所有提交历史(commit)=>`已提交`

流程如下:
工作区=>`git add`=>暂存区=>`git commit`=>本地仓库

设置名字和邮箱：

```bash
git config --global user.name "名字"
git config --global user.email "邮箱"
```

最后是commit，如下：
```bash
git commit -m "这里要说点什么"
```

## 暂存区

查看**暂存区**的内容:
```bash
git diff --staged #查看暂存区内容
git restore --staged #确认后全部取消保存
```

暂存区就是`.git/index`这个文件,记录的是"**下一次提交要包含的文件快照**",而commit提交的就是暂存区的内容

"原子提交"?

提交前可以**预演**和**检查**,有问题就可以回滚

# 回滚

把改动放入暂存区的操作叫做`stage`,即`git add`
已经放入暂存区的改动-->`satges`
还没放入暂存区的改动-->`unstaged`

如果在工作区中有一个文件被修改了:
![[Pasted image 20261020200201.png]]

其中`modified`表示已经**被修改**的文件，但还没用进入暂存区

可以使用`git diff`查看差异：

```bash
git diff
#比较 工作区 和 暂存区
#显示已经修改但还没git add的内容
git diff --staged
#比较 暂存区 和 最新提交
#显示已经git add但是还没git commit的内容
#!这里注意,如果暂存区和HEAD已经一致了,就不会回显
git diff HEAD
#比较 工作区 和 最新提交
```
关系对照如下:
```text
工作区  ──git diff──>  暂存区  ──git diff --staged──>  最新提交(HEAD)
        <──────────────── git diff HEAD ────────────────>
```
只看改了哪些文件(不显示具体内容)
```bash
git diff --stat
git diff --name-only
```
忽略空白字符的差异:
```bash
git diff -w
```

一般输出的内容如下:
```bash
diff --git a/a.txt b/a.txt
index 1234567..89abcde 100644
--- a/a.txt          ← 旧版本
+++ b/a.txt          ← 新版本
@@ -1,3 +1,3 @@       ← 位置：旧文件第1行起3行，新文件第1行起3行
 第一行              ← 前面没符号：未改动
-旧内容              ← 减号：被删除/修改掉的行
+新内容              ← 加号：新增/修改后的行
 第三行
```

如何**回滚**?
```bash
git restore <file> (后面直接追加文件)
```

将**暂存区的所有改动撤销回工作区**,恢复成**最新提交(HEAD)**里的样子
```bash
git restore --staged .
```

将工作区里的所有文件,恢复成暂存区的内容(暂存区为空即为HEAD的内容)
```bash
git restore .
```
注意!这样会将工作区里所有未提交的改动**抹除**,恢复到HEAD版本,同时**没有conmit过的内容无法恢复**.

怎么将已经commit的回档？

`HEAD`是最新提交的`commit`,而`HEAD~1`就是倒数第二个提交的`commit`,以此类推.

```bash
git reset --hard HEAD~1
```
这里`--hard`的意思就是将三个区域的内容**全部回滚**,这里就相当于将最新的commit给删除了
因此在使用前应该先`git status`查看一下

也可以**手动回滚**:
```bash
git revert HEAD
```
进入:
![[Pasted image 20261020213346.png]]
进入vim，直接按`:wq`回车退出
相当于添加了一个新的commit，进行了反向的操作
也就是说，当前commit相较于上个版本做了什么，这个commit就做**反向的相同操作**



同时`git reset`有三种模式

|         | 工作区    | 暂存区    | 提交历史   |
| ------- | ------ | ------ | ------ |
| --hard  | **回滚** | **回滚** | **回滚** |
| --mixed | 保留     | **回滚** | **回滚** |
| --soft  | 保留     | 保留     | **回滚** |

```bash
git show HEAD #查看最新提交的内容
```

# 忽略文件

创建一个`.gitignore`文件,将想要忽略的文件名写在里面
这样原来的文件没有被删除，但是还是要提交的
![[Pasted image 20261020215348.png]]


# 分支与合并

`master`就是一个分支(主)

在类似开发新功能的过程中,最好创建新的分支,等待功能完善后再与主分支合并

`master`和`main`分支一般被默认为是主分支,是比较稳定的.

关系如下：
![[Pasted image 20261021192222.png]]

**创建分支**

```bash
git branch feature/due-date #只是创建一个分支
git switch -c feature/due-date #创建分支的同时切换到那个分支（-c:create）
```
 
**查看分支**

```bash
git branch               #本地分支
git branch -r            #远程分支
git branch -a            #本地+远程

git branch --merged      # 已合并
git branch --no-merged   # 未合并

git branch -v            #查看分支及最后一次提交信息

git branch -vv           #查看分支的跟踪关系
```

**切换分支**

```bash
git switch 分支名
```

在新分支中提交：

![[Pasted image 20261021195254.png]]

返回`master`分支在查看一遍：

![[Pasted image 20261021195332.png]]

可以看到在`new/branch`分支的commit在master中是看不到

**合并分支**

```bash
git merge new/branch1
```

![[Pasted image 20261021195828.png]]

这里的合并分支相当于一个**快进**，即将`master`分支快进到了`new/branch1`这个分支

**注意！！** 像刚才提交了一个commit后，再次提交commit可能会造成**冲突**：
![[Pasted image 20261021200811.png]]
因此git会创建一个新的分支，将两条分支的内容提交为一个新的commit
在冲突解决后，还需要手动提交一次`gti commit`

**删除分支**
```bash
git branch -d 分支名
```
# Rebase

挪动分支，在多人协作是尽量让冲突早点出现，防止后面堆积太多。这就是`Rebase`

```bash
git rebase master 
```

# Stash

除了暂存区和提交历史，还有一个区域叫做`stash`.例如在当前分支改了一半的项目,切换分支时就会提醒是否提交或是放入`stash`(关系如下)

![[Pasted image 20261021202507.png]]

这是切换分支时，原来的改动就不会被覆盖了

如下
```bash
git stash
```
只要是还没有提交的改动,不管在工作区还是暂存区,都会被stash收走

**WIP?==>Work In Progress**

这时在`git status`中就只能看到`clean`了,可以安全地切换分支

重新回到当前分支后,拿回暂存的内容:
```bash
git stash pop
```

# Worktree

一个工作区加上一个暂存区就是一个**worktree**

```bash
git worktree add -b 分支名 文件夹地址（包含文件名） master
```

![[Pasted image 20261021204200.png]]

其中会自动创建一个**新的分支**

查看worktree：
```bash
git worktree list
```

`+`表示分支在其他目录里
      
这里的两个目录用的是同一个提交历史

# ssh

使用`ssh key`来连接本地电脑和`github`,生成两个文件**私钥和公钥)

**生成命令**
```bash
ssh-keygen -t ed25519 -C "2391518106@qq.com"
```
然后是查看**公钥**：
```bash
cat ~/.ssh/id_ed25519.pub
```
复制后到github的设置中找到`ssh and gpg keys`创建一个新的`ssh key`
![[Pasted image 20261021205919.png]]
创建成功

然后是测试一下，连接一下github:

```bash
ssh -T git@github.com
```
成功：
![[Pasted image 20261021210050.png]]

在github上创建一个仓库，在repositories里面new一个

# 上传代码到github仓库中

github给了三条命令，用于将本地仓库提交到github上

```bash
#…or push an existing repository from the command line
git remote add origin https://github.com/suiyaaaaa/test.git
git branch -M master #这里是主分支名，记得统一
git push -u origin master #同上
```
第三行的`-u`就是将本地和github上的两个master绑定在一起

![[Pasted image 20261021211033.png]]

成功！

之后要commit，每次提交到github都需要:
```bash
git push
```

然后是将github上的仓库拉到本地：
![[Pasted image 20261021211716.png]]

复制仓库的地址（ssh），然后再终端中运行：
```bash
git clone git@github.com:suiyaaaaa/test.git 文件夹名
```

![[Pasted image 20261021211855.png]]

成功~
