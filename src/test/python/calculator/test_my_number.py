import unittest

from src.main.python.calculator.illegal_construction import IllegalConstruction
from src.main.python.calculator.integer_number import IntegerNumber
from src.main.python.calculator.my_number import MyNumber
from src.main.python.calculator.times import Times


class TestMyNumber(unittest.TestCase):

    value = 8

    def setUp(self):
        self.number = MyNumber(self.value)
        self.n1 = MyNumber(IntegerNumber(5))
        self.n2 = MyNumber(IntegerNumber(5))
        self.n3 = MyNumber(IntegerNumber(7))

    def test_eq(self):
        self.assertEqual(self.number, MyNumber(self.value))
        other_value = 7
        self.assertNotEqual(self.number, MyNumber(other_value))
        self.assertEqual(self.number, self.number)
        self.assertNotEqual(self.number, self.value)
        try:
            self.assertNotEqual(Times([]), self.number)
        except IllegalConstruction as e:
            self.fail(e)

    def test_str(self):
        self.assertEqual(str(self.number), str(self.value))

    def test_hash(self):
        self.assertNotEqual(hash(self.n1), hash(self.n2))

    def test_get_value_and_type(self):
        self.assertEqual(self.n1.get_value(), 5)
        self.assertEqual(type(self.n1.get_number_type()), IntegerNumber)

if __name__ == '__main__':
    unittest.main()
