import math

from src.main.python.calculator.number_type import NumberType


class RealNumber(NumberType):

    _precision = 6

    def __init__(self, value: float):
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
        return RealNumber(self.value ** other.get_value())

    def __str__(self):
        return f"{self.value:.{self._precision}f}"

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

    def log(self):
        if self.value <= 0:
            return RealNumber(float("nan"))
        return RealNumber(math.log(self.value))
