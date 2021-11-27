"""
6. Вводиться число. Якщо це число додатне, знайти його квадрат, 
якщо від'ємне, збільшити його на 100, якщо дорівнює 0, не змінювати.
"""


def operate():
    digit = int(input("input digit to operate: "))
    if digit == 0:
        return digit
    elif digit > 0:
        return digit ** 2
    else:
        return digit + 100


print(operate())
