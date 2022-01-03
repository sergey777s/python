"""6. Створіть клас в якому буде атребут який буде рахувати кількість створених екземплярів класів."""

count = 0


class SuperClass(object):
    count = 0

    def __init__(self):
        SuperClass.count += 1


superClass = SuperClass()
print(SuperClass.count)
s = SuperClass()
print(SuperClass.count)
