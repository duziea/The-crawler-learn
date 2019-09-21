import requests


def verify_ip(proxypool):

    print(proxypool)
    url = 'https://icanhazip.com/'

    headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
               'accept-encoding': 'gzip, deflate, br',
               'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
               'cache-control': 'max-age=0',
               'cookie': '__cfduid=de9efa2a6f9fae06c541b573175a219b81568089958',
               'sec-fetch-mode': 'navigate',
               'sec-fetch-site': 'none',
               'sec-fetch-user': '?1',
               'upgrade-insecure-requests': '1',
               'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

    useful_proxypool = []
    for i in proxypool:
        ipaddr = i
        proxies = {'https': ipaddr}
        try:
            response = requests.get(url, proxies=proxies, timeout=3, headers=headers,verify=False)
            if response.status_code == 200:
                useful_proxypool.append(ipaddr)
                print('success: ',ipaddr)
                continue
            else:
                print(response.status_code)
                continue
        except requests.exceptions.ProxyError:
            print('代理服务器无法连接')
            continue
        except requests.exceptions.ConnectTimeout:
            print('useless ip address: ',ipaddr)
            continue

    print(useful_proxypool)
    return useful_proxypool

if __name__ == "__main__":
    proxypool = ['119.130.107.252:3128', '222.89.32.157:9999']
    verify_ip(proxypool)