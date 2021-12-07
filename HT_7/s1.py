"""
1. Програма-банкомат.
   Створити програму з наступним функціоналом:
      - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль 
      (файл <users.data>);
      - кожен з користувачів має свій поточний баланс 
      (файл <{username}_balance.data>) та історію транзакцій 
      (файл <{username}_transactions.data>);
      - є можливість як вносити гроші, так і знімати їх. Обов'язкова перевірка 
      введених даних (введено число; знімається не більше, ніж є на рахунку).
   Особливості реалізації:
      - файл з балансом - оновлюється кожен раз при зміні балансу (містить 
      просто цифру з балансом);
      - файл - транзакціями - кожна транзакція у вигляді JSON рядка додається 
      в кінець файла;
      - файл з користувачами: тільки читається. Якщо захочете реалізувати 
      функціонал додавання нового користувача - не стримуйте себе :)
   Особливості функціонала:
      - за кожен функціонал відповідає окрема функція;
      - основна функція - <start()> - буде в собі містити весь workflow 
      банкомата:
      - спочатку - логін користувача - програма запитує ім'я/пароль. 
      Якщо вони неправильні - вивести повідомлення про це і закінчити роботу 
      (хочете - зробіть 3 спроби, а потім вже закінчити роботу - все 
      на ентузіазмі :) )
      - потім - елементарне меню типа:
        Введіть дію:
           1. Продивитись баланс
           2. Поповнити баланс
           3. Вихід
      - далі - фантазія і креатив :)
"""


import os, datetime, json
from json.decoder import JSONDecodeError


def cleanScreen():
    print("\n" * 100)


def getUsernameFromUs():
    username = input("please input your login: ")
    return username


def getPassFromUs():
    pwd = input("please input your password: ")
    return pwd


def isFileExists(fileName):
    return os.path.isfile(f"./{fileName}")


def addUserAndPwdToFile(username, password):
    if isFileExists("users.data"):
        file = open("users.data", 'a')
        file.write(f"{username},{password}\n")
        file.close
    else:
        file = open("users.data", 'w')
        file.write("username,password\n")
        file.close


def isUserPwdInFile(user, password=''):
    if isFileExists("users.data"):
        if password == '':
            with open("users.data") as file:
                for line in file:
                    if user in line:
                        return True
            return False
        with open("users.data") as file:
            for line in file:
                if line == f"{user},{password}\n":
                    return True
            return False
    else:
        return False


def createBalanceFile(username):
    with open(f"{username}_balance.data", 'w') as f:
        f.write("0")


def createTransactionsFile(username):
    f = open(f"{username}_transactions.data", 'w')
    f.close


def getLoginFromUser():
    while True:
        print("Hi, have you account yes or no:")
        if input() == "yes":
            for i in range(1, 4):
                username = getUsernameFromUs()
                password = getPassFromUs()
                if isUserPwdInFile(username, password):
                    return username
                else:
                    print("something wrong, try again: ")
            print("Please call your bank your login or password is incorrect")
        else:
            while True:
                username = getUsernameFromUs()
                password = getPassFromUs()
                if isUserPwdInFile(username):
                    print(f"login '{username}' gets other user, input new:")
                else:
                    break
            addUserAndPwdToFile(username, password)
            createBalanceFile(username)
            createTransactionsFile(username)
            return username  # new user


def showMenu():
    cleanScreen()
    print("choose operation:")
    print("1. Get balance")
    print("2. Add money")
    print("3. Get money")
    print("4. Show history")
    print("5. Exit")


def getUserChoose():
    while True:
        choose = int(input())
        if choose in range(1, 5+1):
            return choose


def getBalance(username):
    with open(f"{username}_balance.data") as file:
        balance = int(file.readline())
        return balance


def operationToJson(user, operation, amount):
    toJson = {datetime.datetime.now().isoformat():
              {"operation": operation,
              "amount": amount,
              "new_balance": getBalance(user)}}

    curData = ''
    with open(f"{user}_transactions.data")as jfile:
        try:
            curData = json.load(jfile)
            curData.update(toJson)
        except JSONDecodeError:
            curData = toJson
        finally:
            with open(f"{user}_transactions.data", 'w') as jfile:
                jfile.write(json.dumps(curData))


def addMoney(username):
    moneyFromUs = int(input("how many money you add: "))
    curBalance = getBalance(username)
    with open(f"{username}_balance.data", 'w') as file:
        file.write(str(curBalance + moneyFromUs))
        print(f"You added {moneyFromUs} UAH")
    operationToJson(username, "added money", moneyFromUs)


def getMoney(username):
    curBalance = getBalance(username)
    while True:
        amount = int(input("how many money you want to get: "))
        if curBalance < amount:
            print(f"you can't get {amount} you have only {curBalance}")
        else:
            with open(f"{username}_balance.data", 'w') as file:
                file.write(str(curBalance - amount))
            print(f"you has got {amount} UAH")
            operationToJson(username, "got money", amount)
            break


def showHistory(username):
    with open(f"{username}_transactions.data") as jfile:
        jset = json.load(jfile)
        for operDate, params in jset.items():
            print(operDate[:10])
            print(f"You {params['operation']} {params['amount']} UAH, your balance is {params['new_balance']}")


def start():
    cleanScreen()
    username = getLoginFromUser()

    def isUsContinue():
        if input("press 1 to continue or any for exit ") == '1':
            return True
        else:
            return False

    while True:
        showMenu()
        userChoice = getUserChoose()
        if userChoice == 1:
            print("your balance is: ")
            print(getBalance(username))
            if isUsContinue():
                continue
            else:
                break
        elif userChoice == 2:
            addMoney(username)
            if isUsContinue():
                continue
            else:
                break
        elif userChoice == 3:
            if getBalance(username) == 0:
                print("you can't get money, your balance is 0 ")
            else:
                getMoney(username)
                if isUsContinue():
                    continue
                else:
                    break
        elif userChoice == 4:
            showHistory(username)
            if isUsContinue():
                continue
            else:
                break
        else:
            break
    print("THANK YOU FOR USING OUR BANK!!! ... or not)))")


start()
