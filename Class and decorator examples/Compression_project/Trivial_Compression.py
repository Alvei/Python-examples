""" Generic example of compressing class from string to bits.
    Using nucleotides example which takes two bites because 4 letters can be represented with that.
    Should adjust based on the number of letters we need to map.
    Inspired by David Kopec's book.  """

class CompressedGene:
    """ Provided a str of characters representing a nucleotides in a gene and
        internally stores the sequence in a a bit string. """
    def __init__(self, gene: str) -> None:
        """ Initialize. """
        self._compress(gene)  # Calls the private method _compress() on the gene.

    def _compress(self, gene: str) -> None:
        """ Compresses the nucleotide. Takes advantage to the facts that there are only 4 values
            and therefore can use two bits binary: 00, 01, 10, 11. Str character is 8 bits
            by default. Creates an int variable called bit_string. int in python ca be of
            any length. Start with sentinel that can be shifted in 1st for loop. """
        self.bit_string: int = 1

        for nucleotide in gene.upper():
            # Shift left two bits to create room what is coming. x << y Returns x with the bits
            # shifted to the left by y places (and new bits on the right-hand-side are zeros).
            self.bit_string <<= 2

            # Add new nucleoide by using "or" bit operator |
            if nucleotide == "A":       # Change the last two bits to 00
                self.bit_string |= 0b00
            elif nucleotide == "C":     # Change the last two bits to 01
                self.bit_string |= 0b01
            elif nucleotide == "G":     # Change the last two bits to 10
                self.bit_string |= 0b10
            elif nucleotide == "T":     # Change the last two bits to 11
                self.bit_string |= 0b11
            else:
                raise ValueError(f"Invalide Nucleotide: {nucleotide}")

    def decompress(self) -> str:
        """ Decompressed method.
            self.bit_string >> i shifts self.bit_string i bits to the right,
            i.e. returns self.bit_string with the i right-most bits chopped off.
            a & b returns the bit-wise AND of a and b. Effectively this means that
            with b = 0b11, a & 0b11 returns the two right-most bits of a. """
        gene: str = ""

        # -1 to exclude the sentinel, go in 2 bits steps
        for num in range(0, self.bit_string.bit_length() -1, 2):

            # self.bit_string >> num moves the bit-string to the right by num steps
            # Get just 2 right-most bits of using & bitwise operator
            bits: int = self.bit_string >> num & 0b11

            # print using bin() to see in bit
            #print(f"{num}\t {bin(self.bit_string>> num)}\t  {bin(bits)}")

            if bits == 0b00:
                gene += "A"
            elif bits == 0b01:
                gene += "C"
            elif bits == 0b10:
                gene += "G"
            elif bits == 0b11:
                gene += "T"
            else:
                raise ValueError(f"Invalide bits: {bits}")
        return gene[::-1] # Reverse string by slicing backwards

    def __str__(self) -> str:
        """ Printing method for the class which is always decompressed. """
        return self.decompress()


if __name__ == "__main__":
    from sys import getsizeof
    original: str = "TAGGGATTAACCGT"*10

    size_original = getsizeof(original)
    print(f"\nOriginal is\t{size_original} bytes.")

    compressed: CompressedGene = CompressedGene(original)
    size_compressed = getsizeof(compressed)

    print(f"Compressed is\t{size_compressed} bytes.")
    print(f"Compression ration is {size_compressed*100/size_original:.2f}%")
    print(f"Orginal and decompressed are the same {original == compressed.decompress()}")
