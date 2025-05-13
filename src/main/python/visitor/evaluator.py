from src.main.python.visitor.visitor import Visitor


class Evaluator(Visitor):
    def __init__(self):
        self.stack = []
        self.__computed_value = None

    def get_result(self):
        # return self.__computed_value if self.__computed_value == self.__computed_value else "NaN"
        return self.stack[-1] if self.stack else None

    def visit_my_number(self, number):
        # self.__computed_value = number.get_value()
        self.stack.append(number.get_number_type())

    def visit_operation(self, o):

        args = o.get_args()
        # Support only binary for now, extendable to n-ary
        evaluated_args = []
        for arg in args:
            arg.accept(self)
            evaluated_args.append(self.stack.pop())

        if len(evaluated_args) == 1:
            # Cas unaire : appliquer l'opération directement sur l’unique argument
            result = o.op(evaluated_args[0])

        else:
            # Start folding from the left
            result = evaluated_args[0]
            for operand in evaluated_args[1:]:
                result = o.op(result, operand)

        self.stack.append(result)

    def visit_matrix(self, matrix):
        self.stack.append(matrix)

    def visit_linear_solution(self, equation):
        result = equation.solve()
        if type(result) == str:
            self.stack.append(result)
        elif hasattr(result, "get_value"):
            self.stack.append(result.get_value())
        else:
            self.stack.append(result)
