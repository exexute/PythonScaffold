#encoding=utf-8

import os
import shutil
from optparse import OptionParser

#获得当前目录
pwd = os.getcwd()
#拼接得到目标目录
distpwd = pwd + "\..\lession_two"

def checkdir(dist):
	#判断目标文件是否存在
	if os.path.exists(dist):
		return True
	else:
		#创建目标目录，然后复制
		os.makedirs(dist)
		return True

def solvedir(path, dist):
	dirs = os.listdir(path)
	
	for dira in dirs:
		fullpath = path + "\\" + dira
		if not os.path.isdir(fullpath) and not os.path.isfile(fullpath):
			print(fullpath + " is not a file or directory")
		elif os.path.isfile(fullpath):
			shutil.copy2(fullpath, dist)
			print("200 OK \tcopy \"" + fullpath + "\" to \"" + dist + "\" succeed")
		elif os.path.isdir(fullpath):
			newdist = dist + "\\" + dira
			checkdir(newdist)
			solvedir(fullpath, newdist)

def solvefile(src, dist):
	shutil.copy2(src, dist)
	print("200 OK \tcopy \"" + src + "\" to \"" + dist + "\" succeed")

def start_copy(src, dist):
	if os.path.isdir(src):
		solvedir(src, dist)
	elif os.path.isfile(src):
		solvefile(src, dist)
	else:
		print("src的值不正确")

def copyfromsrc2dist(src, dist):
	start_copy(src, dist)

def copyfromsrc(src):
	pwd = os.getcwd()
	start_copy(src, pwd)

def main():
	usage = "usage: %prog -s [src] -d [dist]"
	version = "%prog version V1.1.0"
	parser = OptionParser(usage = usage, version = version)
	parser.add_option("-s", "--src", dest = "src", help = "specify the file or directory want to copy")
	parser.add_option("-d", "--dist", dest = "dist", help = "specify the the file or directory that you want to put")
	(options, args) = parser.parse_args()

	if options.src and options.dist:
		src = options.src
		dist = options.dist
		copyfromsrc2dist(src, dist)
	elif options.src is None and options.dist is None:
		print(parser.usage)
	elif options.src:
		src = options.src
		copyfromsrc(src)

if __name__ == "__main__":
	main()
