import unittest

from src.main.python.calculator.complex_number import ComplexNumber
from src.main.python.calculator.arccosinus import Arccosinus
from src.main.python.calculator.illegal_construction import IllegalConstruction
from src.main.python.calculator.integer_number import IntegerNumber
from src.main.python.calculator.my_number import MyNumber
from src.main.python.calculator.notation import Notation
from src.main.python.calculator.rational_number import RationalNumber
from src.main.python.calculator.real_number import RealNumber
from src.main.python.calculator.times import Times


class TestArccosinus(unittest.TestCase):

    value1 = MyNumber(IntegerNumber(8))

    value2 = MyNumber(RealNumber(8.0))

    value3 = MyNumber(RationalNumber(8, 1))

    value4 = MyNumber(ComplexNumber(1, 2))

    def setUp(self):
        params = [self.value1]
        params2 = [self.value2]
        params3 = [self.value3]
        params4 = [self.value4]
        try:
            self.op = Arccosinus(params)
            self.op2 = Arccosinus(params2)
            self.op3 = Arccosinus(params3)
            self.op4 = Arccosinus(params4)
        except IllegalConstruction as e:
            self.fail(e)

    def test_constructor(self):
        self.assertRaises(IllegalConstruction, lambda: Arccosinus(None))
        try:
            self.assertIsNot(self.op, Times([]))
        except IllegalConstruction as e:
            self.fail(e)

    def test_equals(self):
        p = [self.value1]
        try:
            e = Arccosinus(p, Notation.INFIX)
            self.assertEqual(self.op, e)
            self.assertEqual(e, e)
            self.assertNotEqual(
                e,
                Arccosinus(
                    [MyNumber(IntegerNumber(5))],
                    Notation.INFIX,
                ),
            )
        except IllegalConstruction as e:
            self.fail(e)

    def test_equals_integer(self):
        p = [self.value1]
        try:
            e = Arccosinus(p, Notation.INFIX)
            self.assertEqual(self.op, e)
        except IllegalConstruction as e:
            self.fail(e)

    def test_equals_real(self):
        p = [self.value2]
        try:
            e = Arccosinus(p, Notation.INFIX)
            self.assertEqual(self.op2, e)
        except IllegalConstruction as e:
            self.fail(e)

    def test_equals_rational(self):
        p = [self.value3]
        try:
            e = Arccosinus(p, Notation.INFIX)
            self.assertEqual(self.op3, e)
        except IllegalConstruction as e:
            self.fail(e)

    def test_equals_complex(self):
        p = [self.value4]
        try:
            e = Arccosinus(p, Notation.INFIX)
            self.assertEqual(self.op4, e)
        except IllegalConstruction as e:
            self.fail(e)

    def test_hash_code(self):
        p = [self.value1]
        try:
            e = Arccosinus(p, Notation.INFIX)
            self.assertEqual(hash(self.op), hash(e))
        except IllegalConstruction as e:
            self.fail(e)

    def test_none_param_list(self):
        params = None
        self.assertRaises(IllegalConstruction, lambda: Arccosinus(params))


if __name__ == "__main__":
    unittest.main()
