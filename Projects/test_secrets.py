import unittest
from secrets import cypher, char_cypher, list_to_string

class TestCypher(unittest.TestCase):
    """ Simple unit test. Run python -m unittest"""
    def test_msg(self):
        # Test areas with radius > 0
        cypher_key = 3
        test_dict = {'abc': 'def', 'ABC': 'DEF',"b0nj0ur": "e3qm3xu",
                    "b0nj0ur!": "e3qm3xu$", "b0n j0ur!": "e3q2m3xu$"}
        for key, value in test_dict.items():
            self.assertEqual(cypher(key, cypher_key), value)

    def test_types(self):
        # Test for different types
        cypher_key = 3
        test_list = [1, 2+3j, 1.0, ['a', 'b']]
        for value in test_list:
            self.assertRaises(TypeError, cypher, value, cypher_key)

    def test_values(self):
        # Make sure reasonable values are accepted

        # Test with ascii character 254
        self.assertRaises(ValueError, cypher, chr(254), 3)

        #  Make sure reasonable values are accepted, test with ascii character 254
        self.assertRaises(ValueError, cypher, 'B0nj0ur!', 1000)

if __name__ == "__main__":
    unittest.main()