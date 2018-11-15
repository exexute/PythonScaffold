#! /usr/bin/env python3
# encoding=utf-8

import requests
import queue
import threading
from bs4 import BeautifulSoup
import math
import time


'''
搜索漏洞：	https://www.seebug.org/vuldb/vulnerabilities?page=$1$
查看漏洞：	https://www.seebug.org$/vuldb/ssvid-92793$
兑换POC： 	https://www.seebug.org/vuldb/exchange/$92775$	POST
下载POC：	https://www.seebug.org/vuldb/downloadPoc/$92793$
'''

'''
程序流程：
	访问所有page页，拿到全部的exploit_url
	访问所有的exploit_url -> 兑换POC -> 下载POC

2001 100 => 1->20
'''

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/601.2.7 (KHTML, like Gecko) Version/9.0.1 Safari/601.2.7"
}
s_u = "https://www.seebug.org/vuldb/vulnerabilities?page="
c_u = "https://www.seebug.org"
g_u = "https://www.seebug.org/vuldb/exchange/"
d_u = "https://www.seebug.org/vuldb/downloadPoc/"
thread_counts = 100


class SeBug (threading.Thread):

    def __init__(self, s, l):
        threading.Thread.__init__(self)
        self.s = s
        self.num = l
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/601.2.7 (KHTML, like Gecko) Version/9.0.1 Safari/601.2.7"}

    def run(self):
        self.load_exploit_url()

    def load_exploit_url(self):
        for i in range(self.num):
            url = s_u + str(self.s + i)
            #print('\t' + url)
            self.read_exploit(url)

    def read_exploit(self, url):
        r = requests.get(url=url, headers=self.headers)
        self.bs_exploit(r.text)

    def load_poc(self, exploit_code):
        exploit_url = g_u + exploit_code
        r = requests.get(url=exploit_url, headers=self.headers)
        print(r.status_code)
        # check response and decide whether to download
        # get poc    通过响应的长度判断是否兑换成功

    def bs_exploit(self, html):
        soup = BeautifulSoup(html, "html.parser")
        exploits = soup.find_all(name='a', attrs={'class': 'vul-title', })
        for exploit in exploits:
            # get url
            # load_poc(exploit['href'].split('-')[-1])	课中方法
            self.load_poc(exploit['href'].split('-')[1])
            #print('https://www.seebug.org' + exploit['href'], '\t', exploit['title'])


def load_pagecount():
    r = requests.get(
        url="https://www.seebug.org/vuldb/vulnerabilities", headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    return int(soup.find(name='form', id="J-jump-form").input['max'])


def start_load():
    se_threads = []
    page_count = load_pagecount()
    thread_page_count = math.ceil(page_count / int(thread_counts))
    print(thread_page_count)
    for i in range(thread_counts):
        se_threads.append(SeBug(i * thread_page_count, thread_page_count))
    for thread in se_threads:
        thread.start()
    for thread in se_threads:
        thread.join()


def main():
    start_load()

if __name__ == '__main__':
    main()
