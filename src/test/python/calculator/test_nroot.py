import unittest

from src.main.python.calculator.complex_number import ComplexNumber
from src.main.python.calculator.illegal_construction import IllegalConstruction
from src.main.python.calculator.integer_number import IntegerNumber
from src.main.python.calculator.my_number import MyNumber
from src.main.python.calculator.notation import Notation
from src.main.python.calculator.nroot import Nroot
from src.main.python.calculator.plus import Plus
from src.main.python.calculator.rational_number import RationalNumber
from src.main.python.calculator.real_number import RealNumber


class TestNroot(unittest.TestCase):

    value1 = MyNumber(IntegerNumber(8))
    value2 = MyNumber(IntegerNumber(6))

    def setUp(self):
        params = [self.value1, self.value2]
        try:
            self.op = Nroot(params)
        except IllegalConstruction as e:
            self.fail(e)

    def test_constructor(self):
        self.assertRaises(IllegalConstruction, lambda: Nroot(None))
        try:
            self.assertIsNot(self.op, Plus([]))
        except IllegalConstruction as e:
            self.fail(e)

    def test_nroot(self):
        p1 = MyNumber(RealNumber(8))
        p2 = MyNumber(RealNumber(3))
        result = Nroot([p1, p2], Notation.INFIX)
        self.assertEqual(RealNumber(8).nroot(p2).get_value(), result.op(RealNumber(8), RealNumber(3)).get_value())

        p1 = MyNumber(IntegerNumber(8))
        p2 = MyNumber(IntegerNumber(3))
        result = Nroot([p1, p2], Notation.INFIX)
        self.assertEqual(IntegerNumber(8).nroot(p2).get_value(), result.op(IntegerNumber(8), IntegerNumber(3)).get_value())

        p1 = MyNumber(ComplexNumber(10, 0))
        p2 = MyNumber(ComplexNumber(10, 0))
        result = Nroot([p1, p2], Notation.INFIX)
        self.assertEqual(ComplexNumber(10, 0).nroot(p2).get_value(), result.op(ComplexNumber(10, 0), ComplexNumber(10, 0)).get_value())

        p1 = MyNumber(RationalNumber(10, 1))
        p2 = MyNumber(RationalNumber(10, 1))
        result = Nroot([p1, p2], Notation.INFIX)
        self.assertEqual(RationalNumber(10, 1).nroot(p2).get_value(), result.op(RationalNumber(10, 1), RationalNumber(10, 1)).get_value())

    def test_equals(self):
        p = [self.value1, self.value2]
        try:
            e = Nroot(p, Notation.INFIX)
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
        p = [self.value1, self.value2]
        try:
            e = Nroot(p, Notation.INFIX)
            self.assertEqual(hash(self.op), hash(e))
        except IllegalConstruction as e:
            self.fail(e)

    def test_none_param_list(self):
        params = None
        self.assertRaises(IllegalConstruction, lambda: Nroot(params))


if __name__ == "__main__":
    unittest.main()
