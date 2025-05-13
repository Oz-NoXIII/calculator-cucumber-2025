import unittest
from unittest.mock import patch

from src.main.python.calculator.linear_solver import LinearEquationSolver


class TestLinearEquationSolver(unittest.TestCase):

    def setUp(self):
        self.equations = ["2x+3y=5", "3x-4z=7", "y+z=10"]

    def test_unique_solution(self):
        equations = ["2x+3y=5", "3x-4z=7", "y+z=10"]
        solver = LinearEquationSolver(equations)
        solution = solver.solve()

        expected = {"x": 121, "y": -79, "z": 89}
        self.assertEqual(solution.get_value(), expected)

    def test_rounding_behavior(self):
        equations = ["0.5x+0.25y=1", "x-y=0"]
        solver = LinearEquationSolver(equations)
        solution = solver.solve()
        self.assertEqual(solution.get_value(), {"x": 1.33, "y": 1.33})

    def test_multiple_solutions_case(self):
        equations = ["x**2 = 1"]
        solver = LinearEquationSolver(equations)
        result = solver.solve()
        assert result == "Infinite solutions."

    def test_unexpected_solution_format(self):
        equations = ["x + abs(y) = 1"]

        with patch("sympy.solve", return_value="unexpected_format"):
            solver = LinearEquationSolver(equations)
            result = solver.solve()
            assert result == "Unexpected solution format."

    def test_no_solution(self):
        equations = ["x + y = 2", "x + y = 3"]
        solver = LinearEquationSolver(equations)
        result = solver.solve()
        self.assertEqual(result, "No solution found.")

    def test_missing_equal_sign(self):
        equations = ["2x + 3y"]
        solver = LinearEquationSolver(equations)
        result = solver.solve()
        self.assertTrue("Error solving equations" in result)

    def test_invalid_term_format(self):
        equations = ["2x + ? = 4"]
        solver = LinearEquationSolver(equations)
        result = solver.solve()
        self.assertTrue("Error solving equations" in result)

    def test_invalid_syntax(self):
        equations = [""]
        solver = LinearEquationSolver(equations)
        result = solver.solve()
        self.assertTrue(
            result, "Equations must be provided as a non-empty list of strings."
        )

    def test_large_system(self):
        equations = ["x + y + z = 6", "2*x + 5*y + z = -4", "2*x + 3*y + 8*z = 27"]
        solver = LinearEquationSolver(equations)
        result = solver.solve()
        expected = {"x": 7.05, "y": -4.26, "z": 3.21}
        # 0.01 tolerance for float comparison
        self.assertEqual(result.get_value(), expected)

    def test_solution_arrondi_decimal(self):
        equations = ["x + y = 7.12", "x - y = 1.14"]
        solver = LinearEquationSolver(equations)
        result = solver.solve()
        self.assertEqual(result.get_value(), {"x": 4.13, "y": 2.99})

    def test_zero_solution(self):
        equations = ["x + y = 0", "x - y = 0"]
        solver = LinearEquationSolver(equations)
        result = solver.solve()
        self.assertEqual(result.get_value(), {"x": 0, "y": 0})

    def test_generic_exception(self):

        equations = ["x + y = 5", "t ="]
        solver = LinearEquationSolver(equations)
        result = solver.solve()
        self.assertTrue(isinstance(result, str) and "error" in result.lower())

    def test_empty_equations_list(self):
        with self.assertRaises(ValueError) as context:
            LinearEquationSolver([])
        self.assertEqual(
            str(context.exception),
            "Equations must be provided as a non-empty list of strings.",
        )

    def test_non_list_input(self):
        with self.assertRaises(ValueError) as context:
            LinearEquationSolver("not a list")
        self.assertEqual(
            str(context.exception),
            "Equations must be provided as a non-empty list of strings.",
        )

    def test_float_conversion_error(self):
        equations = ["x + y = 'abc'"]
        solver = LinearEquationSolver(equations)
        result = solver.solve()
        self.assertEqual("Error solving equations", result)

    def test_undefined_variable_raises_exception(self):
        equations = ["x + y = z"]
        solver = LinearEquationSolver(equations)
        result = solver.solve()
        self.assertTrue("Error solving equations" in result)

    def test_depth_properties(self):

        self.assertEqual(LinearEquationSolver(self.equations).get_depth(), 0)

    def test_ops_properties(self):

        self.assertEqual(LinearEquationSolver(self.equations).get_ops(), 0)

    def test_nbs_properties(self):
        self.assertEqual(LinearEquationSolver(self.equations).get_nbs(), 0)

    def test_str_representation(self):
        self.assertEqual(
            str(LinearEquationSolver(self.equations)),
            "['2x+3y=5', '3x-4z=7', 'y+z=10']",
        )


if __name__ == "__main__":
    unittest.main()
