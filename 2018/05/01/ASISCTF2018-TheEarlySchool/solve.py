from Crypto.Util.number import *

round = 19

def decrypt(round):
	enc = open("FLAG.enc", "rb").read()
	enc = bin(bytes_to_long(enc))[2:]
	dec = ""
	for r in range(round):
		for i in range(0, len(enc), 3):
			dec += enc[i:i+2]
		enc = dec
		dec = ""
	return enc[:-1]

print hex(int(decrypt(round),2))[2:-1].decode('hex')