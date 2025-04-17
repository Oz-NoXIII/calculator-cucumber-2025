from fractions import Fraction

from src.main.python.calculator.number_type import NumberType


class RationalNumber(NumberType):
    def __init__(self, numerator: int, denominator: int = 1):
        if denominator == 0:
            self.value = Fraction(0, 1)
            self._is_nan = True
        else:
            self.value = Fraction(numerator, denominator)
            self._is_nan = False

    def get_value(self):
        return self.value

    def add(self, other):
        return RationalNumber.from_fraction(self.value + other.get_value())

    def subtract(self, other):
        return RationalNumber.from_fraction(self.value - other.get_value())

    def multiply(self, other):
        return RationalNumber.from_fraction(self.value * other.get_value())

    def divide(self, other):
        if other.get_value() == 0:
            return RationalNumber(0, 1).set_nan()
        return RationalNumber.from_fraction(self.value / other.get_value())

    def is_nan(self):
        return self._is_nan

    def is_infinite(self):
        return False  # Rationals never yield infinity in Fraction

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        return isinstance(other, RationalNumber) and self.value == other.value

    def __hash__(self):
        return hash(self.value)

    @classmethod
    def from_fraction(cls, f: Fraction):
        return RationalNumber(f.numerator, f.denominator)

    def set_nan(self):
        self._is_nan = True
        return self
