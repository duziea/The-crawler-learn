# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class ProxypoolPipeline(object):
    def process_item(self, item, spider):
        return item


class IpPipline(object):
    file_path = r'E:\The-crawler-learn\scrapy_learn\result.txt'
    def __init__(self):
        self.article = open(self.file_path,'a+',encoding='utf-8')
    
    def process_item(self,item,spider):
        success = item['success']
        self.article.write(success)
        return item