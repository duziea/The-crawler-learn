import requests
from bs4 import BeautifulSoup
import lxml
import re

def get_ip66():
    url ='http://www.66ip.cn/nmtq.php?getnum=100&isp=0&anonymoustype=3&start=&ports=&export=&ipaddress=&area=0&proxytype=1&api=66i'
    response = requests.get(url)

    soup = BeautifulSoup(response.text,'lxml')
    ip=r'\.'.join([r'\d{1,3}']*4)
    port =r'\d{2,5}'
    pattern = re.compile(f'{ip}:{port}')
    soup = soup.body.get_text()

    result = re.findall(pattern, soup)

    print(result)
    return result

def verify_ip(proxypool):
    
    print(proxypool)
    url = 'https://icanhazip.com/'
    # url = 'https://www.baidu.com'

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
        # print(proxies)
        try:
            response = requests.get(url,proxies= proxies,timeout=2,headers = headers)  
            if response.status_code == 200:

                useful_proxypool.append(i)
                # print(response.text)
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

def save_as_useful(useful_proxypool):
    print(useful_proxypool)
    with open(r'E:\The-crawler-learn\proxypool\\' + '66ip' + '.txt','w') as f:   
        for i in useful_proxypool:
            ipaddr = i
            f.write(ipaddr + '\n')

    print('save success')

if __name__ == "__main__":
    proxypool = get_ip66()
    useful_proxypool = verify_ip(proxypool)
    save_as_useful(useful_proxypool)