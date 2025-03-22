import math
import unittest

from parameterized import parameterized
from src.main.python.calculator import calculator
from src.main.python.calculator.divides import Divides
from src.main.python.calculator.illegal_construction import IllegalConstruction
from src.main.python.calculator.minus import Minus
from src.main.python.calculator.my_number import MyNumber
from src.main.python.calculator.plus import Plus
from src.main.python.calculator.times import Times


class TestEvaluator(unittest.TestCase):

	def setUp(self):
		self.value1 = 8
		self.value2 = 6


	def test_evaluate_my_number(self):
		self.assertEqual(self.value1, calculator.eval_expression(MyNumber(self.value1)))

	@parameterized.expand([
		("*",),
		("+",),
		("/",),
		("-",),
	])
	def test_evaluate_operations(self, symbol):
		params = [MyNumber(self.value1), MyNumber(self.value2)]
		try:
			match symbol:
				case "+":
					self.assertEqual(self.value1 + self.value2, calculator.eval_expression(Plus(params)))
				case "-":
					self.assertEqual(self.value1 - self.value2, calculator.eval_expression(Minus(params)))
				case "*":
					self.assertEqual(self.value1 * self.value2, calculator.eval_expression(Times(params)))
				case "/":
					self.assertEqual(self.value1 / self.value2, calculator.eval_expression(Divides(params)))
				case _:
					self.fail("Invalid symbol")
		except IllegalConstruction as e:
			self.fail(e)

	def test_evaluate_real_addition(self):
		result = calculator.eval_expression(Plus([MyNumber(1.5), MyNumber(2.25)]))
		self.assertTrue(math.isclose(result, 3.75, rel_tol=1e-9))

	def test_evaluate_real_subtraction(self):
		result = calculator.eval_expression(Minus([MyNumber(5.5), MyNumber(2.25)]))
		self.assertTrue(math.isclose(result, 3.25, rel_tol=1e-9))

	def test_evaluate_real_multiplication(self):
		result = calculator.eval_expression(Times([MyNumber(1.2), MyNumber(3.0)]))
		self.assertTrue(math.isclose(result, 3.6, rel_tol=1e-9))

	def test_evaluate_real_division(self):
		result = calculator.eval_expression(Divides([MyNumber(7.5), MyNumber(2.5)]))
		self.assertTrue(math.isclose(result, 3.0, rel_tol=1e-9))

	def test_division_by_zero_returns_infinity(self):
		result = calculator.eval_expression(Divides([MyNumber(1.0), MyNumber(0.0)]))
		self.assertTrue(math.isinf(result))
		self.assertGreater(result, 0)






if __name__ == '__main__':
	unittest.main()
