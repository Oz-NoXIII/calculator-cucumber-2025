import ast
import os
import sys

from rich.console import Console

from src.main.python.calculator import calculator
from src.main.python.calculator.integer_number import IntegerNumber
from src.main.python.calculator.linear_solver import LinearEquationSolver
from src.main.python.calculator.matrix import Matrix
from src.main.python.calculator.real_number import RealNumber
from src.main.python.parsing.expression_parser import parse_expression

console = Console()


def clear_screen():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")


def wrap_number(value):
    """
    Converts a float/int into a suitable numeric type
    """
    if isinstance(value, int):
        return IntegerNumber(value)
    elif isinstance(value, float):
        return RealNumber(value)
    else:
        raise TypeError(f"Unsupported number type: {type(value)}")


class CalculatorREPL:
    """A REPL (Read-Eval-Print Loop) for the calculator."""

    def __init__(self):
        self._running = False
        self._welcome_message = (
            "Calculator REPL\n"
            "Enter arithmetic expressions to evaluate.\n"
            "Commands: <expression>, 'help', 'linear solver', 'matrix' 'quit'\n"
        )
        self._prompt = "calc> "

    def start(self):
        """Starts the REPL."""
        self._running = True
        print(self._welcome_message)

        while self._running:
            try:
                user_input = input(self._prompt).strip()
                self._process_input(user_input)
            except KeyboardInterrupt:
                print("\nUse 'quit' to exit.")
            except EOFError:
                print("\nExiting calculator.")
                self._running = False

    def _process_input(self, input_str: str):
        """Processes user input (expressions or commands)."""
        if not input_str:
            return

        # Handle commands
        if input_str.lower() == "quit":
            self._running = False
            print("Goodbye!")
            return
        elif input_str.lower() == "help":
            self._print_help()
            return
        elif input_str.lower() == "linear solver":
            self._linear_mode()
        elif input_str.lower().startswith("linear>"):
            self._handle_linear_equation(input_str[7:].strip())
        elif input_str.lower().startswith("matrix "):
            self._handle_matrix_command(input_str[7:].strip())

        else:
            # Parse and evaluate the expression
            try:
                parsed_expr = parse_expression(input_str)
                calculator.print_result(parsed_expr)
            except Exception as e:
                self._handle_parse_error(input_str)

    def _handle_parse_error(self, error):
        """Enhanced error handling with suggestions."""

        # print(f"Syntax error: {type(error)}")
        print(
            f"Syntax error: '{error}' is an invalid expression. \nType 'help' for examples."
        )

    def _handle_linear_equation(self, raw_input):
        if not raw_input:
            print("Please provide equations separated by semicolons.")
            return

        equations = [eq.strip() for eq in raw_input.split(";") if eq.strip()]

        try:
            solver = LinearEquationSolver(equations)
            result = solver.solve()

            if isinstance(result, dict):
                print("Solution:")
                for var, val in result.items():
                    print(f"  {var} = {val}")
            else:
                print(result)
        except Exception as e:
            print(f"Error: {e}")

    def _handle_matrix_command(self, command_str):

        def wrap_matrix(raw_matrix):
            return [[wrap_number(cell) for cell in row] for row in raw_matrix]

        try:
            parts = command_str.split(maxsplit=1)
            if len(parts) < 2:
                print("Usage: matrix <operation> <matrix1> [<matrix2>]")
                return

            operation, rest = parts[0], parts[1]
            args = ast.literal_eval(rest)

            if operation in {"add", "mult"}:
                if not isinstance(args, list) or len(args) != 2:
                    print("Provide two matrices: matrix add [matrix1, matrix2]")
                    return
                m1 = Matrix(wrap_matrix(args[0]))
                m2 = Matrix(wrap_matrix(args[1]))
                result = m1.add(m2) if operation == "add" else m1.multiply(m2)
            elif operation == "trans":
                result = Matrix(wrap_matrix(args)).transpose()
            elif operation == "inv":
                result = Matrix(wrap_matrix(args)).inverse()
            else:
                print(f"Unknown matrix operation: {operation}")
                return

            print("Result:")
            for row in result.data:
                print(row)

        except Exception as e:
            print(f"Matrix error: {e}")

    def _linear_mode(self):
        print("Enter each equation on a new line.")
        print("Type 'ok' when finished.\n")

        equations = []
        while True:
            line = input("eq> ").strip()
            if line.lower() == "ok":
                break
            if line:
                equations.append(line)

        if not equations:
            print("No equations entered.")
            return

        try:
            solver = LinearEquationSolver(equations)
            result = solver.solve()

            if isinstance(result, dict):
                print("Solution:")
                for var, val in result.items():
                    print(f"  {var} = {val}")
            else:
                print(result)
        except Exception as e:
            print(f"Error: {e}")

    def _print_help(self):
        """Prints available commands."""
        help_text = """
        Calculator Help
        ==============

        Supported Notations for <expression>:
        --------------------
        1. Infix (standard):     3 + 4 * 2
        2. Prefix (Polish):      +(3, 4, 2) or +(3 4 2)
        3. Postfix (Reverse):    (3, 4, 2)+ or (3 4 2)+

        Basic Operations:
        -----------------
        +----------------+---------------------+---------------------+---------------------+
        | Operation      | Infix               | Prefix              | Postfix             |
        +----------------+---------------------+---------------------+---------------------+
        | Addition       | a + b               | +(a, b) or +(a b)   | (a, b)+ or (a b)+   |
        | Subtraction    | a - b               | -(a, b) or -(a b)   | (a, b)- or (a b)-   |
        | Multiplication | a * b               | *(a, b) or *(a b)   | (a, b)* or (a b)*   |
        | Division       | a / b               | /(a, b) or /(a b)   | (a, b)/ or (a b)/   |
        | Exponentiation | a ^ b               | ^(a, b) or ^(a b)   | (a, b)^ or (a b)^   |
        | Negation       | (-a)                | (-(a))              | (a-)-               |
        | Inverse        | inv(a)              | inv(a)              | inv(a)              |
        +----------------+---------------------+---------------------+---------------------+

        Advanced Features:
        ------------------
        - Multiple operands:  +(1, 2, 3)  → 6
        - Nested operations:  *(2, +(3, 4))  → 14
        - Complex numbers:    3.5j
        - Parentheses:        (2 + 3) * 4

        Examples:
        ---------
        Infix:       3 * (4 + 5) ^ 2
        Prefix:      *(3, ^(+(4, 5), 2))
        Postfix:     (3, ((4, 5)+, 2)^)*
        matrix mult [[[1,2],[3,4]], [[5,6],[7,8]]]
        matrix add [[[1,2],[3,4]], [[5,6],[7,8]]]
        matrix inv [[1,2],[3,4]]
        matrix trans [[1,2],[3,4]]

        Special Commands:
        -----------------
        help   - Show this help message
        quit   - Exit the calculator
        linear mode    - Enter multiline linear equation solving mode.
        matrix add [A,B]         - Add two matrices A and B
        matrix mult [A,B]        - Multiply two matrices A and B
        matrix trans A           - Transpose matrix A
        matrix inv A             - Invert matrix A

        """
        print(help_text)


if __name__ == "__main__":
    clear_screen()
    repl = CalculatorREPL()
    repl.start()
