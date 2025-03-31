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
		The actual computation of the (binary) arithmetic division of two integers
		:param l: The first integer
		:param r: The second integer that should divide the first
		:return: The integer that is the result of the division, or NaN if the second integer is 0
		"""

		try:

			if isinstance(r, complex) and r.real == 0 and r.imag == 0:
				raise ZeroDivisionError("Division by zero complex number")
			elif r == 0:
				raise ZeroDivisionError("Division by zero")

			return l / r
		except ZeroDivisionError:

			if isinstance(l, float):
				if l == 0.0:
					return float("nan")
				return float("inf") if l > 0 else float("-inf")
			elif isinstance(l, complex):
				return complex(float("nan"), float("nan"))
			else:
				return float("nan")
