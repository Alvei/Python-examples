import unittest
from math import pi
from circle import circle_area

class TestCircleArea(unittest.TestCase):
    """ Simple unit test. Run python -m unittest"""
    def test_area(self):
        # Test areas with radius > 0
        test_dict = {1: pi, 0: 0, 2.1: pi*2.1**2}
        for key, value in test_dict.items():
            self.assertAlmostEqual(circle_area(key), value)

    def test_values(self):
        #  Make sure reasonable values are accepted
        self.assertRaises(ValueError, circle_area, -2)

    def test_types(self):
        # Test for different types
        test_list = [True, 2+3j, "one"]
        for value in test_list:
            self.assertRaises(TypeError, circle_area, value)


if __name__ == "__main__":
    unittest.main()