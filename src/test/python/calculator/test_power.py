import unittest

from src.main.python.calculator.illegal_construction import IllegalConstruction
from src.main.python.calculator.integer_number import IntegerNumber
from src.main.python.calculator.real_number import RealNumber
from src.main.python.calculator.rational_number import RationalNumber
from src.main.python.calculator.my_number import MyNumber
from src.main.python.calculator.notation import Notation
from src.main.python.calculator.power import Power
from src.main.python.calculator.plus import Plus

class TestPower(unittest.TestCase):

    value1 = MyNumber(IntegerNumber(8))
    value2 = MyNumber(IntegerNumber(6))

    value3 = MyNumber(RealNumber(8.0))
    value4 = MyNumber(RealNumber(6.0))

    value5 = MyNumber(RationalNumber(8, 1))
    value6 = MyNumber(RationalNumber(6, 1))

    def setUp(self):
        params = [self.value1, self.value2]
        try:
            self.op = Power(params)
        except IllegalConstruction as e:
            self.fail(e)

    def test_constructor(self):
        self.assertRaises(IllegalConstruction, lambda: Power(None))
        try:
            self.assertIsNot(self.op, Plus([]))
        except IllegalConstruction as e:
            self.fail(e)

    def test_equals_integer(self):
        p = [self.value1, self.value2]
        try:
            e = Power(p, Notation.INFIX)
            print(self.op)
            print(e)
            self.assertEqual(self.op, e)
        except IllegalConstruction as e:
            self.fail(e)

    def test_hash_code(self):
        p = [self.value1, self.value2]
        try:
            e = Power(p, Notation.INFIX)
            self.assertEqual(hash(self.op), hash(e))
        except IllegalConstruction as e:
            self.fail(e)

    def test_none_param_list(self):
        params = None
        self.assertRaises(IllegalConstruction, lambda: Power(params))


if __name__ == "__main__":
    unittest.main()
