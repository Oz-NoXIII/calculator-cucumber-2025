import math
from src.main.python.calculator.number_type import NumberType

class RealNumber(NumberType):
    def __init__(self, value: float):
        self.value = float(value)

    def get_value(self):
        return self.value

    def add(self, other):
        return RealNumber(self.value + other.get_value())

    def subtract(self, other):
        return RealNumber(self.value - other.get_value())

    def multiply(self, other):
        return RealNumber(self.value * other.get_value())

    def divide(self, other):
        try:
            return RealNumber(self.value / other.get_value())
        except ZeroDivisionError:
            return RealNumber(float('inf') if self.value > 0 else float('-inf'))

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        return isinstance(other, RealNumber) and math.isclose(self.value, other.value)


    def is_nan(self):
        return math.isnan(self.value)

    def is_infinite(self):
        return math.isinf(self.value)
