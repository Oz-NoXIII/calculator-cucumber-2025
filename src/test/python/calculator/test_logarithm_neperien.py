import unittest

from src.main.python.calculator.complex_number import ComplexNumber
from src.main.python.calculator.illegal_construction import IllegalConstruction
from src.main.python.calculator.integer_number import IntegerNumber
from src.main.python.calculator.logarithmNeperien import LogarithmNeperien
from src.main.python.calculator.my_number import MyNumber
from src.main.python.calculator.notation import Notation
from src.main.python.calculator.rational_number import RationalNumber
from src.main.python.calculator.real_number import RealNumber
from src.main.python.calculator.times import Times


class TestLogarithmNeperien(unittest.TestCase):

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
            self.op = LogarithmNeperien(params)
            self.op2 = LogarithmNeperien(params2)
            self.op3 = LogarithmNeperien(params3)
            self.op4 = LogarithmNeperien(params4)
        except IllegalConstruction as e:
            self.fail(e)

    def test_constructor(self):
        self.assertRaises(IllegalConstruction, lambda: LogarithmNeperien(None))
        try:
            self.assertIsNot(self.op, Times([]))
        except IllegalConstruction as e:
            self.fail(e)

    def test_logarithmneperien(self):
        p = MyNumber(RealNumber(10))
        result = LogarithmNeperien([p], Notation.INFIX)
        self.assertEqual(RealNumber(10).ln().get_value(), result.op(RealNumber(10)).get_value())

        p2 = MyNumber(IntegerNumber(10))
        result2 = LogarithmNeperien([p2], Notation.INFIX)
        self.assertEqual(IntegerNumber(10).ln().get_value(), result2.op(IntegerNumber(10)).get_value())

        p = MyNumber(ComplexNumber(10, 0))
        result = LogarithmNeperien([p], Notation.INFIX)
        self.assertEqual(ComplexNumber(10, 0).ln().get_value(), result.op(ComplexNumber(10, 0)).get_value())

        p = MyNumber(RationalNumber(10, 1))
        result = LogarithmNeperien([p], Notation.INFIX)
        self.assertEqual(RationalNumber(10, 1).ln().get_value(), result.op(RationalNumber(10, 1)).get_value())

    def test_equals(self):
        p = [self.value1]
        try:
            e = LogarithmNeperien(p, Notation.INFIX)
            self.assertEqual(self.op, e)
            self.assertEqual(e, e)
            self.assertNotEqual(
                e,
                LogarithmNeperien(
                    [MyNumber(IntegerNumber(5))],
                    Notation.INFIX,
                ),
            )
        except IllegalConstruction as e:
            self.fail(e)

    def test_equals_integer(self):
        p = [self.value1]
        try:
            e = LogarithmNeperien(p, Notation.INFIX)
            self.assertEqual(self.op, e)
        except IllegalConstruction as e:
            self.fail(e)

    def test_equals_real(self):
        p = [self.value2]
        try:
            e = LogarithmNeperien(p, Notation.INFIX)
            self.assertEqual(self.op2, e)
        except IllegalConstruction as e:
            self.fail(e)

    def test_equals_rational(self):
        p = [self.value3]
        try:
            e = LogarithmNeperien(p, Notation.INFIX)
            self.assertEqual(self.op3, e)
        except IllegalConstruction as e:
            self.fail(e)

    def test_equals_complex(self):
        p = [self.value4]
        try:
            e = LogarithmNeperien(p, Notation.INFIX)
            self.assertEqual(self.op4, e)
        except IllegalConstruction as e:
            self.fail(e)

    def test_hash_code(self):
        p = [self.value1]
        try:
            e = LogarithmNeperien(p, Notation.INFIX)
            self.assertEqual(hash(self.op), hash(e))
        except IllegalConstruction as e:
            self.fail(e)

    def test_none_param_list(self):
        params = None
        self.assertRaises(IllegalConstruction, lambda: LogarithmNeperien(params))

    def test_logarithm_neperien_null_integer(self):
        p = [MyNumber(IntegerNumber(0))]
        try:
            op = LogarithmNeperien(p)
            result = op.op(IntegerNumber(0))
            self.assertTrue(result.is_nan())

        except IllegalConstruction as e:
            self.fail(e)

    def test_logarithm_neperien_null_real(self):
        p = [MyNumber(RealNumber(0))]
        try:
            op = LogarithmNeperien(p)
            result = op.op(RealNumber(0))
            self.assertTrue(result.is_nan())

        except IllegalConstruction as e:
            self.fail(e)

    def test_logarithm_neperien_null_rational(self):
        p = [MyNumber(RationalNumber(0, 0))]
        try:
            op = LogarithmNeperien(p)
            result = op.op(RationalNumber(0, 0))
            self.assertTrue(result.is_nan())

        except IllegalConstruction as e:
            self.fail(e)

    def test_logarithm_neperien_null_complex(self):
        p = [MyNumber(ComplexNumber(0, 0))]
        try:
            op = LogarithmNeperien(p)
            result = op.op(ComplexNumber(0, 0))
            self.assertTrue(result.is_nan())

        except IllegalConstruction as e:
            self.fail(e)

    def test_logarithm_neperien_negative_integer(self):
        p = [MyNumber(IntegerNumber(-2))]
        try:
            op = LogarithmNeperien(p)
            result = op.op(IntegerNumber(-2))
            self.assertTrue(result.is_nan())

        except IllegalConstruction as e:
            self.fail(e)

    def test_logarithm_neperien_negative_real(self):
        p = [MyNumber(RealNumber(-2))]
        try:
            op = LogarithmNeperien(p)
            result = op.op(RealNumber(-2))
            self.assertTrue(result.is_nan())

        except IllegalConstruction as e:
            self.fail(e)

    def test_logarithm_neperien_negative_rational(self):
        p = [MyNumber(RationalNumber(-2, 1))]
        try:
            op = LogarithmNeperien(p)
            result = op.op(RationalNumber(-2, 1))
            self.assertTrue(result.is_nan())

        except IllegalConstruction as e:
            self.fail(e)

    def test_logarithm_neperien_negative_complex(self):
        pass


if __name__ == "__main__":
    unittest.main()
