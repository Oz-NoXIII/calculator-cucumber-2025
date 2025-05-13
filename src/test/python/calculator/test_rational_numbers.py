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

    def test_nroot(self):
        r1 = RationalNumber(8, 1)
        r2 = RationalNumber(3, 1)
        result = r1.nroot(r2)
        self.assertEqual(result.get_value(), Fraction(2, 1))

    def test_nroot_by_zero(self):
        r1 = RationalNumber(1, 2)
        r2 = RationalNumber(0, 1)
        result = r1.nroot(r2)
        self.assertTrue(result.is_nan())

    def test_sinus(self):
        a = RationalNumber(0, 1)
        result = a.sin()
        self.assertEqual(
            result.get_value(), Fraction(0, 1)
        )

    def test_cosinus(self):
        a = RationalNumber(0, 1)
        result = a.cos()
        self.assertEqual(
            result.get_value(), Fraction(1, 1)
        )

    def test_tangent(self):
        a = RationalNumber(0, 1)
        result = a.tan()
        self.assertEqual(
            result.get_value(), Fraction(0, 1)
        )

    def test_sinus_by_zero(self):
        a = RationalNumber(0, 1)
        result = a.sin()
        self.assertEqual(result.get_value(), 0)

    def test_cosinus_by_zero(self):
        a = RationalNumber(0, 1)
        result = a.cos()
        self.assertEqual(result.get_value(), 1)

    def test_arcsinus(self):
        a = RationalNumber(0, 1)
        result = a.arcsin()
        self.assertEqual(
            result.get_value(), Fraction(0, 1)
        )

    def test_arccosinus(self):
        a = RationalNumber(1, 1)
        result = a.arccos()
        self.assertEqual(
            result.get_value(), Fraction(0, 1)
        )

    def test_arctangent(self):
        a = RationalNumber(0, 1)
        result = a.arctan()
        self.assertEqual(
            result.get_value(), Fraction(0, 1)
        )

    def test_arcsinus_by_negatif(self):
        a = RationalNumber(-10, 1)
        result = a.arcsin()
        self.assertTrue(result.is_nan())

    def test_arccosinus_by_negatif(self):
        a = RationalNumber(-10, 1)
        result = a.arccos()
        self.assertTrue(result.is_nan())

    def test_arcsinus_by_positif(self):
        a = RationalNumber(10, 1)
        result = a.arcsin()
        self.assertTrue(result.is_nan())

    def test_arccosinus_by_positif(self):
        a = RationalNumber(10, 1)
        result = a.arccos()
        self.assertTrue(result.is_nan())

    def test_sinushyperbolic(self):
        a = RationalNumber(0, 1)
        result = a.sinh()
        self.assertEqual(
            result.get_value(), Fraction(0, 1)
        )

    def test_cosinushyperbolic(self):
        a = RationalNumber(0, 1)
        result = a.cosh()
        self.assertEqual(
            result.get_value(), Fraction(1, 1)
        )

    def test_tangenthyperbolic(self):
        a = RationalNumber(0, 1)
        result = a.tanh()
        self.assertEqual(
            result.get_value(), Fraction(0, 1)
        )

    def test_logarithm(self):
        a = RationalNumber(1, 1)
        result = a.log()
        self.assertEqual(result.get_value(), 0)

    def test_logarithm_neperien(self):
        a = RationalNumber(1, 1)
        result = a.ln()
        self.assertEqual(result.get_value(), 0)

    def test_exponent_by_zero(self):
        a = RationalNumber(0, 1)
        result = a.exp()
        self.assertEqual(result.get_value(), 1)

    def test_exponent(self):
        a = RationalNumber(1, 1)
        result = a.exp()
        self.assertEqual(
            result.get_value(), Fraction(6121026514868073, 2251799813685248)
        )

    def test_divide_by_zero(self):
        r1 = RationalNumber(1, 2)
        r2 = RationalNumber(0, 1)
        result = r1.divide(r2)
        self.assertTrue(result.is_nan())

    def test_inverse_by_zero(self):
        r1 = RationalNumber(0, 1)
        result = r1.inverse()
        self.assertTrue(result.is_nan())

    def test_logarithm_by_zero(self):
        r1 = RationalNumber(0, 1)
        result = r1.log()
        self.assertTrue(result.is_nan())

    def test_logarithm_neperien_by_zero(self):
        r1 = RationalNumber(0, 1)
        result = r1.ln()
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
