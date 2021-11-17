strFromUs=input("Пожалуйста введите строку значений через кому и пробел: ").split(", ")
print(strFromUs)
valForTest=input("Введите значение для теста: ")
print(f"{valForTest} -> {strFromUs} : {'True' if strFromUs.count(valForTest) else 'False'}")
