"""
2. Створити клас Person, в якому буде присутнім метод __init__ який буде приймати * аргументів,
які зберігатиме в відповідні змінні. Методи, які повинні бути
в класі Person - show_age, print_name, show_all_information.
   - Створіть 2 екземпляри класу Person та в кожному з екземплярів створіть атребут profession.
"""


class Person(object):
    def __init__(self, name, age, *args):
        self.name = name
        self.age = age


    def show_age(self):
        print(self.age)

    def print_name(self):
        print(self.name)

    def show_all_information(self):
        print(f"name - {self.name}")
        print(f"age - {self.age}")


p1 = Person("Ivan",20)
p1.profession = "superman"
p1.show_all_information()
print(p1.profession)
p2 = Person("ImustBeHere", 37)
p2.profession = "sonOfRichFather"
p2.show_all_information()
print(p2.profession)