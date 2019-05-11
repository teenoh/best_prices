# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
import requests

class BestPricesPipeline(object):
    def open_spider(self, spider):
        print("Spider started \n\n\n\n\n\n\n\n\n\n")
        pass
    
    def process_item(self, item, spider):
        for value in item.values():
            if value == None:
                return item
        
        res = requests.post('https://best-prices-api.herokuapp.com/api/post-item/', data=item)
        return item

    def close_spider(self, spider):
        print("\n\n\n\n\n\n\n\n\n\n Spider closed")
        pass

