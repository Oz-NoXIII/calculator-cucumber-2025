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
