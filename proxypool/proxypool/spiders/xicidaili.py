# -*- coding: utf-8 -*-
import scrapy
from proxypool.items import ipItem

class XiciSpider(scrapy.Spider):
    name = 'xici'
    allowed_domains = ['www.xicidaili.com']
    start_urls = []
    url = 'https://www.xicidaili.com/wn/'
    
    for i in range(1,3):
        start_urls.append(url + str(i))

    # def start_requests(self):
    #     pass

    def parse(self, response):

        item = ipItem()

        for sel in response.xpath('//tr'):
            ip= sel.xpath('.//td[2]/text()').extract_first()
            port=sel.xpath('.//td[3]/text()').extract_first()
            item['ip']=str(ip)+":"+str(port)

            yield item

        return item












# class 66ipSpider(scrapy.Spider):
#     name = '66ip'
#     allowed_domains = ['www.xicidaili.com']
#     # start_urls = ['https://www.xicidaili.com/wn/']

#     def start_requests(self):
#         url = 

#     def parse(self, response):
#         print('spidering')
