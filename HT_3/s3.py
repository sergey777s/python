"""
3. Написати функцiю season, яка приймає один аргумент — номер мiсяця 
(вiд 1 до 12), яка буде повертати пору року, якiй цей мiсяць належить 
(зима, весна, лiто або осiнь)
"""


def season(month):
    if month in range(1, 2) or month == 12:
        print("winter")
    if month in range(3, 5):
        print("spring")
    if month in range(6, 8):
        print("summer")
    if month in range(9, 11):
        print("autumn")


month = int(input("input number of month: "))
if month in range(1, 13):
    season(month)
else:
    print("error")
