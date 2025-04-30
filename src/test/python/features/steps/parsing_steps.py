from behave import given, then, when


@given("the following expression {expression}")
def step_given_expression(context, expression):
    context.expression = expression.strip()


@when("I parse the expression")
def step_when_parse_expression(context):
    from src.main.python.parsing.expression_parser import parse_expression

    context.result = parse_expression(context.expression)


@then("the result should be {expected}")
def step_then_result_type(context, expected):
    assert (
        str(context.result) == expected
    ), f"Expected {expected}, got {str(context.result)}"


@then("the result is between {expected1} or {expected2}")
def step_then_results_type(context, expected1, expected2):
    assert (
        str(context.result) == expected1 or str(context.result) == expected2
    ), f"Expected {expected1} or {expected2}, got {str(context.result)}"
