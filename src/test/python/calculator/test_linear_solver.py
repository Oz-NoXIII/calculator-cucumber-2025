import unittest
from io import StringIO
from unittest.mock import patch

from src.main.python.calculator.linear_solver import (LinearEquationSolver,
                                                      run_interactive_solver)


class TestLinearEquationSolver(unittest.TestCase):

    def test_unique_solution(self):
        equations = ["2x+3y=5", "3x-4z=7", "y+z=10"]
        solver = LinearEquationSolver(equations)
        solution = solver.solve()

        expected = {"x": 121, "y": -79, "z": 89}
        self.assertEqual(solution, expected)

    def test_rounding_behavior(self):
        equations = ["0.5x+0.25y=1", "x-y=0"]
        solver = LinearEquationSolver(equations)
        solution = solver.solve()
        self.assertAlmostEqual(solution["x"], 1.33, places=2)
        self.assertAlmostEqual(solution["y"], 1.33, places=2)

    def test_infinite_solutions(self):
        equations = ["x + y = 2", "2x + 2y = 4"]
        solver = LinearEquationSolver(equations)
        result = solver.solve()
        self.assertTrue(isinstance(result, str) and "singular" in result.lower())

    def test_no_solution(self):
        equations = ["x + y = 2", "x + y = 3"]
        solver = LinearEquationSolver(equations)
        result = solver.solve()
        self.assertTrue(isinstance(result, str) and "singular" in result.lower())

    def test_linear_unique_solution(self):
        equations = ["2x+3y=5", "3x-4z=7", "y+z=10"]
        solver = LinearEquationSolver(equations)
        solution = solver.solve()
        self.assertEqual(solution, {"x": 121, "y": -79, "z": 89})

    @patch("builtins.input", side_effect=["", "x + y = 2", "ok", "n"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_input_empty_and_valid_then_exit(self, mock_stdout, mock_input):
        run_interactive_solver()
        output = mock_stdout.getvalue()
        self.assertIn("Empty input", output)
        self.assertIn("End of program", output)

    @patch("builtins.input", side_effect=["ok", "n"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_no_equation_provided(self, mock_stdout, mock_input):
        run_interactive_solver()
        output = mock_stdout.getvalue()
        self.assertIn("No system supplied", output)

    @patch("builtins.input", side_effect=["x + y = 2", "x + y = 3", "ok", "n"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_incompatible_system(self, mock_stdout, mock_input):
        run_interactive_solver()
        output = mock_stdout.getvalue()
        self.assertIn("Results", output)
        self.assertIn("incompatible", output.lower())

    def test_missing_equal_sign(self):
        equations = ["2x + 3y"]
        solver = LinearEquationSolver(equations)
        result = solver.solve()
        self.assertTrue("missing '=' sign" in result.lower())

    def test_invalid_term_format(self):
        equations = ["2x + ? = 4"]
        solver = LinearEquationSolver(equations)
        result = solver.solve()
        self.assertTrue("invalid term" in result.lower())

    @patch("builtins.input", side_effect=["x + y = 6", "x - y = 0", "ok", "n"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_print_result_from_interactive_solver(self, mock_stdout, mock_input):
        run_interactive_solver()
        output = mock_stdout.getvalue()

        # Vérifie que le bloc de print a bien été exécuté
        self.assertIn("x = ", output)
        self.assertIn("y = ", output)

    @patch("builtins.input", side_effect=["x + y = 2", "ok", "n"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_run_interactive_solver_main(self, mock_stdout, mock_input):

        run_interactive_solver()
        output = mock_stdout.getvalue()
        self.assertIn("Result", output)

    def test_solution_arrondi_entier(self):
        equations = ["x + y = 5.9999999", "x - y = 0.0000001"]
        solver = LinearEquationSolver(equations)
        result = solver.solve()
        self.assertEqual(result, {"x": 3, "y": 3})

    def test_solution_arrondi_decimal(self):
        equations = ["x + y = 7.12", "x - y = 1.14"]
        solver = LinearEquationSolver(equations)
        result = solver.solve()
        self.assertEqual(result, {"x": 4.13, "y": 2.99})

    def test_zero_solution(self):
        equations = ["x + y = 0", "x - y = 0"]
        solver = LinearEquationSolver(equations)
        result = solver.solve()
        self.assertEqual(result, {"x": 0, "y": 0})

    def test_generic_exception(self):

        equations = ["x + y = 5", "t ="]
        solver = LinearEquationSolver(equations)
        result = solver.solve()
        self.assertTrue(isinstance(result, str) and "error" in result.lower())


if __name__ == "__main__":
    unittest.main()
