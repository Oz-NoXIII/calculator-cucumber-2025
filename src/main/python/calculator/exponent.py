from src.main.python.calculator.function import Function


class Exponent(Function):
    """
    This class represents the arithmetic operation "exp".
    The class extends an abstract superclass Function.
    Other subclasses of Function represent other arithmetic operations.
    """

    def __init__(self, elist, n=None):
        """
        Class constructor specifying a number of Expressions to exponent,
        as well as the Notation used to represent the operation.
        :param elist: The list of Expressions to put to exponent
        :param n: The Notation to be used to represent the operation
        :raise IllegalConstruction:  If an empty list of expressions is passed as parameter
        """

        super().__init__(elist, n)
        self._symbol = "exp"
        self._neutral = 0

    def op(self, base):
        """
        The actual computation of the exponent of one integers
        :param base: The first integer
        :return: The integer that is the result of the exponent
        """
        return base.exp()
