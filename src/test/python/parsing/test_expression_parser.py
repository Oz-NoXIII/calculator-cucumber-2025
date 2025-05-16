import math
import unittest

from lark.exceptions import VisitError

from src.main.python.calculator import calculator
from src.main.python.calculator.arccosinus import Arccosinus
from src.main.python.calculator.arcsinus import Arcsinus
from src.main.python.calculator.arctangent import Arctangent
from src.main.python.calculator.cosinus import Cosinus
from src.main.python.calculator.cosinushyperbolic import Cosinushyperbolic
from src.main.python.calculator.divides import Divides
from src.main.python.calculator.inverse import Inverse, MatrixInverse
from src.main.python.calculator.linear_solver import LinearEquationSolver
from src.main.python.calculator.logarithm import Logarithm
from src.main.python.calculator.logarithmNeperien import LogarithmNeperien
from src.main.python.calculator.minus import Minus
from src.main.python.calculator.my_number import MyNumber
from src.main.python.calculator.nroot import Nroot
from src.main.python.calculator.plus import Plus
from src.main.python.calculator.power import Power
from src.main.python.calculator.rand import Rand
from src.main.python.calculator.sinus import Sinus
from src.main.python.calculator.sinushyperbolic import Sinushyperbolic
from src.main.python.calculator.tangent import Tangent
from src.main.python.calculator.tangenthyperbolic import Tangenthyperbolic
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

    def test_parse_expression_sin(self):
        expr_str = "sin(0)"
        result = parse_expression(expr_str)
        self.assertIsInstance(result, Sinus)
        self.assertEqual(len(result.get_args()), 1)
        self.assertIsInstance(result.get_args()[0], MyNumber)

    def test_parse_expression_cos(self):
        expr_str = "cos(0)"
        result = parse_expression(expr_str)
        self.assertIsInstance(result, Cosinus)
        self.assertEqual(len(result.get_args()), 1)
        self.assertIsInstance(result.get_args()[0], MyNumber)

    def test_parse_expression_tan(self):
        expr_str = "tan(0)"
        result = parse_expression(expr_str)
        self.assertIsInstance(result, Tangent)
        self.assertEqual(len(result.get_args()), 1)
        self.assertIsInstance(result.get_args()[0], MyNumber)

    def test_parse_expression_arcsin(self):
        expr_str = "arcsin(0)"
        result = parse_expression(expr_str)
        self.assertIsInstance(result, Arcsinus)
        self.assertEqual(len(result.get_args()), 1)
        self.assertIsInstance(result.get_args()[0], MyNumber)

    def test_parse_expression_arccos(self):
        expr_str = "arccos(0)"
        result = parse_expression(expr_str)
        self.assertIsInstance(result, Arccosinus)
        self.assertEqual(len(result.get_args()), 1)
        self.assertIsInstance(result.get_args()[0], MyNumber)

    def test_parse_expression_arctan(self):
        expr_str = "arctan(0)"
        result = parse_expression(expr_str)
        self.assertIsInstance(result, Arctangent)
        self.assertEqual(len(result.get_args()), 1)
        self.assertIsInstance(result.get_args()[0], MyNumber)

    def test_parse_expression_sinh(self):
        expr_str = "sinh(0)"
        result = parse_expression(expr_str)
        self.assertIsInstance(result, Sinushyperbolic)
        self.assertEqual(len(result.get_args()), 1)
        self.assertIsInstance(result.get_args()[0], MyNumber)

    def test_parse_expression_cosh(self):
        expr_str = "cosh(0)"
        result = parse_expression(expr_str)
        self.assertIsInstance(result, Cosinushyperbolic)
        self.assertEqual(len(result.get_args()), 1)
        self.assertIsInstance(result.get_args()[0], MyNumber)

    def test_parse_expression_tanh(self):
        expr_str = "tanh(0)"
        result = parse_expression(expr_str)
        self.assertIsInstance(result, Tangenthyperbolic)
        self.assertEqual(len(result.get_args()), 1)
        self.assertIsInstance(result.get_args()[0], MyNumber)

    def test_parse_expression_log(self):
        expr_str = "log(0)"
        result = parse_expression(expr_str)
        self.assertIsInstance(result, Logarithm)
        self.assertEqual(len(result.get_args()), 1)
        self.assertIsInstance(result.get_args()[0], MyNumber)

    def test_parse_expression_ln(self):
        expr_str = "ln(0)"
        result = parse_expression(expr_str)
        self.assertIsInstance(result, LogarithmNeperien)
        self.assertEqual(len(result.get_args()), 1)
        self.assertIsInstance(result.get_args()[0], MyNumber)

    def test_parse_expression_rand(self):
        expr_str = "rand(10)"
        result = parse_expression(expr_str)
        self.assertIsInstance(result, Rand)
        self.assertEqual(len(result.get_args()), 1)
        self.assertIsInstance(result.get_args()[0], MyNumber)

    def test_parse_e(self):
        expr_str = "e"
        result = parse_expression(expr_str)
        self.assertEqual(result.get_value(), math.e)

    def test_parse_pi(self):
        expr_str = "pi"
        result = parse_expression(expr_str)
        self.assertEqual(result.get_value(), math.pi)

    def test_parse_expression_nroot(self):
        expr_str = "8 nroot 3"
        result = parse_expression(expr_str)
        self.assertIsInstance(result, Nroot)
        self.assertEqual(len(result.get_args()), 2)
        self.assertIsInstance(result.get_args()[0], MyNumber)
        self.assertIsInstance(result.get_args()[1], MyNumber)

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
