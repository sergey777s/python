def getDictFromUsWithoutDuplWithMinMax():
    val='Start'
    key=1
    dic=dict()
    finDic=dict()
    while len(val):
        val=input("Please insert numbers for dict empty is finish: ")
        if len(val)==0:
            break
        dic[key]=val
        key+=1
    setFromDic=set(dic.values())
    i=1
    minVal=dic[1]
    maxVal=''
    for cur in dic:
        if dic[cur] in setFromDic:
            setFromDic.remove(dic[cur])
            finDic[i]=dic[cur]
            if finDic[i]>maxVal:
                maxVal=finDic[i]
            if finDic[i]<minVal:
                print(finDic[i])
                minVal=finDic[i]
            i+=1
    
    return [finDic,minVal,maxVal]

print("your dict without duplicates: ")
dicMinMax=getDictFromUsWithoutDuplWithMinMax()
print(dicMinMax[0])
print("min="+ dicMinMax[1])
print("max="+ dicMinMax[2])

