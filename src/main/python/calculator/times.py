from src.main.python.calculator.operation import Operation


class  Times(Operation):
	"""
	This class represents the arithmetic multiplication operation "*".
	The class extends an abstract superclass Operation.
	Other subclasses of Operation represent other arithmetic operations.
	"""

	def __init__(self, elist, n=None):
		"""
		Class constructor specifying a number of Expressions to multiply,
   		as well as the Notation used to represent the operation.
		:param elist: The list of Expressions to multiply
		:param n: The Notation to be used to represent the operation
		:raise IllegalConstruction:  If an empty list of expressions is passed as parameter
		"""

		super().__init__(elist, n)
		self._symbol = "*"
		self._neutral = 1

	def op(self, l, r):
		"""
		The actual computation of the (binary) arithmetic multiplication of two integers
		:param l:
		:param r:
		:return: The integer that is the result of the multiplication
		"""

		return l.multiply(r)