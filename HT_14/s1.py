"""
Домашнє завдання №14: Переписати останню версію банкомата з використанням ООП.
"""


import os, datetime, json, csv, sqlite3, requests
from json.decoder import JSONDecodeError


class Bankomat(object):
    atm = dict()
    cassetteNum = (1, 2, 3, 4)
    dbMode = True

    class Screen(object):

        @staticmethod
        def cleanScreen():
            print("\n" * 100)

        def showMenu(self):
            self.cleanScreen()
            print("choose operation:")
            print("1. Get balance")
            print("2. Add money")
            print("3. Get money")
            print("4. Show history")
            print("5. Show exchange rates")
            print("6. Exit")

        def showMenuAdmin(self):
            self.cleanScreen()
            print("choose operation:")
            print("1. -==Get total money inside==-")
            print("2. -==Add cassettes bills==-")
            print("3. -==Add money==-")
            print("4. -==Show history==-")
            print("5. -==Exit==-")

    class Db(object):
        conn = sqlite3.connect("DB.db")
        cursor = conn.cursor()

    def __init__(self):
        self.screen = self.Screen()
        self.db = self.Db()

    def getUsernameFromUs(self):
        self.username = input("please input your login: ")
        return self.username

    def getPassFromUs(self):
        self.pwd = input("please input your password: ")
        return self.pwd

    @staticmethod
    def isFileExists(fileName):
        return os.path.isfile(f"./{fileName}")

    def addUserAndPwdToDB(self, username, password):
        try:
            self.db.cursor.execute("""CREATE TABLE users
                       (user text PRIMARY KEY, password text)
                       """)
        except sqlite3.OperationalError:
            pass
        self.db.cursor.execute("""INSERT INTO users
                           VALUES(?,?)""", (username, password))
        self.db.conn.commit()

    def addUserAndPwdToFile(self, username, password):
        if self.dbMode:
            return self.addUserAndPwdToDB(username, password)
        if self.isFileExists("users.data"):
            file = open("users.data", 'a')
            file.write(f"{username},{password}\n")
            file.close()
        else:
            file = open("users.data", 'w')
            file.write("username,password\n")
            file.close()

    def isUserPwdInDB(self, user, password=''):
        if password == '':
            try:
                self.db.cursor.execute(
                        """SELECT * FROM users WHERE user=?;""", (user,))
                if self.db.cursor.fetchone() is None:
                    return False
                else:
                    return True
            except sqlite3.OperationalError:  # no table users
                return False
        try:
            self.db.cursor.execute("""SELECT * FROM users
                           WHERE user=? AND password=?""", (user, password))
            if self.db.cursor.fetchone() == (str(user), str(password)):
                return True
            else:
                return False
        except sqlite3.OperationalError:  # no table users
            return False

    def isUserPwdInFile(self, user, password=''):
        if self.dbMode:
            return self.isUserPwdInDB(user, password='')
        if self.isFileExists("users.data"):
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

    def createBalanceDB(self, username):
        self.db.cursor.execute("""CREATE TABLE IF NOT EXISTS balance
                       (user text PRIMARY KEY, balance integer)""")
        self.db.cursor.execute("""INSERT INTO balance(user, balance)
        VALUES (?, ?)""", (username, 0))
        self.db.conn.commit()

    def createBalanceFile(self, username):
        if self.dbMode:
            return self.createBalanceDB(username)
        with open(f"{username}_balance.data", 'w') as f:
            f.write("0")

    def createTransactionsDB(self, username):
        self.db.cursor.execute("""CREATE TABLE IF NOT EXISTS transactions
                       (date text,
                       user text,
                       operation text,
                       amount integer,
                       new_balance integer)""")
        self.db.cursor.execute("""INSERT INTO transactions
                       (date, user, operation, amount, new_balance)
        VALUES(?, ?, ?, ?, ?)""",
        (datetime.datetime.now().isoformat()[:10], username, "user registered", 0, 0))
        self.db.conn.commit()

    def createTransactionsFile(self, username):
        if self.dbMode:
            return self.createTransactionsDB(username)
        f = open(f"{username}_transactions.data", 'w')
        f.close()

    def getLoginFromUser(self):
        while True:
            print("Hi, have you account yes or no:")
            if input() == "yes":
                for i in range(1, 4):
                    username = self.getUsernameFromUs()
                    password = self.getPassFromUs()
                    if self.isUserPwdInFile(username, password):
                        return username
                    else:
                        print("something wrong, try again: ")
                print("Please call your bank your login or password is incorrect")
            else:
                while True:
                    username = self.getUsernameFromUs()
                    password = self.getPassFromUs()
                    if self.isUserPwdInFile(username):
                        print(f"login '{username}' gets other user, input new:")
                    else:
                        break
                self.addUserAndPwdToFile(username, password)
                self.createBalanceFile(username)
                self.createTransactionsFile(username)
                return username  # new user

    @staticmethod
    def getUserChoose():
        while True:
            choose = int(input())
            if choose in range(1, 6+1):
                return choose

    def getBalanceDB(self, username):
        self.db.cursor.execute("""SELECT balance FROM balance WHERE user=?""",
                               (username,))
        return int(self.db.cursor.fetchone()[0])

    def getBalance(self, username):
        if self.dbMode:
            return self.getBalanceDB(username)
        with open(f"{username}_balance.data") as file:
            balance = int(file.readline())
            return balance

    def operationToDB(self, user, operation, amount):
        if user == "admin" and operation == "removed money":
            balance = 0
        elif user == "admin":
            balance = self.getBalanceATM()
        else:
            balance = self.getBalance(user)
        self.db.cursor.execute("""INSERT INTO transactions
                       (date, user, operation, amount, new_balance)
                       VALUES (?,?,?,?,?)""",
                       (datetime.datetime.now().isoformat()[:10],
                        user,
                        operation,
                        amount,
                        balance))
        self.db.conn.commit()

    def operationToJson(self, user, operation, amount):
        if self.dbMode:
            return self.operationToDB(user, operation, amount)
        if user == "admin" and operation == "removed money":
            balance = 0
        elif user == "admin":
            balance = self.getBalanceATM()
        else:
            balance = self.getBalance(user)
        toJson = {datetime.datetime.now().isoformat():
                  {
                  "operation": operation,
                  "amount": amount,
                  "new_balance": balance}
                  }

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

    def addMoneyToDB(self, username):
        moneyFromUs = int(input("how many money you add: "))
        curBalance = self.getBalance(username)
        self.db.cursor.execute("""UPDATE balance
        SET balance=?
        WHERE user=?""", (curBalance+moneyFromUs, username))
        self.db.conn.commit()
        self.operationToDB(username, "added money", moneyFromUs)

    def addMoney(self, username):
        if self.dbMode:
            return self.addMoneyToDB(username)
        moneyFromUs = int(input("how many money you add: "))
        curBalance = self.getBalance(username)
        with open(f"{username}_balance.data", 'w') as file:
            file.write(str(curBalance + abs(moneyFromUs)))
            print(f"You added {moneyFromUs} UAH")
        self.operationToJson(username, "added money", moneyFromUs)

    def changeUserBalanceInDB(self, username, curBalance, amount):
        self.db.cursor.execute("""UPDATE balance
                       SET balance=?
                       WHERE user=?""", (curBalance-amount, username))
        self.db.conn.commit()
        self.operationToDB(username, "got money", amount)

    def changeUserBalance(self, username, curBalance, amount):
        if self.dbMode:
            return self.changeUserBalanceInDB(username, curBalance, amount)
        with open(f"{username}_balance.data", 'w') as file:
            file.write(str(curBalance - amount))
        print(f"you has got {amount} UAH")
        self.operationToJson(username, "got money", amount)

    def getDictOfMoneyToPresent(self, cashNeedToPresent, dictOfBillsInATM):
        listOfBillsInATM = list(dictOfBillsInATM.keys())
        listOfBillsInATM.sort(reverse=True)
        present = dict.fromkeys(listOfBillsInATM)

        def isCanPresentAll(cashToPresent, listOfDenoms):
            for i in listOfDenoms:
                if cashToPresent % i == 0 and cashToPresent <= dictOfBillsInATM[i] * i and cashToPresent >= 0:
                    return True
            return False

        curLoop = 0
        try:
            for curDen in listOfBillsInATM:
                if curLoop == len(
                        listOfBillsInATM) - 1 and cashNeedToPresent % curDen == 0:
                    present[curDen] = int(cashNeedToPresent / curDen)
                    cashNeedToPresent = 0
                    break
                if cashNeedToPresent == 0:
                    break
                if cashNeedToPresent // curDen > 0 and isCanPresentAll(
                        cashNeedToPresent - curDen,
                        listOfBillsInATM[curLoop+1:]):
                    present[curDen] = cashNeedToPresent // curDen
                    cashNeedToPresent = cashNeedToPresent % curDen
                elif cashNeedToPresent // curDen > 0 and (
                        isCanPresentAll(
                                cashNeedToPresent - listOfBillsInATM[curLoop],
                                listOfBillsInATM[curLoop+1:]) or isCanPresentAll(
                                        cashNeedToPresent -
                                        listOfBillsInATM[curLoop] -
                                        listOfBillsInATM[curLoop + 1],
                                        listOfBillsInATM[curLoop+2:])):
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
            if present[i] is None:
                present[i] = 0
        return present

    def storeATMbillsToDB(self, atmDict):
        self.db.cursor.execute("""CREATE TABLE IF NOT EXISTS atm
                       (denoms integer PRIMARY KEY, amount integer)""")
        self.db.cursor.execute("""DELETE FROM atm""")
        self.db.conn.commit()
        for item in atmDict.items():
            self.db.cursor.execute(
                    """INSERT OR REPLACE INTO atm(denoms, amount)
            VALUES (?, ?)""", (item))
            self.db.conn.commit()

    def storeATMbillsToFile(self, atmDict):
        if self.dbMode:
            return self.storeATMbillsToDB(atmDict)
        with open("atm", 'w') as file:
            atmWriter = csv.DictWriter(
                    file, fieldnames=list(atmDict.keys()), delimiter='|')
            atmWriter.writeheader()
            atmWriter.writerow(atmDict)

    def getDictFromATMinDB(self):
        billsAmounts = dict()
        self.db.cursor.execute("""SELECT * FROM atm""")
        billsAmounts = dict(self.db.cursor.fetchall())
        return billsAmounts

    def getDictFromATMfile(self):
        if self.dbMode:
            return self.getDictFromATMinDB()
        billsAmounts = dict()
        with open("atm", 'r') as file:
            csvReader = csv.DictReader(file, delimiter='|')
            billsAmounts = dict(next(csvReader))
            return billsAmounts

    def getMoneyFromATMtoClient(self, money):
        billsAmounts = self.getDictFromATMfile()
        billAmmATM = dict()
        for key, val in billsAmounts.items():
            if val != '0':
                billAmmATM[int(key)] = int(val)
        denomsATM = list(billAmmATM.keys())
        dictOfMoneyToClient = self.getDictOfMoneyToPresent(money, billAmmATM)
        if sum(dictOfMoneyToClient.values()) == 0:
            return False
        else:
            toATMfile = {
                    key: billAmmATM[key] - dictOfMoneyToClient[key]
                    for key in billAmmATM}

            for key, amount in toATMfile.items():
                if amount < 0:
                    try:
                        denomsATM.remove(key)
                        tmpKey = key
                        tmpVal = billAmmATM[key]
                        billAmmATM.pop(key, 0)
                        dictOfMoneyToClient = self.getDictOfMoneyToPresent(
                                money, billAmmATM)
                        toATMfile = {
                                key: billAmmATM[key] - dictOfMoneyToClient[key]
                                for key in billAmmATM}
                        toATMfile[key] += abs(amount)
                        toATMfile.update({tmpKey: tmpVal})
                    except KeyError:
                        return False
            self.storeATMbillsToFile(toATMfile)
            for key, val in dictOfMoneyToClient.items():
                if val != 0:
                    print(f"ATM prestnted {val} X {key} UAH")
            return(True)

    def getMoney(self, username):
        curBalance = self.getBalance(username)
        while True:
            amount = int(input("how many money you want to get: "))
            if curBalance < amount:
                print(f"you can't get {amount} you have only {curBalance}")
            else:
                if self.getMoneyFromATMtoClient(amount):
                    self.changeUserBalance(username, curBalance, amount)
                    break
                else:
                    print("We have no this amount, pls try other one...")

    def showHistoryInDB(self, username):
        self.db.cursor.execute(
                """SELECT * FROM transactions WHERE user=?""", (username,))
        for transactList in self.db.cursor.fetchall():
            print(transactList[0])
            if transactList[2] == "user registered":
                print("user registered")
            else:
                print(f"You {transactList[2]} {transactList[3]} UAH, your balance is {transactList[4]}")

    def showHistory(self, username):
        if self.dbMode:
            return self.showHistoryInDB(username)
        with open(f"{username}_transactions.data") as jfile:
            jset = json.load(jfile)
            for operDate, params in jset.items():
                print(operDate[:10])
                print(f"You {params['operation']} {params['amount']} UAH, your balance is {params['new_balance']}")

    afterBalanceCassetesAmount = dict()

    def getBalanceATMinDB(self):
        try:
            self.db.cursor.execute("""SELECT * FROM atm""")
        except sqlite3.OperationalError:
            print("add money first")
            return 0
        result = 0
        for i in self.db.cursor.fetchall():
            self.afterBalanceCassetesAmount[i[0]] = i[1]
            result += i[0] * i[1]
        if result == "":
            return 0
        return result

    def getBalanceATM(self):
        if self.dbMode:
            return self.getBalanceATMinDB()
        try:
            with open("atm") as file:
                reader = csv.DictReader(file, delimiter="|")
                billsDict = dict(list(reader)[0])
                self.afterBalanceCassetesAmount = billsDict
                return sum(int(b) * int(d) for b, d in billsDict.items())
        except FileNotFoundError:
            file = open("atm", 'w')
            file.close()
        except IndexError:
            return 0

    def addBillsATM(self):
        denominat = (10, 20, 50, 100, 200, 500, 1000)
        self.atm.clear()
        print("-==denomination setup==-")
        print()
        for i in self.cassetteNum:
            d = int()
            while True:
                d = int(input(f"add denomination of bills in {i} cassette: "))
                if d not in denominat:
                    print(f"write from available: {denominat}")
                    continue
                else:
                    self.atm.setdefault(d)
                    print(f"you add denomination {d} in {i} cassette: ")
                    break

    def addMoneyATM(self):
        if not self.atm or not len(self.atm.keys()):
            print("First of all setup denominations of bills: ")
            self.addBillsATM()
        else:
            self.screen.cleanScreen()
            print("-==Money ADD setup==-")
            for denomination in list(self.atm.keys()):
                while True:
                    amount = abs(int(
                            input(f"input amount of bills, denomination is {denomination} : ")))
                    if input(f"you entered {amount} bills, type 'yes' if confirm: ") == "yes":
                        break
                    else:
                        continue
                self.atm[denomination] = amount
            self.operationToJson("admin", "removed money", self.getBalanceATM())
            self.storeATMbillsToFile(self.atm)
            self.operationToJson("admin", "added money", self.getBalanceATM())

    def isUsContinue(self):
        if input("press 1 to continue or any for exit ") == '1':
            return True
        else:
            return False

    def startAdmin(self):
        needExit = False
        while True:
            if needExit:
                break
            self.screen.showMenuAdmin()
            adminChoice = self.getUserChoose()
            if adminChoice == 1:
                print("Total balance of wincore nixdorf is: ")
                print(str(self.getBalanceATM()) + " UAH")
                for i in self.afterBalanceCassetesAmount.items():
                    print(f"In cassete with denominal {i[0]} amount is {i[1]}")
                if self.isUsContinue():
                    continue
                else:
                    break
            elif adminChoice == 2:
                self.addBillsATM()
                if self.isUsContinue():
                    continue
                else:
                    break
            elif adminChoice == 3:
                self.addMoneyATM()
                if self.isUsContinue():
                    continue
                else:
                    break
            elif adminChoice == 4:
                self.showHistory("admin")
                if self.isUsContinue():
                    continue
                else:
                    break
            else:
                needExit = True
                break
        print("THANK YOU FOR USING OUR BANK!!! ... or not)))")

    class Currency(object):
        @staticmethod
        def showExchangeRates():
            Bankomat.Screen.cleanScreen()
            try:
                req = requests.get(
                    "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5")
                listOfDictWithCurrencys = json.loads(req.text)
                print("       -==EXCHANGE CURRENCIES==-")
                print("      CURR       BUY        SALE")
                for curDict in listOfDictWithCurrencys:
                    print(f"""{curDict['ccy']:>10} {
                            curDict['buy'][:-3]:>10} {curDict['sale'][:-3]:>10}""")
            except requests.exceptions.RequestException:
                print("Something wrong, pls. try again later..")

    def start(self):
        needExit = False
        self.screen.cleanScreen()
        username = self.getLoginFromUser()
        if username == "admin":
            self.startAdmin()
            needExit = True
        while True:
            if needExit:
                break
            self.screen.showMenu()
            userChoice = self.getUserChoose()
            if userChoice == 1:
                print("your balance is: ")
                print(self.getBalance(username))
                if self.isUsContinue():
                    continue
                else:
                    break
            elif userChoice == 2:
                self.addMoney(username)
                if self.isUsContinue():
                    continue
                else:
                    break
            elif userChoice == 3:
                if self.getBalance(username) == 0:
                    print("you can't get money, your balance is 0 ")
                else:
                    self.getMoney(username)
                    if self.isUsContinue():
                        continue
                    else:
                        break
            elif userChoice == 4:
                self.showHistory(username)
                if self.isUsContinue():
                    continue
                else:
                    break
            elif userChoice == 5:
                currency = self.Currency()
                currency.showExchangeRates()
                if self.isUsContinue():
                    continue
                else:
                    break
            else:
                break
        print("THANK YOU FOR USING OUR BANK!!! ... or not)))")


bankomat = Bankomat()
bankomat.start()
