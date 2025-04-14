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
        """evaluated_args = []
        for arg in o.get_args():
                arg.accept(self)
                evaluated_args.append(self.__computed_value)
        temp = evaluated_args[0]
        maximum = len(evaluated_args)
        for counter in range(1, maximum):
                temp = o.op(temp, evaluated_args[counter])
        self.__computed_value = temp"""
        # -------

        args = o.get_args()
        # Support only binary for now, extendable to n-ary
        evaluated_args = []
        for arg in args:
            arg.accept(self)
            evaluated_args.append(self.stack.pop())

        # Start folding from the left
        result = evaluated_args[0]
        for operand in evaluated_args[1:]:
            result = o.op(result, operand)

        self.stack.append(result)
