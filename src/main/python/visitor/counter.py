from streamerate import stream

from src.main.python.visitor.visitor import Visitor


class Counter(Visitor):

    def __init__(self):
        self.__depth = 0
        self.__ops = 0
        self.__nbs = 0

    def visit_my_number(self, number):
        self.__nbs += 1

    def visit_operation(self, o):
        max_depth = stream(o.get_args).map(lambda e: e.get_depth()).max()
        self.__depth = max(self.__depth, max_depth + 1)
        self.__ops += 1
        o.set_depth(self.__depth)
        o.set_ops(self.__ops)
        o.set_nbs(self.__nbs)

    def visit_linear_solution(self, solution):
        pass

    def visit_matrix(self, matrix):
        """The Visitor can traverse a matrix"""
        pass
