"""
2. Написати скрипт, який буде приймати від користувача назву валюти і 
початкову дату.
   - Перелік валют краще принтануть.
   - Також не забудьте указати, в якому форматі коритувач повинен ввести дату.
   - Додайте перевірку, чи введена дата не знаходиться у майбутньому ;)
   - Також перевірте, чи введена правильна валюта.
   Виконуючи запроси до API архіву курсу валют Приватбанку, вивести 
   інформацію про зміну
   курсу обраної валюти (Нацбанк) від введеної дати до поточної. 
   Приблизний вивід наступний:

   Currency: USD

   Date: 12.12.2021
   NBU:  27.1013   -------

   Date: 13.12.2021
   NBU:  27.0241   -0,0772

   Date: 14.12.2021
   NBU:  26.8846   -0,1395
"""
import datetime
import requests
import json
import time


def getCurrencyUrl(date):
    return "https://api.privatbank.ua/p24api/exchange_rates?json&date=" + date


def getCurrencyList():
    try:
        req = requests.get(
                getCurrencyUrl(datetime.datetime.now().strftime("%d.%m.%Y")))
        j = json.loads(req.text)
        result = list()
        for curDic in j["exchangeRate"][1:]:
            result.append(curDic["currency"])
        return result
    except requests.exceptions.RequestException:
        return []


def getDateFromUs():
    usStr = input("write date in format day.month.year: ")
    try:
        date = datetime.datetime.strptime(usStr, "%d.%m.%Y")
        if date > datetime.datetime.now():
            print("write date before now! ")
            return getDateFromUs()
        else:
            return datetime.datetime.strftime(date, "%d.%m.%Y")
    except ValueError:
        print("Pls. input correct data: ")
        return getDateFromUs()


def getCurrencyFromUs():
    availableCurrencies = getCurrencyList()
    if len(availableCurrencies):
        s = input(f"Avail. currencies {availableCurrencies} input currency: ")
        if s.upper() in availableCurrencies:
            return s.upper()
        else:
            print("please input correct currency ")
            return getCurrencyFromUs()
    else:
        print("server not responding, try again...")
        getCurrencyFromUs()


def getCurrencyNbuRateOnDate(currency, date):
    try:
        req = requests.get(getCurrencyUrl(datetime.datetime.strftime(
                date, "%d.%m.%Y")))
        j = json.loads(req.text)
        for curDic in j["exchangeRate"][1:]:
            if curDic["currency"] == currency:
                return curDic["saleRateNB"]
    except requests.exceptions.RequestException:
        print("connection error, trying again...")
        return getCurrencyNbuRateOnDate(currency, date)


def printCurrenciesChangingFromDate(currency, date):
    date = datetime.datetime.strptime(date, "%d.%m.%Y")
    print(f"CURRENCY: {currency}")
    print()
    delta = datetime.datetime.now() - date
    dateInterval = list()
    for dayNum in range(delta.days + 1):
        dateInterval.append(date + datetime.timedelta(days=dayNum))
    previousCurrency = getCurrencyNbuRateOnDate(currency, date)
    for day in dateInterval:
        time.sleep(0.5)
        curCurrency = getCurrencyNbuRateOnDate(currency, day)
        print(f"Date: {datetime.datetime.strftime(day, '%d.%m.%Y')}")
        currencyDelta = curCurrency - previousCurrency
        print(f"NBU: {curCurrency}    {round(currencyDelta, 6)}")
        previousCurrency = curCurrency
        print()


printCurrenciesChangingFromDate(getCurrencyFromUs(), getDateFromUs())
