from src.main.python.visitor.visitor import Visitor


class Evaluator(Visitor):
    def __init__(self):
        self.__computed_value = None

    def get_result(self):
        return (
            self.__computed_value
            if self.__computed_value == self.__computed_value
            else "NaN"
        )

    def visit_my_number(self, number):
        self.__computed_value = number.get_value()

    def visit_operation(self, o):
        evaluated_args = []
        for arg in o.get_args():
            arg.accept(self)
            evaluated_args.append(self.__computed_value)
        temp = evaluated_args[0]
        maximum = len(evaluated_args)
        for counter in range(1, maximum):
            temp = o.op(temp, evaluated_args[counter])
        self.__computed_value = temp
