import calculator
from src.main.python.calculator.divides import Divides
from src.main.python.calculator.illegal_construction import IllegalConstruction
from src.main.python.calculator.minus import Minus
from src.main.python.calculator.my_number import MyNumber
from src.main.python.calculator.notation import Notation
from src.main.python.calculator.plus import Plus
from src.main.python.calculator.times import Times
from src.main.python.calculator.rational_number import RationalNumber

try:
	e = MyNumber(8)
	calculator.print_result(e)
	calculator.eval_expression(e)

	test = [MyNumber(8), MyNumber(0)]
	e = Divides(test, Notation.PREFIX)
	calculator.print_expression_details(e)
	calculator.eval_expression(e)

	params = [MyNumber(3), MyNumber(4), MyNumber(5)]
	e = Plus(params, Notation.PREFIX)
	calculator.print_expression_details(e)
	calculator.eval_expression(e)

	params2 = [MyNumber(5), MyNumber(3)]
	e = Minus(params2, Notation.INFIX)
	calculator.print_result(e)
	calculator.eval_expression(e)

	params3 = [Plus(params), Minus(params2)]
	e = Times(params3)
	calculator.print_expression_details(e)
	calculator.eval_expression(e)

	params4 = [Plus(params), Minus(params2), MyNumber(5)]
	e = Divides(params4, Notation.POSTFIX)
	calculator.print_result(e)
	calculator.eval_expression(e)

	params_rational = [RationalNumber(1, 2), RationalNumber(1, 3)]
	e = Plus(params_rational)
	print("Evaluating rational addition:")
	calculator.print_result(e)

	params_rational2 = [RationalNumber(3, 4), RationalNumber(1, 4)]
	e = Divides(params_rational2)
	print("Evaluating rational division:")
	calculator.print_result(e)

	from src.main.python.calculator.complex_number import ComplexNumber

	e = Plus([ComplexNumber(1, 1), ComplexNumber(2, 3)])
	print("Complex addition:")
	calculator.print_result(e)

	e = Divides([ComplexNumber(2, 3), ComplexNumber(1, -1)])
	print("Complex division:")
	calculator.print_result(e)



except IllegalConstruction as e:
	print("cannot create operations without parameters")