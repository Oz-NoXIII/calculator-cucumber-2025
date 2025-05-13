import re

from behave import given, then, when

from src.main.python.calculator.linear_solver import LinearEquationSolver


def preprocess_input(equations_str):

    equations = []
    for eq in equations_str.split(";"):
        eq = eq.strip().replace('"', "").replace("'", "")
        eq = re.sub(r"(\d)([a-zA-Z])", r"\1*\2", eq, flags=re.ASCII)  # 2x → 2*x
        eq = re.sub(r"([a-zA-Z])(\d)", r"\1*\2", eq, flags=re.ASCII)  # x2 → x*2
        equations.append(eq)
    return equations


@given("the system of equations {equations}")
def given_system_of_equations(context, equations):
    context.equations = preprocess_input(equations)


@when("I solve the system")
def when_i_solve_the_system(context):
    try:
        context.solver = LinearEquationSolver(context.equations)
        context.result = context.solver.solve()
    except Exception as e:
        context.result = f"Error: {str(e)}"


@when("I try to create the solver")
def when_i_create_the_solver(context):
    try:
        context.solver = LinearEquationSolver(context.equations)
    except Exception as e:
        context.exception = e


@then('I should get the solution "{solution}"')
def then_solution_should_be(context, solution):
    if hasattr(context, "error"):
        assert False, f"Solving failed with error: {context.error}"

    expected = {}
    for pair in solution.split(","):
        var, val = pair.split(":")
        expected[var.strip()] = float(val) if "." in val else int(val)

    result_dict = (
        context.result.get_value() if hasattr(context.result, "get_value") else {}
    )

    for var in expected:
        assert var in result_dict, f"Variable {var} not found in solution"
        assert (
            abs(result_dict[var] - expected[var]) < 1e-9
        ), f"Expected {var}={expected[var]}, got {var}={result_dict[var]}"


@then('I should get "{message}"')
def then_result_should_be(context, message):
    assert (
        str(context.result) == message
    ), f"Expected '{message}' but got '{context.result}'"


@then('I should get an error containing "{error}"')
def then_result_should_contain(context, error):
    assert error in context.result


@then("a ValueError should be raised")
def step_impl(context):
    assert isinstance(context.exception, ValueError)
