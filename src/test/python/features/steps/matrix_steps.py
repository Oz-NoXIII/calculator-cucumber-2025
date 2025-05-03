import ast

from behave import given, then, when

from src.main.python.calculator.integer_number import IntegerNumber
from src.main.python.calculator.matrix import Matrix


def parse_matrix(matrix_str):

    return ast.literal_eval(matrix_str)


@given("I have matrix A = {matrix_str}")
def given_a_matrix_A(context, matrix_str):

    matrix_data = parse_matrix(matrix_str)
    context.matrix_data = []
    for row in matrix_data:
        context.matrix_data.append([IntegerNumber(int(cell)) for cell in row])


@given("I have matrix B = {matrix_str}")
def given_a_matrix_B(context, matrix_str):

    matrix_data = parse_matrix(matrix_str)
    context.other_matrix_data = []
    for row in matrix_data:
        context.other_matrix_data.append([IntegerNumber(int(cell)) for cell in row])


@when("I add the matrices")
def when_i_add_the_matrices(context):
    matrix1 = Matrix(context.matrix_data)
    matrix2 = Matrix(context.other_matrix_data)
    try:
        context.result = matrix1.add(matrix2)
    except ValueError as e:
        context.error_message = str(e)


@when("I multiply the matrices")
def when_i_multiply_the_matrices(context):
    matrix1 = Matrix(context.matrix_data)
    matrix2 = Matrix(context.other_matrix_data)
    context.result = matrix1.multiply(matrix2)


@when("I transpose the matrix")
def when_i_transpose_the_matrix(context):
    matrix = Matrix(context.matrix_data)
    context.result = matrix.transpose()


@when("I invert the matrix")
def when_i_invert_the_matrix(context):
    matrix = Matrix(context.matrix_data)
    try:
        context.result = matrix.inverse()
    except ValueError as e:
        context.error_message = str(e)


@then("the result matrix should be {expected_result}")
def then_the_result_should_be(context, expected_result):
    result_data = parse_matrix(expected_result)
    result_matrix = context.result.data
    for i, row in enumerate(result_data):
        for j, cell in enumerate(row):
            expected_value = cell
            actual_value = (
                result_matrix[i][j].get_value()
                if hasattr(result_matrix[i][j], "get_value")
                else float(result_matrix[i][j])
            )
            assert (
                abs(expected_value - actual_value) < 1e-6
            ), f"Expected {expected_value} but got {actual_value} at position ({i}, {j})"


@then('I should see an error message "{error_message}"')
def then_result_should_contain(context, error_message):
    if hasattr(context, "result"):

        assert error_message in str(
            context.result
        ), f"Expected error message '{error_message}' in result but got '{context.result}'"
    elif hasattr(context, "error_message"):

        assert (
            error_message in context.error_message
        ), f"Expected error message '{error_message}' but got '{context.error_message}'"
    else:
        raise AssertionError("No result or error message found")
