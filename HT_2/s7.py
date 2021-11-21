number=int(input("write number to generate directory: "))
generDic=dict()
for i in range(1,number+1):
    generDic[i]=i*i
print("Your dict is: ")
print(generDic)
