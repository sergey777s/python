"""
Використовуючи бібліотеку requests написати скрейпер для отримання статей / записів із АПІ
Документація на АПІ:
https://github.com/HackerNews/API
Скрипт повинен отримувати із командного рядка одну із наступних категорій:
askstories, showstories, newstories, jobstories

Якщо жодної категорії не указано - використовувати newstories.
Якщо категорія не входить в список - вивести попередження про це і завершити роботу.

Результати роботи зберегти в CSV файл. Зберігати всі доступні поля. Зверніть увагу - інстанси різних типів
мають різний набір полів.

Код повинен притримуватися стандарту pep8.
Перевірити свій код можна з допомогою ресурсу http://pep8online.com/

Для тих, кому хочеться зробити щось "додаткове" - можете зробити наступне: другим параметром cкрипт може приймати
назву HTML тега і за допомогою регулярного виразу видаляти цей тег разом із усим його вмістом із значення
 атрибута "text"
(якщо він існує) отриманого запису.
"""

import requests
import argparse
import json
from csv import DictWriter


def getCategoryFromUs():
    apars = argparse.ArgumentParser(description="write category from askstories, showstories, newstories, jobstories:")
    apars.add_argument("n", nargs='?', default="1")
    group = apars.add_mutually_exclusive_group()
    group.add_argument("--askstories", action="store_true")
    group.add_argument("--showstories", action="store_true")
    group.add_argument("--newstories", action="store_true")
    group.add_argument("--jobstories", action="store_true")
    args = apars.parse_args()
    if args.n == "1":
        if args.askstories:
            return "askstories"
        if args.showstories:
            return "showstories"
        if args.newstories:
            return "newstories"
        if args.jobstories:
            return "jobstories"
        return "newstories"
    else:
        print("wrong key")


def getItems(category='newstories'):
    url = f"https://hacker-news.firebaseio.com/v0/{category}.json"
    resp = requests.get(url)
    if resp.status_code == 200 and resp.text != "null":
        return list(resp.text.replace("[", "").replace("]", "").split(","))
    else:
        return[]


def getAvailableFields(item):
    url = f"https://hacker-news.firebaseio.com/v0/item/{item}.json"
    resp = requests.get(url)
    fields = list()
    if resp.status_code == 200:
        fields = dict(json.loads(resp.text)).keys()
        return fields
    else:
        return []


def getItemDict(item):
    url = f"https://hacker-news.firebaseio.com/v0/item/{item}.json"
    resp = requests.get(url)
    if resp.status_code == 200:
        return dict(json.loads(resp.text))
    else:
        return {}


def getFieldsForItemsInCategory(category):
    uniqueFields = set()
    items = getItems(category)
    remain = len(items)
    print("wait...")
    for item in items:
        for field in getAvailableFields(item):
            uniqueFields.add(field)
        remain -= 1
        print(remain)
    return uniqueFields


def start():
    category = getCategoryFromUs()
    headerFields = list(getFieldsForItemsInCategory(category))
    with open(f"{category}.csv", "w", newline="") as file:
        dictWriter = DictWriter(file, fieldnames=headerFields)
        dictWriter.writeheader()
        print("processing ... ")
        for item in getItems(category):
            dictWriter.writerow(getItemDict(item))



#start()
