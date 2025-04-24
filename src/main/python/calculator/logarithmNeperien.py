from src.main.python.calculator.function import Function


class LogarithmNeperien(Function):
    """
    This class represents the arithmetic sum operation "ln".
    The class extends an abstract superclass Function.
    Other subclasses of Function represent other arithmetic operations.
    """

    def __init__(self, elist, n=None):
        """
        Class constructor specifying a number of Expressions to the logarithm neperien,
        as well as the Notation used to represent the operation.
        :param elist: The list of Expressions to use the logarithm neperien
        :param n: The Notation to be used to represent the operation
        :raise IllegalConstruction:  If an empty list of expressions is passed as parameter
        """

        super().__init__(elist, n)
        self._symbol = "ln"
        self._neutral = 1

    def op(self, base):
        """
        The actual computation of the logarithm neperien of one integers
        :param l: The first integer
        :return: The integer that is the result of the logarithm neperien
        """
        return base.ln()
