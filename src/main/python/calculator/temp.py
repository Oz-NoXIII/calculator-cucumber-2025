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