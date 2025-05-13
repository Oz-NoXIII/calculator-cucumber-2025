import re

import sympy as sp

from src.main.python.calculator.linear_solution import LinearSolution


class LinearEquationSolver:
    def __init__(self, equations):
        if not equations or not isinstance(equations, list):
            raise ValueError(
                "Equations must be provided as a non-empty list of strings."
            )

        self.equations_raw = equations
        self.variables = set()
        self.parsed_system = None

    def accept(self, visitor):
        return visitor.visit_linear_solution(self)

    def preprocess_equation(self, eq):
        # Remove spaces
        eq = eq.replace(" ", "")
        # Insert * between coefficient and variable if missing
        eq = re.sub(r"(\d+)([a-zA-Z])", r"\1*\2", eq, flags=re.ASCII)
        eq = re.sub(r"([a-zA-Z])(\d)", r"\1*\2", eq, flags=re.ASCII)

        return eq

    def parse_equations(self):
        try:

            self.parse_equations()

            processed_eqs = []
            for eq in self.equations_raw:
                eq = self.preprocess_equation(eq)
                if "=" not in eq:
                    raise ValueError(f"Equation '{eq}' does not contain '=' sign.")
                lhs, rhs = eq.split("=")
                processed_eqs.append((lhs, rhs))

            symbols = set()
            sympy_eqs = []

            for lhs, rhs in processed_eqs:
                lhs_expr = sp.sympify(lhs)
                rhs_expr = sp.sympify(rhs)
                sympy_eqs.append(sp.Eq(lhs_expr, rhs_expr))
                symbols.update(lhs_expr.free_symbols)

            self.variables = sorted(list(symbols), key=lambda s: s.name)
            self.parsed_system = sympy_eqs
        except Exception:
            self.parsed_system = None

    def solve(self):
        try:
            self.parse_equations()
            if not self.parsed_system:
                return "Error solving equations"

            solution = sp.solve(self.parsed_system, self.variables, dict=True)
            if not solution:
                return "No solution found."

            if isinstance(solution, list):
                if len(solution) == 1:
                    sol_dict = solution[0]
                    result = {}
                    for var in self.variables:
                        val = sol_dict.get(var)
                        result[str(var)] = (
                            int(val) if val.is_integer else round(float(val), 2)
                        )
                    return LinearSolution(result)
                else:
                    return "Infinite solutions."

            return "Unexpected solution format."

        except Exception as e:
            return f"Error solving equations: {str(e)}"

    def get_depth(self):
        return 0

    def get_ops(self):
        return 0

    def get_nbs(self):
        return len(self.variables)

    def __str__(self):

        return self.equations_raw.__str__()
