"""
6. Вводиться число. Якщо це число додатне, знайти його квадрат, 
якщо від'ємне, збільшити його на 100, якщо дорівнює 0, не змінювати.
"""


def isDigitPositive(digit):
    if digit > 0:
        return True
    else:
        return False


def operate():
    digit = int(input("input digit to operate: "))
    if digit == 0:
        return digit
    elif isDigitPositive(digit):
        return digit ** 2
    else:
        return digit + 100


print(operate())
