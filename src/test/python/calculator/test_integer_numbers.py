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

    def test_divide(self):
        result = IntegerNumber(10).divide(IntegerNumber(2))
        self.assertEqual(result.get_value(), 5)

    def test_divide_by_zero_returns_nan(self):
        result = IntegerNumber(1).divide(IntegerNumber(0))
        self.assertTrue(result.is_nan(), "Expected NaN result for division by zero")


    def test_is_nan_and_infinite(self):
        n = IntegerNumber(7)
        self.assertFalse(n.is_nan())
        self.assertFalse(n.is_infinite())

if __name__ == '__main__':
    unittest.main()
