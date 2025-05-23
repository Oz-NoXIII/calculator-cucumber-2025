from src.main.python.calculator.operation import Operation


class Minus(Operation):
    """
    This class represents the arithmetic operation "-".
    The class extends an abstract superclass Operation.
    Other subclasses of Operation represent other arithmetic operations.
    """

    def __init__(self, elist, n=None):
        """
        Class constructor specifying a number of Expressions to subtract,
        as well as the Notation used to represent the operation.
        :param elist: The list of Expressions to subtract
        :param n: The Notation to be used to represent the operation
        :raise IllegalConstruction:  If an empty list of expressions is passed as parameter
        """

        super().__init__(elist, n)
        self._symbol = "-"
        self._neutral = 0

    def op(self, left, right):
        """
        The actual computation of the (binary) arithmetic subtraction of two integers
        :param left: Left operand
        :param right: Right operand
        :return: The number that is the result of the subtraction
        """

        return left.subtract(right)
