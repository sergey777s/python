"""
1. Створіть функцію, всередині якої будуть записано список із п'яти 
користувачів (ім'я та пароль).
   Функція повинна приймати три аргументи: два - обов'язкових 
   (<username> та <password>) і третій - необов'язковий параметр 
   <silent> (значення за замовчуванням - <False>).
   Логіка наступна:
       якщо введено коректну пару ім'я/пароль - вертається <True>;
       якщо введено неправильну пару ім'я/пароль і <silent> == <True> - 
       функція вертає <False>, інакше (<silent> == <False>) - породжується 
       виключення LoginException
"""


class LoginException(Exception):
    def __init__(self, username, password):
        self.username = username
        self.password = password


def isAutorize(username, password, silent=False):
    dataBase = [["vasya", "111"], ["petya", "222"],
                ["kolya", "s111"], ["vita", "333"], ["1", "2"]]

    def isUsPasInDataBase(user, password):
        for u, p in dataBase:
            if u == username and p == password:
                return True
        return False
    if isUsPasInDataBase(username, password):
        return True
    elif silent:
        return False
    else:
        raise LoginException(username, password)


def getUsername():
    return input("username: ")


def getPwd():
    return input("password: ")


def getSilent():
    s = input("silent or enter to skip: ")
    return True if s == "1" or s == "True" else False


try:
    print(isAutorize(getUsername(), getPwd(), getSilent()))
except LoginException as logEx:
    print(f"Your username {logEx.username} or password {logEx.password} is incorrect!")
