from pwn import *
import itertools

key = "linesuperkeymysecretkeygivemetheflagasisctfisfun"
key2 = "therustlanguageisfun"

#keyDict = ["line","super","key","my","secret","give","me","the","flag","asis","ctf","is","fun","rust","language","is"]

#superkey:ASIS{be_noughty_step_closer_to_see_the_flag}
#mysecretkey:ASIS{imagine_a_flag_in_a_watermelon_how_can_you_capture_it}
#givemetheflag:ASIS{you_should_try_harder_haha}
#asisctfisfun:ASIS{this_is_fake_flag_haha} (v96 in 83c0 call a970)
#therustlanguageisfun:ASIS{that_is_not_the_real_flag}

#index = 36

out = ""
for index in range(15,20):
	for i in range(len(key2)):
		p = process("./right_or_left")
		p.recvuntil("What's The Secret Key?\n")
		p.sendline(key2[index:i+1])
		resp = p.recv(1024)
		if "ASIS" in resp:
			out += key2[index:i] + ":" + resp
			info(key2[index:i] + ":" + resp)
with open("/root/Desktop/out","wb") as f:
	f.write(out)
	f.close()
