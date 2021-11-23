"""
2. Користувачем вводиться початковий і кінцевий рік. \
Створити цикл, який виведе всі високосні роки в цьому проміжку (границі включно).
"""
first = int(input("input first year: "))
last = int(input("input last year: "))
for year in range(first, last):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(f"{year} has more days")
