from behave import given, then, when

from src.main.python.calculator import calculator
from src.main.python.calculator.divides import Divides
from src.main.python.calculator.illegal_construction import IllegalConstruction
from src.main.python.calculator.minus import Minus
from src.main.python.calculator.my_number import MyNumber
from src.main.python.calculator.notation import Notation
from src.main.python.calculator.plus import Plus
from src.main.python.calculator.times import Times


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
            case _:
                assert False, f"{string} is an invalid operation"
    except IllegalConstruction as e:
        assert False, str(e)


@given("the following list of integer numbers")
def given_the_following_list_of_integer_numbers(context):
    for value in context.table.headings:
        context.params.append(MyNumber(int(value)))
        print(f"value = {value}")
    context.op = None


@given("the sum of two numbers {n1:d} and {n2:d}")
def given_the_sum_of_two_numbers(context, n1, n2):
    try:
        context.op = Plus([MyNumber(n1), MyNumber(n2)])
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
    params = [MyNumber(value)]
    context.op.add_more_params(params)


@when(
    'I provide an expression containing an integer operation "{operation}" with the following list of integer numbers'
)
def when_i_provide_an_expression_containing_an_integer_operation_with_the_following_list_of_integer_numbers(
    context, operation
):
    internal_params = []
    for value in context.table.headings:
        internal_params.append(MyNumber(int(value)))
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
        assert expected == result, f"Expected {expected}, found {result}"
    except IllegalConstruction as e:
        assert False, str(e)


@then("the operation evaluates to {expected}")
def then_the_operation_evaluates_to(context, expected):
    result = calculator.eval_expression(context.op)
    if expected != "NaN":
        expected = int(expected)
    assert expected == result, f"Expected {expected}, found {result}"
