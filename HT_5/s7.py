"""
7. Реалізуйте генератор, який приймає на вхід будь-яку ітерабельну 
послідовність (рядок, список, кортеж) і повертає генератор, який буде вертати 
значення з цієї послідовності, при цьому, якщо було повернено останній елемент
 із послідовності - ітерація починається знову.
   Приклад (якщо запустили його у себе - натисніть Ctrl+C ;) ):
   >>>for elem in generator([1, 2, 3]):
   ...    print(elem)
   ...
   1
   2
   3
   1
   2
   3
   1
   .......
"""


def myGen(s):
    cur = 0
    end = len(s)
    while True:
        if cur == end:
            cur = 0
            continue
        yield s[cur]
        cur += 1


myStr = "123"
myIter = myGen(myStr)
for i in myIter:
    print(i)
