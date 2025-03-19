import unittest

from src.main.python.calculator.illegal_construction import IllegalConstruction
from src.main.python.calculator.my_number import MyNumber
from src.main.python.calculator.notation import Notation
from src.main.python.calculator.plus import Plus
from src.main.python.calculator.times import Times


class TestTimes(unittest.TestCase):

	value1 = 8
	value2 = 6

	def setUp(self):
		params = [MyNumber(self.value1), MyNumber(self.value2)]
		try:
			self.op = Times(params)
		except IllegalConstruction as e:
			self.fail(e)

	def test_constructor(self):
		self.assertRaises(IllegalConstruction, lambda: Times(None))
		try:
			self.assertIsNot(self.op, Plus([]))
		except IllegalConstruction as e:
			self.fail(e)

	def test_equals(self):
		p = [MyNumber(self.value1), MyNumber(self.value2)]
		try:
			e = Times(p, Notation.INFIX)
			self.assertEqual(self.op, e)
		except IllegalConstruction as e:
			self.fail(e)

	def test_hash_code(self):
		p = [MyNumber(self.value1), MyNumber(self.value2)]
		try:
			e = Times(p, Notation.INFIX)
			self.assertEqual(hash(self.op), hash(e))
		except IllegalConstruction as e:
			self.fail(e)

	def test_none_param_list(self):
		params = None
		self.assertRaises(IllegalConstruction, lambda: Times(params))


if __name__ == '__main__':
	unittest.main()
