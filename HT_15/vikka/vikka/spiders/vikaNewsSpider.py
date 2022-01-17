import datetime

import scrapy
from ..items import VikkaItem


def getDateFromUser():
    day = input("Please input two digits for day in range 01-31: ")
    while len(day) != 2 or int(day) not in range(1, 31+1):
        day = input("enter 2 digits of day in range 01-31: ")
    month = input("Please input two digits for month in range 01-12: ")
    while len(month) != 2 or int(month) not in range(1, 12+1):
        month = input("enter 2 digits of month in range 01-12: ")
    year = input("Please input four digits for year in range 1900-current year: ")
    while len(year) != 4 or int(year) not in range(1900, int(datetime.datetime.now().strftime("%Y"))+1):
        year = input("enter 4 digits of year in range 1900-current year: ")
    return [year, month, day]


class VikaNewsSpider(scrapy.Spider):
    name = 'vikaNews'
    allowed_domains = ['vikka.ua']
    date = getDateFromUser()

    start_urls = [f'http://vikka.ua/{date[0]}/{date[1]}/{date[2]}']

    def parse(self, response):
        allNews = response.css('a.more-link-style::attr(href)')  # getting all news links
        for pieceOfNews in allNews:
            yield response.follow(pieceOfNews.get(), callback=self.parsePage)
        nextPage = response.css("a.next.page-numbers::attr(href)").get()  # searching next button
        if nextPage:
            yield response.follow(nextPage, callback=self.parse)  # processing next page

    def parsePage(self, response):
        peaceOfNewsText = ""
        tags = ""
        for pieceOfNews in response.css("div.entry-content.-margin-b p::text"):
            peaceOfNewsText += pieceOfNews.get()
        for tag in response.css("div.entry-tags.tags-margin a::text"):
            tags += "#" + tag.get() + ", "
        print(response.css("h1.post-title.-margin-b::text").get())
        title = response.css("h1.post-title.-margin-b::text").get()
        newsDescription = peaceOfNewsText
        tags = tags
        url = response.url
        print(url)
        yield VikkaItem(title=title, newsDescription=newsDescription, tags=tags, url=url)
