from src.main.python.calculator.operation import Operation


class Nroot(Operation):
    """
    This class represents the arithmetic division operation "nsqrt".
    The class extends an abstract superclass Operation.
    Other subclasses of Operation represent other arithmetic operations.
    """

    def __init__(self, elist, n=None):
        """
                Class constructor specifying a number of Expressions to n-root,
        as well as the notation used to represent the operation.
                :param elist: The list of Expressions to put n-root
                :param n: The Notation to be used to represent the operation
                :raise IllegalConstruction:  If an empty list of expressions is passed as parameter
        """
        super().__init__(elist, n)
        self._symbol = "nroot"
        self._neutral = 1

    def op(self, left, right):
        """
        Delegates the n-root to the internal NumberType logic of MyNumber.
        :param left: Left operand
        :param right: Right operand
        :return: MyNumber wrapping the result of n-root using NumberType
        """
        return left.nroot(right)
