from src.main.python.calculator.expression import Expression
from src.main.python.calculator.number_type import NumberType

class ComplexNumber(Expression, NumberType):
    """
    Represents a complex number (a + bi).
    """

    def __init__(self, real, imag=0):
        self.value = complex(real, imag)

    def accept(self, visitor):
        visitor.visit_my_number(self)

    def get_depth(self):
        return 0

    def get_ops(self):
        return 0

    def get_nbs(self):
        return 1

    def get_value(self):
        return self.value

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        if isinstance(other, ComplexNumber):
            return self.value == other.value
        if isinstance(other, complex):
            return self.value == other
        return False

    def __hash__(self):
        return hash(self.value)
