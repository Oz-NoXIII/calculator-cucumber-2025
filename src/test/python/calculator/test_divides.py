import unittest
from math import isnan

from src.main.python.calculator.divides import Divides
from src.main.python.calculator.illegal_construction import IllegalConstruction
from src.main.python.calculator.my_number import MyNumber
from src.main.python.calculator.notation import Notation
from src.main.python.calculator.times import Times


class TestDivides(unittest.TestCase):

    value1 = 8
    value2 = 6

    def setUp(self):
        params = [MyNumber(self.value1), MyNumber(self.value2)]
        try:
            self.op = Divides(params, Notation.INFIX)
        except IllegalConstruction as e:
            self.fail(e)

    def test_constructor(self):
        self.assertRaises(IllegalConstruction, lambda: Divides(None))
        try:
            self.assertIsNot(self.op, Times([]))
        except IllegalConstruction as e:
            self.fail(e)

    def test_equals(self):
        p = [MyNumber(self.value1), MyNumber(self.value2)]
        try:
            e = Divides(p, Notation.INFIX)
            self.assertEqual(self.op, e)
        except IllegalConstruction as e:
            self.fail(e)

    def test_None(self):
        self.assertIsNone(self.op, "Expected self.op to be None")

    def test_hash_code(self):
        p = [MyNumber(self.value1), MyNumber(self.value2)]
        try:
            e = Divides(p, Notation.INFIX)
            self.assertEqual(hash(self.op), hash(e))
        except IllegalConstruction as e:
            self.fail(e)

    def test_none_param_list(self):
        params = None
        self.assertRaises(IllegalConstruction, lambda: Divides(params))

    def test_zero_division(self):
        # Test division by zero
        params = [MyNumber(8), MyNumber(0)]
        try:
            op = Divides(params)
            result = op.op(8, 0)
            self.assertTrue(isnan(result))
        except IllegalConstruction as e:
            self.fail(e)


if __name__ == "__main__":
    unittest.main()
