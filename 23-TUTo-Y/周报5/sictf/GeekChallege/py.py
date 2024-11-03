from pwn import *
from itertools import chain

p = remote('yuanshen.life', 34912)

out = b''
start = b'000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'

for i in range(114):
    for n in range(33, 127):
        p.recvuntil(b'>')
        payload = out + bytes(chr(n), 'utf-8') + b'1' * (113 - i)
        p.sendline(payload)
        
        get = p.recvuntil(b'\n')[0:114]
        if(get != start):
            out += bytes(chr(n), 'utf-8')
            start = get
            print('获取的数据:' + str(get))
            print('当前密码为:' + str(out))
            print('')
            break
        
p.interactive()