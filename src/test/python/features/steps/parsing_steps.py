from behave import given, then, when

from src.main.python.calculator import calculator
from src.main.python.calculator.matrix import Matrix
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
        assert (
            abs(context.result[var] - val) < 1e-6
        ), f"{var} ≠ {val}, got {context.result[var]}"


@then('the result should contain "{text}"')
def step_impl_check_result_text(context, text):
    if hasattr(context, "result"):

        assert text in str(
            context.result
        ), f"Expected error message '{text}' in result but got '{context.result}'"
    elif hasattr(context, "error_message"):

        assert (
            text in context.error_message
        ), f"Expected error message '{text}' but got '{context.text}'"
    else:
        raise AssertionError("No result or error message found")


@given("the matrix calculator is ready")
def step_given_matrix(context):
    context.parser = parse_expression


@when('I parse the matrix expression "{expression}"')
def step_parse_matrix(context, expression):
    try:
        context.result = parse_expression(expression)
    except Exception as e:
        context.exception = e


@then("the matrix should be")
def step_result_matrix_should_be(context):
    evaluated = calculator.eval_expression(context.result)
    assert isinstance(evaluated, Matrix), f"Expected Matrix, got {type(evaluated)}"
    expected = [[cell for cell in row.cells] for row in context.table]
    actual = [[cell.get_value().__str__() for cell in row] for row in evaluated.data]
    assert actual == expected, f"Expected {expected}, got {actual}"


@then("the matrix should be approximately")
def step_result_matrix_should_be_approx(context):
    evaluated = calculator.eval_expression(context.result)
    assert isinstance(evaluated, Matrix), f"Expected Matrix, got {type(evaluated)}"
    expected = [[cell for cell in row.cells] for row in context.table]
    actual = [[cell.__str__() for cell in row] for row in evaluated.data]
    assert actual == expected, f"Expected {expected}, got {actual}"
    for i in range(len(expected)):
        for j in range(len(expected[i])):
            assert (
                abs(float(actual[i][j]) - float(expected[i][j])) < 1e-6
            ), f"Mismatch at ({i}, {j}): expected {expected[i][j]}, got {actual[i][j]}"


@then('an error should be raised with message "{msg}"')
def step_error_should_be_raised(context, msg):
    assert context.error is not None, "Expected an error but none was raised"
    assert msg in context.error, f"Expected message '{msg}' in '{context.error}'"
