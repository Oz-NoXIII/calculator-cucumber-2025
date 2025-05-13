from src.main.python.calculator.function import Function


class Tangenthyperbolic(Function):
    """
    This class represents the arithmetic sum operation "tanh".
    The class extends an abstract superclass Function.
    Other subclasses of Function represent other arithmetic operations.
    """

    def __init__(self, elist, n=None):
        """
        Class constructor specifying a number of Expressions to tangenthyperbolic,
        as well as the Notation used to represent the operation.
        :param elist: The list of Expressions to tanh
        :param n: The Notation to be used to represent the operation
        :raise IllegalConstruction:  If an empty list of expressions is passed as parameter
        """

        super().__init__(elist, n)
        self._symbol = "tanh"
        self._neutral = 0

    def op(self, base):
        """
        The actual computation of the tangenthyperbolic
        :param base: The first integer
        :return: The integer that is the result of the tangenthyperbolic
        """
        return base.tanh()
