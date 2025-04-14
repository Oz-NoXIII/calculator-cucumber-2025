import math
import unittest

from src.main.python import calculator
from src.main.python.calculator.divides import Divides
from src.main.python.calculator.linear_solver import LinearEquationSolver
from src.main.python.calculator.minus import Minus
from src.main.python.calculator.my_number import MyNumber
from src.main.python.calculator.plus import Plus
from src.main.python.calculator.times import Times


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

        # Expected values: x = 1.33, y = 1.33 => rounded to 1.3
        self.assertAlmostEqual(solution["x"], 0.03, places=2)
        self.assertAlmostEqual(solution["y"], 0.03, places=2)

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


if __name__ == "__main__":
    unittest.main()
