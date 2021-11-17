
lstFromUs=list(input("""Пожалуйста введите числа через запятую и пробел для 
	преобразования в список и кортеж: """).split(', '))
if ''.join(lstFromUs).isnumeric():
    lst=list(lstFromUs)
    tpl=tuple(lstFromUs)
    print(f'Output :\nList :{lst}\nTuple :{tpl}')
else:
	print("Ты из Полтавы? :) Вводи только числа разделяя запятой и пробелом!")