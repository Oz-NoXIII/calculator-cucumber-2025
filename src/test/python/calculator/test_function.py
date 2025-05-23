import unittest

from src.main.python.calculator.inverse import Inverse
from src.main.python.calculator.minus import Minus
from src.main.python.calculator.my_number import MyNumber
from src.main.python.calculator.plus import Plus
from src.main.python.calculator.real_number import RealNumber
from src.main.python.visitor.counter import Counter


class TestFunction(unittest.TestCase):

    def setUp(self):
        params1 = [
            MyNumber(RealNumber(5)),
            MyNumber(RealNumber(4)),
            MyNumber(RealNumber(5)),
        ]
        params2 = [MyNumber(RealNumber(4)), MyNumber(RealNumber(6))]
        params3 = [Plus(params1), Minus(params2), MyNumber(RealNumber(10))]
        self.o = Inverse(params3)
        self.o2 = Inverse(params3)
        self.o.accept(Counter())
        self.o2.accept(Counter())

    def test_equals(self):
        self.assertEqual(self.o, self.o2)

    def test_hash_code(self):
        self.assertEqual(hash(self.o), hash(self.o2))

    def test_get_depth(self):
        self.assertEqual(2, self.o.get_depth())

    def test_get_ops(self):
        self.assertEqual(3, self.o.get_ops())

    def test_get_nbs(self):
        self.assertEqual(6, self.o.get_nbs())


if __name__ == "__main__":
    unittest.main()
