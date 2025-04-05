# test_rational_number.py
import unittest
from src.main.python.calculator.rational_number import RationalNumber
from fractions import Fraction

class TestRationalNumber(unittest.TestCase):

    def test_creation(self):
        r = RationalNumber(3, 4)
        self.assertEqual(r.get_value(), Fraction(3, 4))

    def test_add(self):
        r1 = RationalNumber(1, 2)
        r2 = RationalNumber(1, 4)
        result = r1.add(r2)
        self.assertEqual(result.get_value(), Fraction(3, 4))

    def test_subtract(self):
        r1 = RationalNumber(3, 4)
        r2 = RationalNumber(1, 2)
        result = r1.subtract(r2)
        self.assertEqual(result.get_value(), Fraction(1, 4))

    def test_multiply(self):
        r1 = RationalNumber(2, 3)
        r2 = RationalNumber(3, 5)
        result = r1.multiply(r2)
        self.assertEqual(result.get_value(), Fraction(2, 5))

    def test_divide(self):
        r1 = RationalNumber(1, 2)
        r2 = RationalNumber(1, 4)
        result = r1.divide(r2)
        self.assertEqual(result.get_value(), Fraction(2))

    def test_divide_by_zero(self):
        r1 = RationalNumber(1, 2)
        r2 = RationalNumber(0, 1)
        result = r1.divide(r2)
        self.assertTrue(result.is_nan())

    def test_str(self):
        r = RationalNumber(3, 5)
        self.assertEqual(str(r), "3/5")

if __name__ == '__main__':
    unittest.main()
