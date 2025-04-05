import calculator
from src.main.python.calculator.divides import Divides
from src.main.python.calculator.illegal_construction import IllegalConstruction
from src.main.python.calculator.integer_number import IntegerNumber
from src.main.python.calculator.minus import Minus
from src.main.python.calculator.my_number import MyNumber
from src.main.python.calculator.notation import Notation
from src.main.python.calculator.plus import Plus
from src.main.python.calculator.rational_number import RationalNumber
from src.main.python.calculator.real_number import RealNumber
from src.main.python.calculator.times import Times


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

	params5 = [MyNumber(IntegerNumber(10)), MyNumber(IntegerNumber(5))]
	e = Divides(params5, Notation.INFIX)
	calculator.print_expression_details(e)
	calculator.eval_expression(e)

	e = Divides([MyNumber(IntegerNumber(5)), MyNumber(IntegerNumber(0))])
	calculator.print_result(e)
	calculator.eval_expression(e)

	sub1 = Plus([MyNumber(IntegerNumber(3)), MyNumber(IntegerNumber(4)), MyNumber(IntegerNumber(5))])
	sub2 = Minus([MyNumber(IntegerNumber(5)), MyNumber(IntegerNumber(3))])
	sub3 = MyNumber(IntegerNumber(5))
	e = Times([sub1, sub2, sub3])
	calculator.print_expression_details(e)
	calculator.eval_expression(e)

	params_rational = [MyNumber(RationalNumber(1, 2)), MyNumber(RationalNumber(1, 3))]
	e = Plus(params_rational)
	calculator.print_result(e)
	calculator.eval_expression(e)

	params_rational2 = [MyNumber(RationalNumber(3, 4)), MyNumber(RationalNumber(1, 4))]
	e = Divides(params_rational2)
	calculator.print_result(e)
	calculator.eval_expression(e)

	r1 = MyNumber(RationalNumber(1, 2))
	e_div_zero = Divides([r1, MyNumber(RationalNumber(0, 1))])
	calculator.print_result(e_div_zero)
	calculator.eval_expression(e_div_zero)



except IllegalConstruction as e:
	print("cannot create operations without parameters")