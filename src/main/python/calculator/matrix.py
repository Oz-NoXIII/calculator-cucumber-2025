import numpy as np

from src.main.python.calculator.integer_number import IntegerNumber
from src.main.python.calculator.real_number import RealNumber


class Matrix:
    def __init__(self, data):
        """
        Initializes a matrix with data supplied as a list of lists.
        """
        if not isinstance(data, list) or not all(isinstance(row, list) for row in data):
            raise ValueError("The matrix must be a list of lists.")

        row_lengths = [len(row) for row in data]
        if len(set(row_lengths)) != 1:
            raise ValueError("All matrix rows must have the same size.")

        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def accept(self, visitor):
        visitor.visit_matrix(self)

    def get_depth(self):
        return 2

    def get_ops(self):
        return self.rows * self.cols

    def get_nbs(self):
        return self.rows * self.cols

    def __str__(self):
        def format_value(value):

            if hasattr(value, "get_value"):
                return str(value.get_value())
            return str(value)

        rows_str = []
        for row in self.data:
            row_str = ", ".join(format_value(item) for item in row)
            rows_str.append(f"[{row_str}]")
        return f"[{', '.join(rows_str)}]"

    def _cast_to_appropriate_type(self, value):
        """
        Converts values to their appropriate type (Integer, Real, Rational).
        """
        if hasattr(value, "get_value"):
            value = value.get_value()

        if isinstance(value, (int, float)):
            return IntegerNumber(value) if isinstance(value, int) else RealNumber(value)
        else:
            raise ValueError("Unsupported number type")

    def add(self, other):

        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Dies must have the same dimensions for addition.")

        result = []
        for i in range(self.rows):
            row_result = []
            for j in range(self.cols):
                val1 = self.data[i][j]
                val2 = other.data[i][j]
                try:
                    val1 = self._cast_to_appropriate_type(val1)
                    val2 = self._cast_to_appropriate_type(val2)
                except ValueError as e:
                    raise ValueError("Unsupported number type") from e

                result_value = val1.add(val2)
                row_result.append(result_value)
            result.append(row_result)

        return Matrix(result)

    def subtract(self, other):

        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for subtraction.")

        result = []
        for i in range(self.rows):
            row_result = []
            for j in range(self.cols):

                val1 = self.data[i][j]
                val2 = other.data[i][j]
                try:
                    val1 = self._cast_to_appropriate_type(val1)
                    val2 = self._cast_to_appropriate_type(val2)
                except ValueError as e:
                    raise ValueError("Unsupported number type") from e
                result_value = val1.subtract(val2)
                row_result.append(result_value)
            result.append(row_result)

        return Matrix(result)

    def multiply(self, other):

        if self.cols != other.rows:
            raise ValueError(
                "The number of columns in the first matrix must be equal to the number of rows in the second matrix."
            )

        result = []
        for i in range(self.rows):
            row_result = []
            for j in range(other.cols):
                product = IntegerNumber(0)
                for k in range(self.cols):
                    val1 = self.data[i][k]
                    val2 = other.data[k][j]
                    product = product.add(
                        self._cast_to_appropriate_type(val1).multiply(
                            self._cast_to_appropriate_type(val2)
                        )
                    )
                row_result.append(product)
            result.append(row_result)

        return Matrix(result)

    def transpose(self):
        numeric_data = [
            [cell.get_value() if hasattr(cell, "get_value") else cell for cell in row]
            for row in self.data
        ]

        result = np.linalg.matrix_transpose(numeric_data)
        return Matrix(result.tolist())

    def inverse(self):
        numeric_data = [
            [cell.get_value() if hasattr(cell, "get_value") else cell for cell in row]
            for row in self.data
        ]

        if self.rows != self.cols:
            raise ValueError("The matrix must be square to calculate the inverse.")
        try:
            result = np.linalg.inv(numeric_data)
            return Matrix(result.tolist())
        except np.linalg.LinAlgError:
            raise ValueError("The matrix is not invertible.")
