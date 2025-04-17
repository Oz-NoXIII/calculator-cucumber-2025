from src.main.python.calculator.operation import Operation


class Plus(Operation):
    """
    This class represents the arithmetic sum operation "+".
    The class extends an abstract superclass Operation.
    Other subclasses of Operation represent other arithmetic operations.
    """

    def __init__(self, elist, n=None):
        """
        Class constructor specifying a number of Expressions to add,
        as well as the Notation used to represent the operation.
        :param elist: The list of Expressions to add
        :param n: The Notation to be used to represent the operation
        :raise IllegalConstruction:  If an empty list of expressions is passed as parameter
        """

        super().__init__(elist, n)
        self._symbol = "+"
        self._neutral = 0

    def op(self, left, right):
        """
        The actual computation of the (binary) arithmetic addition of two integers
        :param left: The first integer
        :param right: The second integer that should be added to the first
        :return: The integer that is the result of the addition
        """

        return left + right
