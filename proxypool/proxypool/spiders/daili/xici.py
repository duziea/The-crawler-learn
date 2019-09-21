
import requests
import random
from bs4 import BeautifulSoup


def get_xici():
    url = 'https://www.xicidaili.com/wn/'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': '_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWI1YzdlZmM1OThhNDQ5NDFmMTY5ODEzMjU0ZmZlMmY2BjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMVUzaHZmVGZ2R0R0cFJVaVMrNHV4YmVIdEY3THloMkZHTzRTSEZWOUtVQTA9BjsARg%3D%3D--4c9773e68361acf60358bba96f96a69386d8b8f5; Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1568078831,1568093800; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1568093839',
        'Host': 'www.xicidaili.com',
        'If-None-Match': 'W/"7fc23bf2b41a390329a0611a6438735b"',
        'Referer': 'https://www.xicidaili.com/wn/3',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    }

    i = random.randint(1, 1)
    url1 = url + str(i)
    print(url1)

    response = requests.get(url1, headers=headers)

    print(response)
    soup = BeautifulSoup(response.text, 'lxml')

    soup1 = soup.table
    soup1 = soup1.find_all('tr')

    proxypool = []
    for i in range(1, 100):
        item = soup1[i]
        tds = item.select('td')
        ip = tds[1].get_text()
        port = tds[2].get_text()
        # addr = tds[3].a.get_text()
        # anonymous = tds[4].get_text()
        # schema = tds[5].get_text()
        # speed = tds[6].div['title']
        # connect_time = tds[7].div['title']
        # survive_time = tds[8].get_text()
        # verify_time = tds[9].get_text()

        proxypool.append(f'{ip}:{port}')

    return proxypool


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
            response = requests.get(url, proxies=proxies, timeout=1, headers=headers)
            if response.status_code == 200:
                useful_proxypool.append(ipaddr)
                print('success: ',ipaddr)
                continue
            else:
                print(response.status_code)
                continue
        except requests.exceptions.ProxyError:
            continue
        except requests.exceptions.ConnectTimeout:
            print('useless ip address: ',ipaddr)
            continue

    print(useful_proxypool)
    return useful_proxypool

def save_as_txt(useful_proxypool):
    print(useful_proxypool)
    with open(r'E:\The-crawler-learn\proxypool\\' + 'proxypool' + '.txt', 'w') as f:
        for i in useful_proxypool:
            ipaddr = i
            f.write(ipaddr + '\n')

    print('save')

def save_as_useful(useful_proxypool):
    print(useful_proxypool)
    with open(r'E:\The-crawler-learn\proxypool\\' + 'xici' + '.txt', 'w') as f:
        for i in useful_proxypool:
            ipaddr = i
            f.write(ipaddr + '\n')

    print('save')


def open_txt():
    ls = []
    with open(r'E:\The-crawler-learn\proxypool\\' + 'xici' + '.txt', 'r') as f:
        for line in f.readlines():
            line1 = line.replace('\n', '')
            ls.append(line1)

    print(ls)
    return ls


if __name__ == "__main__":
    proxypool = get_xici()
    useful_proxypool = verify_ip(proxypool)
    save_as_useful(useful_proxypool)
