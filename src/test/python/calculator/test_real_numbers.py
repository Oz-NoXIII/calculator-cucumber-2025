# test_real_number.py
import math
import unittest

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

    def test_inverse(self):
        r1 = RealNumber(5.0)
        result = r1.inverse()
        self.assertAlmostEqual(result.get_value(), 0.2)

    def test_e(self):
        a = RealNumber("e")
        self.assertEqual(a.get_value(), math.e)

    def test_pi(self):
        a = RealNumber("pi")
        self.assertEqual(a.get_value(), math.pi)

    def test_error_str(self):
        self.assertRaises(ValueError, lambda: RealNumber("mauvaise valeur"))

    def test_rand(self):
        a = RealNumber(10)
        result = a.rand()
        self.assertTrue(0 <= result.get_value() <= 1)

    def test_power(self):
        r1 = RealNumber(2.0)
        r2 = RealNumber(3.0)
        result = r1.pow(r2)
        self.assertAlmostEqual(result.get_value(), 8.0)

    def test_nroot(self):
        r1 = RealNumber(8.0)
        r2 = RealNumber(3.0)
        result = r1.nroot(r2)
        self.assertAlmostEqual(result.get_value(), 2.0)

    def test_zero_nroot_by_zero(self):
        a = RealNumber(0.0)
        result = a.nroot(RealNumber(0.0))
        self.assertTrue(result.is_nan(), "Expected NaN from 0.0 nroot 0.0")

    def test_sinus(self):
        a = RealNumber(math.pi / 2)
        result = a.sin()
        self.assertEqual(result.get_value(), 1)

    def test_cosinus(self):
        a = RealNumber(math.pi)
        result = a.cos()
        self.assertEqual(result.get_value(), -1)

    def test_tangent(self):
        a = RealNumber(0)
        result = a.tan()
        self.assertEqual(result.get_value(), 0)

    def test_tangent_by_zero(self):
        a = RealNumber(math.pi / 2)
        result = a.tan()
        self.assertTrue(result.is_nan(), "Expected NaN from tan (pi/2)")

    def test_sinus_by_zero(self):
        a = RealNumber(0)
        result = a.sin()
        self.assertEqual(result.get_value(), 0)

    def test_cosinus_by_zero(self):
        a = RealNumber(0)
        result = a.cos()
        self.assertEqual(result.get_value(), 1)

    def test_arcsinus(self):
        a = RealNumber(0)
        result = a.arcsin()
        self.assertEqual(result.get_value(), 0)

    def test_arccosinus(self):
        a = RealNumber(1)
        result = a.arccos()
        self.assertEqual(result.get_value(), 0)

    def test_arctangent(self):
        a = RealNumber(0)
        result = a.arctan()
        self.assertEqual(result.get_value(), 0)

    def test_arcsinus_by_negatif(self):
        a = RealNumber(-10)
        result = a.arcsin()
        self.assertTrue(result.is_nan(), "Expected NaN from arcsin(-10)")

    def test_arccosinus_by_negatif(self):
        a = RealNumber(-10)
        result = a.arccos()
        self.assertTrue(result.is_nan(), "Expected NaN from arccos(-10)")

    def test_arcsinus_by_positif(self):
        a = RealNumber(10)
        result = a.arcsin()
        self.assertTrue(result.is_nan(), "Expected NaN from arcsin(10)")

    def test_arccosinus_by_positif(self):
        a = RealNumber(10)
        result = a.arccos()
        self.assertTrue(result.is_nan(), "Expected NaN from arccos(10)")

    def test_sinushyperbolic(self):
        a = RealNumber(0)
        result = a.sinh()
        self.assertEqual(result.get_value(), 0)

    def test_cosinushyperbolic(self):
        a = RealNumber(0)
        result = a.cosh()
        self.assertEqual(result.get_value(), 1)

    def test_tangenthyperbolic(self):
        a = RealNumber(0)
        result = a.tanh()
        self.assertEqual(result.get_value(), 0)

    def test_logarithm(self):
        a = RealNumber(1)
        result = a.log()
        self.assertEqual(result.get_value(), 0)

    def test_logarithm_neperien(self):
        a = RealNumber(1)
        result = a.ln()
        self.assertEqual(result.get_value(), 0)

    def test_exponent(self):
        a = RealNumber(1)
        result = a.exp()
        self.assertEqual(result.get_value(), 2.718281828459045)

    def test_exponent_by_zero(self):
        a = RealNumber(0)
        result = a.exp()
        self.assertEqual(result.get_value(), 1)

    def test_divide_normal(self):
        r1 = RealNumber(10.0)
        r2 = RealNumber(2.0)
        result = r1.divide(r2)
        self.assertAlmostEqual(result.get_value(), 5.0)

    def test_zero_divided_by_zero(self):
        a = RealNumber(0.0)
        result = a.divide(RealNumber(0.0))
        self.assertTrue(result.is_nan(), "Expected NaN from 0.0 / 0.0")

    def test_inverse_by_zero(self):
        a = RealNumber(0.0)
        result = a.inverse()
        self.assertTrue(result.is_infinite())

    def test_logarithm_by_zero(self):
        a = RealNumber(0.0)
        result = a.log()
        self.assertTrue(result.is_nan(), "Expected NaN from log(0)")

    def test_logarithm_neperien_by_zero(self):
        a = RealNumber(0.0)
        result = a.ln()
        self.assertTrue(result.is_nan(), "Expected NaN from ln(0)")

    def test_positive_divided_by_zero(self):
        a = RealNumber(1.0)
        result = a.divide(RealNumber(0.0))
        self.assertTrue(result.is_infinite())
        self.assertGreater(result.get_value(), 0)

    def test_negative_divided_by_zero(self):
        a = RealNumber(-1.0)
        result = a.divide(RealNumber(0.0))
        self.assertTrue(result.is_infinite())
        self.assertLess(result.get_value(), 0)

    def test_sqrt_of_negative_real(self):
        a = RealNumber(-9.0)
        result = a.sqrt()
        self.assertTrue(result.is_nan(), "Expected NaN from sqrt(-9.0)")

    def test_is_nan_and_is_infinite(self):
        r_nan = RealNumber(float("nan"))
        r_inf = RealNumber(float("inf"))
        self.assertTrue(r_nan.is_nan())
        self.assertFalse(r_nan.is_infinite())
        self.assertTrue(r_inf.is_infinite())
        self.assertFalse(r_inf.is_nan())

    def test_divide_by_zero(self):
        a = RealNumber(1.0)
        b = RealNumber(0.0)
        result = a.divide(b)
        self.assertTrue(result.is_infinite())

    def test_precision_setting(self):
        RealNumber.set_precision(4)
        r = RealNumber(math.pi)
        self.assertEqual(str(r), "3.1416")

    def test_precision_getting(self):
        precision = RealNumber.get_precision()
        self.assertEqual(precision, 6)

    def test_scientific_notation(self):
        RealNumber.set_precision(6)
        r = RealNumber(6.022e23)
        self.assertEqual(r.to_scientific(), "6.022000E+23")

        r2 = RealNumber(1.6e-35)
        sci = r2.to_scientific()
        self.assertTrue("E-35" in sci or "e-35" in sci)

    def test_degrees_conversion(self):
        rad = RealNumber(math.pi)
        deg = rad.to_degrees()
        self.assertTrue(math.isclose(deg.get_value(), 180.0, rel_tol=1e-9))

    def test_radians_conversion(self):
        deg = RealNumber(180)
        rad = deg.to_radians()
        self.assertTrue(math.isclose(rad.get_value(), math.pi, rel_tol=1e-9))

    def test_sqrt(self):
        r = RealNumber(4.0)
        self.assertEqual(r.sqrt().get_value(), 2.0)

    def test_hash_and_eq(self):
        a = RealNumber(1.123456789)
        b = RealNumber(1.123456789)
        self.assertEqual(hash(a), hash(b))
        self.assertEqual(a, b)

    def test_log_positive(self):
        r = RealNumber(math.e)
        result = r.ln()
        self.assertAlmostEqual(result.get_value(), 1.0, places=6)

    def test_log_zero(self):
        r = RealNumber(0.0)
        self.assertTrue(r.log().is_nan())

    def test_log_negative(self):
        r = RealNumber(-1.0)
        self.assertTrue(r.log().is_nan())


if __name__ == "__main__":
    unittest.main()
