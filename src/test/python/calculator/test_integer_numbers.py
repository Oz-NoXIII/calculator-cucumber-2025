import unittest

from src.main.python.calculator.integer_number import IntegerNumber


class TestIntegerNumber(unittest.TestCase):

    def test_create(self):
        n = IntegerNumber(5)
        self.assertEqual(n.get_value(), 5)

    def test_add(self):
        result = IntegerNumber(3).add(IntegerNumber(2))
        self.assertEqual(result.get_value(), 5)

    def test_subtract(self):
        result = IntegerNumber(5).subtract(IntegerNumber(3))
        self.assertEqual(result.get_value(), 2)

    def test_multiply(self):
        result = IntegerNumber(4).multiply(IntegerNumber(3))
        self.assertEqual(result.get_value(), 12)

    def test_inverse(self):
        result = IntegerNumber(5).inverse()
        self.assertEqual(result.get_value(), 0)

    def test_divide(self):
        result = IntegerNumber(10).divide(IntegerNumber(2))
        self.assertEqual(result.get_value(), 5)

    def test_power(self):
        result = IntegerNumber(10).pow(IntegerNumber(2))
        self.assertEqual(result.get_value(), 100)

    def test_nroot(self):
        result = IntegerNumber(8).nroot(IntegerNumber(3))
        self.assertEqual(result.get_value(), 2)

    def test_root_by_zero_returns_nan(self):
        result = IntegerNumber(1).nroot(IntegerNumber(0))
        self.assertTrue(result.is_nan(), "Expected NaN result for nroot by zero")

    def test_e(self):
        a = IntegerNumber("e")
        self.assertEqual(a.get_value(), 2)

    def test_pi(self):
        a = IntegerNumber("pi")
        self.assertEqual(a.get_value(), 3)

    def test_error_str(self):
        self.assertRaises(ValueError, lambda: IntegerNumber("mauvaise valeur"))

    def test_sinus(self):
        a = IntegerNumber(3)
        result = a.sin()
        self.assertEqual(result.get_value(), 0)

    def test_cosinus(self):
        a = IntegerNumber(3)
        result = a.cos()
        self.assertEqual(result.get_value(), 0)

    def test_tangent(self):
        a = IntegerNumber(0)
        result = a.tan()
        self.assertEqual(result.get_value(), 0)

    def test_sinus_by_zero(self):
        a = IntegerNumber(0)
        result = a.sin()
        self.assertEqual(result.get_value(), 0)

    def test_cosinus_by_zero(self):
        a = IntegerNumber(0)
        result = a.cos()
        self.assertEqual(result.get_value(), 1)

    def test_arcsinus(self):
        a = IntegerNumber(0)
        result = a.arcsin()
        self.assertEqual(result.get_value(), 0)

    def test_arccosinus(self):
        a = IntegerNumber(1)
        result = a.arccos()
        self.assertEqual(result.get_value(), 0)

    def test_arctangent(self):
        a = IntegerNumber(0)
        result = a.arctan()
        self.assertEqual(result.get_value(), 0)

    def test_arcsinus_by_negatif(self):
        a = IntegerNumber(-10)
        result = a.arcsin()
        self.assertTrue(result.is_nan(), "Expected NaN result for arcsin(-10)")

    def test_arccosinus_by_negatif(self):
        a = IntegerNumber(-10)
        result = a.arccos()
        self.assertTrue(result.is_nan(), "Expected NaN result for arccos(-10)")

    def test_arcsinus_by_positif(self):
        a = IntegerNumber(10)
        result = a.arcsin()
        self.assertTrue(result.is_nan(), "Expected NaN result for arcsin(10)")

    def test_arccosinus_by_positif(self):
        a = IntegerNumber(10)
        result = a.arccos()
        self.assertTrue(result.is_nan(), "Expected NaN result for arccos(10)")

    def test_sinushyperbolic(self):
        a = IntegerNumber(0)
        result = a.sinh()
        self.assertEqual(result.get_value(), 0)

    def test_cosinushyperbolic(self):
        a = IntegerNumber(0)
        result = a.cosh()
        self.assertEqual(result.get_value(), 1)

    def test_tangenthyperbolic(self):
        a = IntegerNumber(0)
        result = a.tanh()
        self.assertEqual(result.get_value(), 0)

    def test_logarithm(self):
        a = IntegerNumber(1)
        result = a.log()
        self.assertEqual(result.get_value(), 0)

    def test_logarithm_neperien(self):
        a = IntegerNumber(1)
        result = a.ln()
        self.assertEqual(result.get_value(), 0)

    def test_exponent(self):
        a = IntegerNumber(1)
        result = a.exp()
        self.assertEqual(result.get_value(), 2)

    def test_exponent_by_zero(self):
        a = IntegerNumber(0)
        result = a.exp()
        self.assertEqual(result.get_value(), 1)

    def test_divide_by_zero_returns_nan(self):
        result = IntegerNumber(1).divide(IntegerNumber(0))
        self.assertTrue(result.is_nan(), "Expected NaN result for division by zero")

    def test_inverse_by_zero_returns_nan(self):
        result = IntegerNumber(0).inverse()
        self.assertTrue(result.is_nan(), "Expected NaN result for division by zero")

    def test_logarithm_by_zero_returns_nan(self):
        result = IntegerNumber(0).log()
        self.assertTrue(result.is_nan(), "Expected NaN result for division by zero")

    def test_logarithm_neperien_by_zero_returns_nan(self):
        result = IntegerNumber(0).ln()
        self.assertTrue(result.is_nan(), "Expected NaN result for division by zero")

    def test_is_nan_and_infinite(self):
        n = IntegerNumber(7)
        self.assertFalse(n.is_nan())
        self.assertFalse(n.is_infinite())

    def test_get_value(self):
        n = IntegerNumber(5)
        n1 = IntegerNumber(12)
        self.assertEqual(n.get_value(), 5)
        self.assertEqual(n1.get_value(), 12)

    def test_get_value_nan(self):
        n = IntegerNumber(5)
        re = n.divide(IntegerNumber(0))
        self.assertEqual(re.get_value().__str__(), "nan")


if __name__ == "__main__":
    unittest.main()
