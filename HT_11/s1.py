"""
Сайт для виконання завдання: https://jsonplaceholder.typicode.com

Написати програму, яка буде робити наступне:
1. Робить запрос на https://jsonplaceholder.typicode.com/users і вертає 
коротку інформацію про користувачів (ID, ім'я, нікнейм)
2. Запропонувати обрати користувача (ввести ID)
3. Розробити наступну менюшку (із вкладеними пунктами):
   1. Повна інформація про користувача
   2. Пости:
      - перелік постів користувача (ID та заголовок)
      - інформація про конкретний пост (ID, заголовок, текст, кількість 
      коментарів + перелік їхніх ID)
   3. ТУДУшка:
      - список невиконаних задач
      - список виконаних задач
   4. Вивести URL рандомної картинки

"""

import random
import requests
import json


def clearScreen():
    print("\n" * 100)


def getListOfDictsFromUrl(url):
    try:
        req = requests.get(url)
        j = json.loads(req.text)
        return j
    except requests.exceptions.RequestException:
        print("connection error, pls try again")
        return []


lastKey = ""
result = dict()
listOfUserInfosDict = list()


def getInlineDict(dic, lastKey=""):
    if lastKey == "" and not any([isinstance(v, dict) for v in dic.values()]):
        return dic
    for key, val in dic.items():
        if isinstance(val, dict) and not (
                any([isinstance(v, dict) for v in val.values()])):
            lastKey += key+"."
            for k, v in val.items():
                result.update({lastKey + k: v})
            return result
        elif isinstance(val, dict):
            lastKey += key + "."
            return getInlineDict(val, lastKey)
        else:
            result[lastKey+key] = val
    return getInlineDict(val)


def getUserDetailsDict(fields, listOfDicts):
    if isinstance(listOfDicts, dict):
        lst = list()
        lst.append(listOfDicts)
        listOfDicts = lst
    result = dict()
    for dic in listOfDicts:
        inlineDict = getInlineDict(dic)
        for key, val in inlineDict.items():
            if key in fields:
                result[key] = val
        yield result


availableIds = []


def showShortUserDetails():
    listOfDicts = getListOfDictsFromUrl(
            "https://jsonplaceholder.typicode.com/users")
    global listOfUserInfosDict
    listOfUserInfosDict = listOfDicts
    fields = ["id", "name", "username"]
    for dic in getUserDetailsDict(fields, listOfDicts):
        availableIds.append(dic['id'])
        print(f"""userid={dic['id']}   username = {
                dic['name']}   nickname = {dic['username']}""")


def getUserId():
    userId = int(input("input UserID: "))
    while userId not in availableIds:
        userId = int(input("input CORRECT UserID: "))
    return userId


def getUserChoiseForMenu(menu):
    for m in menu:
        print(m)
    userChoise = int(input("make your choise: "))
    while userChoise not in range(len(menu)+1):
        userChoise = int(input("make your CORRECT choise: "))
    return userChoise


clearScreen()
showShortUserDetails()
userChoise = 0
userId = getUserId()
while userChoise != 5:
    clearScreen()
    userChoise = getUserChoiseForMenu(("1. Show full user info",
                                       "2. Show posts",
                                       "3. Show TODOs",
                                       "4. Show random picture",
                                       "5. Exit"))
    if userChoise == 1:
        clearScreen()
        for dic in listOfUserInfosDict:
            if dic['id'] == userId:
                for key, val in getInlineDict(dic).items():
                    print(f"{key} = {val}")
        input("press any key to continue")
        clearScreen()
    elif userChoise == 2:
        clearScreen()
        while userChoise != 3:
            clearScreen()
            userChoise = getUserChoiseForMenu(("1. Show posts id with title ",
                                               "2. Post information",
                                               "3. Exit"))
            if userChoise == 1:
                clearScreen()
                postsDict = getListOfDictsFromUrl(
                        f"https://jsonplaceholder.typicode.com/posts?userId={userId}")
                for dic in getUserDetailsDict(["id", "title"], postsDict):
                    print(f"user id = {dic['id']} title = {dic['title']}")
                input("press any key for continue...")
                clearScreen()
            if userChoise == 2:
                clearScreen()
                postId = int(input("input post id: "))
                postsDict = getListOfDictsFromUrl(
                        f"https://jsonplaceholder.typicode.com/posts/{postId}")
                for dic in getUserDetailsDict(["id", "title", "body"], postsDict):
                    print(f"user id = {dic['id']} title = {dic['title']} body = {dic['body']}")
                postsDict = getListOfDictsFromUrl(
                        f"https://jsonplaceholder.typicode.com/posts/{postId}/comments")
                print(f"sum of comments: {len(postsDict)}")
                print("IDs of comments: ")
                for dic in getUserDetailsDict(["id"], postsDict):
                    print(f"{dic['id']} ")
                input("press any key for continue...")
                clearScreen()
    elif userChoise == 3:
        clearScreen()
        userChoise = 0
        while userChoise != 3:
            clearScreen()
            userChoise = getUserChoiseForMenu(("1. Show TODOs not done ",
                                               "2. Show TODOs done",
                                               "3. Exit"))
            postsDict = getListOfDictsFromUrl(
                    f"https://jsonplaceholder.typicode.com/todos?userId={userId}")
            clearScreen()
            for dic in getUserDetailsDict(["title", "completed"], postsDict):
                if userChoise == 1 and not dic["completed"]:
                    print(f"{dic['title']} ")
                if userChoise == 2 and dic["completed"]:
                    print(f"{dic['title']} ")
            input("press any key for continue...")
            clearScreen()
    elif userChoise == 4:
        clearScreen()
        postsDict = getListOfDictsFromUrl(
                f"https://jsonplaceholder.typicode.com/photos")
        urls = list()
        for dic in getUserDetailsDict(["url"], postsDict):
            urls.append(dic['url'])
        print(random.choice(urls))
        input("press any key for continue...")
