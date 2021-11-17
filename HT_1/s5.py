decNums=list(input("""Введите десятичные числа через запятую и пробел для
                  преобразования в шестнадцатеричную
                  систему счисления:""").split(", "))
result=""
for i in decNums:
    current=hex(int(i))[2:]
    if len(str(current))==1:
        current='0'+current
    result+=current+", "
print(result)
