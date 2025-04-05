from behave import given, when, then

from src.main.python.calculator import calculator
from src.main.python.calculator.divides import Divides
from src.main.python.calculator.illegal_construction import IllegalConstruction
from src.main.python.calculator.integer_number import IntegerNumber
from src.main.python.calculator.minus import Minus
from src.main.python.calculator.my_number import MyNumber
from src.main.python.calculator.notation import Notation
from src.main.python.calculator.plus import Plus
from src.main.python.calculator.real_number import RealNumber
from src.main.python.calculator.times import Times
from fractions import Fraction
from src.main.python.calculator.rational_number import RationalNumber
from src.main.python.visitor.evaluator import Evaluator


@given('I initialise a calculator')
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
            case _:
                assert False, f"{string} is an invalid operation"
    except IllegalConstruction as e:
        assert False, str(e)

@given("the following list of integer numbers")
def given_the_following_list_of_integer_numbers(context):
    for value in context.table.headings:
        context.params.append(MyNumber(IntegerNumber(int(value))))
        print(f"value = {value}")
    context.op = None

@given("the sum of two numbers {n1:d} and {n2:d}")
def given_the_sum_of_two_numbers(context, n1, n2):
    try:
        params = [MyNumber(IntegerNumber(n1)), MyNumber(IntegerNumber(n2))]
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

@when('I provide an expression containing an integer operation "{operation}" with the following list of integer numbers')
def when_i_provide_an_expression_containing_an_integer_operation_with_the_following_list_of_integer_numbers(context, operation):
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
            case _:
                assert False, "Invalid operation result type"
        result = calculator.eval_expression(op)
        assert expected == result.get_value(), f"Expected {expected}, found {result.get_value()}"
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




@given("the following list of rational numbers")
def given_list_of_rational_numbers(context):
    context.params = []
    for value in context.table.headings:
        num, denom = map(int, value.split("/"))
        context.params.append(RationalNumber(num, denom))

@when("I perform an addition")
def when_i_perform_an_addition(context):
    context.op = Plus(context.params)

@then("the rational is evaluates to {expected}")
def then_operation_evaluates_to_fraction(context, expected):
    result = calculator.eval_expression(context.op)
    expected_fraction = Fraction(expected)
    assert result == expected_fraction, f"Expected {expected_fraction}, got {result}"

@given('a real number {value:g}')
def step_given_real_number_1(context, value):
    context.num1 = MyNumber(RealNumber(value))

@given('another real number {value:g}')
def step_given_real_number_2(context, value):
    context.num2 = MyNumber(RealNumber(value))


@when('I divide them')
def step_when_divide_them(context):
    expr = Divides([context.num1, context.num2], Notation.INFIX)
    visitor = Evaluator()
    expr.accept(visitor)
    context.result = visitor.get_result()


@then('the result should be positive infinity')
def step_then_result_inf(context):
    assert context.result.is_infinite()
    assert context.result.get_value() > 0

@then('the result should be NaN')
def step_then_result_nan(context):
    assert context.result.is_nan()

@when('I add them')
def step_when_add(context):
    expr = Plus([context.num1, context.num2], Notation.INFIX)
    visitor = Evaluator()
    expr.accept(visitor)
    context.result = visitor.get_result()


@when('I subtract them')
def step_when_subtract(context):
    expr = Minus([context.num1, context.num2], Notation.INFIX)
    visitor = Evaluator()
    expr.accept(visitor)
    context.result = visitor.get_result()


@when('I multiply them')
def step_when_multiply(context):
    expr = Times([context.num1, context.num2], Notation.INFIX)
    visitor = Evaluator()
    expr.accept(visitor)
    context.result = visitor.get_result()


@then('the result should be {expected:g}')
def step_then_result(context, expected):
    actual = context.result.get_value()
    assert abs(actual - expected) < 1e-9, f"Expected {expected}, got {actual}"

