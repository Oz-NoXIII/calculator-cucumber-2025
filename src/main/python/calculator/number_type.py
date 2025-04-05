from abc import ABC, abstractmethod

class NumberType(ABC):
    """
    Interface for all supported numeric types (integers, reals, rationals, complexes, etc.).
    """
    @abstractmethod
    def get_value(self):
        """Returns the native value (int, float, fraction, complex, etc.)."""
        pass

    @abstractmethod
    def add(self, other):
        pass

    @abstractmethod
    def subtract(self, other):
        pass

    @abstractmethod
    def multiply(self, other):
        pass

    @abstractmethod
    def divide(self, other):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def is_nan(self):
        pass

    @abstractmethod
    def is_infinite(self):
        pass

