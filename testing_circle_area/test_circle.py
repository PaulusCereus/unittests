import unittest
from circle import circle_area
from math import pi

class TestCircleArea(unittest.TestCase):

    def test_area(self):
        self.assertEqual(circle_area(2.5), pi * 2.5 ** 2)
        self.assertEqual(circle_area(5), pi * 5 ** 2)
        self.assertEqual(circle_area(0), 0)
        self.assertEqual(circle_area(1), pi)

    def test_values(self):
        self.assertRaises(ValueError, circle_area, -2)
        self.assertRaises(ValueError, circle_area, -1)
        self.assertRaises(ValueError, circle_area, -7)

    def test_types(self):
        self.assertRaises(TypeError, circle_area, 'str')
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError, circle_area, [1, 2])
        self.assertRaises(TypeError, circle_area, 3 + 8j)