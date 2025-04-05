from abc import ABC

from src.main.python.calculator.expression import Expression
from src.main.python.calculator.number_type import NumberType
from fractions import Fraction

class RationalNumber(Expression, NumberType, ABC):
    """
    Represent a rational number as an exact fraction.
    """

    def __init__(self, numerator, denominator=1):
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        self.value = Fraction(numerator, denominator)


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
        if isinstance(other, RationalNumber):
            return self.value == other.value
        elif isinstance(other, Fraction):
            return self.value == other
        elif isinstance(other, int):
            return self.value == Fraction(other, 1)
        return False


    def __hash__(self):
        """
		Generate a hash code for the number
		:return: The hash code for the number
		"""
        return hash(self.value)
