import unittest

from parameterized import parameterized

from src.main.python.calculator.divides import Divides
from src.main.python.calculator.illegal_construction import IllegalConstruction
from src.main.python.calculator.integer_number import IntegerNumber
from src.main.python.calculator.minus import Minus
from src.main.python.calculator.my_number import MyNumber
from src.main.python.calculator.notation import Notation
from src.main.python.calculator.plus import Plus
from src.main.python.calculator.times import Times


class TestNotation(unittest.TestCase):

    # Helper method (not a test)
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)

    def help_notation(self, s, o, n):
        """Auxiliary method to test notation."""
        o.accept_notation(n)
        self.assertEqual(s, str(o))

    # Helper method (not a test)
    def help_notations(self, symbol, value1, value2, op):
        """Auxiliary method to test all notations."""
        # Prefix notation
        self.help_notation(f"{symbol} ({value1}, {value2})", op, Notation.PREFIX)
        # Infix notation
        self.help_notation(f"( {value1} {symbol} {value2} )", op, Notation.INFIX)
        # Postfix notation
        self.help_notation(f"({value1}, {value2}) {symbol}", op, Notation.POSTFIX)

    @parameterized.expand(
        [
            ("*",),
            ("+",),
            ("/",),
            ("-",),
        ]
    )
    def testOutput(self, symbol):
        """Parameterized test to check output for different operations."""
        value1 = MyNumber(IntegerNumber(8))
        value2 = MyNumber(IntegerNumber(6))
        op = None
        params = [value1, value2]

        try:
            match symbol:
                case "+":
                    op = Plus(params)
                case "-":
                    op = Minus(params)
                case "*":
                    op = Times(params)
                case "/":
                    op = Divides(params)
                case _:
                    self.fail("Invalid symbol")
        except IllegalConstruction as e:
            self.fail(f"IllegalConstruction exception: {e}")

        # Test all notations
        self.help_notations(symbol, value1, value2, op)  # add assertion here


if __name__ == "__main__":
    unittest.main()
