import unittest

from lark.exceptions import VisitError

from src.main.python.calculator import calculator
from src.main.python.calculator.divides import Divides
from src.main.python.calculator.inverse import Inverse, MatrixInverse
from src.main.python.calculator.linear_solver import LinearEquationSolver
from src.main.python.calculator.minus import Minus
from src.main.python.calculator.my_number import MyNumber
from src.main.python.calculator.plus import Plus
from src.main.python.calculator.power import Power
from src.main.python.calculator.times import Times
from src.main.python.calculator.transpose import MatrixTranspose
from src.main.python.parsing.expression_parser import parse_expression


class TestExpressionParser(unittest.TestCase):

    def test_parse_expression_infix(self):
        # Infix notation
        expr_str = "1 + 2 * 3 - 4 / 5.0"
        result = parse_expression(expr_str)
        self.assertIsInstance(result, Minus)
        self.assertEqual(len(result.get_args()), 2)
        self.assertIsInstance(result.get_args()[0], Plus)
        self.assertIsInstance(result.get_args()[1], Divides)
        self.assertEqual(len(result.get_args()[0].get_args()), 2)
        self.assertIsInstance(result.get_args()[0].get_args()[0], MyNumber)
        self.assertIsInstance(result.get_args()[0].get_args()[1], Times)
        self.assertEqual(len(result.get_args()[1].get_args()), 2)
        self.assertIsInstance(result.get_args()[1].get_args()[0], MyNumber)
        self.assertIsInstance(result.get_args()[1].get_args()[1], MyNumber)

    def test_parse_expression_prefix(self):
        # Prefix notation
        expr_str = "-(+(1 *(2 3)) /(4 5))"
        result = parse_expression(expr_str)
        self.assertIsInstance(result, Minus)
        self.assertEqual(len(result.get_args()), 2)
        self.assertIsInstance(result.get_args()[0], Plus)
        self.assertIsInstance(result.get_args()[1], Divides)
        self.assertEqual(len(result.get_args()[0].get_args()), 2)
        self.assertIsInstance(result.get_args()[0].get_args()[0], MyNumber)
        self.assertIsInstance(result.get_args()[0].get_args()[1], Times)
        self.assertEqual(len(result.get_args()[1].get_args()), 2)
        self.assertIsInstance(result.get_args()[1].get_args()[0], MyNumber)
        self.assertIsInstance(result.get_args()[1].get_args()[1], MyNumber)

    def test_parse_expression_postfix(self):
        # Prefix notation
        expr_str = "((1 (2 3)*)+ (4 5)/)-"
        result = parse_expression(expr_str)
        self.assertIsInstance(result, Minus)
        self.assertEqual(len(result.get_args()), 2)
        self.assertIsInstance(result.get_args()[0], Plus)
        self.assertIsInstance(result.get_args()[1], Divides)
        self.assertEqual(len(result.get_args()[0].get_args()), 2)
        self.assertIsInstance(result.get_args()[0].get_args()[0], MyNumber)
        self.assertIsInstance(result.get_args()[0].get_args()[1], Times)
        self.assertEqual(len(result.get_args()[1].get_args()), 2)
        self.assertIsInstance(result.get_args()[1].get_args()[0], MyNumber)
        self.assertIsInstance(result.get_args()[1].get_args()[1], MyNumber)

    def test_parse_expression_with_negation(self):
        expr_str = "(- 1) + 2 * 3j"
        result = parse_expression(expr_str)
        print(result)
        self.assertIsInstance(result, Plus)
        self.assertEqual(len(result.get_args()), 2)
        self.assertIsInstance(result.get_args()[0], Times)
        self.assertIsInstance(result.get_args()[1], Times)
        self.assertEqual(len(result.get_args()[1].get_args()), 2)
        self.assertIsInstance(result.get_args()[1].get_args()[0], MyNumber)
        self.assertIsInstance(result.get_args()[1].get_args()[1], MyNumber)

    def test_parse_expression_pow_inv(self):
        expr_str = "1 ^ 2"
        result = parse_expression(expr_str)
        self.assertIsInstance(result, Power)
        self.assertEqual(len(result.get_args()), 2)
        self.assertIsInstance(result.get_args()[0], MyNumber)
        self.assertIsInstance(result.get_args()[1], MyNumber)

        expr_str = "1 ^ (inv(2))"
        result = parse_expression(expr_str)
        self.assertIsInstance(result, Power)
        self.assertEqual(len(result.get_args()), 2)
        self.assertIsInstance(result.get_args()[0], MyNumber)
        self.assertIsInstance(result.get_args()[1], Inverse)

    def test_simple_linear_solution(self):
        result = parse_expression('solve_linear("x + y = 2; x - y = 0")')
        expected = {"x": 1, "y": 1}
        res = result.solve()
        self.assertEqual(res.get_value(), expected)

    def test_syntax_error(self):
        result = parse_expression('solve_linear("x + = y")')
        self.assertIsInstance(result, LinearEquationSolver)
        res = calculator.eval_expression(result)
        self.assertIn("Error", res)

    def test_no_solution(self):
        result = parse_expression('solve_linear("x + y = 2; x + y = 3")')
        self.assertIsInstance(result, LinearEquationSolver)
        res = calculator.eval_expression(result)

        self.assertIn("No solution", res or "incompatible" in res)

    def test_infinite_solutions(self):
        result = parse_expression('solve_linear("x + y = 2; 2x + 2y = 4")')
        self.assertIsInstance(result, LinearEquationSolver)
        res = calculator.eval_expression(result)
        self.assertIn("Error", res)

    def test_addition(self):
        expr = "[[1, 2], [3, 4]] + [[5, 6], [7, 8]]"
        result = parse_expression(expr)
        self.assertIsInstance(result, Plus)

    def test_subtraction(self):
        expr = "[[10, 20], [30, 40]] - [[1, 2], [3, 4]]"
        result = parse_expression(expr)

        self.assertIsInstance(result, Minus)

    def test_multiplication(self):
        expr = "[[1, 2], [3, 4]] * [[2, 0], [1, 2]]"
        result = parse_expression(expr)

        self.assertIsInstance(result, Times)

    def assertMatrixAlmostEqual(self, actual_matrix, expected_values, places=4):
        actual_data = [
            [round(cell, places) for cell in row] for row in actual_matrix.data
        ]
        self.assertEqual(actual_data, expected_values)

    def test_inverse(self):
        expr = "inv([[4, 7], [2, 6]])"
        result = parse_expression(expr)
        self.assertIsInstance(result, MatrixInverse)

    def test_transpose(self):
        expr = "transpose([[1, 2], [3, 4]])"
        result = parse_expression(expr)
        self.assertIsInstance(result, MatrixTranspose)

    def test_inverse_non_square(self):
        try:
            expr = "inv([[1, 2, 3], [4, 5, 6]])"
            parse_expression(expr)
        except VisitError as e:
            self.assertIn("matrix must be square", str(e))

    def test_inverse_non_invertible(self):
        try:
            parse_expression("inv([[1, 2], [2, 4]])")
        except VisitError as e:
            self.assertIn("not invertible", str(e))


if __name__ == "__main__":
    unittest.main()
