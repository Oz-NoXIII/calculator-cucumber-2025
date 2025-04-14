import re

import numpy as np

def run_interactive_solver():

    while True:
        print("\nEnter your equations one by one. Type 'ok' to solve.\n")

        equations = []
        while True:
            line = input(f"Équation {len(equations)+1} > ")
            if line.strip().lower() == "ok":
                break
            if line.strip() == "":
                print(
                    " Empty input. Please enter a valid equation or press 'ok' to continue.."
                )
                again = (
                    input("\nWould you like to solve a different system? (y/n) : ")
                    .strip()
                    .lower()
                )
                if again != "y":
                    print("End of program.")
                    break
            equations.append(line.strip())

        if not equations:
            print("No system supplied.")
            again = (
                input("\nWould you like to solve a different system? (y/n) : ")
                .strip()
                .lower()
            )
            if again != "y":
                print("End of program.")
                break

        solver = LinearEquationSolver(equations)
        result = solver.solve()

        print("Results :")
        if isinstance(result, dict):
            for var, val in result.items():
                print(f"  {var} = {val}")
        else:
            print(f"{result}")

        again = (
            input("\nWould you like to solve a different system? (y/n) : ")
            .strip()
            .lower()
        )
        if again != "y":
            print("End of program.")
            break


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
            if "=" not in eq:
                raise ValueError(f"Equation '{eq}' is invalid (missing '=' sign).")

            lhs, rhs = eq.split("=")
            lhs_terms = re.findall(r"[+-]?[^+-]+", lhs.replace(" ", ""))
            const = float(rhs.strip())
            eq_dict = {}

            for term in lhs_terms:
                term = term.replace(" ", "")
                match = re.fullmatch(r"([+-]?)(\d+(?:\.\d+)?|\d+/\d+)?([a-zA-Z])", term)
                if not match:
                    raise ValueError(f"Invalid term '{term}' in equation '{eq}'")

                sign, coeff, var = match.groups()
                coeff = float(coeff) if coeff else 1.0
                if sign == "-":
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
            A = np.array(self.coeff_matrix)
            b = np.array(self.constants)
            solution = np.linalg.solve(A, b)

            result = {}
            for var, val in zip(self.variables, solution):
                if np.isclose(val, round(val), atol=1e-8):
                    result[var] = int(round(val))
                else:
                    result[var] = round(val, 2)
            return result

        except np.linalg.LinAlgError as e:
            return f"Incompatible or undetermined system : {e}"

        except Exception as e:
            return f"Syntax or analysis errors: {e}"
