from behave import *

from src.main.python.calculator.integer_number import IntegerNumber
from src.main.python.calculator.matrix import Matrix
from src.main.python.calculator.rational_number import RationalNumber
from src.main.python.calculator.real_number import RealNumber


@given("the following IntegerNumber matrix:")
def given_the_following_integer_matrix(context):
    context.matrix_data = []
    for row in context.table:
        context.matrix_data.append(
            [IntegerNumber(int(cell)) for cell in row.cells]
        )  # Convert to IntegerNumber


@given("I have the following RealNumber matrix:")
def given_the_following_real_matrix(context):
    context.matrix_data = []
    for row in context.table:
        context.matrix_data.append(
            [RealNumber(float(cell)) for cell in row.cells]
        )  # Convert to RealNumber


@given("I have the following RationalNumber matrix:")
def given_the_following_rational_matrix(context):
    context.matrix_data = []
    for row in context.table:
        context.matrix_data.append(
            [
                (
                    RationalNumber(int(cell.split("/")[0]), int(cell.split("/")[1]))
                    if "/" in cell
                    else RealNumber(float(cell))
                )
                for cell in row.cells
            ]
        )  # Convert to RationalNumber if fraction


@given("I have the following matrix:")
def given_the_following_matrix(context):
    context.other_matrix_data = []
    for row in context.table:
        context.other_matrix_data.append(
            [RealNumber(float(cell)) for cell in row.cells]
        )  # Default to RealNumber


@when("I add the matrices")
def when_i_add_the_matrices(context):
    matrix1 = Matrix(context.matrix_data)
    matrix2 = Matrix(context.other_matrix_data)
    context.result = matrix1.add(matrix2)


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
    context.result = matrix.inverse()


@then("the result should be:")
def then_the_result_should_be(context):
    result_data = context.result.data
    for i, row in enumerate(context.table):
        for j, cell in enumerate(row.cells):
            assert float(cell) == float(result_data[i][j])


@then('I should see an error message "{error_message}"')
def then_result_should_be(context, error_message):
    assert context.result == error_message
