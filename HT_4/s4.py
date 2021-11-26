"""
4. Написати функцію < prime_list >, яка прийматиме 2 аргументи - 
початок і кінець діапазона, і вертатиме список простих чисел 
всередині цього діапазона.
"""


def is_prime(digit):
    digit = int(digit)
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


def prime_list(start, end):
    result = list()
    for d in range(start, end + 1):
        if is_prime(d):
            result.append(d)
    return result


print(prime_list(0, 30))
