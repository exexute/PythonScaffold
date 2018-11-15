import requests
import json


def get_headers():
    data = {
        'username': 'username',
        'password': 'passwd'
    }
    data = json.dumps(data)

    url = "https://api.zoomeye.org/user/login"
    r = requests.post(url=url, data=data)
    headers = {
        "Authorization": "JWT " + json.loads(r.text)['access_token']
    }
    return headers


def host_search(headers, params):
    url = "https://api.zoomeye.org/host/search" + params
    r = requests.get(url=url, headers=headers)
    if r.status_code == 401:
        headers = get_headers()
        r = requests.get(url=url, headers=headers)
        if r.status_code == 200:
            read_host(json.loads(r.text))
    elif r.status_code == 200:
        read_host(json.loads(r.text))
    else:
        print(r.status_code)


def web_search(headers, params):
    url = "https://api.zoomeye.org/web/search" + params
    r = requests.get(url=url, headers=headers)
    if r.status_code == 401:
        headers = get_headers()
        r = requests.get(url=url, headers=headers)
        read_web(json.loads(r.text))
    elif r.status_code == 200:
        read_web(json.loads(r.text))
    else:
        print(r.status_code)


def read_host(ans):
    for i in range(len(ans['matches'])):
        print(ans['matches'][i]['ip'], ':', ans[
              'matches'][i]['portinfo']['port'])


def read_web(ans):
    for i in range(len(ans['matches'])):
        print("URL:%30s\tIP:%15s" %
              (ans['matches'][i]['site'], ans['matches'][i]['ip'][0]))


def host():
    host_param = input("查询字符串：")
    host_pages = int(input("查询页数(10条/页)："))
    headers = get_headers()
    for i in range(1, host_pages + 1):
        host_search(headers, '?query=' + host_param + '&page=' + str(i))


def web():
    host_param = input("查询字符串：")
    host_pages = int(input("查询页数(10条/页):"))
    headers = get_headers()
    for i in range(1, host_pages + 1):
        web_search(headers, '?query=' + host_param + '&page=' + str(i))


def main():
    print("查询类型：\n\t1 - 主机查询\n\t2 - WEB查询\n\t3 - 结束查询")
    while True:
        types = int(input("\n查询类型:"))
        if types == 1:
            host()
        elif types == 2:
            web()
        elif types == 3:
            break
        else:
            pass

if __name__ == '__main__':
    main()
