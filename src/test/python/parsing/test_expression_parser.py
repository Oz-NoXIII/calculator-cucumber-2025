import unittest
from unittest.mock import patch

from src.main.python.calculator.divides import Divides
from src.main.python.calculator.inverse import Inverse
from src.main.python.calculator.minus import Minus
from src.main.python.calculator.my_number import MyNumber
from src.main.python.calculator.plus import Plus
from src.main.python.calculator.power import Power
from src.main.python.calculator.times import Times
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
        self.assertIsInstance(result, dict)
        self.assertIn("x", result)
        self.assertIn("y", result)
        self.assertEqual(result["x"], 1.0)
        self.assertEqual(result["y"], 1.0)

    def test_syntax_error(self):
        result = parse_expression('solve_linear("x + = y")')
        self.assertIsInstance(result, str)
        self.assertIn("error", result.lower())

    def test_no_solution(self):
        result = parse_expression('solve_linear("x + y = 2; x + y = 3")')
        self.assertIsInstance(result, str)
        self.assertIn("no solution", result.lower() or "incompatible" in result.lower())

    def test_infinite_solutions(self):
        result = parse_expression('solve_linear("x + y = 2; 2x + 2y = 4")')
        self.assertIsInstance(result, str)
        self.assertIn("error solving equations", result.lower())

    @patch(
        "src.main.python.calculator.linear_solver.LinearEquationSolver.solve",
        return_value={"x": 1},
    )
    def test_parser_calls_solver(self, mock_solve):
        result = parse_expression('solve_linear("x + y = 2; x - y = 0")')
        mock_solve.assert_called_once()
        self.assertEqual(result, {"x": 1})


if __name__ == "__main__":
    unittest.main()
