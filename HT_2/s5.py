'''
5. Написати скрипт, який залишить в словнику тільки пари із унікальними 
значеннями (дублікати значень - видалити). Словник для
   роботи захардкодити свій.
                Приклад словника (не використовувати):
                {'a': 1, 'b': 3, 'c': 1, 'd': 5}
                Очікуваний результат:
                {'a': 1, 'b': 3, 'd': 5}
'''
val = 'Start'
key = 1
dic = dict()
finDic = dict()
while len(val):
    val = input("Please insert value for dict empty is finish: ")
    if len(val) == 0:
        break
    dic[key] = val
    key += 1
i = 1
for d in dic:
    if isinstance(dic[d], list):
        dic[d] = str(dic[d])
for cur in dic:
    if dic[cur] not in finDic.values():
        print(finDic)
        finDic[i] = dic[cur]
        i += 1
for d in finDic:
    finDic[d]=eval(str(finDic[d]))
print("your dict without duplicates: ")
print(finDic)
