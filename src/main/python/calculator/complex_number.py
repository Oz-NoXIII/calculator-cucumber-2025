import cmath

from src.main.python.calculator.number_type import NumberType


class ComplexNumber(NumberType):
    def __init__(self, real: float, imag: float = 0.0):
        self.value = complex(real, imag)

    def get_value(self):
        return self.value

    def add(self, other):
        return ComplexNumber.from_complex(self.value + other.get_value())

    def subtract(self, other):
        return ComplexNumber.from_complex(self.value - other.get_value())

    def multiply(self, other):
        return ComplexNumber.from_complex(self.value * other.get_value())

    def divide(self, other):
        if other.get_value() == 0:
            return ComplexNumber(0, 0).set_nan()
        return ComplexNumber.from_complex(self.value / other.get_value())

    def pow(self, other):
        if other.get_value() == 0:
            return ComplexNumber(0, 0).set_nan()
        return ComplexNumber.from_complex(self.value ** other.get_value())

    def modulus(self):
        return abs(self.value)

    def conjugate(self):
        return ComplexNumber.from_complex(self.value.conjugate())

    def sqrt(self):
        return ComplexNumber.from_complex(cmath.sqrt(self.value))

    def is_nan(self):
        return self.value != self.value

    def is_infinite(self):
        return (
            self.value.real == float("inf")
            or self.value.imag == float("inf")
            or self.value.imag == float("-inf")
        ) or self.value.real == float("-inf")

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        return isinstance(other, ComplexNumber) and self.value == other.value

    def __hash__(self):
        return hash(self.value)

    @classmethod
    def from_complex(cls, c: complex):
        return cls(c.real, c.imag)

    def set_nan(self):
        self.value = complex(float("nan"), float("nan"))
        return self
