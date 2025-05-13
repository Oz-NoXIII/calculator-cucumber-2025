from src.main.python.calculator.expression import Expression


class LinearSolution(Expression):
    def __init__(self, solution_dict):
        self.solution = solution_dict

    def accept(self, visitor):
        return visitor.visit_linear_solution(self)

    def __str__(self):
        return "\n".join(f"{k} = {v}" for k, v in self.solution.items())

    def get_value(self):
        return self.solution

    def get_depth(self):
        return 0

    def get_ops(self):
        return 0

    def get_nbs(self):
        return len(self.solution)

    def __eq__(self, other):
        return isinstance(other, LinearSolution) and self.solution == other.solution
