"""
1. http://quotes.toscrape.com/ - написати скрейпер для збору всієї доступної 
інформації про записи:
   цитата, автор, інфа про автора... Отриману інформацію зберегти в CSV файл 
   та в базу. Результати зберегти в репозиторії.
   Пагінацію по сторінкам робити динамічною (знаходите лінку на наступну 
   сторінку і берете з неї URL). Хто захардкодить
   пагінацію зміною номеру сторінки в УРЛі - буде наказаний ;)

"""

from bs4 import BeautifulSoup
import requests
import csv
import sqlite3

url = "http://quotes.toscrape.com/"


def getResponse(url):
    try:
        resp = requests.get(url)
        return resp
    except requests.exceptions.RequestException:
        print("this page not responding")


def getSoup(url):
    resp = getResponse(url)
    soup = BeautifulSoup(resp.text, "lxml")
    return soup


def getUrlRoot():
    return "http://quotes.toscrape.com"


allQuotesData = list()


def processing(curQuote, page):
    print("\n" * 30)
    print("...LOADING...")
    print("Page = " + str(page))
    print("8" + "=" * curQuote + "Э" + (18 - 2 * curQuote) * " " + """(_!_)""")


page = 0


def parseAllPagesFrom(url):
    soup = getSoup(url)
    quotesSoup = soup.find_all("div", class_="quote")
    global page
    curQuote = 0
    page += 1
    for quote in quotesSoup:
        curQuote += 1
        quoteText = quote.find("span", class_="text").text
        authorSoup = quote.find("small", class_="author")
        author = authorSoup.text
        authorLink = getUrlRoot() + authorSoup.parent("a")[0].get("href")
        authorInfo = getSoup(authorLink).body.div.find(
                class_="author-details").text
        keywords = quote.div.meta.get("content")
        tagsSoup = quote.div.find_all("a")
        tags = {tag.text: getUrlRoot() + tag.get("href") for tag in tagsSoup}
        try:
            buttonNextLink = soup.nav.ul.find(
                    "li", class_="next").a.get("href")
        except AttributeError:
            buttonNextLink = None
        nextPageLink = None if buttonNextLink is None else getUrlRoot() + buttonNextLink
        allQuotesData.append({
                "quote": quoteText,
                "author": author,
                "authorLink": authorLink,
                "authorInfo": authorInfo,
                "keyWords": keywords,
                "tags": [t for t in tags.keys()],
                "tagLinks": [v for v in tags.values()]
                })
        processing(curQuote, page)
    if nextPageLink is not None:
        return parseAllPagesFrom(nextPageLink)


def writeToCsv(dic):
    with open("quotesBase.csv", 'w') as csvFile:
        csvWriter = csv.DictWriter(
                csvFile, fieldnames=dic[0].keys(), delimiter="|")
        csvWriter.writeheader()
        csvWriter.writerows(dic)


def writeToDatabase(dic):
    conn = sqlite3.connect("quotesBase.db")
    cursor = conn.cursor()
    try:
        cursor.execute("""DROP TABLE quotes""")
        conn.commit()
    except sqlite3.OperationalError:
        pass
    cursor.execute("""CREATE TABLE quotes(
            quote TEXT,
            author TEXT,
            authorLink TEXT,
            authorInfo TEXT,
            keyWords TEXT,
            tags TEXT,
            tagLinks TEXT
            )""")
    conn.commit()
    for quoteDic in allQuotesData:
        cursor.execute(
                """INSERT INTO quotes VALUES(?, ?, ?, ?, ?, ?, ?)""",
                (quoteDic['quote'], quoteDic['author'], quoteDic['authorLink'],
                 quoteDic['authorInfo'], quoteDic['keyWords'],
                 str(quoteDic['tags']), str(quoteDic['tagLinks'])))
        conn.commit()


parseAllPagesFrom(getUrlRoot())
writeToCsv(allQuotesData)
writeToDatabase(allQuotesData)
