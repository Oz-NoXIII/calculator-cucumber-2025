import unittest
from fractions import Fraction

from src.main.python.calculator.rational_number import RationalNumber


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

    def test_inverse(self):
        r1 = RationalNumber(2, 3)
        result = r1.inverse()
        self.assertEqual(result.get_value(), Fraction(3, 2))

    def test_divide(self):
        r1 = RationalNumber(1, 2)
        r2 = RationalNumber(1, 4)
        result = r1.divide(r2)
        self.assertEqual(result.get_value(), Fraction(2))

    def test_power(self):
        r1 = RationalNumber(2, 1)
        r2 = RationalNumber(1, 1)
        result = r1.pow(r2)
        self.assertEqual(result.get_value(), Fraction(2))

    def test_divide_by_zero(self):
        r1 = RationalNumber(1, 2)
        r2 = RationalNumber(0, 1)
        result = r1.divide(r2)
        self.assertTrue(result.is_nan())

    def test_divide_by_zero(self):
        r1 = RationalNumber(0, 1)
        result = r1.inverse()
        self.assertTrue(result.is_nan())

    def test_str(self):
        self.assertEqual(str(RationalNumber(6, 12)), "1/2")
        self.assertEqual(str(RationalNumber(18, 12)), "3/2")
        self.assertEqual(str(RationalNumber(4, 3)), "4/3")
        self.assertEqual(str(RationalNumber(-7, 3)), "-7/3")
        self.assertEqual(str(RationalNumber(3, 1)), "3")
        self.assertEqual(str(RationalNumber(1, 0)), "NaN")

    def test_mix_str(self):
        self.assertEqual(RationalNumber(6, 12).to_mixed_str(), "1/2")
        self.assertEqual(RationalNumber(18, 12).to_mixed_str(), "1 1/2")
        self.assertEqual(RationalNumber(4, 3).to_mixed_str(), "1 1/3")
        self.assertEqual(RationalNumber(-7, 3).to_mixed_str(), "-2 1/3")
        self.assertEqual(RationalNumber(3, 1).to_mixed_str(), "3")
        self.assertEqual(RationalNumber(-9, 4).to_mixed_str(), "-2 1/4")
        self.assertEqual(RationalNumber(-11, 5).to_mixed_str(), "-2 1/5")
        self.assertEqual(RationalNumber(0, 5).to_mixed_str(), "0")
        self.assertEqual(RationalNumber(0, -7).to_mixed_str(), "0")
        self.assertEqual(RationalNumber(1, 0).to_mixed_str(), "NaN")

    def test_hash(self):
        r = RationalNumber(3, 4)

        self.assertEqual(hash(r), hash(r))

    def test_is_infinite(self):

        r = RationalNumber(1, 0)
        self.assertFalse(r.is_infinite())

    def test_eq(self):
        r = RationalNumber(3, 4)
        s = RationalNumber(1, 2)
        self.assertEqual(r, r)
        self.assertNotEqual(r, s)


if __name__ == "__main__":
    unittest.main()
