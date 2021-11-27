"""
2. Написати функцію < bank > , яка працює за наступною логікою: 
    користувач робить вклад у розмірі < a > одиниць 
    строком на < years > років під < percents > відсотків 
    (кожен рік сума вкладу збільшується на цей відсоток, ці гроші 
    додаються до суми вкладу і в наступному році на них також 
    нараховуються відсотки). Параметр < percents > є необов'язковим 
    і має значення по замовчуванню < 10 > (10%). 
    Функція повинна принтануть і вернуть суму, яка буде на рахунку.
"""


def getMoneyFromClient():
    money = float(input("input sum of deposit: "))
    return money


def getYearsOfDeposit():
    years = int(input("How meny years you want keep your money:"))
    return years


def getPercent():
    percent = float(input("choose your percent, default is ten: ") or "10")
    percent = percent * 0.01
    return percent


def bank(money, years, percent):
    for year in range(int(years)):
        money += float(money) * float(percent)
    return round(money, 2)


print(bank(getMoneyFromClient(), getYearsOfDeposit(), getPercent()))
