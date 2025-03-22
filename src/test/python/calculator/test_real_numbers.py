import unittest
import math

from src.main.python.calculator.my_number import MyNumber
from src.main.python.calculator.plus import Plus
from src.main.python.calculator.minus import Minus
from src.main.python.calculator.times import Times
from src.main.python.calculator.divides import Divides

class TestRealNumbers(unittest.TestCase):

    def test_my_number_accepts_float(self):
        n = MyNumber(3.14)
        self.assertIsInstance(n.get_value(), float)
        self.assertEqual(n.get_value(), 3.14)

    def test_addition_with_floats(self):
        e = Plus([MyNumber(1.1), MyNumber(2.2)])
        result = e.op(1.1, 2.2)
        self.assertTrue(math.isclose(result, 3.3, rel_tol=1e-9))

    def test_subtraction_with_floats(self):
        e = Minus([MyNumber(5.5), MyNumber(2.2)])
        result = e.op(5.5, 2.2)
        self.assertTrue(math.isclose(result, 3.3, rel_tol=1e-9))

    def test_multiplication_with_floats(self):
        e = Times([MyNumber(2.0), MyNumber(3.5)])
        result = e.op(2.0, 3.5)
        self.assertEqual(result, 7.0)

    def test_division_with_floats(self):
        e = Divides([MyNumber(7.0), MyNumber(2.0)])
        result = e.op(7.0, 2.0)
        self.assertEqual(result, 3.5)

    def test_division_by_zero_float(self):
        e = Divides([MyNumber(1.0), MyNumber(0.0)])
        result = e.op(1.0, 0.0)
        self.assertTrue(math.isinf(result))
        self.assertGreater(result, 0)

        result_neg = e.op(-1.0, 0.0)
        self.assertTrue(math.isinf(result_neg))
        self.assertLess(result_neg, 0)

        result_nan = e.op(0.0, 0.0)
        self.assertTrue(math.isnan(result_nan))

if __name__ == '__main__':
    unittest.main()
