# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QypcItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    tax_num = scrapy.Field()
    compony_name = scrapy.Field()
    name = scrapy.Field()
