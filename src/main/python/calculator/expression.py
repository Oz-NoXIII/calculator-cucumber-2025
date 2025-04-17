from abc import ABC, abstractmethod


class Expression(ABC):  # pragma: no cover
    """
    Expression is an abstract class that represents arithmetic expressions.
    It has two concrete subclasses Operation and MyNumber.
    """

    @abstractmethod
    def accept(self, visitor):
        """
        Accept is a method needed to implement the visitor design pattern
        :param visitor: The visitor object being passed as a parameter
        """
        pass

    @abstractmethod
    def get_depth(self):
        """
        Get the depth of the arithmetic expression
        :return: The depth of the arithmetic expression
        """
        pass

    @abstractmethod
    def get_ops(self):
        """
        Get the number of operations in the arithmetic expression
        :return: The number of operations in the arithmetic expression
        """
        pass

    @abstractmethod
    def get_nbs(self):
        """
        Get the number of numbers in the arithmetic expression
        :return: The number of numbers in the arithmetic expression
        """
        pass
