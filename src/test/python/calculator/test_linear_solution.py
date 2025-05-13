import unittest

from src.main.python.calculator.linear_solution import LinearSolution


class TestLinearSolution(unittest.TestCase):

    def setUp(self):
        # Solutions de test
        self.simple_solution = LinearSolution({"x": 2.5, "y": -1.0})
        self.empty_solution = LinearSolution({})
        self.complex_solution = LinearSolution({"a": 1 + 2j, "b": 3 - 4j})

    def test_initialization(self):

        self.assertEqual(self.simple_solution.solution, {"x": 2.5, "y": -1.0})
        self.assertEqual(self.empty_solution.solution, {})
        self.assertEqual(self.complex_solution.solution, {"a": 1 + 2j, "b": 3 - 4j})

    def test_accept_visitor(self):

        class MockVisitor:
            def __init__(self):
                self.called = False

            def visit_linear_solution(self, solution):
                self.called = True
                return "visited"

        visitor = MockVisitor()
        result = self.simple_solution.accept(visitor)

        self.assertTrue(visitor.called)
        self.assertEqual(result, "visited")

    def test_str_representation(self):

        self.assertEqual(str(self.simple_solution), "x = 2.5\ny = -1.0")
        self.assertEqual(str(self.empty_solution), "")
        self.assertEqual(str(self.complex_solution), "a = (1+2j)\nb = (3-4j)")

    def test_get_value(self):

        self.assertEqual(self.simple_solution.get_value(), {"x": 2.5, "y": -1.0})
        self.assertEqual(self.empty_solution.get_value(), {})

    def test_depth_properties(self):

        self.assertEqual(self.simple_solution.get_depth(), 0)
        self.assertEqual(self.complex_solution.get_depth(), 0)

    def test_ops_properties(self):

        self.assertEqual(self.simple_solution.get_ops(), 0)
        self.assertEqual(self.complex_solution.get_ops(), 0)

    def test_nbs_properties(self):

        self.assertEqual(self.simple_solution.get_nbs(), 2)
        self.assertEqual(self.empty_solution.get_nbs(), 0)
        self.assertEqual(self.complex_solution.get_nbs(), 2)

    def test_equality(self):

        same_solution = LinearSolution({"x": 2.5, "y": -1.0})
        different_solution = LinearSolution({"x": 1.0, "y": 2.0})

        self.assertEqual(self.simple_solution, same_solution)
        self.assertNotEqual(self.simple_solution, different_solution)
        self.assertNotEqual(self.simple_solution, "not a solution")

    def test_empty_solution(self):

        self.assertEqual(len(self.empty_solution.solution), 0)
        self.assertEqual(str(self.empty_solution), "")
        self.assertEqual(self.empty_solution.get_nbs(), 0)

    def test_complex_numbers(self):

        self.assertEqual(str(self.complex_solution), "a = (1+2j)\nb = (3-4j)")
        self.assertEqual(self.complex_solution.get_value()["a"], 1 + 2j)


if __name__ == "__main__":
    unittest.main()
