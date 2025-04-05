# test_real_number.py
import unittest
import math
from src.main.python.calculator.real_number import RealNumber

class TestRealNumber(unittest.TestCase):

    def test_create_real_number(self):
        r = RealNumber(3.14)
        self.assertEqual(r.get_value(), 3.14)

    def test_add(self):
        r1 = RealNumber(1.5)
        r2 = RealNumber(2.5)
        result = r1.add(r2)
        self.assertAlmostEqual(result.get_value(), 4.0)

    def test_subtract(self):
        r1 = RealNumber(5.0)
        r2 = RealNumber(1.5)
        result = r1.subtract(r2)
        self.assertAlmostEqual(result.get_value(), 3.5)

    def test_multiply(self):
        r1 = RealNumber(2.0)
        r2 = RealNumber(3.0)
        result = r1.multiply(r2)
        self.assertAlmostEqual(result.get_value(), 6.0)

    def test_divide_normal(self):
        r1 = RealNumber(10.0)
        r2 = RealNumber(2.0)
        result = r1.divide(r2)
        self.assertAlmostEqual(result.get_value(), 5.0)

    def test_divide_by_zero_positive(self):
        r1 = RealNumber(1.0)
        r2 = RealNumber(0.0)
        result = r1.divide(r2)
        self.assertTrue(math.isinf(result.get_value()))
        self.assertGreater(result.get_value(), 0)

    def test_divide_zero_by_zero(self):
        r1 = RealNumber(0.0)
        r2 = RealNumber(0.0)
        result = r1.divide(r2)
        self.assertFalse(math.isnan(result.get_value()))

    def test_is_nan_and_is_infinite(self):
        r_nan = RealNumber(float("nan"))
        r_inf = RealNumber(float("inf"))
        self.assertTrue(r_nan.is_nan())
        self.assertFalse(r_nan.is_infinite())
        self.assertTrue(r_inf.is_infinite())
        self.assertFalse(r_inf.is_nan())


if __name__ == '__main__':
    unittest.main()
