import unittest
from src.main.python.calculator.complex_number import ComplexNumber
from src.main.python.calculator.plus import Plus
from src.main.python.calculator.times import Times
from src.main.python.calculator.minus import Minus
from src.main.python.calculator.divides import Divides

class TestComplexNumber(unittest.TestCase):

    def test_str(self):
        c = ComplexNumber(2, 3)
        self.assertEqual(str(c), "(2+3j)")

    def test_equality(self):
        c1 = ComplexNumber(1, 2)
        c2 = ComplexNumber(1, 2)
        self.assertEqual(c1, c2)
        self.assertEqual(c1, complex(1, 2))

    def test_addition(self):
        a = ComplexNumber(1, 1)
        b = ComplexNumber(2, 3)
        expr = Plus([a, b])
        result = expr.op(a.get_value(), b.get_value())
        self.assertEqual(result, complex(3, 4))

    def test_multiplication(self):
        a = ComplexNumber(1, 2)
        b = ComplexNumber(3, 4)
        expr = Times([a, b])
        result = expr.op(a.get_value(), b.get_value())
        self.assertEqual(result, complex(-5, 10))

    def test_subtraction(self):
        a = ComplexNumber(3, 2)
        b = ComplexNumber(1, 1)
        expr = Minus([a, b])
        result = expr.op(a.get_value(), b.get_value())
        self.assertEqual(result, complex(2, 1))

    def test_division(self):
        a = ComplexNumber(2, 3)
        b = ComplexNumber(1, -1)
        expr = Divides([a, b])
        result = expr.op(a.get_value(), b.get_value())
        self.assertAlmostEqual(result.real, -0.5, places=9)
        self.assertAlmostEqual(result.imag, 2.5, places=9)

    def test_division_by_zero_complex(self):
        a = ComplexNumber(1, 1)
        b = ComplexNumber(0, 0)
        expr = Divides([a, b])
        with self.assertRaises(ZeroDivisionError):
            expr.op(a.get_value(), b.get_value())

if __name__ == '__main__':
    unittest.main()
