import unittest
from unittest.mock import MagicMock

from parameterized import parameterized

from src.main.python.calculator import calculator
from src.main.python.calculator.divides import Divides
from src.main.python.calculator.illegal_construction import IllegalConstruction
from src.main.python.calculator.integer_number import IntegerNumber
from src.main.python.calculator.inverse import Inverse
from src.main.python.calculator.linear_solution import LinearSolution
from src.main.python.calculator.linear_solver import LinearEquationSolver
from src.main.python.calculator.matrix import Matrix
from src.main.python.calculator.minus import Minus
from src.main.python.calculator.my_number import MyNumber
from src.main.python.calculator.plus import Plus
from src.main.python.calculator.power import Power
from src.main.python.calculator.times import Times
from src.main.python.visitor.counter import Counter
from src.main.python.visitor.evaluator import Evaluator
from src.main.python.visitor.printer import Printer


class TestEvaluator(unittest.TestCase):

    def setUp(self):
        self.evaluator = Evaluator()
        self.value1 = MyNumber(IntegerNumber(8))
        self.value2 = MyNumber(IntegerNumber(6))
        # Setup test matrix
        self.test_matrix = Matrix(
            [
                [MyNumber(IntegerNumber(1)), MyNumber(IntegerNumber(2))],
                [MyNumber(IntegerNumber(3)), MyNumber(IntegerNumber(4))],
            ]
        )

        # Setup test linear solutions
        equations = ["2x+3y=5", "3x-4z=7", "y+z=10"]
        equations2 = ["2x+3y=", "3x-4z=7", "y+z=10"]
        self.solver = LinearEquationSolver(equations)
        self.solver1 = LinearEquationSolver(equations2)

        self.solution_with_dict = LinearSolution({"x": 2, "y": 3})
        self.solution_with_dict.solve = MagicMock(return_value={"x": 2, "y": 3})

        self.solution_with_string = LinearSolution("No solution")
        self.solution_with_string.solve = MagicMock(return_value="No solution")

    def test_evaluate_my_number(self):
        self.assertEqual(
            self.value1.get_number_type(), calculator.eval_expression(self.value1)
        )

    @parameterized.expand(
        [
            ("*",),
            ("+",),
            ("/",),
            ("-",),
            ("^",),
            ("1/",),
        ]
    )
    def test_evaluate_operations(self, symbol):
        params = [self.value1, self.value2]
        paramsUnit = [self.value1]
        try:
            match symbol:
                case "+":
                    expected = self.value1.get_number_type().add(
                        self.value2.get_number_type()
                    )
                    result = calculator.eval_expression(Plus(params))
                case "-":
                    expected = self.value1.get_number_type().subtract(
                        self.value2.get_number_type()
                    )
                    result = calculator.eval_expression(Minus(params))
                case "*":
                    expected = self.value1.get_number_type().multiply(
                        self.value2.get_number_type()
                    )
                    result = calculator.eval_expression(Times(params))
                case "/":
                    expected = self.value1.get_number_type().divide(
                        self.value2.get_number_type()
                    )
                    result = calculator.eval_expression(Divides(params))
                case "^":
                    expected = self.value1.get_number_type().pow(
                        self.value2.get_number_type()
                    )
                    result = calculator.eval_expression(Power(params))
                case "1/":
                    expected = self.value1.get_number_type().inverse()
                    result = calculator.eval_expression(Inverse(paramsUnit))
                case _:
                    self.fail("Invalid symbol")

            self.assertEqual(expected.get_value(), result.get_value())

        except IllegalConstruction as e:
            self.fail(e)

    def test_visit_matrix(self):
        """Test evaluation of matrix"""
        self.evaluator.visit_matrix(self.test_matrix)

        # Check stack contains exactly the matrix
        self.assertEqual(len(self.evaluator.stack), 1)
        self.assertIsInstance(self.evaluator.stack[0], Matrix)

        counter = Counter()
        self.test_matrix.accept(counter)
        # Verify matrix data
        result_matrix = self.evaluator.stack[0]
        self.assertEqual(result_matrix.rows, 2)
        self.assertEqual(result_matrix.cols, 2)
        self.assertEqual(result_matrix.data[0][0].get_value(), 1)
        self.assertEqual(result_matrix.data[1][1].get_value(), 4)

    def test_visit_linear_solution_with_dict(self):

        solution = LinearSolution({"x": 1, "y": 2})
        counter = Counter()
        solution.accept(counter)
        self.evaluator.visit_linear_solution(self.solver)
        res = self.evaluator.stack[0]
        self.assertEqual(len(self.evaluator.stack), 1)
        self.assertIsInstance(self.evaluator.stack[0], dict)
        self.assertEqual(res, {"x": 121, "y": -79, "z": 89})

    def test_visit_linear_solution_with_string(self):

        self.evaluator.visit_linear_solution(self.solver1)

        res = self.evaluator.stack[0]
        self.assertEqual(len(self.evaluator.stack), 1)
        self.assertIsInstance(res, str)
        self.assertEqual(res, "Error solving equations")

    def test_visit_linear_solution(self):
        solution = LinearSolution({"x": 1.0, "y": 2.5, "z": -3})
        printer = Printer(notation="infix")
        solution.accept(printer)
        expected_output = "x = 1.0\ny = 2.5\nz = -3"
        self.assertEqual(printer.result.strip(), expected_output)

    def test_solver_with_unique_solution(self):
        eqs = ["x + y = 2", "x - y = 0"]
        solver = LinearEquationSolver(eqs)
        evaluator = Evaluator()
        solver.accept(evaluator)
        result = evaluator.stack.pop()
        self.assertEqual(result, {"x": 1.0, "y": 1.0})

    def test_solver_with_error(self):
        eqs = ["x + y = 2", "x + y = 3"]
        solver = LinearEquationSolver(eqs)
        evaluator = Evaluator()
        solver.accept(evaluator)
        result = evaluator.stack.pop()
        self.assertTrue(isinstance(result, str))
        self.assertIn("no solution", result.lower())

    def test_visit_linear_solution_with_dict_result(self):

        mock_solution = MagicMock()
        mock_solution.solve.return_value = {"x": 2, "y": 3}

        self.evaluator.visit_linear_solution(mock_solution)

        self.assertEqual(len(self.evaluator.stack), 1)
        self.assertEqual(self.evaluator.stack[0], {"x": 2, "y": 3})

    def test_visit_linear_solution_with_object_result(self):

        class SolutionResult:
            def get_value(self):
                return {"x": 4, "y": 5}

        mock_solution = MagicMock()
        mock_solution.solve.return_value = SolutionResult()

        self.evaluator.visit_linear_solution(mock_solution)

        self.assertEqual(len(self.evaluator.stack), 1)
        self.assertEqual(self.evaluator.stack[0], {"x": 4, "y": 5})

    def test_visit_linear_solution_with_string_result(self):

        mock_solution = MagicMock()
        mock_solution.solve.return_value = "No solution"

        self.evaluator.visit_linear_solution(mock_solution)

        self.assertEqual(len(self.evaluator.stack), 1)
        self.assertEqual(self.evaluator.stack[0], "No solution")


if __name__ == "__main__":
    unittest.main()
