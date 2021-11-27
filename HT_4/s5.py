"""
5. Написати функцію < fibonacci >, яка приймає 
один аргумент і виводить всі числа Фібоначчі, що не перевищують його.
"""


def fibonacci(end):
    for cur in range(1, end):
        if cur == 1:
            prev = 0
            nex = 1
            print(cur)
        cur = prev + nex
        if cur > end:
            break
        print(cur)
        prev, nex = nex, cur

fibonacci(int(input("input last for fibonacci: ")))
