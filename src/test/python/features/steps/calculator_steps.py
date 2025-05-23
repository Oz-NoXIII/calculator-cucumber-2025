import math
from fractions import Fraction

from behave import given, then, when

from src.main.python.calculator import calculator
from src.main.python.calculator.complex_number import ComplexNumber
from src.main.python.calculator.divides import Divides
from src.main.python.calculator.illegal_construction import IllegalConstruction
from src.main.python.calculator.integer_number import IntegerNumber
from src.main.python.calculator.inverse import Inverse
from src.main.python.calculator.minus import Minus
from src.main.python.calculator.my_number import MyNumber
from src.main.python.calculator.notation import Notation
from src.main.python.calculator.plus import Plus
from src.main.python.calculator.power import Power
from src.main.python.calculator.rational_number import RationalNumber
from src.main.python.calculator.real_number import RealNumber
from src.main.python.calculator.times import Times
from src.main.python.visitor.evaluator import Evaluator


@given("I initialise a calculator")
def step_initialize_calculator(context):
    context.params = []
    context.op = None


@given("an integer operation '{string}'")
def given_an_integer_operation(context, string):
    try:
        match string:
            case "+":
                context.op = Plus([])
            case "-":
                context.op = Minus([])
            case "*":
                context.op = Times([])
            case "/":
                context.op = Divides([])
            case "^":
                context.op = Power([])
            case "1/":
                context.op = Inverse([])
            case _:
                assert False, f"{string} is an invalid operation"
    except IllegalConstruction as e:
        assert False, str(e)


@given("the following list of integer numbers")
def given_the_following_list_of_integer_numbers(context):
    for value in context.table.headings:
        context.params.append(MyNumber(IntegerNumber(int(value))))
    context.op = None


@given("the sum of two numbers {n1:d} and {n2:d}")
def given_the_sum_of_two_numbers(context, n1, n2):
    try:
        context.op = Plus([MyNumber(IntegerNumber(n1)), MyNumber(IntegerNumber(n2))])
    except IllegalConstruction as e:
        assert False, str(e)


@then("its {notation} notation is {expected}")
def then_its_notation_is(context, notation, expected):
    match notation:
        case "INFIX":
            context.op.accept_notation(Notation.INFIX)
        case "PREFIX":
            context.op.accept_notation(Notation.PREFIX)
        case "POSTFIX":
            context.op.accept_notation(Notation.POSTFIX)
        case _:
            assert False, f"{notation} is not a correct notation"

    assert str(context.op) == expected, f"Expected {expected}, found {str(context.op)}"


@when("I provide a {name} number {value:d}")
def when_i_provide_a_number(context, name, value):
    params = [MyNumber(IntegerNumber(value))]
    context.op.add_more_params(params)


@when(
    'I provide an expression containing an integer operation "{operation}" with the following list of integer numbers'
)
def when_i_provide_an_expression_containing_an_integer_operation_with_the_following_list_of_integer_numbers(
    context, operation
):
    internal_params = []
    for value in context.table.headings:
        internal_params.append(MyNumber(IntegerNumber(int(value))))
    try:
        match operation:
            case "+":
                internal_op = Plus(internal_params)
            case "-":
                internal_op = Minus(internal_params)
            case "*":
                internal_op = Times(internal_params)
            case "/":
                internal_op = Divides(internal_params)
            case "^":
                internal_op = Power(internal_params)
            case "1/":
                internal_op = Inverse(internal_params)
            case _:
                assert False, "Invalid operation"
    except IllegalConstruction as e:
        assert False, str(e)

    params = [internal_op]
    context.op.add_more_params(params)


@then("the {operation} is {expected:d}")
def then_the_operation_is(context, operation, expected):
    try:
        match operation:
            case "sum":
                op = Plus(context.params)
            case "difference":
                op = Minus(context.params)
            case "product":
                op = Times(context.params)
            case "quotient":
                op = Divides(context.params)
            case "power":
                op = Power(context.params)
            case "inverse":
                op = Inverse(context.params)
            case _:
                assert False, "Invalid operation result type"
        result = calculator.eval_expression(op)
        assert (
            expected == result.get_value()
        ), f"Expected {expected}, found {result.get_value()}"
    except IllegalConstruction as e:
        assert False, str(e)


@then("the operation evaluates to {expected}")
def then_the_operation_evaluates_to(context, expected):
    result = calculator.eval_expression(context.op)
    if expected == "NaN":
        assert result.is_nan(), "Expected NaN, but got a value"
    else:
        expected = int(expected)
        actual = result.get_value() if hasattr(result, "get_value") else result
        assert expected == actual, f"Expected {expected}, found {actual}"


@when("I perform an addition")
def when_i_perform_an_addition(context):
    context.op = Plus(context.params)


@then("the rational is evaluates to {expected}")
def then_operation_evaluates_to_fraction(context, expected):
    result = calculator.eval_expression(context.op)
    expected_fraction = Fraction(expected)
    assert result == expected_fraction, f"Expected {expected_fraction}, got {result}"


