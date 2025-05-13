import unittest

from src.main.python.calculator.integer_number import IntegerNumber
from src.main.python.calculator.matrix import Matrix
from src.main.python.calculator.my_number import MyNumber
from src.main.python.calculator.transpose import MatrixTranspose


class TestMatrixTranspose(unittest.TestCase):

    def setUp(self):

        self.matrix_2x3 = Matrix(
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

        self.matrix_3x2 = Matrix(
            [
                [MyNumber(IntegerNumber(1)), MyNumber(IntegerNumber(4))],
                [MyNumber(IntegerNumber(2)), MyNumber(IntegerNumber(5))],
                [MyNumber(IntegerNumber(3)), MyNumber(IntegerNumber(6))],
            ]
        )

        self.square_matrix = Matrix(
            [
                [MyNumber(IntegerNumber(1)), MyNumber(IntegerNumber(2))],
                [MyNumber(IntegerNumber(3)), MyNumber(IntegerNumber(4))],
            ]
        )

        self.empty_matrix = None

    def test_transpose_2x3_matrix(self):

        transpose_op = MatrixTranspose([self.matrix_2x3])
        result = transpose_op.op(self.matrix_2x3)

        self.assertIsInstance(result, Matrix)

        self.assertEqual(result.rows, 3)
        self.assertEqual(result.cols, 2)

        expected_values = [[1, 4], [2, 5], [3, 6]]
        for i in range(3):
            for j in range(2):
                self.assertEqual(result.data[i][j], expected_values[i][j])

    def test_transpose_square_matrix(self):

        transpose_op = MatrixTranspose([self.square_matrix])
        result = transpose_op.op(self.square_matrix)

        self.assertEqual(result.rows, 2)
        self.assertEqual(result.cols, 2)

        expected_values = [[1, 3], [2, 4]]
        for i in range(2):
            for j in range(2):
                self.assertEqual(result.data[i][j], expected_values[i][j])

    def test_double_transpose(self):

        transpose_op = MatrixTranspose([self.matrix_2x3])
        once = transpose_op.op(self.matrix_2x3)
        twice = transpose_op.op(once)

        self.assertEqual(twice.rows, self.matrix_2x3.rows)
        self.assertEqual(twice.cols, self.matrix_2x3.cols)

        for i in range(2):
            for j in range(3):
                self.assertEqual(
                    twice.data[i][j], self.matrix_2x3.data[i][j].get_value()
                )

    def test_symbol_property(self):

        transpose_op = MatrixTranspose([self.matrix_2x3])
        self.assertEqual(transpose_op._symbol, "tr")

    def test_empty_matrix(self):

        with self.assertRaises(ValueError):
            Matrix([])

    def test_non_matrix_input(self):

        transpose_op = MatrixTranspose([self.matrix_2x3])

        with self.assertRaises(AttributeError):
            transpose_op.op("not a matrix")

    def test_1x1_matrix(self):

        matrix_1x1 = Matrix([[MyNumber(IntegerNumber(5))]])
        transpose_op = MatrixTranspose([matrix_1x1])
        result = transpose_op.op(matrix_1x1)

        self.assertEqual(result.rows, 1)
        self.assertEqual(result.cols, 1)
        self.assertEqual(result.data[0][0], 5)


if __name__ == "__main__":
    unittest.main()
