"""
6. Маємо рядок --> 
"f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345" 
-> просто потицяв по клавi
   Створіть ф-цiю, яка буде отримувати рядки на зразок цього, яка оброблює наступні випадки:
-  якщо довжина рядка в діапазонi 30-50 -> прiнтує довжину, кiлькiсть букв та цифр
-  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр (лише з буквами)
-  якщо довжина бульше 50 - > ваша фантазiя
"""
from functools import reduce


def getOnlyChars(commonStr):
    chars = list()
    for s in commonStr:
        if 'a' <= s <= 'z' or 'A' <= s <= 'Z':
            chars.append(s)
    return chars


def getOnlyDigits(commonStr):
    temp = ''
    digits = list()
    for s in commonStr:
        if '0' <= s <= '9':
            temp += f'{s}'
        else:
            if len(temp) != 0:
                digits.append(int(temp))
                temp = ''
    if len(temp) != 0:
        digits.append(int(temp))
    return digits


def strMap(someStr):
    if len(someStr) in range(30, 51):
        print(f'length is {len(someStr)} sum of digits '
                             f'is {len(getOnlyDigits(someStr))} sum of chars '
                             f'is {len(getOnlyChars(someStr))}')
    if len(someStr) in range(1, 30):
        print(f"sum of digits : {reduce(lambda p, n: p + n, getOnlyDigits(someStr))}") 
        print(''.join(getOnlyChars(someStr)))
    if len(someStr) > 50:
        s = b'''\xd0\xa1\xd0\xb0\xd1\x88\xd0\xb0 \xd0\xb8 
        \xd0\x96\xd0\xb5\xd0\xbd\xd1\x8f \xd0\xbd\xd0\xb5 
        \xd0\xbd\xd0\xb0\xd0\xb4\xd0\xbe \xd1\x82\xd0\xb0\xd0\xba:'''
        print(s.decode('utf-8')+")")


strMap(input("input your string:"))