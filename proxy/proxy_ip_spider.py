# encoding=utf-8

'''
已完成:
	1.访问提供免费代理IP的网站
	2.解析返回内容、抓取代理地址（IP、端口）
	3.验证代理地址有效性
	4.将结果存放在MYSQL数据库中

后续使用：
	将此脚本设置为定时任务，每天早上6点自动更新代理IP
'''

import requests
from bs4 import BeautifulSoup as bs
import pymysql


class MySqlHelper:

    def __init__(self, host, name, pwd, db):
        self.db = pymysql.connect(host, name, pwd, db)

    def __del__(self):
        self.db.close()

    def conn(self, host, name, pwd, db):
        db = pymysql.connect(host, name, pwd, db)

    def show_msg(self):
        if self.db == '':
            print("未连接数据库，不能查看信息")
        else:
            cursor = self.db.cursor()
            cursor.execute("select version()")
            ver = cursor.fetchone()
            cursor.execute('select user()')
            user = cursor.fetchone()
            cursor.execute('select database()')
            database = cursor.fetchone()
            print("database version: %s" % (ver))
            print("current db user: %s" % (user))
            print("current db: %s" % (database))
    '''
	cmd:本次执行的命令，此函数用于插入、更新、删除
	'''

    def execute_no_param(self, cmd):
        cursor = self.db.cursor()
        try:
            cursor.execute(cmd)
            self.db.commit()
        except:
            self.db.rollback()

    def execute_with_param(self, cmd, param):
        cursor = self.db.cursor()
        length = len(param)
        try:
            cursor.execute(cmd, param)
            self.db.commit()
            print('insert succeed')
        except Exception as e:
            self.db.rollback()
            print(repr(e))

    def select_no_param(self, cmd):
        cursor = self.db.cursor()
        try:
            cursor.execute(cmd)
            results = cursor.fetchall()
            print(results)
        except:
            pass

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/601.2.7 (KHTML, like Gecko) Version/9.0.1 Safari/601.2.7"
}

free_proxy = []


def ydl_all_ip():
    urls = []
    url = 'http://www.youdaili.net/'
    r = requests.get(url=url, headers=headers)
    soup = bs(r.text, "html.parser")
    a_s = soup.find(name='div', id='MBC0').find_all(
        name='ul')[1].find_all(name='a')
    for a in a_s:
        proxy_spider(a['href'])
        # urls.append(a['href'])


def proxy_spider(url):
    #url = 'http://www.youdaili.net/Daili/guonei/35311.html'
    r = requests.get(url=url, headers=headers)
    soup = bs(r.text, "html.parser")
    ips = soup.find(name='div', attrs={
                    'class': 'content', }).find_all(name='p')

    proxy_ips = []
    try:
        for ip in ips:
            ipstr = ip.string.split('#')[0]
            sock = ipstr.split('@')[0]
            proxy_ips.append(sock)
    except:
        pass

    for sock in proxy_ips:
        proxy_check_run(proxy_dict=sock)


def proxy_check_start(proxy):
    try:
        url = 'https://www.baidu.com'
        r = requests.get(url=url, proxies=proxy, headers=headers, timeout=6)
        if r.status_code == 200:
            free_proxy.append(proxy)
    except:
        pass


def proxy_check_run(proxy_list=None, proxy_dict=None):
    if proxy_list == None and proxy_dict is not None:
        proxy = {}
        proxy['http'] = proxy_dict
        proxy_check_start(proxy)
    elif proxy_list is not None and proxy_dict is None:
        proxy = {}
        proxy[proxy_list[1].lower()] = proxy_list[0]
        proxy_check_start(proxy)


def xc_proxy_ip():
    proxys = []
    url = 'http://www.xicidaili.com/'
    r = requests.get(url=url, headers=headers)
    soup = bs(r.text, 'html.parser')
    trs = soup.find(name='table', id='ip_list').find_all(name='tr')

    for tr in trs:
        tds = tr.find_all(name='td')
        if len(tds) == 0:
            pass
        else:
            ip = tds[1].string
            port = tds[2].string
            types = tds[5].string

            proxys.append([('%s:%s' % (ip, port)), types])

    for proxy in proxys:
        proxy_check_run(proxy_list=proxy)


def save2db():
    # 连接数据库
    sql = MySqlHelper('host/ip', 'username', 'password', 'database')
    for proxy in free_proxy:
        # 插入数据
        # 在py2中，dict.keys()获得列表；py3中，获得dict_key()对象，需要使用list转换为列表后使用
        keys = list(proxy.keys())
        key = keys[0]
        sock = proxy[key]
        print(key, sock)
        sql.execute_with_param(
            "INSERT INTO proxy_ip(sock, types) VALUES(%s, %s)", (sock, key))


def main():
    xc_proxy_ip()
    ydl_all_ip()

    save2db()

if __name__ == '__main__':
    main()
