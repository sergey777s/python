"""
3. Напишіть програму, де клас «геометричні фігури» (figure) містить властивість color з початковим
значенням white і метод для зміни кольору фігури, а його підкласи «овал» (oval) і «квадрат» (square)
містять методи __init__ для завдання початкових розмірів об'єктів при їх створенні.
"""


class Figure(object):
    color = "white"
    def changeColor(self, color):
        self.color = color


class Oval(Figure):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height


class Square(Figure):
    def __init__(self, side):
        self.side = side
