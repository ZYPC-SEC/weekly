# 运维常用的一些linux的命令学习

## 1.服务与日志

```bash
systemctl status 服务名    #查看当前服务运行状态附带最近日志
sudo systemctl start|stop|restart|reload 服务名
sudo systemctl enable --now 服务名
systemctl --failed
sudo systemctl daemon-reload
```

- `start`：立即运行；`enable`：开机自启，二者不是一回事。
- `restart`：重启；`reload`：尽量不中断地重新加载配置。
- 修改 `.service` 单元文件后通常需要 `daemon-reload`
- `--failed`:**列出当前系统中所有处于“失败”（failed）状态的 systemd 单元（通常是服务）**。

```bash
sudo journalctl -u 服务名 -n 100 --no-pager
sudo journalctl -u 服务名 -f
sudo journalctl --since today
sudo journalctl -p err -b
```

- `-u`：指定服务
- `-f`：实时跟踪
- `-b`：本次启动
- `-p err`：错误级别
- 权限不足时加 `sudo`

`journalctl` 是 **systemd** 体系中用来**查询和查看系统日志**的命令。

`--no-pager`

**禁止分页输出**。默认情况下，`journalctl` 会调用 `less` 等分页器，让你按空格翻页。加上这个参数后，日志会**直接全部打印到终端**并结束，适合在脚本中处理或快速查看。

`--since` 用于**限定 journalctl 只显示在指定时间点之后产生的日志**.

## 2.资源排查

```bash
uptime
free -h
df -h
df -i
du -sh 目录
du -xh --max-depth=1 /var | sort -h
top
ps aux --sort=-%cpu | head
ps aux --sort=-%mem | head
```

- `uptime`

  显示系统**已运行时长**、当前时间、登录用户数，以及 **1/5/15 分钟的平均负载**。负载值可快速判断系统整体压力。

- `free -h`

  查看**内存和交换分区（swap）使用情况**。`-h` 表示以人类可读单位（GB/MB）显示，方便快速看剩余内存。

- `df -h`

  查看**磁盘空间使用率**（按挂载点）。`-h` 同样是人类可读单位，用来判断哪个分区快满了。

- `df -i`

  查看 inode 使用情况。即使磁盘空间还有剩余，如果 inode 耗尽，也无法创建新文件。它和 `df -h` 互补。

- `du -sh 目录`

  统计**指定目录的总占用大小**。`-s` 表示汇总（不展开子目录），`-h` 是人类可读单位。例如 `du -sh /var/log` 看日志目录总大小。

`du -xh --max-depth=1 /var | sort -h`

逐层分析 `/var` 下**各子目录占用大小并排序**：

- `-x`：不跨越文件系统边界（不统计挂载的其他分区）
- `-h`：人类可读单位
- `--max-depth=1`：只显示 `/var` 下一级子目录的汇总，不继续深入
- `| sort -h`：按大小排序（`-h` 让 sort 能正确理解 K/M/G 单位）

`top` ：

**实时动态查看系统资源**：CPU、内存、负载、进程列表等。默认按 CPU 使用率排序，适合交互式观察。

`ps aux --sort=-%cpu | head` ：

**按 CPU 使用率从高到低**列出进程，只取前 10 行（`head` 默认 10 行）。`ps aux` 列出所有进程，`--sort=-%cpu` 表示按 CPU 降序排列。适合快速找出 CPU 消耗大户。

`ps aux --sort=-%mem | head` ：

同上，但**按内存使用率从高到低**排序，快速定位内存占用最高的进程。

## 3.网络排查

```bash
ip -br addr          # 网卡和 IP
ip route             # 默认网关
ss -tulpn            # 监听端口及进程
ss -tn               # TCP 连接
ping -c 4 目标
curl -I URL          # 响应头
curl -v URL          # 完整请求过程
dig +short 域名
dig @8.8.8.8 域名
```

`ip -br addr`：

以**简洁格式（brief）**列出所有网卡的**接口名、状态和 IP 地址**。`-br` 让输出更紧凑，适合快速查看本机有哪些网卡、各自 IP 是多少。相比老旧的 `ifconfig`，这是现代 Linux 推荐方式。

`ip route`

查看**内核路由表**，最重要的是看**默认网关**（default via ...）。用来确认本机流量默认从哪条路由出去。

`ss -tn`

查看**当前已建立的 TCP 连接**（`-t` TCP，`-n` 数字显示）

`curl -I URL`

只请求并显示 **HTTP 响应头**（`-I` 即 HEAD 请求），不下载正文。用来快速检查状态码、服务器类型、缓存策略等。

`curl -v URL`

显示**完整的请求与响应过程**（verbose 详细模式），包括 DNS 解析、TCP 连接、TLS 握手、请求头、响应头等。排查接口或 HTTPS 问题时非常有用。

`dig +short 域名`

查询域名的 **DNS 记录**，`+short` 只输出精简结果（通常就是解析到的 IP），不显示冗长的完整应答。适合快速确认域名解析成什么 IP。

`dig @8.8.8.8 域名`

**指定 DNS 服务器**（这里是 Google 的 8.8.8.8）来查询域名。用来对比本地 DNS 与公共 DNS 的解析结果，判断是否是本地 DNS 配置或缓存问题。

