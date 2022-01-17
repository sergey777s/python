# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv
from .spiders import vikaNewsSpider
from itemadapter import ItemAdapter
import json


class VikkaPipeline:
    def open_spider(self, spider):
        v = vikaNewsSpider.VikaNewsSpider
        with open(f"{v.date[0]}_{v.date[1]}_{v.date[2]}.csv", "a") as file:
            self.csvWriter = csv.writer(file)

    def process_item(self, item, spider):
        print("+++++++++++++++++++++++++++++" + item.title)
        return item
