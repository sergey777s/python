'''
2. Написати скрипт, який пройдеться по списку, який складається із кортежів, і
 замінить для кожного кортежа останнє значення.
   Список із кортежів можна захардкодити. Значення, на яке замінюється 
   останній елемент кортежа вводиться користувачем.
   Значення, введене користувачем, можна ніяк не конвертувати (залишити 
   рядком). Кількість елементів в кортежу повинна бути різна.
   Приклад списка котежів: [(10, 20, 40), (40, 50, 60, 70), (80, 90), (1000,)]
             Очікуваний результат, якщо введено "100":
Expected Output: [(10, 20, "100"), (40, 50, 60, "100"), (80, "100"), ("100",)]
'''
'''tupleFromUs = ("start")
lstOfTuples = list()
while len(tupleFromUs):
    tupleFromUs = tuple(input("input values in tuples, empty for finish: "))
    lstOfTuples.append(list(tupleFromUs))
lstOfTuples.pop()'''
lstOfTuples = [(10, 20, 40), (40, 50, 60, 70), (80, 90), (1000,)]
valueForChange = int(input("insert value for change: "))
finListOfTuples = list()
tmpList = list()
for t in lstOfTuples:
    tmpList.append(list(t)[:-1])
    tmpList[0].append(valueForChange)
    finListOfTuples.append(tuple(tmpList[0]))
    tmpList.clear()
print("your list is : ")
print(finListOfTuples)
