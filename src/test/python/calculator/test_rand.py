import unittest

from src.main.python.calculator.complex_number import ComplexNumber
from src.main.python.calculator.illegal_construction import IllegalConstruction
from src.main.python.calculator.integer_number import IntegerNumber
from src.main.python.calculator.my_number import MyNumber
from src.main.python.calculator.notation import Notation
from src.main.python.calculator.rand import Rand
from src.main.python.calculator.rational_number import RationalNumber
from src.main.python.calculator.real_number import RealNumber
from src.main.python.calculator.times import Times


class TestRand(unittest.TestCase):

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
            self.op = Rand(params)
            self.op2 = Rand(params2)
            self.op3 = Rand(params3)
            self.op4 = Rand(params4)
        except IllegalConstruction as e:
            self.fail(e)

    def test_constructor(self):
        self.assertRaises(IllegalConstruction, lambda: Rand(None))
        try:
            self.assertIsNot(self.op, Times([]))
        except IllegalConstruction as e:
            self.fail(e)

    def test_rand(self):
        p = MyNumber(RealNumber(0))
        result = Rand([p], Notation.INFIX)
        self.assertTrue(0 <= result.op(RealNumber(0)).get_value() <= 1)

        p2 = MyNumber(IntegerNumber(10))
        result2 = Rand([p2], Notation.INFIX)
        self.assertTrue(0 <= result.op(IntegerNumber(0)).get_value() <= 10)

        p = MyNumber(ComplexNumber(0, 0))
        result = Rand([p], Notation.INFIX)
        self.assertTrue(0 <= result.op(ComplexNumber(0, 0)).get_value().real <= 1)
        self.assertTrue(0 <= result.op(ComplexNumber(0, 0)).get_value().imag <= 1)

        p = MyNumber(RationalNumber(10, 7))
        result = Rand([p], Notation.INFIX)
        self.assertTrue(0 <= result.op(RationalNumber(10, 7)).get_value().numerator <= 10)
        self.assertTrue(0 <= result.op(RationalNumber(10, 7)).get_value().denominator <= 7)

    def test_equals(self):
        p = [self.value1]
        try:
            e = Rand(p, Notation.INFIX)
            self.assertEqual(self.op, e)
            self.assertEqual(e, e)
            self.assertNotEqual(
                e,
                Rand(
                    [MyNumber(IntegerNumber(5))],
                    Notation.INFIX,
                ),
            )
        except IllegalConstruction as e:
            self.fail(e)

    def test_equals_integer(self):
        p = [self.value1]
        try:
            e = Rand(p, Notation.INFIX)
            self.assertEqual(self.op, e)
        except IllegalConstruction as e:
            self.fail(e)

    def test_equals_real(self):
        p = [self.value2]
        try:
            e = Rand(p, Notation.INFIX)
            self.assertEqual(self.op2, e)
        except IllegalConstruction as e:
            self.fail(e)

    def test_equals_rational(self):
        p = [self.value3]
        try:
            e = Rand(p, Notation.INFIX)
            self.assertEqual(self.op3, e)
        except IllegalConstruction as e:
            self.fail(e)

    def test_equals_complex(self):
        p = [self.value4]
        try:
            e = Rand(p, Notation.INFIX)
            self.assertEqual(self.op4, e)
        except IllegalConstruction as e:
            self.fail(e)

    def test_hash_code(self):
        p = [self.value1]
        try:
            e = Rand(p, Notation.INFIX)
            self.assertEqual(hash(self.op), hash(e))
        except IllegalConstruction as e:
            self.fail(e)

    def test_none_param_list(self):
        params = None
        self.assertRaises(IllegalConstruction, lambda: Rand(params))


if __name__ == "__main__":
    unittest.main()
