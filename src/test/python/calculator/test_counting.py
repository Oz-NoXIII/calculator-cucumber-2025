import unittest

from parameterized import parameterized

from src.main.python.calculator.divides import Divides
from src.main.python.calculator.illegal_construction import IllegalConstruction
from src.main.python.calculator.minus import Minus
from src.main.python.calculator.my_number import MyNumber
from src.main.python.calculator.plus import Plus
from src.main.python.calculator.times import Times
from src.main.python.visitor.counter import Counter


class TestCounting(unittest.TestCase):

	def setUp(self):
		self.value1 = 8
		self.value2 = 6
		self.e = None

	def test_number_counting(self):
		e = MyNumber(self.value1)
		e.accept(Counter())
		self.assertEqual(0, e.get_depth())
		self.assertEqual(0, e.get_ops())
		self.assertEqual(1, e.get_nbs())

	@parameterized.expand([
		("*",),
		("+",),
		("/",),
		("-",),
	])
	def test_operation_counting(self, symbol):
		params = [MyNumber(self.value1), MyNumber(self.value2)]
		try:
			match symbol:
				case "+":
					self.e = Plus(params)
				case "-":
					self.e = Minus(params)
				case "*":
					self.e = Times(params)
				case "/":
					self.e = Divides(params)
				case _:
					self.fail("Invalid symbol")
		except IllegalConstruction as e:
			self.fail(e)

		self.e.accept(Counter())
		self.assertEqual(1, self.e.get_depth())
		self.assertEqual(1, self.e.get_ops())
		self.assertEqual(2, self.e.get_nbs())


if __name__ == '__main__':
	unittest.main()
