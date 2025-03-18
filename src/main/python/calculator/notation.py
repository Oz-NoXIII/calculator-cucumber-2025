from enum import Enum

class Notation(Enum):
	"""
	Enumeration of the 3 ways to represent an arithmetic expression as a String:
	"""

	# Prefix notation, e.g. "+(1,2)" or "+ 1 2"
	PREFIX = 0

	# Infix notation, e.g. "1+2"
	INFIX = 1

	# Postfix notation, e.g. "(1,2)+" or "1 2 +"
	POSTFIX = 2

