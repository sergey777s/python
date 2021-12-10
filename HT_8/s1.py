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
"""
1. Доповніть програму-банкомат з попереднього завдання таким функціоналом, як 
використання банкнот.
   Отже, у банкомата повинен бути такий режим як "інкассація", за допомогою 
   якого в нього можна "загрузити" деяку кількість банкнот (вибирається 
   номінал і кількість).
   Зняття грошей з банкомату повинно відбуватись в межах наявних банкнот за 
   наступним алгоритмом - видається мінімальна кількість банкнот наявного 
   номіналу. P.S. Будьте обережні з використанням "жадібного" алгоритму 
   (коли вибирається спочатку найбільша банкнота, а потім - наступна 
   за розміром і т.д.) - в деяких випадках він працює неправильно або 
   не працює взагалі. Наприклад, якщо треба видати 160 грн., а в наявності є 
   банкноти номіналом 20, 50, 100, 500,  банкомат не зможе видати суму 
   (бо спробує видати 100 + 50 + (невідомо), а потрібно було 100 + 20 + 20 + 20 ).

   Особливості реалізації:
   - перелік купюр: 10, 20, 50, 100, 200, 500, 1000;
   - у одного користувача повинні бути права "інкасатора". Відповідно і у 
   нього буде своє власне меню із пунктами:
     - переглянути наявні купюри;
     - змінити кількість купюр;
   - видача грошей для користувачів відбувається в межах наявних купюр;
   - якщо гроші вносяться на рахунок - НЕ ТРЕБА їх розбивати і вносити в 
   банкомат - не ускладнюйте собі життя, та й, наскільки я розумію, банкомати 
   все, що в нього входить, відкладає в окрему касету.
2. Для кращого засвоєння - перед написанням коду із п.1 - видаліть код для 
старої програми-банкомату і напишіть весь код наново (завдання на самоконтроль).
   До того ж, скоріш за все, вам прийдеться і так багато чого переписати.
"""

import os, datetime, json, csv
from json.decoder import JSONDecodeError
atm = dict()
cassetteNum = (1, 2, 3, 4)


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


def showMenuAdmin():
    cleanScreen()
    print("choose operation:")
    print("1. -==Get total money inside==-")
    print("2. -==Add cassettes bills==-")
    print("3. -==Add money==-")
    print("4. -==Show history==-")
    print("5. -==Exit==-")


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
    if user == "admin" and operation == "removed money":
        balance = 0
    elif user == "admin":
        balance = getBalanceATM()
    else:
        balance = getBalance(user)
    toJson = {datetime.datetime.now().isoformat():
              {"operation": operation,
              "amount": amount,
              "new_balance": balance}}

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
        file.write(str(curBalance + abs(moneyFromUs)))
        print(f"You added {moneyFromUs} UAH")
    operationToJson(username, "added money", moneyFromUs)


def changeUserBalance(username, curBalance, amount):
    with open(f"{username}_balance.data", 'w') as file:
        file.write(str(curBalance - amount))
    print(f"you has got {amount} UAH")
    operationToJson(username, "got money", amount)


def getDictOfMoneyToPresent(cashNeedToPresent, listOfBillsInATM):
    listOfBillsInATM.sort(reverse=True)
    present = dict.fromkeys(listOfBillsInATM)

    def isCanPresentAll(cashToPresent, listOfDenoms):
        for i in listOfDenoms:
            if cashToPresent % i == 0:
                return True
        return False

    curLoop = 0
    try:
        for curDen in listOfBillsInATM:
            if curLoop == len(listOfBillsInATM)-1 and cashNeedToPresent % curDen == 0:
                present[curDen] = int(cashNeedToPresent / curDen)
                cashNeedToPresent = 0
                break
            if cashNeedToPresent == 0:
                break
            if cashNeedToPresent // curDen > 0 and isCanPresentAll(cashNeedToPresent - curDen, listOfBillsInATM[curLoop+1:]):
                present[curDen] = cashNeedToPresent // curDen
                cashNeedToPresent = cashNeedToPresent % curDen
            elif cashNeedToPresent // curDen > 0 and (isCanPresentAll(cashNeedToPresent - listOfBillsInATM[curLoop], listOfBillsInATM[curLoop+1:]) or isCanPresentAll(cashNeedToPresent - listOfBillsInATM[curLoop] - listOfBillsInATM[curLoop + 1], listOfBillsInATM[curLoop+2:])):
                present[curDen] = cashNeedToPresent // curDen
                cashNeedToPresent = cashNeedToPresent % curDen
                present[listOfBillsInATM[curLoop-1]] = cashNeedToPresent // curDen
                cashNeedToPresent = cashNeedToPresent % listOfBillsInATM[curLoop-1]
            elif cashNeedToPresent % curDen == 0:
                present[curDen] = int(cashNeedToPresent / curDen)
                cashNeedToPresent = 0
            curLoop += 1
    except IndexError:
        for i in present.keys():
            present[i] = 0
    for i in present.keys():
        if present[i] == None:
            present[i] = 0
    return present


