# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class ProxypoolPipeline(object):
    def process_item(self, item, spider):
        return item

class IpInfoPipeline(object):
    def process_item(self,item,spider):
        try:
        #我们只需要IP地址与端口，因此只把字典值写进txt文件
            content = item['ip']
            open("xinresult.txt","a").write(content+"\n")

        except:
            pass
        return item
