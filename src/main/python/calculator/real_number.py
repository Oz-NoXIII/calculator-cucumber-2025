import math
import random

from src.main.python.calculator.number_type import NumberType


class RealNumber(NumberType):

    _precision = 6

    def __init__(self, value):
        if isinstance(value, str):
            match value:
                case "pi":
                    self.value = float(math.pi)
                    self._is_nan = math.isnan(self.value)
                    self._is_infinite = math.isinf(self.value)
                case "e":
                    self.value = float(math.e)
                    self._is_nan = math.isnan(self.value)
                    self._is_infinite = math.isinf(self.value)
                case _:
                    raise ValueError(f"Valeur inconnue : {value}")
        else:
            self.value = float(value)
            self._is_nan = math.isnan(self.value)
            self._is_infinite = math.isinf(self.value)

    def get_value(self):
        return self.value

    def add(self, other):
        return RealNumber(self.value + other.get_value())

    def subtract(self, other):
        return RealNumber(self.value - other.get_value())

    def multiply(self, other):
        return RealNumber(self.value * other.get_value())

    def divide(self, other):
        divisor = other.get_value()
        if divisor == 0.0:
            if self.value == 0.0:
                return RealNumber(float("nan"))
            return (
                RealNumber(float("inf"))
                if self.value > 0
                else RealNumber(float("-inf"))
            )
        return RealNumber(self.value / divisor)

    def pow(self, other):
        try:
            return RealNumber(self.value ** other.get_value())
        except Exception:
            return RealNumber(float("nan"))

    def rand(self):
        random.seed()
        return RealNumber(random.randint(0, 100) / 100)

    def log(self):
        if self.value <= 0:
            return RealNumber(float("nan"))
        return RealNumber(math.log(self.value, 10))

    def ln(self):
        if self.value <= 0:
            return RealNumber(float("nan"))
        return RealNumber(math.log(self.value))

    def exp(self):
        return RealNumber(math.exp(self.value))

    def nroot(self, other):
        try:
            return RealNumber((self.value ** (1 / other.get_value())))
        except Exception:
            return RealNumber(float("nan"))

    def sin(self):
        return RealNumber(math.sin(self.value))

    def cos(self):
        return RealNumber(math.cos(self.value))

    def tan(self):
        if abs(math.cos(self.value).real) <= 1e-14:
            return RealNumber(float("nan"))
        return RealNumber(math.tan(self.value))

    def arcsin(self):
        if not (-1 <= self.value <= 1):
            return RealNumber(float("nan"))
        return RealNumber(math.asin(self.value))

    def arccos(self):
        if not (-1 <= self.value <= 1):
            return RealNumber(float("nan"))
        return RealNumber(math.acos(self.value))

    def arctan(self):
        return RealNumber(math.atan(self.value))

    def sinh(self):
        return RealNumber(math.sinh(self.value))

    def cosh(self):
        return RealNumber(math.cosh(self.value))

    def tanh(self):
        return RealNumber(math.tanh(self.value))

    def inverse(self):
        if self.value == 0.0:
            return RealNumber(float("inf"))
        return RealNumber(1 / self.value)

    def __str__(self):
        raw = f"{self.value:.{self._precision}f}"
        return raw.rstrip("0").rstrip(".")

    def __eq__(self, other):
        return isinstance(other, RealNumber) and math.isclose(
            self.value, other.value, rel_tol=1e-9
        )

    def is_nan(self):
        return math.isnan(self.value)

    def is_infinite(self):
        return math.isinf(self.value)

    def to_degrees(self):
        return RealNumber(math.degrees(self.value))

    def to_radians(self):
        return RealNumber(math.radians(self.value))

    def to_scientific(self):
        return f"{self.value:.{self._precision}E}"

    def __hash__(self):
        return hash(round(self.value, self._precision))

    @classmethod
    def set_precision(cls, precision: int):
        cls._precision = precision

    @classmethod
    def get_precision(cls):
        return cls._precision

    def sqrt(self):
        if self.value < 0.0:
            return RealNumber(float("nan"))
        return RealNumber(math.sqrt(self.value))
