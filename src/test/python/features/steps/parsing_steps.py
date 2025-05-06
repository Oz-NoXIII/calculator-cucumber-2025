from behave import given, then, when

from src.main.python.parsing.expression_parser import parse_expression


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


@when("I evaluate the expression '{expr}'")
def step_impl_parse_expression(context, expr):
    context.result = parse_expression(expr)

@then("the result should contain")
def step_impl_check_result_table(context):
    assert isinstance(context.result, dict), f"Expected dict, got: {context.result}"
    for row in context.table:
        var, val = row[0].split("=")
        var, val = var.strip(), float(val.strip())
        assert var in context.result
        assert abs(context.result[var] - val) < 1e-6, f"{var} ≠ {val}, got {context.result[var]}"

@then('the result should contain "{text}"')
def step_impl_check_result_text(context, text):
    assert isinstance(context.result, str)
    #assert text.lower() in context.result.lower()