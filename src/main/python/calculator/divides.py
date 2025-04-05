from src.main.python.calculator.operation import Operation


class Divides(Operation):
	"""
	This class represents the arithmetic division operation "/".
 	The class extends an abstract superclass Operation.
 	Other subclasses of Operation represent other arithmetic operations.
	"""

	def __init__(self, elist, n=None):
		"""
		Class constructor specifying a number of Expressions to divide,
     	as well as the notation used to represent the operation.
		:param elist: The list of Expressions to divide
		:param n: The Notation to be used to represent the operation
		:raise IllegalConstruction:  If an empty list of expressions is passed as parameter
		"""
		super().__init__(elist, n)
		self._symbol = "/"
		self._neutral = 1

	def op(self, l, r):
		"""
        Delegates the division to the internal NumberType logic of MyNumber.
        :param l: Left operand
        :param r: Right operand
        :return: MyNumber wrapping the result of l / r using NumberType division
        """
		return l.divide(r)

