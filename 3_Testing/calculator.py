"""
    Stwórz klasę Calculator, w ktorej zaimplementujesz dzialania:
    - dodawanie,
    - odejmowanie,
    - mnozenie,
    - dzielenie.
    Napisz testy, które przetestuja wczesniej wymienione metody.
"""

import unittest

class Calculator:
    def __init__(self, numOne, numTwo):
        self.numOne = numOne
        self.numTwo = numTwo

    def sum(self):
        return self.numOne + self.numTwo

    def sub(self):
        return self.numOne - self.numTwo

    def multi(self):
        return self.numOne * self.numTwo

    def divi(self):
        return self.numOne / self.numTwo
    pass


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f'dodawanie {a} + {b} = {Calculator(a, b).sum()}')
print(f'odejmowanie {a} - {b} = {Calculator(a, b).sub()}')
print(f'mnożenie {a} * {b} = {Calculator(a, b).multi()}')
print(f'dzielenie {a} / {b} = {Calculator(a, b).divi()}')


class TestCalculator(unittest.TestCase):
    one = 2
    two = 2

    def test_add(self):
        add = Calculator(TestCalculator.one, TestCalculator.two).sum()
        self.assertEqual(add, 4)

    def test_sub(self):
        sub = Calculator(TestCalculator.one, TestCalculator.two).sub()
        self.assertEqual(sub, 0)

    def test_mul(self):
        mul = Calculator(TestCalculator.one, TestCalculator.two).multi()
        self.assertEqual(mul, 4)

    def test_div(self):
        divi = Calculator(TestCalculator.one, TestCalculator.two).divi()
        self.assertEqual(divi, 1)

    pass
