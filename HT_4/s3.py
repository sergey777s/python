"""
3. Написати функцию < is_prime >, яка прийматиме 1 
аргумент - число від 0 до 1000, и яка вертатиме True, 
якщо це число просте, и False - якщо ні.
"""


def is_prime(digit):
    if digit == 2:
        return True
    elif digit == 1:
        return False
    if not digit % 2:
        return False
    else:
        for i in range(2, digit-1):
            if not digit % i:
                return False
    return True


d = int(input("input from 0 to 1000 for check on simple: "))
if d in range(0, 1000 + 1):
    print(is_prime(d))
else:
    print("not in range")
