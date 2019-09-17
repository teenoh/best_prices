# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
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
        
        environment = os.environ.get("ENVIRONMENT", "development")
        
        if environment == 'production':
            API_URL = 'https://best-prices-api.herokuapp.com/api/post-item/'
        
        if environment == 'aws_production':
            API_URL = 'http://develop.upcqqqxpap.us-west-2.elasticbeanstalk.com/api/post-item/'
            /api/post-item/'
        
        else:
            API_URL = 'http://localhost:8000/api/post-item/'

        res = requests.post(API_URL, data=item)
        return item

    def close_spider(self, spider):
        print("\n\n\n\n\n\n\n\n\n\n Spider closed")
        pass

