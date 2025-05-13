import math

import calculator

from src.main.python.calculator.complex_number import ComplexNumber
from src.main.python.calculator.cosinus import Cosinus
from src.main.python.calculator.divides import Divides
from src.main.python.calculator.exponent import Exponent
from src.main.python.calculator.illegal_construction import IllegalConstruction
from src.main.python.calculator.integer_number import IntegerNumber
from src.main.python.calculator.inverse import Inverse
from src.main.python.calculator.logarithm import Logarithm
from src.main.python.calculator.logarithmNeperien import LogarithmNeperien
from src.main.python.calculator.minus import Minus
from src.main.python.calculator.my_number import MyNumber
from src.main.python.calculator.notation import Notation
from src.main.python.calculator.plus import Plus
from src.main.python.calculator.power import Power
from src.main.python.calculator.rational_number import RationalNumber
from src.main.python.calculator.real_number import RealNumber
from src.main.python.calculator.sinus import Sinus
from src.main.python.calculator.times import Times
from src.main.python.parsing.expression_parser import parse_expression
from src.main.python.visitor.evaluator import Evaluator

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

    RealNumber.set_precision(8)

    x = RealNumber(3.1415926535)
    y = RealNumber(1.8e2)
    print("Normal:", x)
    print("Normal:", y)
    print("\nScientific:", x.to_scientific())
    print("\nScientific:", y.to_scientific())

    angle = RealNumber(math.pi)
    print("\nRadians to degrees:", angle.to_degrees())

    deg = RealNumber(180)
    print("\nDegrees to radians:", deg.to_radians())

    params5 = [MyNumber(IntegerNumber(10)), MyNumber(IntegerNumber(5))]
    e = Divides(params5, Notation.INFIX)
    calculator.print_expression_details(e)
    calculator.eval_expression(e)

    e = Divides([MyNumber(IntegerNumber(5)), MyNumber(IntegerNumber(0))])
    calculator.print_result(e)
    calculator.eval_expression(e)

    sub1 = Plus(
        [
            MyNumber(IntegerNumber(3)),
            MyNumber(IntegerNumber(4)),
            MyNumber(IntegerNumber(5)),
        ]
    )
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

    e = Plus([MyNumber(ComplexNumber(1, 1)), MyNumber(ComplexNumber(2, 3))])
    calculator.print_result(e)
    calculator.eval_expression(e)

    e = Divides([MyNumber(ComplexNumber(2, 3)), MyNumber(ComplexNumber(1, -1))])
    calculator.print_result(e)
    calculator.eval_expression(e)

    z = ComplexNumber(3, 4)  # 3 + 4i

    # modulus: |z| = 5
    mod_expr = z.modulus()
    evaluator = Evaluator()
    mod_result = evaluator.get_result()
    print(f"Modulus of {z}: {mod_expr} ")

    # conjugate: 3 - 4i
    conj_expr = z.conjugate()
    evaluator = Evaluator()
    conj_result = evaluator.get_result()
    print(f"Conjugate of {z}: {conj_expr} ")

    # sqrt: sqrt(3+4i)
    sqrt_expr = z.sqrt()
    evaluator = Evaluator()
    sqrt_result = evaluator.get_result()
    print(f"Sqrt of {z}: {sqrt_expr}")

    r = RealNumber(6.022e23)
    print(r.to_scientific())

    # pow : pow(1/4 ^ (1/4))
    rPow = MyNumber(RationalNumber(1, 4))
    e = Power([rPow, rPow], Notation.INFIX)
    calculator.print_expression_details(e)
    calculator.eval_expression(e)

    # pow : pow(1 +2i ^ (1 + 2i))
    rPowC = MyNumber(ComplexNumber(1, 2))
    rPowC2 = MyNumber(RealNumber(2))
    e = Power([rPowC, rPowC2], Notation.INFIX)
    calculator.print_expression_details(e)
    calculator.eval_expression(e)

    # inverse : inverse(5)
    rInv = MyNumber(RealNumber(5))
    e = Inverse([rInv], Notation.INFIX)
    calculator.print_expression_details(e)
    calculator.eval_expression(e)

    # logarithm : log(1)
    rLog = MyNumber(ComplexNumber(1, 0))
    e = Logarithm([rLog], Notation.INFIX)
    calculator.print_expression_details(e)
    calculator.eval_expression(e)

    # logarithm neperien : ln(1)
    rLogN = MyNumber(RealNumber(1))
    e = LogarithmNeperien([rLogN], Notation.INFIX)
    calculator.print_expression_details(e)
    calculator.eval_expression(e)

    # exponent : exp(1)
    rExp = MyNumber(RealNumber(1))
    e = Exponent([rExp], Notation.INFIX)
    calculator.print_expression_details(e)
    calculator.eval_expression(e)

    # sinus : sin(0)
    rSin = MyNumber(RealNumber(0))
    e = Sinus([rSin], Notation.INFIX)
    calculator.print_expression_details(e)
    calculator.eval_expression(e)

    # cosinus : cos(0)
    rCos = MyNumber(RealNumber(0))
    e = Cosinus([rCos], Notation.INFIX)
    calculator.print_expression_details(e)
    calculator.eval_expression(e)

    expr = "[[1, 2], [3, 4]] - [[2, 0], [1, 2]]"
    result = parse_expression(expr)

    calculator.print_result(result)
    calculator.print_expression_details(result)

    expr = "inv([[1, 2], [3, 4]])"
    result = parse_expression(expr)
    calculator.print_expression_details(result)

    expr = "transpose([[1, 2], [3, 4]])"
    result = parse_expression(expr)
    calculator.print_expression_details(result)

    res = parse_expression('solve_linear("2x + 3y = 5; 3x - 4z = 7; y + z = 10")')
    calculator.print_expression_details(res)

except IllegalConstruction:
    print("cannot create operations without parameters")
