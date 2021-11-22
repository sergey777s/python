'''
1. Написати скрипт, який конкатенує всі елементи в списку і виведе їх на екран
. Список можна "захардкодити".
   Елементами списку повинні бути як рядки, так і числа.
'''
lstFromUs = [1, 2, "test", 3.14, "another test"]
strFromLst = str()
for i in lstFromUs:
    strFromLst += str(i)
print("your final string is: " + strFromLst)
