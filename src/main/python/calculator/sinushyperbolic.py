from src.main.python.calculator.function import Function


class Sinushyperbolic(Function):
    """
    This class represents the arithmetic operation "sinushyperbolic".
    The class extends an abstract superclass Function.
    Other subclasses of Function represent other arithmetic operations.
    """

    def __init__(self, elist, n=None):
        """
        Class constructor specifying a number of Expressions to use the sinushyperbolic,
        as well as the Notation used to represent the operation.
        :param elist: The list of Expressions to use the sinushyperbolic
        :param n: The Notation to be used to represent the operation
        :raise IllegalConstruction:  If an empty list of expressions is passed as parameter
        """

        super().__init__(elist, n)
        self._symbol = "sinh"
        self._neutral = 0

    def op(self, base):
        """
        The actual computation of the sinushyperbolic of one integers
        :param base: The first integer
        :return: The integer that is the result of the sinushyperbolic
        """
        return base.sinh()
