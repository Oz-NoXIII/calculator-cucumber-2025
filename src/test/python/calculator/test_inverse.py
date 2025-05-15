import unittest

from src.main.python.calculator.complex_number import ComplexNumber
from src.main.python.calculator.illegal_construction import IllegalConstruction
from src.main.python.calculator.integer_number import IntegerNumber
from src.main.python.calculator.inverse import Inverse, MatrixInverse
from src.main.python.calculator.matrix import Matrix
from src.main.python.calculator.my_number import MyNumber
from src.main.python.calculator.notation import Notation
from src.main.python.calculator.rational_number import RationalNumber
from src.main.python.calculator.real_number import RealNumber
from src.main.python.calculator.times import Times


class TestInverse(unittest.TestCase):

    value1 = MyNumber(IntegerNumber(8))

    def setUp(self):
        params = [self.value1]
        self.invertible_matrix = Matrix(
            [
                [MyNumber(IntegerNumber(4)), MyNumber(IntegerNumber(3))],
                [MyNumber(IntegerNumber(3)), MyNumber(IntegerNumber(2))],
            ]
        )

        self.singular_matrix = Matrix(
            [
                [MyNumber(IntegerNumber(1)), MyNumber(IntegerNumber(2))],
                [MyNumber(IntegerNumber(2)), MyNumber(IntegerNumber(4))],
            ]
        )

        self.simple_matrix = Matrix([[MyNumber(IntegerNumber(5))]])
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

    def test_inverse(self):
        p = MyNumber(RealNumber(10))
        result = Inverse([p], Notation.INFIX)
        self.assertEqual(RealNumber(10).inverse().get_value(), result.op(RealNumber(10)).get_value())

        p2 = MyNumber(IntegerNumber(10))
        result2 = Inverse([p2], Notation.INFIX)
        self.assertEqual(IntegerNumber(10).inverse().get_value(), result2.op(IntegerNumber(10)).get_value())

        p = MyNumber(ComplexNumber(10, 0))
        result = Inverse([p], Notation.INFIX)
        self.assertEqual(ComplexNumber(10, 0).inverse().get_value(), result.op(ComplexNumber(10, 0)).get_value())

        p = MyNumber(RationalNumber(10, 1))
        result = Inverse([p], Notation.INFIX)
        self.assertEqual(RationalNumber(10, 1).inverse().get_value(), result.op(RationalNumber(10, 1)).get_value())

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

    def test_inverse_of_invertible_matrix(self):

        inverse_op = MatrixInverse([self.invertible_matrix])
        result = inverse_op.op(self.invertible_matrix)

        self.assertIsInstance(result, Matrix)

        self.assertEqual(result.rows, 2)
        self.assertEqual(result.cols, 2)

        expected_values = [[-2, 3], [3, -4]]
        for i in range(2):
            for j in range(2):
                self.assertAlmostEqual(
                    result.data[i][j], expected_values[i][j], places=5
                )

    def test_inverse_of_singular_matrix(self):

        inverse_op = MatrixInverse([self.singular_matrix])

        with self.assertRaises(ValueError) as context:
            inverse_op.op(self.singular_matrix)

        self.assertIn("not invertible", str(context.exception).lower())

    def test_inverse_of_1x1_matrix(self):

        inverse_op = MatrixInverse([self.simple_matrix])
        result = inverse_op.op(self.simple_matrix)

        self.assertIsInstance(result, Matrix)
        self.assertEqual(result.rows, 1)
        self.assertEqual(result.cols, 1)

        self.assertAlmostEqual(result.data[0][0], 0.2, places=5)

    def test_symbol_property(self):

        inverse_op = MatrixInverse([self.invertible_matrix])
        self.assertEqual(inverse_op._symbol, "^(-1)")

    def test_non_square_matrix(self):

        non_square_matrix = Matrix(
            [
                [
                    MyNumber(IntegerNumber(1)),
                    MyNumber(IntegerNumber(2)),
                    MyNumber(IntegerNumber(3)),
                ],
                [
                    MyNumber(IntegerNumber(4)),
                    MyNumber(IntegerNumber(5)),
                    MyNumber(IntegerNumber(6)),
                ],
            ]
        )

        inverse_op = MatrixInverse([non_square_matrix])

        with self.assertRaises(ValueError) as context:
            inverse_op.op(non_square_matrix)

        self.assertIn("must be square", str(context.exception).lower())

    def test_empty_matrix(self):

        with self.assertRaises(ValueError) as context:
            Matrix([])
        self.assertIn(
            "all matrix rows must have the same size", str(context.exception).lower()
        )


if __name__ == "__main__":
    unittest.main()
