import unittest
from Work_1 import multiplication_table

class TestMultiplicationTable(unittest.TestCase):

    def test_multiplication_table(self):
        actual_result = multiplication_table(3)
        self.assertEqual(actual_result, "number is too big")

    def test_multiplication_with_zero(self):
        actual_result = multiplication_table(0)
        self.assertEqual(actual_result, "Number must be greater than zero")

    def test_multiplication_with_large_number(self):
        actual_result = multiplication_table(26)
        self.assertEqual(actual_result, "number is too big")

if __name__ == '__main__':
    unittest.main()