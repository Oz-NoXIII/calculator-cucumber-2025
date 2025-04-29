import re

from behave import *

from src.main.python.calculator.linear_solver import LinearEquationSolver


def preprocess_input(equations_str):

    equations = []
    for eq in equations_str.split(";"):
        eq = eq.strip().replace('"', "").replace("'", "")
        eq = re.sub(r"(\d)([a-zA-z])", r"\1*\2", eq)  # 2x → 2*x
        eq = re.sub(r"([a-zA-z])(\d)", r"\1*\2", eq)  # x2 → x*2
        equations.append(eq)
    return equations


@given("the system of equations {equations}")
def step_impl(context, equations):
    context.equations = preprocess_input(equations)
    print(f"DEBUG - Cleaned equations: {context.equations}")


@when("I solve the system")
def step_impl(context):
    try:
        context.solver = LinearEquationSolver(context.equations)
        context.result = context.solver.solve()
    except Exception as e:
        context.result = f"Error: {str(e)}"


@when("I try to create the solver")
def step_impl(context):
    try:
        context.solver = LinearEquationSolver(context.equations)
    except Exception as e:
        context.exception = e


@then('I should get the solution "{solution}"')
def step_impl(context, solution):
    if hasattr(context, "error"):
        assert False, f"Solving failed with error: {context.error}"

    expected = {}
    for pair in solution.split(","):
        var, val = pair.split(":")
        expected[var.strip()] = float(val) if "." in val else int(val)

    for var in expected:
        assert abs(context.result[var] - expected[var]) < 0.01


@then('I should get "{message}"')
def step_impl(context, message):
    assert (
        str(context.result) == message
    ), f"Expected '{message}' but got '{context.result}'"


@then('I should get an error containing "{error}"')
def step_impl(context, error):
    assert error in context.result


@then("a ValueError should be raised")
def step_impl(context):
    assert isinstance(context.exception, ValueError)
