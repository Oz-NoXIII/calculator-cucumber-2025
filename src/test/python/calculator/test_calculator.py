import sys
from io import StringIO
from unittest import TestCase
from unittest.mock import Mock, patch

from src.main.python.calculator.calculator import (print_expression_details,
                                                   print_result)


class TestCalculator(TestCase):

    def setUp(self):
        # Capture printed output
        self.captured_output = StringIO()
        self.original_stdout = sys.stdout
        sys.stdout = self.captured_output

        # Mock expression object
        self.mock_expr = Mock()
        self.mock_expr.__str__ = lambda self: "MockExpr"
        self.mock_expr.get_depth.return_value = 2
        self.mock_expr.get_ops.return_value = 3
        self.mock_expr.get_nbs.return_value = 4
        self.mock_expr.accept.return_value = None

    def tearDown(self):
        # Restore normal stdout
        sys.stdout = self.original_stdout

    @patch("src.main.python.calculator.calculator.eval_expression")
    def test_print_result_normal(self, mock_eval_expression):
        mock_eval_expression.return_value = 42
        print_result(self.mock_expr)
        output = self.captured_output.getvalue()
        self.assertIn("The result of evaluating expression", output)
        self.assertIn("is: 42", output)

    @patch("src.main.python.calculator.calculator.eval_expression")
    def test_print_result_nan(self, mock_eval_expression):
        mock_eval_expression.return_value = float("nan")
        print_result(self.mock_expr)
        output = self.captured_output.getvalue()
        self.assertIn("is: NaN", output)

    @patch("src.main.python.calculator.calculator.eval_expression")
    def test_print_expression_details(self, mock_eval_expression):
        mock_eval_expression.return_value = 10
        print_expression_details(self.mock_expr)
        output = self.captured_output.getvalue()
        self.assertIn("It contains 2 levels of nested expressions", output)
        self.assertIn("3 operations", output)
        self.assertIn("4 numbers", output)
