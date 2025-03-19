from src.main.python.calculator.expression import Expression


class MyNumber(Expression):
	"""
	MyNumber is a concrete class that represents arithmetic numbers,
	which are a special kind of Expressions, just like operations are.
	"""

	def __init__(self, value):
		"""
		Constructor for MyNumber
		:param value: The value of the number
		"""
		self.value = value

	def accept(self, visitor):
		"""
		Accept is a method needed to implement the visitor design pattern
		:param visitor: The visitor object being passed as a parameter
		"""
		visitor.visit_my_number(self)

	def get_depth(self):
		"""
		Get the depth of the arithmetic expression
		:return: The depth of the arithmetic expression
		"""
		return 0

	def get_ops(self):
		"""
		Get the number of operations in the arithmetic expression
		:return: The number of operations in the arithmetic expression
		"""
		return 0

	def get_nbs(self):
		"""
		Get the number of numbers in the arithmetic expression
		:return: The number of numbers in the arithmetic expression
		"""
		return 1

	def get_value(self):
		"""
		Get the value of the number
		:return: The value of the number
		"""
		return self.value

	def __str__(self):
		"""
		Convert the number to a string
		:return: The number as a string
		"""
		return str(self.value)

	def __eq__(self, other):
		"""
		Compare two numbers for equality
		:param other: The other number to compare
		:return: True if the numbers are equal, False otherwise
		"""
		if not isinstance(other, MyNumber):
			return False
		return self.value == other.value

	def __hash__(self):
		"""
		Generate a hash code for the number
		:return: The hash code for the number
		"""
		return hash(self.value)