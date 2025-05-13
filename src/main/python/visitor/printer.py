from src.main.python.visitor.visitor import Visitor


class Printer(Visitor):
    def __init__(self, notation):
        self.result = ""
        self.__notation = notation

    def visit_operation(self, op):
        op.set_notation(self.__notation)

    def visit_my_number(self, number):
        pass

    def visit_linear_solution(self, solution):
        self.result += str(solution)

    def visit_matrix(self, matrix):
        """The Visitor can traverse a matrix"""
        pass
