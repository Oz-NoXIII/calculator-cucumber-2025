from src.main.python.visitor.counter import Counter
from src.main.python.visitor.evaluator import Evaluator


def print_result(e):
    result = eval_expression(e)
    print(f"The result of evaluating expression {e}")
    print(f"is: {'NaN' if result != result else result}.\n")


def print_expression_details(e):
    print_result(e)
    e.accept(Counter())
    print(f"It contains {e.get_depth()} levels of nested expressions, ")
    print(f"{e.get_ops()} operations")
    print(f" and {e.get_nbs()} numbers.\n")


def eval_expression(e):
    visitor = Evaluator()
    e.accept(visitor)
    return visitor.get_result()
