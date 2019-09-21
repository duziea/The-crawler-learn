# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import QypcItem
import requests

class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['https://app.gsxt.gov.cn/']

    def start_requests(self):
        searchword = '91320282571372633B'
        url = 'https://app.gsxt.gov.cn/gsxt/corp-query-app-search-1.html'
        headers = {
            'Host': 'app.gsxt.gov.cn',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept-Encoding': 'br, gzip, deflate',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.5(0x17000523) NetType/WIFI Language/zh_CN',
            'Referer': 'https://servicewechat.com/wx5b0ed3b8c0499950/7/page-frame.html',
            'Content-Length': '229',
            'Accept-Language': 'zh-cn',
        }
        form_data = {
            'conditions': '{"excep_tab":"0","ill_tab":"0","area":"0","cStatus":"0","xzxk":"0","xzcf":"0","dydj":"0"}',
            'searchword': searchword,
            'sourceType': 'W',
        }
        response = requests.post(url, headers = headers, data=form_data)
        print(response.text)

    def parse(self, response):
        items = []
        result = json.loads(response.text)
        compony_name = result['data']['result']['data'][0]["entName"]
        legelRep = result['data']['result']['data'][0]["legelRep"]
        print(compony_name)
        print(legelRep)
    
        item = QypcItem()
        item['compony_name'] = compony_name
        item['legelRep'] = legelRep

        items.append(item)

        return items