@given("a real number {value:g}")
def given_real_number_1(context, value):
    context.num1 = MyNumber(RealNumber(float(value)))


@given("another real number {value:g}")
def given_real_number_2(context, value):
    context.num2 = MyNumber(RealNumber(value))


@when("I divide them")
def when_divide_them(context):
    context.expr = Divides([context.num1, context.num2], Notation.INFIX)
    n1 = context.num1.get_number_type()
    n2 = context.num2.get_number_type()
    context.result = n1.divide(n2)


@then("the result should be Infinity")
def step_infinity(context):
    val = context.result.get_value()
    assert context.result.is_infinite() and val > 0, f"Expected +∞, got {val}"


@then("the result should be -Infinity")
def step_neg_infinity(context):
    val = context.result.get_value()
    assert context.result.is_infinite() and val < 0, f"Expected -∞, got {val}"


@then("the result should be NaN")
def then_result_nan(context):
    assert context.result.is_nan()


@when("I add them")
def when_add(context):
    context.expr = Plus([context.num1, context.num2], Notation.INFIX)
    n1 = context.num1.get_number_type()
    n2 = context.num2.get_number_type()
    context.result = n1.add(n2)


@when("I subtract them")
def when_subtract(context):
    context.expr = Minus([context.num1, context.num2], Notation.INFIX)
    n1 = context.num1.get_number_type()
    n2 = context.num2.get_number_type()
    context.result = n1.subtract(n2)


@when("I multiply them")
def when_multiply(context):
    context.expr = Times([context.num1, context.num2], Notation.INFIX)
    n1 = context.num1.get_number_type()
    n2 = context.num2.get_number_type()
    context.result = n1.multiply(n2)


@when("I power the first to the second them")
def when_power(context):
    context.expr = Power([context.num1, context.num2], Notation.INFIX)
    n1 = context.num1.get_number_type()
    n2 = context.num2.get_number_type()
    context.result = n1.pow(n2)


@when("I inverse it")
def when_inverse(context):
    context.expr = Inverse([context.num1], Notation.INFIX)
    n1 = context.num1.get_number_type()
    context.result = n1.inverse()


@when("I use the sinus to it")
def when_sinus(context):
    context.expr = Inverse([context.num1], Notation.INFIX)
    n1 = context.num1.get_number_type()
    context.result = n1.sin()


@when("I use the cosinus to it")
def when_cosinus(context):
    context.expr = Inverse([context.num1], Notation.INFIX)
    n1 = context.num1.get_number_type()
    context.result = n1.cos()


@when("I use the exponent to it")
def when_exponent(context):
    context.expr = Inverse([context.num1], Notation.INFIX)
    n1 = context.num1.get_number_type()
    context.result = n1.exp()


@when("I use the log to it")
def when_logarithm(context):
    context.expr = Inverse([context.num1], Notation.INFIX)
    n1 = context.num1.get_number_type()
    context.result = n1.log()


@when("I use the ln to it")
def when_logarithm_neperien(context):
    context.expr = Inverse([context.num1], Notation.INFIX)
    n1 = context.num1.get_number_type()
    context.result = n1.ln()


@then("the result should be {expected:g}")
def then_result(context, expected):
    actual = context.result.get_value()
    assert abs(actual - expected) < 1e-9, f"Expected {expected}, got {actual}"


@given("a rational number {value}")
def given_rational1(context, value):
    n, d = map(int, value.split("/"))
    context.num1 = MyNumber(RationalNumber(n, d))


@given("another rational number {value}")
def given_rational2(context, value):
    n, d = map(int, value.split("/"))
    context.num2 = MyNumber(RationalNumber(n, d))


@given("an integer number {value:d}")
def given_integer(context, value):
    context.num2 = MyNumber(IntegerNumber(value))


@then('its fraction form is "{expected}"')
def step_fraction(context, expected):
    assert str(
        context.num1.get_number_type() == expected
    ), f"Expected {expected}, got {context.num1.get_number_type()}"


@then('its mixed form is "{expected}"')
def step_mixed(context, expected):
    assert (
        context.num1.get_number_type().to_mixed_str() == expected
    ), f"Expected {expected}, got {context.num1.get_number_type().to_mixed_str()}"


def parse_number(val: str):
    if "/" in val:
        n, d = map(int, val.split("/"))
        return MyNumber(RationalNumber(n, d))
    else:
        return MyNumber(IntegerNumber(int(val)))


@given("the following list of rational numbers")
def given_rational_list(context):
    context.params = []
    for val in context.table.headings:
        context.params.append(parse_number(val))


@given("the following mixed list of rational and integer numbers")
def given_mixed_list(context):
    context.params = []
    for val in context.table.headings:
        context.params.append(parse_number(val))


@when("I compute their sum")
def compute_sum(context):
    context.expr = Plus(context.params)


