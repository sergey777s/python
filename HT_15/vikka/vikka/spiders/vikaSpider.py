import datetime

import scrapy


def getDateFromUser():
    date = datetime.datetime.strptime(input("input year/month/day: "), "%y/%m/%d")
    return date


class VikkaSpyder(scrapy.Spider):
    name = "vikkaSpider"
    start_urls = [f"https://www.vikka.ua/{'sss'}"]
    alowed_domains = ["vikka.ua"]

