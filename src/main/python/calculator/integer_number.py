import math
import random

from src.main.python.calculator.number_type import NumberType


class IntegerNumber(NumberType):
    def __init__(self, value: int):
        if isinstance(value, str):
            match value:
                case "pi":
                    self.value = int(math.pi)
                case "e":
                    self.value = int(math.e)
                case _:
                    raise ValueError(f"Valeur inconnue : {value}")
        else:
            self.value = value

    def get_value(self):
        return self.value

    def add(self, other):
        return IntegerNumber(self.value + other.get_value())

    def subtract(self, other):
        return IntegerNumber(self.value - other.get_value())

    def multiply(self, other):
        return IntegerNumber(self.value * other.get_value())

    def divide(self, other):
        if other.get_value() == 0:
            return Integernan()
        return IntegerNumber(self.value // other.get_value())

    def inverse(self):
        if self.value == 0:
            return Integernan()
        return IntegerNumber(1 // self.value)

    def rand(self):
        random.seed()
        return random.randint(0, self.value)

    def pow(self, other):
        return IntegerNumber(self.value ** other.get_value())

    def log(self):
        if self.value <= 0:
            return Integernan()
        return IntegerNumber(int(math.log(self.value, 10)))

    def ln(self):
        if self.value <= 0:
            return Integernan()
        return IntegerNumber(int(math.log(self.value)))

    def exp(self):
        return IntegerNumber(int(math.exp(self.value)))

    def nroot(self, other):
        if (other.get_value() == 0):
            return Integernan()
        return IntegerNumber(int((self.value ** (1 / other.get_value()))))

    def sin(self):
        return IntegerNumber(int(math.sin(self.value)))

    def cos(self):
        return IntegerNumber(int(math.cos(self.value)))

    def tan(self):
        return IntegerNumber(int(math.tan(self.value)))

    def arcsin(self):
        if not (-1 <= self.value <= 1):
            return Integernan()
        return IntegerNumber(int(math.asin(self.value)))

    def arccos(self):
        if not (-1 <= self.value <= 1):
            return Integernan()
        return IntegerNumber(int(math.acos(self.value)))

    def arctan(self):
        return IntegerNumber(int(math.atan(self.value)))

    def sinh(self):
        return IntegerNumber(int(math.sinh(self.value)))

    def cosh(self):
        return IntegerNumber(int(math.cosh(self.value)))

    def tanh(self):
        return IntegerNumber(int(math.tanh(self.value)))

    def __str__(self):
        return str(self.value)

    def is_nan(self):
        return False

    def is_infinite(self):
        return False


class Integernan(IntegerNumber):
    def __init__(self):
        super().__init__(0)

    def get_value(self):
        return float("nan")

    def is_nan(self):
        return True
