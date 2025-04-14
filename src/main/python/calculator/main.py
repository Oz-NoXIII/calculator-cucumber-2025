import tkinter as tk

import calculator

from src.main.python.calculator.divides import Divides
from src.main.python.calculator.illegal_construction import IllegalConstruction
from src.main.python.calculator.linear_solver import (LinearEquationSolver,
                                                      run_interactive_solver)
from src.main.python.calculator.minus import Minus
from src.main.python.calculator.my_number import MyNumber
from src.main.python.calculator.notation import Notation
from src.main.python.calculator.plus import Plus
from src.main.python.calculator.times import Times
from src.main.python.gui.linear_solver_gui import LinearSolverGUI

try:
    e = MyNumber(8)
    calculator.print_result(e)
    calculator.eval_expression(e)

    test = [MyNumber(8), MyNumber(0)]
    e = Divides(test, Notation.PREFIX)
    calculator.print_expression_details(e)
    calculator.eval_expression(e)

    params = [MyNumber(3), MyNumber(4), MyNumber(5)]
    e = Plus(params, Notation.PREFIX)
    calculator.print_expression_details(e)
    calculator.eval_expression(e)

    params2 = [MyNumber(5), MyNumber(3)]
    e = Minus(params2, Notation.INFIX)
    calculator.print_result(e)
    calculator.eval_expression(e)

    params3 = [Plus(params), Minus(params2)]
    e = Times(params3)
    calculator.print_expression_details(e)
    calculator.eval_expression(e)

    params4 = [Plus(params), Minus(params2), MyNumber(5)]
    e = Divides(params4, Notation.POSTFIX)
    calculator.print_result(e)
    calculator.eval_expression(e)

    print("Solving system of linear equations:")
    equations = ["2x+3y=5", "3x-4z=7", "y+z=10"]

    solver = LinearEquationSolver(equations)
    solution = solver.solve()
    print("Solution:")
    print(solution)

    run_interactive_solver()

    root = tk.Tk()
    app = LinearSolverGUI(root)
    root.mainloop()

except IllegalConstruction as e:
    print("cannot create operations without parameters")
