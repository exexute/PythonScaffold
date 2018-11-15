# encoding=utf-8

import requests
import json
from bs4 import BeautifulSoup as bs
import urllib
'''
推酷登录分析：
	1.无验证码
	2.需要token
	3.POST
'''
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
}

sr = requests.Session()


def load_token():
    url = "http://www.tuicool.com/login"
    r = requests.get(url=url, headers=header)
    soup = bs(r.text, "html.parser")
    head = soup.head.find(name='meta', attrs={'name': 'csrf-token'})
    return head['content']


def login(token):
    uname = input("input your e-mail:")
    pwd = input("input your pwd:")
    url = 'http://www.tuicool.com/login'
    data = "utf8=%E2%9C%93&authenticity_token=" + token + \
        "&email=" + uname + "&password=" + pwd + "&remember=1"

    r = sr.post(url=url, headers=header, data=data, allow_redirects=False)
    anslen = len(r.content)
    if anslen == 9138:
        print("login failed")
    elif anslen == 95:
        print("login succeed")


def showinfo():
    url = "http://www.tuicool.com/settings/info"
    r = sr.get(url)
    print(r.text)


def main():
    token = load_token()
    login(token)
    showinfo()  # 这这里可以放上自己想要阅读的内容

if __name__ == '__main__':
    main()
