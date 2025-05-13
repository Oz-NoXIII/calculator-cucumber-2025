from src.main.python.calculator.function import Function


class MatrixTranspose(Function):

    def __init__(self, elist, n=None):

        super().__init__(elist, n)
        self._symbol = "tr"

    def op(self, base):
        return base.transpose()
