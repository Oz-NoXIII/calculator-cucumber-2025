import unittest

from src.main.python.calculator.illegal_construction import IllegalConstruction
from src.main.python.calculator.integer_number import IntegerNumber
from src.main.python.calculator.real_number import RealNumber
from src.main.python.calculator.complex_number import ComplexNumber
from src.main.python.calculator.rational_number import RationalNumber
from src.main.python.calculator.my_number import MyNumber
from src.main.python.calculator.notation import Notation
from src.main.python.calculator.power import Power
from src.main.python.calculator.times import Times


class TestPower(unittest.TestCase):


    value1 = MyNumber(IntegerNumber(8))
    value2 = MyNumber(IntegerNumber(6))

    value3 = MyNumber(RealNumber(8.0))
    value4 = MyNumber(RealNumber(6.0))

    value5 = MyNumber(RationalNumber(8, 1))
    value6 = MyNumber(RationalNumber(6, 1))

    value7 = MyNumber(ComplexNumber(1, 2))
    value8 = MyNumber(ComplexNumber(1, 2))

    def setUp(self):
        params = [self.value1, self.value2]
        params2 = [self.value3, self.value4]
        params3 = [self.value5, self.value6]
        params4 = [self.value7, self.value8]
        try:
            self.op = Power(params)
            self.op2 = Power(params2)
            self.op3 = Power(params3)
            self.op4 = Power(params4)
        except IllegalConstruction as e:
            self.fail(e)

    def test_constructor(self):
        self.assertRaises(IllegalConstruction, lambda: Power(None))
        try:
            self.assertIsNot(self.op, Times([]))
        except IllegalConstruction as e:
            self.fail(e)

    def test_equals(self):
        p = [self.value1, self.value2]
        try:
            e = Power(p, Notation.INFIX)
            self.assertEqual(self.op, e)
            self.assertEqual(e, e)
            self.assertNotEqual(
                e,
                Power(
                    [MyNumber(IntegerNumber(5)), MyNumber(IntegerNumber(4))],
                    Notation.INFIX,
                ),
            )
        except IllegalConstruction as e:
            self.fail(e)

    def test_equals_integer(self):
        p = [self.value1, self.value2]
        try:
            e = Power(p, Notation.INFIX)
            self.assertEqual(self.op, e)
        except IllegalConstruction as e:
            self.fail(e)

    def test_equals_real(self):
        p = [self.value3, self.value4]
        try:
            e = Power(p, Notation.INFIX)
            self.assertEqual(self.op2, e)
        except IllegalConstruction as e:
            self.fail(e)

    def test_equals_rational(self):
        p = [self.value5, self.value6]
        try:
            e = Power(p, Notation.INFIX)
            self.assertEqual(self.op3, e)
        except IllegalConstruction as e:
            self.fail(e)

    def test_equals_complex(self):
        p = [self.value7, self.value8]
        try:
            e = Power(p, Notation.INFIX)
            self.assertEqual(self.op4, e)
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

    def test_power_null_integer(self):
        pn = IntegerNumber(0)
        pn2 = IntegerNumber(0)
        self.assertEqual(pn.pow(pn2).get_value(), 1)

    def test_power_null_real(self):
        pn = RealNumber(0)
        pn2 = RealNumber(0)
        self.assertEqual(pn.pow(pn2).get_value(), 1.0)

    def test_power_null_rational(self):
        pn = RationalNumber(0)
        pn2 = RationalNumber(0)
        self.assertEqual(pn.pow(pn2).get_value(), 1/1)

    def test_power_null_complex(self):
        pn = ComplexNumber(0, 0)
        pn2 = ComplexNumber(0, 0)
        result = pn.pow(pn2)
        self.assertTrue(result.is_nan())

    def test_power_negative_integer(self):
        pn = IntegerNumber(-2)
        pn2 = IntegerNumber(-4)
        self.assertEqual(pn.pow(pn2).get_value(), 0.0625)

    def test_power_negative_real(self):
        pn = RealNumber(-2.0)
        pn2 = RealNumber(-4.0)
        self.assertEqual(pn.pow(pn2).get_value(), 0.0625)

    def test_power_negative_rational(self):
        pn = RationalNumber(-2, 1)
        pn2 = RationalNumber(-4, 1)
        self.assertEqual(pn.pow(pn2).get_value(), 1/16)

if __name__ == "__main__":
    unittest.main()
