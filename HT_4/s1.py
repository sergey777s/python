"""
1. Написати функцію < square > , яка прийматиме один аргумент - сторону 
квадрата, і вертатиме 3 значення (кортеж): периметр квадрата, 
площа квадрата та його діагональ.
"""


def getSide():
    side = int(input("input size of square side: "))
    return side


def getTupleOfPerimAreaDiagonal(side):
    perimAreaDiagonal = tuple()
    print()
    perimAreaDiagonal = (side * 4, side * side, (2 ** 0.5) * side)
    return perimAreaDiagonal


def square(side):
    perimAreaDiag = getTupleOfPerimAreaDiagonal(side)
    return perimAreaDiag


print(square(getSide()))
