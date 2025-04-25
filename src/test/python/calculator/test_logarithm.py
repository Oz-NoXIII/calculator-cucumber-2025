import unittest

from src.main.python.calculator.illegal_construction import IllegalConstruction
from src.main.python.calculator.integer_number import IntegerNumber
from src.main.python.calculator.real_number import RealNumber
from src.main.python.calculator.complex_number import ComplexNumber
from src.main.python.calculator.rational_number import RationalNumber
from src.main.python.calculator.my_number import MyNumber
from src.main.python.calculator.notation import Notation
from src.main.python.calculator.logarithm import Logarithm
from src.main.python.calculator.times import Times


class TestLogarithm(unittest.TestCase):

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
            self.op = Logarithm(params)
            self.op2 = Logarithm(params2)
            self.op3 = Logarithm(params3)
            self.op4 = Logarithm(params4)
        except IllegalConstruction as e:
            self.fail(e)

    def test_constructor(self):
        self.assertRaises(IllegalConstruction, lambda: Logarithm(None))
        try:
            self.assertIsNot(self.op, Times([]))
        except IllegalConstruction as e:
            self.fail(e)

    def test_equals(self):
        p = [self.value1]
        try:
            e = Logarithm(p, Notation.INFIX)
            self.assertEqual(self.op, e)
            self.assertEqual(e, e)
            self.assertNotEqual(
                e,
                Logarithm(
                    [MyNumber(IntegerNumber(5))],
                    Notation.INFIX,
                ),
            )
        except IllegalConstruction as e:
            self.fail(e)

    def test_equals_integer(self):
        p = [self.value1]
        try:
            e = Logarithm(p, Notation.INFIX)
            self.assertEqual(self.op, e)
        except IllegalConstruction as e:
            self.fail(e)

    def test_equals_real(self):
        p = [self.value2]
        try:
            e = Logarithm(p, Notation.INFIX)
            self.assertEqual(self.op2, e)
        except IllegalConstruction as e:
            self.fail(e)

    def test_equals_rational(self):
        p = [self.value3]
        try:
            e = Logarithm(p, Notation.INFIX)
            self.assertEqual(self.op3, e)
        except IllegalConstruction as e:
            self.fail(e)

    def test_equals_complex(self):
        p = [self.value4]
        try:
            e = Logarithm(p, Notation.INFIX)
            self.assertEqual(self.op4, e)
        except IllegalConstruction as e:
            self.fail(e)

    def test_hash_code(self):
        p = [self.value1]
        try:
            e = Logarithm(p, Notation.INFIX)
            self.assertEqual(hash(self.op), hash(e))
        except IllegalConstruction as e:
            self.fail(e)

    def test_none_param_list(self):
        params = None
        self.assertRaises(IllegalConstruction, lambda: Logarithm(params))

    def test_logarithm_null_integer(self):
        p = [MyNumber(IntegerNumber(0))]
        try:
            op = Logarithm(p)
            result = op.op(IntegerNumber(0))
            self.assertTrue(result.is_nan())

        except IllegalConstruction as e:
            self.fail(e)

    def test_logarithm_null_real(self):
        p = [MyNumber(RealNumber(0))]
        try:
            op = Logarithm(p)
            result = op.op(RealNumber(0))
            self.assertTrue(result.is_nan())

        except IllegalConstruction as e:
            self.fail(e)

    def test_logarithm_null_rational(self):
        p = [MyNumber(RationalNumber(0, 0))]
        try:
            op = Logarithm(p)
            result = op.op(RationalNumber(0, 0))
            self.assertTrue(result.is_nan())

        except IllegalConstruction as e:
            self.fail(e)

    def test_logarithm_null_complex(self):
        p = [MyNumber(ComplexNumber(0, 0))]
        try:
            op = Logarithm(p)
            result = op.op(ComplexNumber(0, 0))
            self.assertTrue(result.is_nan())

        except IllegalConstruction as e:
            self.fail(e)

    def test_logarithm_negative_integer(self):
        p = [MyNumber(IntegerNumber(-2))]
        try:
            op = Logarithm(p)
            result = op.op(IntegerNumber(-2))
            self.assertTrue(result.is_nan())

        except IllegalConstruction as e:
            self.fail(e)

    def test_logarithm_negative_real(self):
        p = [MyNumber(RealNumber(-2))]
        try:
            op = Logarithm(p)
            result = op.op(RealNumber(-2))
            self.assertTrue(result.is_nan())

        except IllegalConstruction as e:
            self.fail(e)

    def test_logarithm_negative_rational(self):
        p = [MyNumber(RationalNumber(-2, 1))]
        try:
            op = Logarithm(p)
            result = op.op(RationalNumber(-2, 1))
            self.assertTrue(result.is_nan())

        except IllegalConstruction as e:
            self.fail(e)

    def test_logarithm_negative_complex(self):
        pass

if __name__ == "__main__":
    unittest.main()
