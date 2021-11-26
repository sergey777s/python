"""
7. Написати функцію, яка приймає на вхід список і підраховує 
кількість однакових елементів у ньому.
"""


def sumOfDuplicates(elements):
    dictOfDupl = dict()
    temp = list()
    for el in elements:
        if str(type(el)) == "<class 'list'>":
            temp.extend([el[i] for i in range(len(el))])
        else:
            temp.append(el)
    elements = temp
    print(elements)
    dictOfDupl = dict.fromkeys(set(elements))
    for key in dictOfDupl.keys():
        sumOfCurDupl = 0
        for el in elements:
            if key == el:
                sumOfCurDupl += 1
        dictOfDupl[key] = sumOfCurDupl
    for cur in dictOfDupl.keys():
        print(f"Element {cur} appear in list('s) {dictOfDupl[cur]} times")


sumOfDuplicates([1, 2, 1, 1, [1, 2, 1], 'd', [1, 2], 1, [1, 2]])
