import scrapy
import datetime
from ..items import VikaprojectItem


def getDateFromUser():
    while True:
        date = input("write date in format xx.xx.xxxx: ")
        try:
            d = datetime.datetime.strptime(date, "%d.%m.%Y")
        except ValueError:
            print("write digits in date format xx.xx.xxxx!")
            continue
        if d > datetime.datetime.now():
            print("don't write future date")
        else:
            break
    day = d.strftime("%d")
    month = d.strftime("%m")
    year = d.strftime("%Y")
    return [year, month, day]


class VikanewsSpider(scrapy.Spider):
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

    @staticmethod
    def parsePage(response):
        peaceOfNewsText = ""
        tags = ""
        for pieceOfNews in response.css("div.entry-content.-margin-b ::text"):
            peaceOfNewsText += pieceOfNews.get()
        for tag in response.css("div.entry-tags.tags-margin a::text"):
            tags += "#" + tag.get() + ", "
        print(response.css("h1.post-title.-margin-b::text").get())
        title = response.css("h1.post-title.-margin-b::text").get()
        newsDescription = peaceOfNewsText
        tags = tags
        url = response.url
        print(url)
        yield VikaprojectItem(title=title, newsDescription=newsDescription, tags=tags, url=url)
