import os

from lark import Lark, Transformer, v_args

from src.main.python.calculator.complex_number import ComplexNumber
from src.main.python.calculator.divides import Divides
from src.main.python.calculator.integer_number import IntegerNumber
from src.main.python.calculator.inverse import Inverse, MatrixInverse
from src.main.python.calculator.linear_solver import LinearEquationSolver
from src.main.python.calculator.matrix import Matrix
from src.main.python.calculator.minus import Minus
from src.main.python.calculator.my_number import MyNumber
from src.main.python.calculator.notation import Notation
from src.main.python.calculator.plus import Plus
from src.main.python.calculator.power import Power
from src.main.python.calculator.real_number import RealNumber
from src.main.python.calculator.times import Times
from src.main.python.calculator.transpose import MatrixTranspose
from src.main.python.calculator.sinus import Sinus
from src.main.python.calculator.nroot import Nroot


# Get the directory where the current script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the path to the grammar file
grammar_path = os.path.join(script_dir, "grammar", "notation.lark")
# Load grammar from file or string
with open(grammar_path, "r") as f:
    grammar = f.read()

parser = Lark(grammar, parser="lalr", start="start")


class ExprTransformer(Transformer):

    @v_args(inline=True)
    def integer_number(self, token):
        return MyNumber(IntegerNumber(int(token)))

    @v_args(inline=True)
    def real_number(self, token):
        return MyNumber(RealNumber(float(token)))

    @v_args(inline=True)
    def complex_number(self, token):
        return MyNumber(ComplexNumber(0, token.get_value()))

    def add(self, args):

        return Plus(args)

    def sub(self, args):

        return Minus(args)

    def mul(self, args):

        return Times(args)

    def div(self, args):
        return Divides(args)

    @v_args(inline=True)
    def cst_e(self, args):
        return MyNumber(args)

    def nroot(self, args):
        return Nroot(args)

    def sin(self, token):
        return Sinus(token)

    @v_args(inline=True)
    def neg(self, token):
        return Times([token, MyNumber(IntegerNumber(-1))])

    def pow(self, args):
        return Power(args)

    def inverse(self, token):
        return Inverse(token)

    @v_args(inline=True)
    def linear_expr(self, equation_str):
        raw = str(equation_str)[1:-1]  # enlever les guillemets
        equations = [eq.strip() for eq in raw.split(";") if eq.strip()]
        solver = LinearEquationSolver(equations)
        return solver

    def row(self, items):
        return items

    def matrix(self, rows):
        if len(rows) == 1 and isinstance(rows[0], Matrix):
            return rows[0]  # évite double wrapping
        return Matrix(rows)

    @v_args(inline=True)
    def transpose(self, token):
        return MatrixTranspose([token])

    def matrix_inverse(self, children):
        matrix = children[0]
        return MatrixInverse([matrix], Notation.POSTFIX)


def parse_expression(expr_str: str):
    tree = parser.parse(expr_str)
    return ExprTransformer().transform(tree)
