# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv
import os
from pathlib import Path
from .spiders import vikaNewsSpider
from scrapy.exporters import  CsvItemExporter
from itemadapter import ItemAdapter


class VikkaPipeline:
    def open_spider(self, spider):
        v = vikaNewsSpider.VikaNewsSpider
        self.file = open(f"{v.date[0]}_{v.date[1]}_{v.date[2]}.csv", "ab")
        self.exporter = CsvItemExporter(self.file)
        self.exporter.fields_to_export("title", "newsDescription", "tags", "url")
        self.exporter.start_exporting()
        #
        # with open(f"{v.date[0]}_{v.date[1]}_{v.date[2]}.csv", "a") as file:

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        print("+++++++++++++++++++++++++++++")
        self.exporter.export_item(item)
        return item
