from lark import Lark, Transformer, v_args

from src.main.python.calculator.divides import Divides
from src.main.python.calculator.integer_number import IntegerNumber
from src.main.python.calculator.minus import Minus
from src.main.python.calculator.my_number import MyNumber
from src.main.python.calculator.plus import Plus
from src.main.python.calculator.times import Times
import os

# Get the directory where the current script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the path to the grammar file
grammar_path = os.path.join(script_dir, 'grammar', 'infix.lark')
# Load grammar from file or string
with open(grammar_path, 'r') as f:
    infix_grammar = f.read()

infix_parser = Lark(infix_grammar, parser='lalr', start='start')


@v_args(inline=True)
class ExprTransformer(Transformer):
    def integer_number(self, token):
        return MyNumber(IntegerNumber(token))

    def add(self, left, right):
        return Plus([left, right])

    def sub(self, left, right):
        return Minus([left, right])

    def mul(self, left, right):
        return Times([left, right])

    def div(self, left, right):
        return Divides([left, right])

    def neg(self, token):
        return MyNumber(IntegerNumber(int(token.get_value()) * -1))


def parse_expression(expr_str: str, notation='infix'):
    if notation == 'infix':
        tree = infix_parser.parse(expr_str)
        return ExprTransformer().transform(tree)
