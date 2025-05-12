from src.main.python.calculator.function import Function


class Arctangent(Function):
    """
    This class represents the arithmetic sum operation "arctan".
    The class extends an abstract superclass Function.
    Other subclasses of Function represent other arithmetic operations.
    """

    def __init__(self, elist, n=None):
        """
        Class constructor specifying a number of Expressions to arctangent,
        as well as the Notation used to represent the operation.
        :param elist: The list of Expressions to arctan
        :param n: The Notation to be used to represent the operation
        :raise IllegalConstruction:  If an empty list of expressions is passed as parameter
        """

        super().__init__(elist, n)
        self._symbol = "arctan"
        self._neutral = 0

    def op(self, base):
        """
        The actual computation of the arctangent
        :param base: The first integer
        :return: The integer that is the result of the arctangent
        """
        return base.arctan()
