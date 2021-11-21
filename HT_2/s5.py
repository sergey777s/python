val='Start'
key=1
dic=dict()
finDic=dict()
while len(val):
    val=input("Please insert value for dict empty is finish: ")
    if len(val)==0:
        break
    dic[key]=val
    key+=1
setFromDic=set(dic.values())
i=1
for cur in dic:
    if dic[cur] in setFromDic:
        setFromDic.remove(dic[cur])
        finDic[i]=dic[cur]
        i+=1
print("your dict without duplicates: ")
print(finDic)

