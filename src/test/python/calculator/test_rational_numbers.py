import unittest
from fractions import Fraction

from src.main.python.calculator.rational_number import RationalNumber
from src.main.python.calculator.plus import Plus
from src.main.python.calculator.divides import Divides
from src.main.python.calculator.times import Times
from src.main.python.calculator.minus import Minus

class TestRationalNumber(unittest.TestCase):

    def test_create_simple_fraction(self):
        r = RationalNumber(1, 2)
        self.assertEqual(str(r), "1/2")

    def test_create_whole_number(self):
        r = RationalNumber(4, 2)
        self.assertEqual(str(r), "2")

    def test_equal_fractions(self):
        self.assertEqual(RationalNumber(2, 4), RationalNumber(1, 2))

    def test_addition(self):
        r1 = RationalNumber(1, 3)
        r2 = RationalNumber(1, 6)
        expr = Plus([r1, r2])
        result = expr.op(r1.get_value(), r2.get_value())
        self.assertEqual(result, RationalNumber(1,2))

    def test_subtraction(self):
        r1 = RationalNumber(1, 3)
        r2 = RationalNumber(1, 6)
        expr = Minus([r1, r2])
        result = expr.op(r1.get_value(), r2.get_value())
        self.assertEqual(result, RationalNumber(1,6))

    def test_multiplication(self):
        r1 = RationalNumber(1, 3)
        r2 = RationalNumber(1, 6)
        expr = Times([r1, r2])
        result = expr.op(r1.get_value(), r2.get_value())
        self.assertEqual(result, RationalNumber(1, 18))

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            RationalNumber(1, 0)

if __name__ == '__main__':
    unittest.main()
