import os
import tkinter as tk
import unittest
from unittest import SkipTest
from unittest.mock import patch

from src.main.python.gui.linear_solver_gui import LinearSolverGUI


class TestLinearSolverGUI(unittest.TestCase):

    def setUp(self):
        # Skip if no display environment (e.g. GitHub Actions)
        if not os.environ.get("DISPLAY"):
            raise SkipTest("No display available for GUI tests")
        self.root = tk.Tk()
        self.root.withdraw()
        self.gui = LinearSolverGUI(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_widgets_created(self):
        self.assertIsInstance(self.gui.input_text, tk.Text)
        self.assertIsInstance(self.gui.output_label, tk.Label)

    @patch("tkinter.messagebox.showwarning")
    def test_warn_if_no_input(self, mock_warning):
        self.gui.input_text.delete("1.0", tk.END)
        self.gui.solve()
        mock_warning.assert_called_once()

    def test_reset_fields(self):
        self.gui.input_text.insert(tk.END, "x + y = 2")
        self.gui.output_label.config(text="Result")
        content = self.gui.input_text.get("1.0", tk.END).strip()
        self.gui.reset_fields()
        self.assertNotEqual(content, "")
        self.assertEqual(self.gui.output_text.get("1.0", tk.END).strip(), "")

    def test_display_solution(self):
        self.gui.input_text.insert(tk.END, "x + y = 6\nx - y = 0")
        self.gui.solve()
        result = self.gui.output_text.get("1.0", tk.END).strip()
        self.assertIn("x = ", result)
        self.assertIn("y = ", result)

    def test_display_error(self):
        self.gui.input_text.insert(tk.END, "x + ?= 5\nx - y = 1")
        self.gui.solve()
        result = self.gui.output_text.get("1.0", tk.END).strip()
        self.assertIn("Invalid term", result)

    @patch("tkinter.messagebox.showerror")
    @patch(
        "src.main.python.calculator.linear_solver.LinearEquationSolver.solve",
        side_effect=Exception("mocked failure"),
    )
    def test_solver_exception_shows_error_message(self, mock_solve, mock_showerror):
        self.gui.input_text.insert(tk.END, "x + y = 2")
        self.gui.solve()
        mock_showerror.assert_called_once()
        self.gui.output_text.configure(state="normal")
        content = self.gui.output_text.get("1.0", tk.END).strip()
        self.gui.output_text.configure(state="disabled")
        self.assertEqual(content, "")


if __name__ == "__main__":
    unittest.main()
