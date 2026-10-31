# 2026-10-26 第一周周报（10.19 - 10.26）

## 本周总结

主线是 Pwn 的栈溢出入门，从 `ret2win` 到 `ret2shellcode` 打通了完整链路：自己算偏移、自己拼 payload、自己接 shell。围绕这条线顺手把 UPX 脱壳和 XTEA 逆向也啃了一遍，最后把四类题型（ret2win / ret2shellcode / XTEA / UPX）写成了可复用的自动解算脚本 `autopwn`。本周还第一次走完 GitHub 的 fork → 分支 → PR 流程。

### 学咗乜嘢

- **Pwn / 栈溢出基础**：`leave` 本质是 `mov rsp, rbp; pop rbp`，所以覆盖顺序是 `buf` → `saved rbp` → 返回地址，第三格才是控制点；64 位跳 `system` 前要 16 字节栈对齐，缺一个 `ret` gadget 就会崩。
- **Pwn / ret2win**：`offset = 缓冲区大小 + RBP = 72`，返址填后门函数绝对地址（`0x00401156`），前面垫一个纯净 `ret`（`0x0040119e`）做对齐跳板。
- **Pwn / ret2shellcode**：需要栈可执行（`execstack`）或落到 W+X 段；payload = `shellcode + 填充(offset-23) + ret_gadget + shellcode_addr`，本周这题的 `offset=136`、shellcode 落在 `0x7fffffffdd40`。
- **Reverse / UPX 脱壳**：`upx -d` 直接脱，脱完重新看导入表和字符串，壳内字符串是压缩的、脱壳后才可读。
- **Reverse / XTEA**：从二进制里扒 TEA/XTEA/XXTEA 的 delta 常量（`0x9E3779B9` 一类）定位算法，再爆破轮数与密钥排布，Python 重写解密比动态调试快得多。
- **工程化**：把重复劳动抽成 `autopwn`（四个 solver + 一个调度器 + 共享支撑库），按真实二进制判定，不靠题名猜、不硬编码偏移。
- **Git 协作**：fork → `git checkout -b` → commit → push → PR 的完整闭环，以及 blobless clone（`--filter=blob:none`）在图片多的仓库里能省掉 90% 的下载时间。

### 下周待做事项

- 把 `ret2libc` 补上：泄露 libc 基址 → 算 `system` / `/bin/sh` 偏移 → 二次溢出，完成标准是本地靶机稳定拿 shell。
- 学 `one_gadget` 与 `__libc_csu_init` 的通用 gadget 用法，并写进 `autopwn` 作为第五个 solver。
- 给 `autopwn` 加一层：遇到非 Pwn 题型（Misc 隐写、简单 Crypto）能识别并提示路由，而不是直接报错。
- 补完 `格式化字符串` 的基础（任意地址读写），至少能解一道本地题。

### 知识分享

#### ret2shellcode 里两个最容易踩的坑

**坑一：`saved rbp` 不能填 `p64(0)`。** 看着无害，实测会直接失败；填 8 字节垃圾（`b"A"*8`）反而正常。原因是函数返回时 `leave` 已经把 `rbp` 弹走，后面若还有二次 `leave`/栈帧操作，`rbp` 为 0 会让 `mov rsp, rbp` 直接把栈顶搬到 0 附近，进程当场 `SIGSEGV`。

**坑二：gadget 必须来自可执行段。** 符号表里挂着 `g_pop_rdi`，字节确实是 `5f c3`，但定义在 `.data`（RW，不可执行），跳过去就是 `SIGSEGV`。用 `readelf -lW` 按 `PF_X` 过滤后再找 gadget，别信符号表给的名字。

验证偏移的最小流程：

```python
from pwn import *
context(arch='amd64', os='linux', log_level='debug')

shellcode = asm(shellcraft.sh())      # 或手写 23 字节 execve("/bin/sh")
offset    = 136                        # 缓冲区 + saved rbp
ret_gadget = 0x40119e                  # 纯净 ret，负责 16 字节栈对齐
buf_addr   = 0x7fffffffdd40            # shellcode 落点，需先确认栈可执行

payload = flat(shellcode, b"A" * (offset - len(shellcode)), ret_gadget, buf_addr)
```

调试三件套：`log_level='debug'` 看收发字节、`gdb.attach(p)` 断在 `ret` 看栈、`checksec` 先确认 `NX` / `PIE` / `Canary` 状态——`NX enabled` 的题就别往栈上写 shellcode 了。

### 情感、思考、观点

这周的进度基本是"卡住 → 记一条 txt → 过两天再看懂了"堆出来的。`pwn/` 目录里躺着 `偏移量看[],不行就加减8.txt`、`exp的那个脚本偏移放进去前要先[]+8.txt` 这种文件名——现在看着挺好笑，但当时确实是靠一次次 `+8` 试出来的，说明我对栈帧布局还是"能算但不算信"。

自动化那块反而顺手。把四类题的判定逻辑写成脚本之后，回看题目能立刻说出"这题靠什么特征识别、偏移从哪来"，比单纯做一题收获大。所以下周想继续这个思路：先写判定，再做解题。

另外 GitHub 流程第一次走通，感觉最麻烦的不是 git 命令，而是环境：证书吊销检查、代理、凭证 helper 这类和题目无关的东西能耗掉一晚上。已经记在笔记里了，下次直接抄。

---

## 本周题目记录

| 题目 | 方向 | 状态 | 关键思路 |
| --- | --- | --- | --- |
| ret2win | Pwn | 已解 | `offset=72`，返址跳后门函数 `0x401156`，`ret` 对齐 |
| ret2shellcode | Pwn | 已解 | 栈可执行，`offset=136`，payload 返址栈上 shellcode |
| upx 加壳题 | Reverse | 已解 | `upx -d` 脱壳后看字符串/导入表 |
| XTEA 加密题 | Reverse | 已解 | 扒 delta 常量定位算法，Python 重写解密 |

## 本周产出

- `autopwn/`：`01_ret2win.py`、`02_ret2shellcode.py`、`03_xtea.py`、`04_upx.py` + `run_all.sh` 调度，退出码约定 `0` 取到 flag / `2` 跑通未取到 / `1` 异常 / `3` 环境缺失。
- `lab_tools/`：靶机课程构建与调试脚本（`build_all.sh`、`ctf-tools.sh`、`dbg_*.sh`）。
- 本仓库：`26-ZD-l2/Week-01.md`（本文件），通过 PR 提交。

## 参考

- pwntools 文档：https://docs.pwntools.com/
- CTF Wiki · 栈溢出：https://ctf-wiki.org/pwn/linux/user-mode/stackoverflow/x86/stackoverflow-basic/
- UPX 官方：https://upx.github.io/
