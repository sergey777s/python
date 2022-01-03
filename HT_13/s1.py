"""
1. Створити клас Calc, який буде мати атребут last_result та 4 методи. Методи повинні виконувати математичні
операції з 2-ма числами, а саме додавання, віднімання, множення, ділення.
   - Якщо під час створення екземпляру класу звернутися до атребута last_result він повинен повернути пусте значення
   - Якщо використати один з методів - last_result повенен повернути результат виконання попереднього методу.
   - Додати документування в клас (можете почитати цю статтю: https://realpython.com/documenting-python-code/ )
"""


class Calc(object):
    """This class represents simple calculator with four operations"""
    last_result = None

    def add(self, o1, o2):
        """adding two operands"""
        self.last_result = o1 + o2
        return self.last_result

    def subtraction(self, o1, o2):
        """substract operand o2 from operand o1"""
        self.last_result = o1 - o2
        return self.last_result

    def multiplication(self, o1, o2):
        """multiplicate two operands"""
        self.last_result = o1 * o2
        return self.last_result

    def division(self, o1, o2):
        """division operand o2 from operand o1, nothing to do if o2 is zero"""
        try:
            self.last_result = o1 / o2
            return self.last_result
        except ZeroDivisionError:
            self.last_result = o1
            return o1


def getOperand():
    return int(input())


def getOperation():
    o = input()
    while o not in ("+", "-", "*", "/"):
        o = input()
    return o


def start():
    calc = Calc()
    while True:
        if input("input 'last' if you want to see last result or any to calculate: ") == "last":
            print(calc.last_result)
            continue
        print("input first operand: ")
        o1 = getOperand()
        print("input operation (+ - * /) are supported: ")
        operat = getOperation()
        print("input last operand: ")
        o2 = getOperand()
        print("result:")
        if operat == "+":
            print(calc.add(o1, o2))
        elif operat == "-":
            print(calc.subtraction(o1, o2))
        elif operat == "/":
            print(calc.division(o1, o2))
        elif operat == "*":
            print(calc.multiplication(o1, o2))


start()
