from abc import ABC, abstractmethod

class NumberType(ABC): #pragma: no cover
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

    def is_nan(self):
        return False

    def is_infinite(self):
        return False

    def set_nan(self):
        raise NotImplementedError("set_nan() must be implemented by subclass")

    def set_infinity(self, positive=True):
        raise NotImplementedError("set_infinity() must be implemented by subclass")


