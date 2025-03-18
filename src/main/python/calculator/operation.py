from re import match

from pyxtension.streams import stream
from abc import ABC, abstractmethod

from src.main.python.calculator import notation
from src.main.python.calculator.illegal_construction import IllegalConstruction
from src.main.python.calculator.notation import Notation
from src.main.python.visitor.printer import Printer


class Operation(ABC):

	@abstractmethod
	def __init__(self, elist, n):
		if elist is None:
			raise IllegalConstruction("the list of expressions is None")
		else:
			self.__args = elist
		if n is not None:
			self.__notation = n
		self.__depth = 0
		self.__ops = 0
		self.__nbs = 0
		self._symbol = ""
		self._neutral = None

	@abstractmethod
	def __init__(self, elist):
		self.__init__(elist, None)

	@abstractmethod
	def op(self, l, r):
		pass

	def add_more_params(self, params):
		self.__args.extend(params)

	def accept(self, visitor):
		for a in self.__args:
			a.accept(visitor)
		visitor.visit_operation(self)

	def accept_notation(self, notation):
		self.__notation = notation
		self.accept(Printer(notation))

	def get_args(self):
		return self.__args

	def get_notation(self):
		return self.__notation

	def get_depth(self):
		return self.__depth

	def get_ops(self):
		return self.__ops

	def get_nbs(self):
		return self.__nbs

	def set_notation(self, n):
		self.__notation = n

	def set_depth(self, depth):
		self.__depth = depth

	def set_ops(self, ops):
		self.__ops = ops

	def set_nbs(self, nbs):
		self.__nbs = nbs

	def __str__(self):
		s = stream(self.__args).map(str)
		match self.__notation:
			case Notation.INFIX:
				return ("( " +
						s.reduce(lambda s1, s2: s1 + " " + self._symbol + " " + s2).orElse("") +
						" )")

			case Notation.PREFIX:
				return (self._symbol + " " +
						"(" +
						s.reduce(lambda s1, s2:s1 + ", " + s2).orElse("") +
						")")

			case Notation.POSTFIX:
				return ("(" +
						s.reduce(lambda s1, s2:s1 + ", " + s2).orElse("") +
						")" +
						" " + self._symbol)


	def __eq__(self, other):
		if other is None:
			return False
		if self == other:
			return True
		# getClass() instead of instanceof() because an addition is not the same as a multiplication
		if self.__class__ != other.__class__:
			return False
		if self.__args != other.get_args():
			return False
		return True


