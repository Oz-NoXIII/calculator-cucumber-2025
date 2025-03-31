import numpy as np
import re

class LinearEquationSolver:

    def __init__(self, equation):
        self.equations = equation
        self.variables = []
        self.coeff_matrix = []
        self.constants = []

    def parse_equations(self):
        var_set = set()
        parsed_equations = []

        for eq in self.equations:
            if '=' not in eq:
                raise ValueError(f"Equation '{eq}' is invalid (missing '=' sign).")

            lhs, rhs = eq.split('=')
            lhs_terms = re.findall(r'[+-]?\s*\d*\s*[a-zA-Z]', lhs.replace(' ', ''))
            const = int(rhs.strip())
            eq_dict = {}

            for term in lhs_terms:
                term = term.replace(' ', '')
                match = re.fullmatch(r'([+-]?)(\d*)([a-zA-Z])', term)
                if not match:
                    raise ValueError(f"Invalid term '{term}' in equation '{eq}'")

                sign, coeff, var = match.groups()
                coeff = int(coeff) if coeff else 1.0
                if sign == '-':
                    coeff = -coeff
                eq_dict[var] = eq_dict.get(var, 0.0) + coeff
                var_set.add(var)

            parsed_equations.append((eq_dict, const))

        self.variables = sorted(var_set)

        for eq_dict, const in parsed_equations:
            row = [eq_dict.get(var, 0.0) for var in self.variables]
            self.coeff_matrix.append(row)
            self.constants.append(const)


    def solve(self):
        try:
            self.parse_equations()
            A = np.array(self.coeff_matrix, dtype=int)
            b = np.array(self.constants, dtype=int)
            solution = np.linalg.solve(A, b)

            result = {}
            for var, val in zip(self.variables, solution):
                if np.isclose(val, round(val), atol=1e-8):
                    result[var] = int(round(val))
                else:
                    result[var] = round(val, 2)
            return result

        except np.linalg.LinAlgError:
            return "Incompatible system: no unique solution (none or infinite)."
        except Exception as e:
            return f"Syntax or analysis errors: {e}"


if __name__ == "__main__":
    equations = [
        "2x+3y=5",
        "3x-4z=7",
        "y+z=10"
    ]
    solver = LinearEquationSolver(equations)
    solution = solver.solve()
    print("Solution:")
    print(solution)
