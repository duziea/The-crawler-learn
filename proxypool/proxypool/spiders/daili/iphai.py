import requests
import random
from bs4 import BeautifulSoup

def get_iphai():
    url ='http://www.iphai.com'
    headers = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
 'Accept-Encoding': 'gzip, deflate',
 'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
 'Cache-Control': 'max-age=0',
 'Connection': 'keep-alive',
 'Cookie': 'PHPSESSID=6sii048p1a23tvfn6a91i42ms0; '
           '5d6fb81d1f871a290099d01c15e4d68d=44d67230eedcd34b97916ff23fdebab7f3bd1359s%3A1%3A%22%2F%22%3B; '
           'YII_CSRF_TOKEN=be9968e60abae1008546720b647b31b1feacfa69s%3A40%3A%22b40f9459af32b405c96298ffa32caef7dd77cad3%22%3B; '
           'BAEID=4B2DBA0CE47738C737F470847ACDC53F; '
           'Hm_lvt_1528f7f4830b519951a59e6a1656f499=1568109785; '
           'Hm_lpvt_1528f7f4830b519951a59e6a1656f499=1568109785',
 'Upgrade-Insecure-Requests': '1',
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) '
               'Gecko/20100101 Firefox/69.0',
 'host': 'www.iphai.com'
    }

    response = requests.get(url,headers = headers)
    # print(response.text)
    soup = BeautifulSoup(response.text,'lxml')

    soup1 = soup.table
    soup1 = soup1.find_all('tr')

    proxypool = []
    for i in range(1,len(soup1)):
        item = soup1[i]
        tds = item.select('td')
        ip = tds[0].get_text().strip()
        port = tds[1].get_text().strip()

        proxypool.append(f'{ip}:{port}')

    print(proxypool)
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
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
                }

    useful_proxypool = []
    for i in proxypool:
        ipaddr = i
        proxies = {'https':ipaddr}
        try:
            response = requests.get(url,proxies= proxies,timeout=2,headers = headers)  
            if response.status_code == 200:
                useful_proxypool.append(i)
                print('success ip ',ipaddr)
                continue
            else:
                print(response.status_code)
                continue
        except requests.exceptions.ProxyError:
            continue
        except requests.exceptions.ConnectTimeout:
            print('useless ip ',ipaddr)
            continue
        except TypeError:
            break
        
    print(useful_proxypool)
    return useful_proxypool

def save_as_txt(useful_proxypool):
    print(useful_proxypool)
    with open(r'E:\The-crawler-learn\proxypool\\' + 'proxypool' + '.txt','w') as f:   
        for i in useful_proxypool:
            ipaddr = i[0] + ':' + i[1]
            f.write(ipaddr + '\n')

    print('save')

def save_as_useful(useful_proxypool):
    print(useful_proxypool)
    with open(r'E:\The-crawler-learn\proxypool\\' + 'iphai' + '.txt','w') as f:   
        for i in useful_proxypool:
            ipaddr = i
            f.write(ipaddr + '\n')

    print('save success')

def open_txt():
    ls = []
    with open(r'E:\The-crawler-learn\proxypool\\' + 'proxypool' + '.txt','r') as f:   
        for line in f.readlines():
            line1 = line.replace('\n','')
            ls.append(line1)

    print(ls)
    return ls


if __name__ == "__main__":
    proxypool = get_iphai()
    useful_proxypool = verify_ip(proxypool)
    save_as_useful(useful_proxypool)


