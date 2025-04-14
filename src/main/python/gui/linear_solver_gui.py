import tkinter as tk
from tkinter import messagebox

from src.main.python.calculator.linear_solver import LinearEquationSolver


class LinearSolverGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Linear Equation Solver")

        self.instructions = tk.Label(
            root, text="Enter one equation per line (ex: 2x+3y=5):", anchor="w"
        )
        self.instructions.pack(fill="x", padx=10, pady=(10, 0))

        self.input_text = tk.Text(root, height=10, width=50)
        self.input_text.pack(padx=10, pady=5)

        self.solve_button = tk.Button(root, text="Solve", command=self.solve)
        self.solve_button.pack(pady=5)

        self.output_label = tk.Label(root, text="Result:", anchor="w")
        self.output_label.pack(fill="x", padx=10, pady=(10, 0))

        self.output_text = tk.Text(root, height=5, width=50, state="disabled")
        self.output_text.pack(padx=10, pady=(0, 10))

    def solve(self):
        raw_input = self.input_text.get("1.0", tk.END).strip()
        if not raw_input:
            messagebox.showwarning("Empty entry", "Please enter at least one equation.")
            return

        equations = [line for line in raw_input.split("\n") if line.strip()]

        solver = LinearEquationSolver(equations)
        try:
            result = solver.solve()
        except Exception as e:
            messagebox.showerror("Error", f"Resolution error :\n{e}")
            return

        self.output_text.configure(state="normal")
        self.output_text.delete("1.0", tk.END)
        if isinstance(result, dict):
            for var, val in result.items():
                self.output_text.insert(tk.END, f"{var} = {val}\n")
        else:
            self.output_text.insert(tk.END, str(result))
            result_str = f"Error : {result}"
        self.output_text.configure(state="disabled")

    def reset_fields(self):
        self.input_text.delete("1.0", tk.END)
        self.output_text.configure(state="normal")
        self.output_text.delete("1.0", tk.END)
        self.output_text.configure(state="disabled")


