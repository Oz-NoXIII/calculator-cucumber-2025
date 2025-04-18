import cmath
import unittest

from src.main.python.calculator.complex_number import ComplexNumber


class TestComplexNumber(unittest.TestCase):

    def test_addition(self):
        a = ComplexNumber(2, 3)
        b = ComplexNumber(1, -1)
        result = a.add(b)
        self.assertEqual(result.get_value(), complex(3, 2))

    def test_subtraction(self):
        a = ComplexNumber(5, 2)
        b = ComplexNumber(1, 4)
        result = a.subtract(b)
        self.assertEqual(result.get_value(), complex(4, -2))

    def test_multiplication(self):
        a = ComplexNumber(1, 2)
        b = ComplexNumber(3, 4)
        result = a.multiply(b)
        self.assertEqual(result.get_value(), complex(-5, 10))

    def test_division(self):
        a = ComplexNumber(1, 2)
        b = ComplexNumber(3, 4)
        result = a.divide(b)
        expected = complex(0.44, 0.08)
        self.assertAlmostEqual(result.get_value().real, expected.real, places=2)
        self.assertAlmostEqual(result.get_value().imag, expected.imag, places=2)

    def test_nan_on_divide_by_zero(self):
        a = ComplexNumber(1, 2)
        b = ComplexNumber(0, 0)
        result = a.divide(b)
        self.assertTrue(result.is_nan())

    def test_modulo(self):
        a = ComplexNumber(1, 2)
        b = ComplexNumber(3, 4)
        mod1 = a.modulus()
        mod2 = b.modulus()
        self.assertEqual(mod1, 2.23606797749979)
        self.assertEqual(mod2, 5.0)

    def test_conjugate(self):
        a = ComplexNumber(1, 2)
        b = ComplexNumber(3, 4)
        result1 = a.conjugate()
        result2 = b.conjugate()
        self.assertEqual(result1.get_value(), ComplexNumber(1, -2).get_value())
        self.assertEqual(result2.get_value(), ComplexNumber(3, -4).get_value())

    def test_str_(self):
        self.assertEqual(ComplexNumber(3, 0).__str__(), "(3+0j)")
        self.assertEqual(ComplexNumber(0, 4).__str__(), "4j")
        self.assertEqual(ComplexNumber(3, -2).__str__(), "(3-2j)")
        self.assertEqual(ComplexNumber(3, 2).__str__(), "(3+2j)")
        self.assertEqual(ComplexNumber(0, 0).__str__(), "0j")

    def test_eq(self):
        z1 = ComplexNumber(2, 3)
        z2 = ComplexNumber(2, 3)
        z3 = ComplexNumber(3, 2)
        self.assertEqual(z1, z2)
        self.assertNotEqual(z1, z3)
        self.assertNotEqual(z1, 5)

    def test_hash_consistency(self):
        z1 = ComplexNumber(1, 2)
        z2 = ComplexNumber(1, 2)
        z3 = ComplexNumber(2, 1)
        self.assertEqual(hash(z1), hash(z2))
        self.assertNotEqual(hash(z1), hash(z3))

    def test_is_infinite(self):
        z_inf = ComplexNumber(float("inf"), 2)
        z_inf2 = ComplexNumber(2, float("-inf"))
        z_norm = ComplexNumber(3, 4)
        self.assertTrue(z_inf.is_infinite())
        self.assertTrue(z_inf2.is_infinite())
        self.assertFalse(z_norm.is_infinite())

    def test_sqrt_positive(self):
        z = ComplexNumber(3, 4)  # sqrt(3+4i)
        z1 = ComplexNumber(-4, 0)
        root = z.sqrt().get_value()
        root1 = z1.sqrt().get_value()
        expected = cmath.sqrt(complex(3, 4))
        self.assertAlmostEqual(root.real, expected.real, places=6)
        self.assertAlmostEqual(root.imag, expected.imag, places=6)
        self.assertAlmostEqual(root1.real, 0.0, places=6)
        self.assertAlmostEqual(root1.imag, 2.0, places=6)
