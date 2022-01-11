"""
3. Напишіть програму, де клас «геометричні фігури» (figure) містить властивість color з початковим
значенням white і метод для зміни кольору фігури, а його підкласи «овал» (oval) і «квадрат» (square)
містять методи __init__ для завдання початкових розмірів об'єктів при їх створенні.
4. Видозмініть програму так, щоб метод __init__ мався в класі «геометричні фігури» та приймав кольор фігури при
створенні екземпляру, а методи __init__ підкласів доповнювали його та додавали початкові розміри.
"""


class Figure(object):

    def __init__(self, color):
        self.color = color

    def changeColor(self, color):
        self.color = color


class Oval(Figure):
    def __init__(self, radius, height, color):
        self.radius = radius
        self.height = height
        Figure.__init__(self, color)


class Square(Figure):
    def __init__(self, side, color):
        self.side = side
        super.__init__(self, color)

