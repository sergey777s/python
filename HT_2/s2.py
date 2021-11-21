tupleFromUs=("start")
lstOfTuples=list();
while len(tupleFromUs):
    tupleFromUs=tuple(input("input values in tuples, empty for finish: "))
    lstOfTuples.append(list(tupleFromUs))
lstOfTuples.pop()
valueForChange=111
for i in range(0,len(lstOfTuples)):
    lstOfTuples[i][len(lstOfTuples[i])-1]=valueForChange
    print(i)
print("I have changed last values for you: ")
print(tuple(lstOfTuples))
