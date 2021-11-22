'''
3. Написати скрипт, який видалить пусті елементи із списка. 
Список можна "захардкодити".
Sample data: [(), (), ('',), ('a', 'b'), {}, ('a', 'b', 'c'), ('d'), '', []]
	Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
'''
lstOfTuples = list([(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')])
tempLst = list()
for i in range(0, len(lstOfTuples)):
    if len(lstOfTuples[i]) != 0 :
        tempLst.append(lstOfTuples[i])
print("I have removed empty values for you: ")
print(tuple(tempLst))
