"""
2. Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
   - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
   - щось своє :)
   Якщо якийсь із параментів не відповідає вимогам - породити виключення 
   із відповідним текстом.
"""


class LoginNotValid(Exception):
    def __init__(self, username, password, status):
        self.username = username
        self.password = password
        self.status = status


def isValid(login, password):

    def isLoginValid():
        if len(login) in range(3, 50+1):
            return True
        raise LoginNotValid(login, password, "login lenght lower 3 or upper 50")

    def isPassMore8():
        if len(password) > 8:
            return True
        raise LoginNotValid(login, password, "password lenght lower 8")

    def isPasHaveDigit():
        if all(map(str.isalpha, password)):
            raise LoginNotValid(login, password, "you have not digits")
        return True

    def isPasHaveUpperLetter():
        if all(map(str.islower, password)):
            raise LoginNotValid(login, password, "you have not UPPER letters")
        return True

    try:
        checks = [isLoginValid(), isPassMore8(), isPasHaveDigit(), isPasHaveUpperLetter()]
        if all(checks):
            return True
    except LoginNotValid as err:
        if __name__ == "__main__":
            print(f"Your login: {err.username} or pass {err.password} with status {err.status}")
            return False
        else:
            raise err


def getLogin():
    return input("login: ")


def getPassword():
    return input("password: ")


#isValid(getLogin(), getPassword())
