import re

import sympy as sp

# from src.main.python.visitor.linearsolvervisitor import SolverVisitor
# from src.main.python.visitor.visitor import Visitor


class LinearEquationSolver:
    def __init__(self, equations):
        if not equations or not isinstance(equations, list):
            raise ValueError(
                "Equations must be provided as a non-empty list of strings."
            )

        self.equations_raw = equations
        self.variables = set()
        self.parsed_system = None

    def preprocess_equation(self, eq):
        # Remove spaces
        eq = eq.replace(" ", "")
        # Insert * between coefficient and variable if missing
        eq = re.sub(r"(\d)([a-zA-Z])", r"\1*\2", eq)
        eq = re.sub(r"([a-zA-Z])(\d)", r"\1*\2", eq)
        return eq

    def parse_equations(self):
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

    def solve(self):
        try:
            self.parse_equations()
            if not self.parsed_system:
                return "Error solving equations: Cannot convert expression to float"

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
                    return result
                else:
                    return "Infinite solutions."

            return "Unexpected solution format."

        except Exception as e:
            return f"Error solving equations: {str(e)}"


"""import sympy as sp
import re

class LinearEquationSolver:
    def __init__(self, equations):
        self.equations = equations
        self.parsed_equations = []  # Pour stocker les équations converties en objets
        self.variables = []  # Pour stocker les variables extraites des équations

    def parse_equation(self, eq):
        # Ajout de '*' entre les coefficients et les variables
        eq = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', eq)  # Pour '2x' devient '2*x'
        eq = re.sub(r'([a-zA-Z])(\d)', r'\1*\2', eq)  # Pour 'x2' devient 'x*2'

        try:
            # Divise l'équation en gauche (lhs) et droite (rhs)
            lhs, rhs = eq.split("=")

            # Utilise sympy pour convertir l'expression en objets manipulables
            lhs_expr = sp.sympify(lhs)
            rhs_expr = sp.sympify(rhs)

            # Retourne une équation sous forme de relation SymPy
            return sp.Eq(lhs_expr, rhs_expr)

        except Exception as e:
            print(f"Error parsing equation: {eq} -> {e}")
            return None

    def parse(self):
        for eq in self.equations:
            parsed_eq = self.parse_equation(eq)
            if parsed_eq is not None:  # Vérification explicite de la validité de l'équation
                self.parsed_equations.append(parsed_eq)

                # Extraire les variables des équations (en utilisant set pour éliminer les doublons)
                self.variables.extend([str(var) for var in parsed_eq.free_symbols])

        # Supprimer les doublons dans la liste des variables
        self.variables = list(set(self.variables))  # Convertion en set puis liste pour éliminer les doublons

    def solve(self):
        self.parse()  # Convertit les chaînes d'équations en objets manipulables
        # Utilisation de sympy.solve pour résoudre les équations
        solutions = sp.solve(self.parsed_equations, self.variables)
        return solutions"""


if __name__ == "__main__":
    equations = ["2x + 3y = 5", "3x - 4z = 7", "y + z = 10"]

    solver = LinearEquationSolver(equations)
    result = solver.solve()
    print(result)
