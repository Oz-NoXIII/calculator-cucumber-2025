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


