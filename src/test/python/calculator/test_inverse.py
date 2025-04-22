import unittest

from src.main.python.calculator.inverse import Inverse
from src.main.python.calculator.illegal_construction import IllegalConstruction
from src.main.python.calculator.integer_number import IntegerNumber
from src.main.python.calculator.my_number import MyNumber
from src.main.python.calculator.notation import Notation
from src.main.python.calculator.times import Times


class TestInverse(unittest.TestCase):

    value1 = MyNumber(IntegerNumber(8))

    def setUp(self):
        params = [self.value1]
        try:
            self.op = Inverse(params, Notation.INFIX)
        except IllegalConstruction as e:
            self.fail(e)

    def test_constructor(self):
        self.assertRaises(IllegalConstruction, lambda: Inverse(None))
        try:
            self.assertIsNot(self.op, Times([]))
        except IllegalConstruction as e:
            self.fail(e)

    def test_equals(self):
        p = [self.value1]
        try:
            e = Inverse(p, Notation.INFIX)
            self.assertEqual(self.op, e)
        except IllegalConstruction as e:
            self.fail(e)

    def test_None(self):
        try:
            result = self.op is None
            self.assertFalse(result)
        except Exception as e:
            self.fail(f"An exception was thrown: {e}")
        self.op = None
        self.assertIsNone(self.op)

    def test_hash_code(self):
        p = [self.value1]
        try:
            e = Inverse(p, Notation.INFIX)
            self.assertEqual(hash(self.op), hash(e))
        except IllegalConstruction as e:
            self.fail(e)

    def test_none_param_list(self):
        params = None
        self.assertRaises(IllegalConstruction, lambda: Inverse(params))

    def test_zero_division(self):
        # Test division by zero

        params = [MyNumber(IntegerNumber(0))]
        try:
            op = Inverse(params)
            result = op.op(IntegerNumber(0))
            self.assertTrue(result.is_nan())

        except IllegalConstruction as e:
            self.fail(e)


if __name__ == "__main__":
    unittest.main()
