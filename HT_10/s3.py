"""
3. Конвертер валют. Прийматиме від користувача назву двох валют і суму (для першої).
   Робить запрос до API архіву курсу валют Приватбанку (на поточну дату) і виконує
   конвертацію введеної суми з однієї валюти в іншу.
"""
import datetime
import requests
import json


j = json


def getCurrencyUrl(date):
    return "https://api.privatbank.ua/p24api/exchange_rates?json&date=" + date


def getJsonAfterRequest():
    try:
        req = requests.get(
                getCurrencyUrl(datetime.datetime.now().strftime("%d.%m.%Y")))
        j = json.loads(req.text)
        return j
    except requests.exceptions.RequestException:
        return None


def getCurrencyList():
    result = list()
    for curDic in j["exchangeRate"][1:]:
        result.append(curDic["currency"])
    return result


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


def getCurrencyNbuRateOnDate(currency, date, nameOfOperation):
    for curDic in j["exchangeRate"][1:]:
        if curDic["currency"] == currency:
            return curDic[nameOfOperation]


def converter(currency1, amount, currency2):
    curDate = datetime.datetime.now().strftime("%d.%m.%Y")
    uahAmount = getCurrencyNbuRateOnDate(
            currency1, curDate, "purchaseRateNB") * amount
    return round(uahAmount / getCurrencyNbuRateOnDate(
            currency2, curDate, "saleRateNB"), 2)


def start():
    global j
    j = getJsonAfterRequest()
    if j is None:
        print("system not responding, please execute after some time")
    else:
        print("Input first currency for sale: ")
        cur1 = getCurrencyFromUs()
        amount = abs(int(input("what amount you want to exchange: ")))
        print("Input last currency for buy: ")
        cur2 = getCurrencyFromUs()
        print(f"you get: {converter(cur1, amount, cur2)} {cur2}")


start()
