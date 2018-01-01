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