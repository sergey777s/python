import csv

import scrapy
from ..items import VikkaItem
from ..pipelines import VikkaPipeline


def getDateFromUser():
    # day = input("Please input two digits for day: ")
    # while len(day) != 2:
    #     day = input("enter 2 digits of day: ")
    # month = input("Please input two digits for month: ")
    # while len(month) != 2:
    #     month = input("enter 2 digits of month: ")
    # year = input("Please input four digits for year: ")
    # while len(year) != 4:
    #     year = input("enter 4 digits of year: ")
    day = "30"
    month = "11"
    year = "2017"
    return [year, month, day]


class VikaNewsSpider(scrapy.Spider):
    name = 'vikaNews'
    allowed_domains = ['vikka.ua']
    date = getDateFromUser()

    start_urls = [f'http://vikka.ua/{date[0]}/{date[1]}/{date[2]}']

    def parse(self, response):
        allNews = response.css('a.more-link-style::attr(href)')
        # yield response.follow(allNews[0].get(), callback=self.parsePage)
        for pieceOfNews in allNews:
            yield response.follow(pieceOfNews.get(), callback=self.parsePage)
        nextPage = response.css("a.next.page-numbers::attr(href)").get()
        if nextPage:
            yield response.follow(nextPage, callback=self.parse)

    def parsePage(self, response):
        # oneNewsItem = VikkaItem()
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
        url = response.css('a.more-link-style ::attr(href)').get()
        # print(oneNewsItem.title+"______________________________________________")
        # self.storeToFile(oneNewsItem)
        yield VikkaItem(title=title, newsDescription=newsDescription, tags=tags, url=url)
        # yield
        # {
        # "tittle": response.css("h1.post-title.-margin-b::text").get(),
        # "newsDescription": peaceOfNewsText,
        # "tags": tags,
        # "url": response.css('a.more-link-style ::attr(href)').get()
        # }

    def storeToFile(self, item):
        with open(f"{self.date[0]}_{self.date[1]}_{self.date[2]}.csv", "a") as file:
            csvWriter = csv.writer(file)
            csvWriter.writerow(item.title)