## 4.打包与备份

```bash
tar -czf backup.tar.gz 目录/     创建压缩归档文件
tar -tzf backup.tar.gz   查看归档内容不解压
tar -xzf backup.tar.gz -C /目标目录解压归档到指定目录

rsync -av 源目录/ 目标目录/    同步复制目录
rsync -avn 源目录/ 目标目录/     预演试运行（不做改动）
```

首先分析一个每一个参数的作用

- `tar`：归档工具
- `-c`：create，创建新的归档文件 
- `-z`：用 gzip 压缩
- `-x`：extract，解压
- `-t`：list，列出归档中的文件列表
- `-C /目标目录`：change directory，解压前切换到 `/目标目录`，即把内容释放到该目录
- `-f backup.tar.gz`：指定输出文件名（`-f` 后面必须紧跟文件名）
- `目录/`：要打包的源目录第一句的作用是创建压缩归档文件。 结果：把 `目录/` 打包并 gzip 压缩成 `backup.tar.gz`

- `rsync`：增量同步工具
- `-a`：archive 模式，递归并保留权限、时间、符号链接等属性
- `-v`：verbose，显示详细过程
- `源目录/`：**结尾的斜杠很关键**，表示“源目录里的内容”，而不是目录本身
- `目标目录/`：同步到目标目录
- `-n`：dry-run，只模拟显示“将会做什么”，不真正复制或删除任何文件

## 5. 定时任务 cron

```bash
crontab -l    列出当前的定时任务
crontab -e     编辑当前用户的定时任务
```

```
格式：分 时 日 月 周 命令
```

```bash
示例： 0 3 * * * /usr/local/bin/backup.sh >> /var/log/backup.log 2>&1     尽量写绝对路径
```

## 6. 进程与端口

```bash
ps aux    查看系统所有的进程（BSD分格）
ps -ef     查看系统所有的进程（system v 分格）
pgrep -a 进程名    按照名称查找进程PID

kill PID       向进程发送默认信号（TERM，优雅终止）
kill -9 PID     强制杀死进程
kill -l         列出所有可用信号
```

- `ps`：process status，查看进程
- `a`：显示所有终端上的进程（包括其他用户的）
- `u`：以用户为中心的格式显示（带 USER、%CPU、%MEM 等列）
- `x`：显示没有控制终端的进程（如后台服务）
- `-e`：every，显示所有进程
- `-f`：full，完整格式（带 UID、PID、PPID、C、STIME、TTY、TIME、CMD）

```bash
lsof -p PID  列出指定进程（PID）当前打开的所有文件。
sudo lsof -iTCP:80 -sTCP:LISTEN   找出哪个进程在监听 TCP 80 端口。
sudo lsof +L1
```

- `lsof` 可查看进程打开的文件和占用端口的进程。
- `lsof +L1` 可查找已删除但未释放的文件。
- `-iTCP:80`：筛选出与 TCP 协议、80 端口相关的网络文件。
- `-sTCP:LISTEN`：进一步筛选状态为 `LISTEN`（监听中）的连接

## 7. 用户管理

```bash
id    查看当前用户的身份信息
who    查看当前谁登录在系统上
groups 用户名   查看指定的用户属于哪些组
getent passwd 用户名    查询用户的 passwd 条目
getent group 组名       查询组的 group 条目
last        查看历史登录记录
```

```bash
sudo adduser 用户名   创建新用户（交互式）
sudo usermod -aG sudo 用户名    把用户加入 sudo组（管理员权限）
sudo deluser --remove-home 用户名  删除用户并同时删除其家目录
sudo passwd 用户名   修改指定用户的密码
sudo chage -l 用户名   修改用户名密码的有效期
sudo visudo   安全地编辑 sudoers 配置文件
```

- `-a`：append，追加（**必须配合 `-G` 使用**，否则会覆盖原有附加组）
- `-G sudo`：把用户加入 `sudo` 组
- `visudo`：专门用于编辑 `/etc/sudoers` 的工具

## 8. 磁盘挂载

```bash
lsblk -f    查看设备及其文件的系统信息
sudo blkid  查看块设备的 UUID、LABEL、文件系统类型
df -hT   查看已挂载文件系统的使用情况
findmnt  以树状形式显示挂载关系

sudo mount /dev/sdb1 /mnt/data  挂载分区到指定目录
sudo umount /mnt/data  卸载挂载点
```

- `blkid`：block device identification，识别块设备属性
- `df`：disk free，显示文件系统磁盘空间使用
- `-h`：human-readable，以 K/M/G 显示
- `-T`：显示文件系统类型（Type）
- `mount`：挂载文件系统
- `umount`：卸载文件系统

## 9. 日志分析

主要位置：

- `journalctl`：systemd 系统和服务日志
- `/var/log/`：传统日志目录
- `dmesg`：内核日志
- 日志可能已轮转成 `.gz` 文件

```bash
sudo journalctl -u 服务名 -n 100 --no-pager
sudo journalctl -p err -b
sudo tail -f /var/log/syslog
grep -i "error" 日志文件
zgrep -i "error" 日志文件.gz
sudo dmesg -T
```

大概先学这么多知识，剩下的知识后续进行补充。
