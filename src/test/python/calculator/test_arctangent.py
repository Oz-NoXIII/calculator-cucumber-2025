import unittest

from src.main.python.calculator.arctangent import Arctangent
from src.main.python.calculator.complex_number import ComplexNumber
from src.main.python.calculator.illegal_construction import IllegalConstruction
from src.main.python.calculator.integer_number import IntegerNumber
from src.main.python.calculator.my_number import MyNumber
from src.main.python.calculator.notation import Notation
from src.main.python.calculator.rational_number import RationalNumber
from src.main.python.calculator.real_number import RealNumber
from src.main.python.calculator.times import Times


class TestArctangent(unittest.TestCase):

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
            self.op = Arctangent(params)
            self.op2 = Arctangent(params2)
            self.op3 = Arctangent(params3)
            self.op4 = Arctangent(params4)
        except IllegalConstruction as e:
            self.fail(e)

    def test_constructor(self):
        self.assertRaises(IllegalConstruction, lambda: Arctangent(None))
        try:
            self.assertIsNot(self.op, Times([]))
        except IllegalConstruction as e:
            self.fail(e)

    def test_arctangent(self):
        p = MyNumber(RealNumber(0))
        result = Arctangent([p], Notation.INFIX)
        self.assertEqual(RealNumber(0).arctan().get_value(), result.op(RealNumber(0)).get_value())

        p2 = MyNumber(IntegerNumber(0))
        result2 = Arctangent([p2], Notation.INFIX)
        self.assertEqual(IntegerNumber(0).arctan().get_value(), result2.op(IntegerNumber(0)).get_value())

        p = MyNumber(ComplexNumber(0, 0))
        result = Arctangent([p], Notation.INFIX)
        self.assertEqual(ComplexNumber(0, 0).arctan().get_value(), result.op(ComplexNumber(0, 0)).get_value())

        p = MyNumber(RationalNumber(0, 1))
        result = Arctangent([p], Notation.INFIX)
        self.assertEqual(RationalNumber(0, 1).arctan().get_value(), result.op(RationalNumber(0, 1)).get_value())

    def test_equals(self):
        p = [self.value1]
        try:
            e = Arctangent(p, Notation.INFIX)
            self.assertEqual(self.op, e)
            self.assertEqual(e, e)
            self.assertNotEqual(
                e,
                Arctangent(
                    [MyNumber(IntegerNumber(5))],
                    Notation.INFIX,
                ),
            )
        except IllegalConstruction as e:
            self.fail(e)

    def test_equals_integer(self):
        p = [self.value1]
        try:
            e = Arctangent(p, Notation.INFIX)
            self.assertEqual(self.op, e)
        except IllegalConstruction as e:
            self.fail(e)

    def test_equals_real(self):
        p = [self.value2]
        try:
            e = Arctangent(p, Notation.INFIX)
            self.assertEqual(self.op2, e)
        except IllegalConstruction as e:
            self.fail(e)

    def test_equals_rational(self):
        p = [self.value3]
        try:
            e = Arctangent(p, Notation.INFIX)
            self.assertEqual(self.op3, e)
        except IllegalConstruction as e:
            self.fail(e)

    def test_equals_complex(self):
        p = [self.value4]
        try:
            e = Arctangent(p, Notation.INFIX)
            self.assertEqual(self.op4, e)
        except IllegalConstruction as e:
            self.fail(e)

    def test_hash_code(self):
        p = [self.value1]
        try:
            e = Arctangent(p, Notation.INFIX)
            self.assertEqual(hash(self.op), hash(e))
        except IllegalConstruction as e:
            self.fail(e)

    def test_none_param_list(self):
        params = None
        self.assertRaises(IllegalConstruction, lambda: Arctangent(params))

    def test_None(self):
        try:
            result = self.op is None
            self.assertFalse(result)
        except Exception as e:
            self.fail(f"An exception was thrown: {e}")
        self.op = None
        self.assertIsNone(self.op)


if __name__ == "__main__":
    unittest.main()
