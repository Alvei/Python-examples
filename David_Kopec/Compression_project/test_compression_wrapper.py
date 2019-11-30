""" Test the bit compression. """
import unittest

from compression_wrapper import BitStringCompression

class Test_CompressedGene(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(BitStringCompression("TAGGGATTAACCGT").data, "TAGGGATTAACCGT")

    def test_str(self):
        original: str = "TAGGGATTAACCGT"
        self.assertEqual(original.__str__(), "TAGGGATTAACCGT")

if __name__ == "__main__":
    unittest.main()
