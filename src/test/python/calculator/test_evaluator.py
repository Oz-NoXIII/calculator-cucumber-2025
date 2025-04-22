import unittest

from parameterized import parameterized

from src.main.python.calculator import calculator
from src.main.python.calculator.divides import Divides
from src.main.python.calculator.illegal_construction import IllegalConstruction
from src.main.python.calculator.integer_number import IntegerNumber
from src.main.python.calculator.minus import Minus
from src.main.python.calculator.my_number import MyNumber
from src.main.python.calculator.plus import Plus
from src.main.python.calculator.times import Times
from src.main.python.calculator.power import Power


class TestEvaluator(unittest.TestCase):

    def setUp(self):
        self.value1 = MyNumber(IntegerNumber(8))
        self.value2 = MyNumber(IntegerNumber(6))

    def test_evaluate_my_number(self):
        self.assertEqual(
            self.value1.get_number_type(), calculator.eval_expression(self.value1)
        )

    @parameterized.expand(
        [
            ("*",),
            ("+",),
            ("/",),
            ("-",),
            ("^",),
        ]
    )
    def test_evaluate_operations(self, symbol):
        params = [self.value1, self.value2]
        try:
            match symbol:
                case "+":
                    expected = self.value1.get_number_type().add(
                        self.value2.get_number_type()
                    )
                    result = calculator.eval_expression(Plus(params))
                case "-":
                    expected = self.value1.get_number_type().subtract(
                        self.value2.get_number_type()
                    )
                    result = calculator.eval_expression(Minus(params))
                case "*":
                    expected = self.value1.get_number_type().multiply(
                        self.value2.get_number_type()
                    )
                    result = calculator.eval_expression(Times(params))
                case "/":
                    expected = self.value1.get_number_type().divide(
                        self.value2.get_number_type()
                    )
                    result = calculator.eval_expression(Divides(params))
                case "^":
                    expected = self.value1.get_number_type().pow(
                        self.value2.get_number_type()
                    )
                    result = calculator.eval_expression(Power(params))
                case _:
                    self.fail("Invalid symbol")

            self.assertEqual(expected.get_value(), result.get_value())

        except IllegalConstruction as e:
            self.fail(e)


if __name__ == "__main__":
    unittest.main()
