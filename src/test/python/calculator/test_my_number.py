import unittest

from src.main.python.calculator.illegal_construction import IllegalConstruction
from src.main.python.calculator.my_number import MyNumber
from src.main.python.calculator.times import Times


class TestMyNumber(unittest.TestCase):

    value = 8

    def setUp(self):
        self.number = MyNumber(self.value)

    def test_equal(self):
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


if __name__ == "__main__":
    unittest.main()
