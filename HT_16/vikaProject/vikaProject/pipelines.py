# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from .DataBase import DataBase
from .spiders.vikaNews import VikanewsSpider


class VikaprojectPipeline:

    def __init__(self):
        self.db = DataBase()
        self.date = VikanewsSpider.date

    def open_spider(self, spider):
        self.db.createTable(self.date)

    def process_item(self, item, spider):
        self.db.addData(self.date, (item['title'], item['newsDescription'], item['tags'], item['url']))
        print("---------------------------------------------")
        return item

    def close_spider(self, spider):
        self.db.closeConnection()

