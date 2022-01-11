"""
5. Створіть за допомогою класів та продемонструйте свою реалізацію шкільної бібліотеки(включіть фантазію).
"""

import datetime


class SchoolLibrary(object):
    booksNames = dict()
    journal = dict()
    daysToReceiveBook = 5

    def openNewLibrary(self):
        userInput = "1"
        while len(userInput) > 0:
            userInput = input("Add book to library, (empty for finish) book name: ")
            if len(userInput) == 0:
                print(self.booksNames)
                break
            if self.booksNames.get(userInput, -1) == -1:
                self.booksNames[userInput] = abs(int(input("quantity: ")))
            else:
                self.booksNames[userInput] += abs(int(input("quantity: ")))

    def __init__(self):
        self.openNewLibrary()

    def addBook(self, bookName, quantity):
        self.booksNames[bookName] += quantity

    def giveBooksToPupil(self, nameOfBook, pupilName):
        if self.booksNames.get(nameOfBook, -1) > 0:
            self.booksNames[nameOfBook] -= 1
            self.journal.update({nameOfBook: dict.fromkeys(pupilName)})
            self.journal[nameOfBook][pupilName] = dict.fromkeys(["startDate", "endDate", "returned"])
            self.journal[nameOfBook][pupilName]["startDate"] = datetime.datetime.now()
            self.journal[nameOfBook][pupilName]["endDate"] = datetime.timedelta(
                days=self.daysToReceiveBook) + datetime.datetime.now()
            self.journal[nameOfBook][pupilName]["returned"] = False
        else:
            print("please choose other book")
            return 0

    def getBookFromPupil(self, nameOfBook, pupilName):
        try:
            self.booksNames[nameOfBook] += 1
            self.journal[nameOfBook][pupilName]["returned"] = True
        except KeyError:
            print("write name of book correctly! ")
            return self.getBookFromPupil(nameOfBook, pupilName)


def getNameOfBook():
    return input("input name of book you want to get:")


def getPupilName():
    return input("please input your name: ")


def start():
    lib = SchoolLibrary()
    while True:
        userChoise = int(input('if you want to get book press 1 or 2 to return book to library, any digit to exit: '))
        if userChoise == 1:
            if lib.giveBooksToPupil(getNameOfBook(), getPupilName()) != 0:
                print(f"you must return this book in {lib.daysToReceiveBook} days")
                continue
            else:
                continue
        elif userChoise == 2:
            lib.getBookFromPupil(getNameOfBook(), getPupilName())
            continue
        else:
            break

    for book, studentDesc in lib.journal.items():
        for student, desc in studentDesc.items():
            if desc is None:
                continue
            if desc["returned"] == False:
                print(f"Today book {book} was given to pupil {student}")
            else:
                print(f"Today book {book} was returned from pupil {student}")
    print("the library is closed everyone thanks everyone is free")


start()