@when("I compute their product")
def compute_product(context):
    context.expr = Times(context.params)


@given("a rational expression {name} using {op} with the list")
def given_define_expression(context, name, op):
    params = [parse_number(v) for v in context.table.headings]
    match op:
        case "+":
            context.expr = Plus(params)
        case "-":
            context.expr = Minus(params)
        case "*":
            context.expr = Times(params)
        case "/":
            context.expr = Divides(params)
        case "^":
            context.expr = Power(params)
        case "1/":
            context.expr = Inverse(params)
        case _:
            raise AssertionError(f"Unsupported op: {op}")

    if not hasattr(context, "subexprs"):
        context.subexprs = {}
    context.subexprs[name] = context.expr


@when("I combine expressions {expr_names} with {op}")
def when_combine_named_expressions(context, expr_names, op):
    names = [n.strip('"') for n in expr_names.split(",")]
    params = [context.subexprs[name] for name in names]

    match op:
        case "+":
            context.expr = Plus(params)
        case "-":
            context.expr = Minus(params)
        case "*":
            context.expr = Times(params)
        case "/":
            context.expr = Divides(params)
        case "^":
            context.expr = Power(params)
        case "1/":
            context.expr = Inverse(params)
        case _:
            raise AssertionError(f"Unsupported combination op: {op}")


@then("the rational result should be {expected}")
def expected_fraction(context, expected):
    evaluator = Evaluator()
    context.expr.accept(evaluator)
    result = evaluator.get_result().get_value()
    expected_frac = Fraction(expected)
    assert result == expected_frac, f"Expected {expected_frac}, got {result}"


def parse_complex(s):
    s = s.replace("i", "j")
    return MyNumber(ComplexNumber.from_complex(complex(s)))


@given("a complex number {value}")
def given_c1(context, value):
    context.num1 = parse_complex(value)


@given("another complex number {value}")
def given_c2(context, value):
    context.num2 = parse_complex(value)


@when("I get its modulus")
def modulus(context):
    context.result = context.num1.get_number_type().modulus()


@when("I get its conjugate")
def conjugate(context):
    context.result = context.num1.get_number_type().conjugate()


@when("I take the square root")
def step_sqrt(context):
    context.result = context.num1.get_number_type().sqrt()


@then("the complex result should be {expected}")
def result_complex(context, expected):
    expected_c = complex(expected.replace("i", "j"))
    actual = context.result.get_value()
    assert abs(actual.real - expected_c.real) < 1e-9
    assert abs(actual.imag - expected_c.imag) < 1e-9


@then("the result is approximately {expected:g}")
def real_result(context, expected):
    expected = float(expected)

    if hasattr(context.result, "get_value"):
        actual = context.result.get_value()
    else:
        actual = context.result
    assert math.isclose(
        actual, expected, abs_tol=1e-6
    ), f"Expected {expected}, got {actual}"


@then("the result is close to {expected} within {tolerance:g}")
def step_result_close(context, expected, tolerance):
    expected = expected.strip()

    # Complex number: 3+2i
    if "i" in expected:
        expected_val = complex(expected.replace("i", "j"))
        actual_val = context.result.get_value()
        assert isinstance(actual_val, complex), "Expected complex result"
        assert math.isclose(
            actual_val.real, expected_val.real, abs_tol=tolerance
        ), f"Real part mismatch: expected {expected_val.real}, got {actual_val.real}"
        assert math.isclose(
            actual_val.imag, expected_val.imag, abs_tol=tolerance
        ), f"Imag part mismatch: expected {expected_val.imag}, got {actual_val.imag}"

    # Rational number: 3/4
    elif "/" in expected:
        expected_val = Fraction(expected)
        actual_val = context.result.get_value()
        assert actual_val == expected_val, f"Expected {expected_val}, got {actual_val}"

    # Real/float: 3.1416
    else:
        expected_val = float(expected)
        actual_val = context.result.get_value()
        assert math.isclose(
            actual_val, expected_val, abs_tol=tolerance
        ), f"Expected {expected_val}, got {actual_val}"


@when("I convert to radians")
def convert_to_radians(context):
    context.result = context.num1.get_number_type().to_radians()


@when("I convert to degrees")
def convert_to_degrees(context):
    context.result = context.num1.get_number_type().to_degrees()


@when("I set the precision to {value}")
def set_precision(context, value):
    RealNumber.set_precision(value)


@then('its string representation is "{expected}"')
def check_string(context, expected):
    assert (
        str(context.num1) == expected
    ), f"Expected {expected}, got {str(context.num1)}"


@then('the scientific notation is "{expected}"')
def check_scientific(context, expected):
    assert (
        context.num1.get_number_type().to_scientific() == expected
    ), f"Expected {expected}, got {context.num1.get_number_type().to_scientific()}"


@when("I take the logarithm")
def step_log(context):
    context.result = context.num1.get_number_type().ln()
