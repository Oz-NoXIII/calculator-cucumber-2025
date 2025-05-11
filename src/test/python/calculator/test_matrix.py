import unittest

from src.main.python.calculator.integer_number import IntegerNumber
from src.main.python.calculator.matrix import Matrix
from src.main.python.calculator.real_number import RealNumber


class TestMatrixOperations(unittest.TestCase):

    def test_matrix_addition_with_integer_numbers(self):

        matrix1 = Matrix(
            [[IntegerNumber(1), IntegerNumber(2)], [IntegerNumber(3), IntegerNumber(4)]]
        )
        matrix2 = Matrix(
            [[IntegerNumber(5), IntegerNumber(6)], [IntegerNumber(7), IntegerNumber(8)]]
        )

        result = matrix1.add(matrix2)
        expected_result = Matrix(
            [
                [IntegerNumber(6).get_value(), IntegerNumber(8).get_value()],
                [IntegerNumber(10).get_value(), IntegerNumber(12).get_value()],
            ]
        )

        self.assertEqual(
            [[cell.get_value() for cell in row] for row in result.data].__str__(),
            expected_result.__str__(),
        )

    def test_matrix_subtraction(self):
        matrix1 = Matrix(
            [[IntegerNumber(1), IntegerNumber(2)], [IntegerNumber(3), IntegerNumber(4)]]
        )
        matrix2 = Matrix(
            [[IntegerNumber(5), IntegerNumber(6)], [IntegerNumber(7), IntegerNumber(8)]]
        )
        result = matrix1.subtract(matrix2)
        expected_result = [
            [IntegerNumber(-4).get_value(), IntegerNumber(-4).get_value()],
            [IntegerNumber(-4).get_value(), IntegerNumber(-4).get_value()],
        ]

        self.assertEqual(
            [[cell.get_value() for cell in row] for row in result.data].__str__(),
            expected_result.__str__(),
        )

    def test_matrix_multiplication_with_integer_numbers(self):

        matrix1 = Matrix(
            [[IntegerNumber(1), IntegerNumber(2)], [IntegerNumber(3), IntegerNumber(4)]]
        )
        matrix2 = Matrix(
            [[IntegerNumber(5), IntegerNumber(6)], [IntegerNumber(7), IntegerNumber(8)]]
        )

        result = matrix1.multiply(matrix2)
        expected_result = Matrix(
            [
                [IntegerNumber(19).get_value(), IntegerNumber(22).get_value()],
                [IntegerNumber(43).get_value(), IntegerNumber(50).get_value()],
            ]
        )

        self.assertEqual(
            [[cell.get_value() for cell in row] for row in result.data].__str__(),
            expected_result.__str__(),
        )

    def test_matrix_transpose(self):

        matrix = Matrix(
            [
                [
                    IntegerNumber(1).get_value(),
                    IntegerNumber(2).get_value(),
                    IntegerNumber(3).get_value(),
                ],
                [
                    IntegerNumber(4).get_value(),
                    IntegerNumber(5).get_value(),
                    IntegerNumber(6).get_value(),
                ],
            ]
        )

        result = matrix.transpose()
        expected_result = Matrix(
            [
                [IntegerNumber(1).get_value(), IntegerNumber(4).get_value()],
                [IntegerNumber(2).get_value(), IntegerNumber(5).get_value()],
                [IntegerNumber(3).get_value(), IntegerNumber(6).get_value()],
            ]
        )

        self.assertEqual(str(result), str(expected_result))

    def test_matrix_inverse(self):

        matrix = Matrix([[4, 7], [2, 6]])

        result = matrix.inverse()
        expected_result = Matrix([[0.6, -0.7], [-0.2, 0.4]])

        result_data_rounded = [
            [round(value, 2) for value in row] for row in result.data
        ]
        expected_result_data_rounded = [
            [round(value, 2) for value in row] for row in expected_result.data
        ]

        self.assertEqual(result_data_rounded, expected_result_data_rounded)

    def test_matrix_addition_error(self):
        matrix1 = Matrix(
            [[IntegerNumber(1), IntegerNumber(2)], [IntegerNumber(3), IntegerNumber(4)]]
        )
        matrix2 = Matrix([[IntegerNumber(5), IntegerNumber(6)]])

        with self.assertRaises(ValueError):
            matrix1.add(matrix2)

    def test_matrix_substraction_error(self):
        matrix2 = Matrix(
            [[IntegerNumber(1), IntegerNumber(2)], [IntegerNumber(3), IntegerNumber(4)]]
        )
        matrix1 = Matrix([[IntegerNumber(5), IntegerNumber(6)]])

        with self.assertRaises(ValueError):
            matrix1.subtract(matrix2)

    def test_matrix_multiplication_error(self):
        matrix1 = Matrix(
            [[IntegerNumber(1), IntegerNumber(2)], [IntegerNumber(3), IntegerNumber(4)]]
        )
        matrix2 = Matrix([[IntegerNumber(5), IntegerNumber(6)]])

        with self.assertRaises(ValueError):
            matrix1.multiply(matrix2)

    def test_matrix_inverse_error(self):
        matrix = Matrix(
            [
                [IntegerNumber(1), IntegerNumber(2), IntegerNumber(3)],
                [IntegerNumber(4), IntegerNumber(5), IntegerNumber(6)],
            ]
        )

        with self.assertRaises(ValueError):
            matrix.inverse()

    def test_matrix_inverse_non_inversible(self):
        matrix = Matrix(
            [
                [IntegerNumber(1).get_value(), IntegerNumber(2).get_value()],
                [IntegerNumber(2).get_value(), IntegerNumber(4).get_value()],
            ]
        )

        with self.assertRaises(ValueError):
            matrix.inverse()

    def test_invalid_matrix_format(self):

        with self.assertRaises(ValueError):
            Matrix([[IntegerNumber(1), IntegerNumber(2)], [IntegerNumber(3)]])

    def test_matrix_multiplication_invalid(self):

        matrix1 = Matrix([[1, 2, 3], [4, 5, 6]])
        matrix2 = Matrix([[7, 8], [9, 10]])

        with self.assertRaises(ValueError):
            matrix1.multiply(matrix2)

    def test_matrix_is_not_a_list_of_lists(self):

        with self.assertRaises(ValueError):
            Matrix(
                [IntegerNumber(1), IntegerNumber(2), IntegerNumber(3), IntegerNumber(4)]
            )

        with self.assertRaises(ValueError):
            Matrix(IntegerNumber(5))

        with self.assertRaises(ValueError):
            Matrix("not a matrix")

    def test_matrix_contains_non_list_elements(self):

        with self.assertRaises(ValueError):
            Matrix([[IntegerNumber(1), IntegerNumber(2)], IntegerNumber(3)])

        with self.assertRaises(ValueError):
            Matrix([[1, 2], "not a list"])

    def test_invalid_number_type(self):
        with self.assertRaises(ValueError) as context:
            Matrix([[[], []], [[], []]]).subtract(Matrix([["a", "b"], ["c", "d"]]))
        self.assertEqual(str(context.exception), "Unsupported number type")

        with self.assertRaises(ValueError) as context:
            Matrix([["a", "b"], ["c", "d"]]).add(Matrix([["a", "b"], ["c", "d"]]))
        self.assertEqual(str(context.exception), "Unsupported number type")

        with self.assertRaises(ValueError):
            Matrix([[[], []], [[], []]]).multiply(Matrix([[1, 2, 3], [4, 5, 6]]))
        self.assertEqual(str(context.exception), "Unsupported number type")

    def test_accept(self):

        class TestVisitor:
            def visit_matrix(self, matrix):
                self.visited = matrix

        matrix = Matrix(
            [[IntegerNumber(1), IntegerNumber(2)], [IntegerNumber(3), IntegerNumber(4)]]
        )

        visitor = TestVisitor()
        matrix.accept(visitor)

        self.assertEqual(visitor.visited, matrix)

    def test_get_depth(self):

        matrix = Matrix(
            [[IntegerNumber(1), IntegerNumber(2)], [IntegerNumber(3), IntegerNumber(4)]]
        )

        self.assertEqual(matrix.get_depth(), 2)

    def test_get_ops(self):

        matrix = Matrix(
            [[IntegerNumber(1), IntegerNumber(2)], [IntegerNumber(3), IntegerNumber(4)]]
        )

        self.assertEqual(matrix.get_ops(), 4)

    def test_get_nbs(self):

        matrix = Matrix(
            [[IntegerNumber(1), IntegerNumber(2)], [IntegerNumber(3), IntegerNumber(4)]]
        )

        self.assertEqual(matrix.get_nbs(), 4)

    def test_matrix_addition_with_real_numbers(self):

        matrix1 = Matrix(
            [[RealNumber(1.5), RealNumber(2.5)], [RealNumber(3.5), RealNumber(4.5)]]
        )
        matrix2 = Matrix(
            [[RealNumber(5.5), RealNumber(6.5)], [RealNumber(7.5), RealNumber(8.5)]]
        )

        result = matrix1.add(matrix2)
        expected_result = Matrix(
            [
                [RealNumber(7.0).get_value(), RealNumber(9.0).get_value()],
                [RealNumber(11.0).get_value(), RealNumber(13.0).get_value()],
            ]
        )

        self.assertEqual(
            [[cell.get_value() for cell in row] for row in result.data].__str__(),
            expected_result.__str__(),
        )

    """def test_matrix_addition_with_rational_numbers(self):

        matrix1 = Matrix(
            [
                [RationalNumber(1, 2), RationalNumber(2, 3)],
                [RationalNumber(3, 4), RationalNumber(5, 6)],
            ]
        )
        matrix2 = Matrix(
            [
                [RationalNumber(5, 6), RationalNumber(7, 8)],
                [RationalNumber(9, 10), RationalNumber(11, 12)],
            ]
        )

        result = matrix1.add(matrix2)
        expected_result = Matrix(
            [
                [RationalNumber(8, 6).get_value(), RationalNumber(37, 24).get_value()],
                [RationalNumber(33, 20).get_value(), RationalNumber(7, 4).get_value()],
            ]
        )

        self.assertEqual([[cell.get_value() for cell in row] for row in result.data].__str__(), expected_result.__str__())
"""

    def test_matrix_multiplication_with_real_numbers(self):

        matrix1 = Matrix(
            [[RealNumber(1.5), RealNumber(2.5)], [RealNumber(3.5), RealNumber(4.5)]]
        )
        matrix2 = Matrix(
            [[RealNumber(5.5), RealNumber(6.5)], [RealNumber(7.5), RealNumber(8.5)]]
        )

        result = matrix1.multiply(matrix2)
        expected_result = Matrix(
            [
                [RealNumber(27.0).get_value(), RealNumber(31.0).get_value()],
                [RealNumber(53.0).get_value(), RealNumber(61.0).get_value()],
            ]
        )

        self.assertEqual(
            [[cell.get_value() for cell in row] for row in result.data].__str__(),
            expected_result.__str__(),
        )


if __name__ == "__main__":
    unittest.main()
