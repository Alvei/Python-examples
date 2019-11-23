""" Test the bit compression. """
import unittest

from Trivial_Compression import CompressedGene

class Test_CompressedGene(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(CompressedGene("TAGGGATTAACCGT").decompress(), "TAGGGATTAACCGT")

    def test_compressed_values_error(self):
        with self.assertRaises(ValueError):
            CompressedGene("ABC")

    def test_str(self):
        original: str = "TAGGGATTAACCGT"
        self.assertEqual(original.__str__(), "TAGGGATTAACCGT")

if __name__ == "__main__":
    unittest.main()
