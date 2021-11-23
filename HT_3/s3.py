"""
3. Написати функцiю season, яка приймає один аргумент — номер мiсяця 
(вiд 1 до 12), яка буде повертати пору року, якiй цей мiсяць належить 
(зима, весна, лiто або осiнь)
"""


def season(month):
    if month in (1, 2) or month == 12:
        print("winter")
    if month in (3, 4, 5):
        print("spring")
    if month in (6, 7, 8):
        print("summer")
    if month in (9, 10, 11):
        print("autumn")


month = int(input("input number of month: "))
if month in range(1, 13):
    season(month)
else:
    print("error")
