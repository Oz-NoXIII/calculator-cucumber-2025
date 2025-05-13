import cmath

from src.main.python.calculator.number_type import NumberType


class ComplexNumber(NumberType):
    def __init__(self, real: float, imag: float = 0.0):
        if isinstance(real, str):
            match real:
                case "pi":
                    self.value = complex(cmath.pi, 0)
                case "e":
                    self.value = complex(cmath.e, 0)
                case _:
                    raise ValueError(f"Valeur inconnue : {real}")
        else:
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

    def inverse(self):
        if self.value == 0:
            return ComplexNumber(0, 0).set_nan()
        return ComplexNumber.from_complex(1 / self.value)

    def pow(self, other):
        if other.get_value() == 0:
            return ComplexNumber(0, 0).set_nan()
        return ComplexNumber.from_complex(self.value ** other.get_value())

    def log(self):
        if self.value == 0:
            return ComplexNumber(0, 0).set_nan()
        return ComplexNumber.from_complex(cmath.log10(self.value))

    def ln(self):
        if self.value == 0:
            return ComplexNumber(0, 0).set_nan()
        return ComplexNumber.from_complex(cmath.log(self.value))

    def exp(self):
        return ComplexNumber.from_complex(cmath.exp(self.value))

    def nroot(self, other):
        if (other.get_value() == 0):
            return ComplexNumber(0, 0).set_nan()
        return ComplexNumber.from_complex(self.value ** (1 / other.get_value()))

    def sin(self):
        return ComplexNumber.from_complex(cmath.sin(self.value))

    def cos(self):
        return ComplexNumber.from_complex(cmath.cos(self.value))

    def tan(self):
        print(cmath.cos(self.value))
        if (abs(cmath.cos(self.value).real) <= 1e-14):
            return ComplexNumber(0, 0).set_nan()
        return ComplexNumber.from_complex(cmath.tan(self.value))

    def arcsin(self):
        return ComplexNumber.from_complex(cmath.asin(self.value))

    def arccos(self):
        return ComplexNumber.from_complex(cmath.acos(self.value))

    def arctan(self):
        return ComplexNumber.from_complex(cmath.atan(self.value))

    def sinh(self):
        return ComplexNumber.from_complex(cmath.sinh(self.value))

    def cosh(self):
        return ComplexNumber.from_complex(cmath.cosh(self.value))

    def tanh(self):
        return ComplexNumber.from_complex(cmath.tanh(self.value))

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
