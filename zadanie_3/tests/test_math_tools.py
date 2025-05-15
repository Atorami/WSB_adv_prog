import unittest
from awesome_lib.math_tools import rectangle_area, average, factorial

class TestMathTools(unittest.TestCase):
    def test_area(self):
        self.assertEqual(rectangle_area(3, 4), 12)

    def test_average(self):
        self.assertEqual(average([1, 2, 3]), 2.0)

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)