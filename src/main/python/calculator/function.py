from abc import ABC, abstractmethod

from src.main.python.calculator.illegal_construction import IllegalConstruction
from src.main.python.calculator.notation import Notation
from src.main.python.calculator.number_type import NumberType
from src.main.python.visitor.printer import Printer


class Function(ABC):  # pragma: no cover

    @abstractmethod
    def __init__(self, elist, n=None):
        if elist is None:
            raise IllegalConstruction("the list of expressions is None")
        else:
            self.__args = elist
        self.__notation = Notation.INFIX
        if n is not None:
            self.__notation = n
        self.accept_notation(self.__notation)
        self.__depth = 0
        self.__ops = 0
        self.__nbs = 0
        self._symbol = ""
        self._neutral = None

    @abstractmethod
    def op(self, left: NumberType):
        pass

    def add_more_params(self, params):
        self.__args.extend(params)

    def accept(self, visitor):
        for a in self.__args:
            a.accept(visitor)
        visitor.visit_operation(self)

    def accept_notation(self, n):
        self.__notation = n
        self.accept(Printer(n))

    def get_args(self):
        return self.__args

    def get_notation(self):
        return self.__notation

    def get_depth(self):
        return self.__depth

    def get_ops(self):
        return self.__ops

    def get_nbs(self):
        return self.__nbs

    def set_notation(self, n):
        self.__notation = n

    def set_depth(self, depth):
        self.__depth = depth

    def set_ops(self, ops):
        self.__ops = ops

    def set_nbs(self, nbs):
        self.__nbs = nbs

    def __str__(self):
        args_str = [str(arg) for arg in self.__args]
        match self.__notation:
            # infix = prefix because only one param
            case Notation.INFIX:
                if not args_str:
                    return f"{self._symbol} ("
                combined = ", ".join(args_str)
                return f"{self._symbol} ({combined})"

            case Notation.PREFIX:
                if not args_str:
                    return f"{self._symbol} ("
                combined = ", ".join(args_str)
                return f"{self._symbol} ({combined})"

            case Notation.POSTFIX:
                if not args_str:
                    return f"() {self._symbol}"
                combined = ", ".join(args_str)
                return f"({combined}) {self._symbol}"

    def __eq__(self, other):
        if other is None:
            return False
        # __class__ instead of instanceof because an addition is not the same as a multiplication
        if self.__class__ != other.__class__:
            return False
        if self.__args != other.get_args():
            return False
        return True

    def __hash__(self):
        return hash((self._neutral, hash(self._symbol), tuple(self.__args)))