def storeATMbillsToFile(atmDict):
    with open("atm", 'w') as file:
        atmWriter = csv.DictWriter(file, fieldnames=list(atmDict.keys()), delimiter='|')
        atmWriter.writeheader()
        atmWriter.writerow(atmDict)


def getMoneyFromATMtoClient(money):
    billsAmounts = dict()
    with open("atm", 'r') as file:
        csvReader = csv.DictReader(file, delimiter='|')
        billsAmounts = dict(next(csvReader))
    billAmmATM = dict()
    for key, val in billsAmounts.items():
        billAmmATM[int(key)] = int(val)
    denomsATM = list(billAmmATM.keys())
    dictOfMoneyToClient = getDictOfMoneyToPresent(money, denomsATM)
    if sum(dictOfMoneyToClient.values()) == 0:
        return False
    else:
        toATMfile = {key:billAmmATM[key]-dictOfMoneyToClient[key] for key in billAmmATM}
        for amount in toATMfile.values():
            if amount < 0:
                return False
        storeATMbillsToFile(toATMfile)
        for key, val in dictOfMoneyToClient.items():
            if val != 0:
                print(f"ATM prestnted {val} X {key} UAH")
        return(True)
    pass


def getMoney(username):
    curBalance = getBalance(username)
    while True:
        amount = int(input("how many money you want to get: "))
        if curBalance < amount:
            print(f"you can't get {amount} you have only {curBalance}")
        else:
            if getMoneyFromATMtoClient(amount):
                changeUserBalance(username, curBalance, amount)
                break
            else:
                print("We have no this amount, pls try other one...")


def showHistory(username):
    with open(f"{username}_transactions.data") as jfile:
        jset = json.load(jfile)
        for operDate, params in jset.items():
            print(operDate[:10])
            print(f"You {params['operation']} {params['amount']} UAH, your balance is {params['new_balance']}")


def getBalanceATM():
    try:
        with open("atm") as file:
            reader = csv.DictReader(file, delimiter="|")
            billsDict = dict(list(reader)[0])
            return sum(int(b) * int(d) for b, d in billsDict.items())
    except FileNotFoundError:
        file = open("atm", 'w')
        file.close()
    except IndexError:
        return 0


def addBillsATM():
    denominat = (10, 20, 50, 100, 200, 500, 1000)
    atm.clear()
    print("-==denomination setup==-")
    print()
    for i in cassetteNum:
        d = int()
        while True:
            d = int(input(f"add denomination of bills in {i} cassette: "))
            if d not in denominat:
                print(f"write from available: {denominat}")
                continue
            else:
                atm.setdefault(d)
                print(f"you add denomination {d} in {i} cassette: ")
                break


def addMoneyATM():
    if not atm or not len(atm.keys()):
        print("First of all setup denominations of bills: ")
        addBillsATM()
    else:
        cleanScreen()
        print("-==Money ADD setup==-")
        for denomination in list(atm.keys()):
            while True:
                amount = abs(int(input(f"input amount of bills, denomination is {denomination} : ")))
                if input(f"you entered {amount} bills, type 'yes' if confirm: ") == "yes":
                    break
                else:
                    continue
            atm[denomination] = amount
        operationToJson("admin", "removed money", getBalanceATM())
        storeATMbillsToFile(atm)
        operationToJson("admin", "added money", getBalanceATM())


def isUsContinue():
    if input("press 1 to continue or any for exit ") == '1':
        return True
    else:
        return False


def startAdmin():
    while True:
        showMenuAdmin()
        adminChoice = getUserChoose()
        if adminChoice == 1:
            print("Total balance of wincore nixdorf is: ")
            print(str(getBalanceATM()) + " UAH")
            if isUsContinue():
                continue
            else:
                break
        elif adminChoice == 2:
            addBillsATM()
            if isUsContinue():
                continue
            else:
                break
        elif adminChoice == 3:
            addMoneyATM()
            if isUsContinue():
                continue
            else:
                break
        elif adminChoice == 4:
            showHistory("admin")
            if isUsContinue():
                continue
            else:
                break
        else:
            break
        print("THANK YOU FOR USING OUR BANK!!! ... or not)))")
    pass


def start():
    cleanScreen()
    username = getLoginFromUser()
    if username == "admin":
        startAdmin()
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
