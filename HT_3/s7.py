"""
7. Ну і традиційно -> калькулятор :)
повинна бути 1 ф-цiя яка б приймала 3 аргументи - один з яких операцiя, яку зробити!
"""

def calc(digit1,oper,digit2):
    if oper == '+':
        print(int(digit1) + int(digit2))
    if oper == '-':
        print(int(digit1) - int(digit2))
    if oper == '*':
        print(int(digit1) * int(digit2))
    if oper == '/':
        print(int(digit1) / int(digit2))


s = input("calculate:")
d1 = int()
d2 = int()
o = ''
if '+' in s:
    d1, d2 = s.split('+')
    o = '+'
else:
    if '-' in s:
        d1, d2 = s.split('-')
        o = '-'
    else:
        if '*' in s:
            d1, d2 = s.split('*')
            o = '*'
        else:
            if '/' in s:
                d1, d2 = s.split('/')
                o = '/'
            else:
                print("nothing to do, sorry")
if len(o):
    try:
        calc(d1, o, d2)
    except ZeroDivisionError:
        print(0)
        