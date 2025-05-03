import os
import sys

from src.main.python.calculator import calculator
from src.main.python.parsing.expression_parser import parse_expression
from rich.console import Console

console = Console()


def clear_screen():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")


class CalculatorREPL:
    """A REPL (Read-Eval-Print Loop) for the calculator."""

    def __init__(self):
        self._running = False
        self._welcome_message = (
            "Calculator REPL\n"
            "Enter arithmetic expressions to evaluate.\n"
            "Commands: <expression>, 'help', 'quit'\n"
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

        # Parse and evaluate the expression
        try:
            parsed_expr = parse_expression(input_str)
            calculator.print_result(parsed_expr)
        except Exception:
            self._handle_parse_error(input_str)

    def _handle_parse_error(self, error):
        """Enhanced error handling with suggestions."""

        print(f"Syntax error: '{error}' is an invalid expression. \nType 'help' for examples.")

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

        Special Commands:
        -----------------
        help   - Show this help message
        quit   - Exit the calculator
        """
        print(help_text)


if __name__ == "__main__":
    clear_screen()
    repl = CalculatorREPL()
    repl.start()
    
