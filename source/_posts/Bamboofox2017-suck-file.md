---
title: Bamboofox2017-suck-file
date: 2018-01-01 18:10:48
tags:
---

## Question

### Binary
[a79cc81251ba4c66ed91ccd01b423598818a76cf](a79cc81251ba4c66ed91ccd01b423598818a76cf)

睇番個file header 似乎係一個zip file
但係似乎pk變左細階 , 所以導致unzip唔到
![](img1.png)

將個header改番做正常zip file之後 , 可以正常解壓縮
![](img2.png)

但係入面又有另一個file , 個header又係錯既
咁既情況之下唯有寫條script自動搞啦

```python
import zipfile
import os
startFile = "a79cc81251ba4c66ed91ccd01b423598818a76cf"

def fixHeader(fileName):
	with open(fileName,"r+b") as f:
		data = f.read()
		f.seek(0)
		f.write("\x50\x4b" + data[2:])
		f.truncate()


def sorted_dir(folder):
    def getmtime(name):
        path = os.path.join(folder, name)
        return os.path.getmtime(path)
    return sorted(os.listdir(folder), key=getmtime, reverse=True)


while True:
	l = sorted_dir("./")
	print l
	fixHeader(l[0])
	zip_ref = zipfile.ZipFile(l[0], 'r')
	zip_ref.extractall("./")
	zip_ref.close()
```

解左100次之後 , 終於有個flag file出左黎
![](img3.png)

### Flag
BAMBOOFOX{Fil3_hE4d3r_15_imp0rtaNt}