# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class VikaprojectItem(scrapy.Item):
    title = scrapy.Field()
    newsDescription = scrapy.Field()
    tags = scrapy.Field()
    url = scrapy.Field()
