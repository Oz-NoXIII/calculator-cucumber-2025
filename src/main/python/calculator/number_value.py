from abc import ABC, abstractmethod

class NumberValue(ABC):
    """
    Interface for all supported numeric types (integers, reals, rationals, complexes, etc.).
    """
    @abstractmethod
    def get_value(self):
        """Returns the native value (int, float, fraction, complex, etc.)."""
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __hash__(self):
        pass
