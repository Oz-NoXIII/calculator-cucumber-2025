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

    def test_zero_divided_by_zero(self):
        a = RealNumber(0.0)
        result = a.divide(RealNumber(0.0))
        self.assertTrue(result.is_nan(), "Expected NaN from 0.0 / 0.0")

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


    def test_hash_and_eq(self):
        a = RealNumber(1.123456789)
        b = RealNumber(1.123456789)
        self.assertEqual(hash(a), hash(b))
        self.assertEqual(a, b)


    def test_log_positive(self):
        r = RealNumber(math.e)
        result = r.log()
        self.assertAlmostEqual(result.get_value(), 1.0, places=6)

    def test_log_zero(self):
        r = RealNumber(0.0)
        self.assertTrue(r.log().is_nan())

    def test_log_negative(self):
        r = RealNumber(-1.0)
        self.assertTrue(r.log().is_nan())

if __name__ == '__main__':
    unittest.main()
