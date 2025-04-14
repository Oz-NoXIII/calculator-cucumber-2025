from abc import ABC, abstractmethod


class Visitor(ABC): #pragma: no cover
	"""
	The Visitor Interface of the Visitor Design Pattern
	"""

	@abstractmethod
	def visit_my_number(self, number):
		"""
		The Visitor can traverse a number (a subtype of Expression)
		:param number: The number being visited
		"""
		pass

	@abstractmethod
	def visit_operation(self, op):
		"""
		The Visitor can traverse an operation (a subtype of Expression)
		:param op: The operation being visited
		"""
		pass