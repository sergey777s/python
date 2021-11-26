"""
1. Написати функцію < square > , яка прийматиме один аргумент - сторону 
квадрата, і вертатиме 3 значення (кортеж): периметр квадрата, 
площа квадрата та його діагональ.
"""


def getSide():
    side = int()
    side = input("input size of square side: ")
    return side


def getTupleOfPerimAreaDiagonal(side):
    side = int(side)
    perimAreaDiagonal = tuple()
    print()
    perimAreaDiagonal = (side * 4, side * side, (2 ** 0.5) * side)
    return perimAreaDiagonal


def square(side):
    side = int(side)
    perimAreaDiag = getTupleOfPerimAreaDiagonal(side)
    return perimAreaDiag


print(square(getSide()))
