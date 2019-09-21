# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from proxypool.items import IpItem
import requests


class IphaiSpider(scrapy.Spider):
    name = 'iphai'
    allowed_domains = ['http://www.iphai.com']
    start_urls = ['http://www.iphai.com']

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        soup1 = soup.table.find_all('tr')
        # items = []
        for i in range(1, len(soup1)):
            item = IpItem()
            result = soup1[i]
            tds = result.select('td')
            ip = tds[0].get_text().strip()
            port = tds[1].get_text().strip()
            ipaddr = f'{ip}:{port}'
            item['ip'] = ipaddr
            # items.append(item)
            yield self.verify(item)

    def verify(self, item):
        ipaddr = item['ip']
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
        proxies = {'https': ipaddr}
        try:
            response = requests.get(url, headers=headers, proxies=proxies)
            if response.status_code == 200:
                print('success: ', ipaddr)
                item['success'] = ipaddr
                yield item
            else:
                print(response.status_code)
                item['fail'] = ipaddr
                yield item
        except requests.exceptions.ProxyError:
            print(ipaddr, '代理服务器无法连接')
            item['fail'] = ipaddr
            yield item
            
        except requests.exceptions.ConnectTimeout:
            print('useless ip address: ', ipaddr)
            item['fail'] = ipaddr
            yield item

    # def verify_ip(self,ipaddr):
    #     url = 'https://icanhazip.com/'

    #     headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    #             'accept-encoding': 'gzip, deflate, br',
    #             'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    #             'cache-control': 'max-age=0',
    #             'cookie': '__cfduid=de9efa2a6f9fae06c541b573175a219b81568089958',
    #             'sec-fetch-mode': 'navigate',
    #             'sec-fetch-site': 'none',
    #             'sec-fetch-user': '?1',
    #             'upgrade-insecure-requests': '1',
    #             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
    #     proxies = {'https': ipaddr}
    #     try:
    #         response = requests.get(url,headers=headers, proxies=proxies)
    #         if response.status_code == 200:
    #             print('success: ',ipaddr)
    #             return(ipaddr)
    #         else:
    #             print(response.status_code)
    #             return ''
    #     except requests.exceptions.ProxyError:
    #         print(ipaddr,'代理服务器无法连接')
    #         return ''
    #     except requests.exceptions.ConnectTimeout:
    #         print('useless ip address: ',ipaddr)
    #         return ''
