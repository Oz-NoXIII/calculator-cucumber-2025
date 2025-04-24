from src.main.python.calculator.function import Function


class Inverse(Function):
    """
    This class represents the arithmetic operation "1/".
    The class extends an abstract superclass Function.
    Other subclasses of Function represent other arithmetic operations.
    """

    def __init__(self, elist, n=None):
        """
        Class constructor specifying a number of Expressions to inverse,
        as well as the Notation used to represent the operation.
        :param elist: The list of Expressions to inverse
        :param n: The Notation to be used to represent the operation
        :raise IllegalConstruction:  If an empty list of expressions is passed as parameter
        """

        super().__init__(elist, n)
        self._symbol = "1/"
        self._neutral = 1

    def op(self, base):
        """
        The actual computation of the inverse of one integers
        :param base: The first integer
        :return: The integer that is the result of the power
        """
        return base.inverse()
