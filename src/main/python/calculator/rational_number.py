import math
from fractions import Fraction

from src.main.python.calculator.number_type import NumberType


class RationalNumber(NumberType):
    def __init__(self, numerator: int, denominator: int = 1):
        n = numerator
        d = denominator
        if isinstance(numerator, str):
            match numerator:
                case "pi":
                    n = math.pi
                case "e":
                    n = math.e
                case _:
                    raise ValueError(f"Valeur inconnue : {numerator}")
        if isinstance(denominator, str):
            match denominator:
                case "pi":
                    d = math.pi
                case "e":
                    d = math.e
                case _:
                    raise ValueError(f"Valeur inconnue : {denominator}")
        if isinstance(numerator, int) and isinstance(denominator, int):
            if denominator == 0:
                self.value = Fraction(0, 1)
                self._is_nan = True
            else:
                self.value = Fraction(numerator, denominator)
                self._is_nan = False
        else:
            self.value = Fraction(int(n), int(d))
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

    def inverse(self):
        if self.value == 0:
            return RationalNumber(0, 1).set_nan()
        return RationalNumber.from_fraction(1 / self.value)

    def pow(self, other):
        frac = Fraction(self.value ** other.get_value())
        return RationalNumber(frac.numerator, frac.denominator)

    def log(self):
        if self.value <= 0:
            return RationalNumber(0, 1).set_nan()
        frac = Fraction(math.log(self.value, 10))
        return RationalNumber(frac.numerator, frac.denominator)

    def ln(self):
        if self.value <= 0:
            return RationalNumber(0, 1).set_nan()
        frac = Fraction(math.log(self.value))
        return RationalNumber(frac.numerator, frac.denominator)

    def exp(self):
        frac = Fraction(math.exp(self.value))
        return RationalNumber(frac.numerator, frac.denominator)

    def sin(self):
        frac = Fraction(math.sin(self.value))
        return RationalNumber(frac.numerator, frac.denominator)

    def cos(self):
        frac = Fraction(math.cos(self.value))
        return RationalNumber(frac.numerator, frac.denominator)

    def tan(self):
        frac = Fraction(math.tan(self.value))
        return RationalNumber(frac.numerator, frac.denominator)

    def arcsin(self):
        if not(-1 <= self.value <= 1):
            return RationalNumber(0, 1).set_nan()
        frac = Fraction(math.asin(self.value))
        return RationalNumber(frac.numerator, frac.denominator)

    def arccos(self):
        if not(-1 <= self.value <= 1):
            return RationalNumber(0, 1).set_nan()
        frac = Fraction(math.acos(self.value))
        return RationalNumber(frac.numerator, frac.denominator)

    def arctan(self):
        frac = Fraction(math.atan(self.value))
        return RationalNumber(frac.numerator, frac.denominator)

    def to_mixed_str(self):

        if self._is_nan:
            return "NaN"
        num, den = self.value.numerator, self.value.denominator
        whole = int(num / den)
        remainder = abs(num) % den
        if remainder == 0:
            return str(whole)
        elif abs(num) < den:
            return f"{num}/{den}"
        else:
            return f"{whole} {remainder}/{den}"

    def is_nan(self):
        return self._is_nan

    def is_infinite(self):
        return False  # Rationals never yield infinity in Fraction

    def __str__(self):
        if self._is_nan:
            return "NaN"
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
