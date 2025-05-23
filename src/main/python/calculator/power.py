from src.main.python.calculator.operation import Operation


class Power(Operation):
    """
    This class represents the arithmetic sum operation "^".
    The class extends an abstract superclass Operation.
    Other subclasses of Operation represent other arithmetic operations.
    """

    def __init__(self, elist, n=None):
        """
        Class constructor specifying a number of Expressions to power,
        as well as the Notation used to represent the operation.
        :param elist: The list of Expressions to pow
        :param n: The Notation to be used to represent the operation
        :raise IllegalConstruction:  If an empty list of expressions is passed as parameter
        """

        super().__init__(elist, n)
        self._symbol = "^"
        self._neutral = 1

    def op(self, base, exponent):
        """
        The actual computation of the power of two integers
        :param base: The base
        :param exponent: The exponent
        :return: The result of the base to the power of the exponent
        """

        return base.pow(exponent)
