import calculator
from src.main.python.calculator.divides import Divides
from src.main.python.calculator.illegal_construction import IllegalConstruction
from src.main.python.calculator.minus import Minus
from src.main.python.calculator.my_number import MyNumber
from src.main.python.calculator.notation import Notation
from src.main.python.calculator.plus import Plus
from src.main.python.calculator.real_number import RealNumber
from src.main.python.calculator.times import Times
from src.main.python.calculator.rational_number import RationalNumber

try:
	e = MyNumber(RealNumber(8))
	calculator.print_result(e)
	calculator.eval_expression(e)

	test = [MyNumber(RealNumber(8)), MyNumber(RealNumber(0))]
	e = Divides(test, Notation.PREFIX)
	calculator.print_expression_details(e)
	calculator.eval_expression(e)

	params = [MyNumber(RealNumber(3)), MyNumber(RealNumber(4)), MyNumber(RealNumber(5))]
	e = Plus(params, Notation.PREFIX)
	calculator.print_expression_details(e)
	calculator.eval_expression(e)

	params2 = [MyNumber(RealNumber(5)), MyNumber(RealNumber(3))]
	e = Minus(params2, Notation.INFIX)
	calculator.print_result(e)
	calculator.eval_expression(e)

	params3 = [Plus(params), Minus(params2)]
	e = Times(params3)
	calculator.print_expression_details(e)
	calculator.eval_expression(e)

	params4 = [Plus(params), Minus(params2), MyNumber(RealNumber(5))]
	e = Divides(params4, Notation.POSTFIX)
	calculator.print_result(e)
	calculator.eval_expression(e)





except IllegalConstruction as e:
	print("cannot create operations without parameters")