from src.main.python.calculator.number_type import NumberType

class IntegerNumber(NumberType):
    def __init__(self, value: int):
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

    def pow(self, other):
        return IntegerNumber(self.value ** other.get_value())

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
