"""
8. Написати функцію, яка буде реалізувати логіку циклічного зсуву 
елементів в списку. Тобто, функція приймає два аргументи: список і величину 
зсуву (якщо ця величина додатня - пересуваємо з кінця на початок, 
якщо від'ємна - навпаки - пересуваємо елементи з початку списку в його кінець).
   Наприклад:
       fnc([1, 2, 3, 4, 5], shift=1) --> [5, 1, 2, 3, 4]
       fnc([1, 2, 3, 4, 5], shift=-2) --> [3, 4, 5, 1, 2]
"""


def isShiftRight(shift):
    if shift > 0:
        return True
    elif shift < 0:
        return False


def loopOfShift(listOfEl, shiftSize):
    listOfEl = list(listOfEl)
    shiftSize = int(shiftSize)
    if isShiftRight(shiftSize):
        tempEnd = listOfEl[:len(listOfEl) - shiftSize]
        tempStart = listOfEl[len(listOfEl) - shiftSize:]
        tempStart.extend(tempEnd)
        result = tempStart
        print(result)
    elif shiftSize == 0:
        print(listOfEl)
    else:
        shiftSize = abs(shiftSize)
        tempStart = listOfEl[shiftSize:]
        tempEnd = listOfEl[:shiftSize]
        tempStart.extend(tempEnd)
        result = tempStart
        print(result)


listOfEl = input("write symbols: ").split()
shiftSize = int(input("write shift: "))
if abs(shiftSize) < len(listOfEl):
    loopOfShift(listOfEl, shiftSize)
else:
    print("write other size")
