""" Generic example of compressing class from string to bits.
    Using nucleotides example which takes two bites because 4 letters can be represented with that.
    Should adjust based on the number of letters we need to map. """

class CompressedGene:
    """ Is provided a str of characters representing a nucleotides in a gene and
        internally stores the sequence in a a bit string. """
    def __init__(self, gene: str) -> None:
        """ Initialize. """
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        """ Compresses the nucleotide. """
        self.bit_string: int = 1    # start with sentinel

        for nucleotide in gene.upper():
            self.bit_string <<= 2   # Shift left two bits to create room what is coming

            # Add new nucleoide by using "or" operator |
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
        """ Decompressed method. """
        gene: str = ""
        for num in range(0, self.bit_string.bit_length() -1, 2):    # -1 to exclude the sentinel
            bits: int = self.bit_string >> num & 0b11               # Get just 2 relevant bit
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
        """ Printing method for the class which is always decompressed """
        return self.decompress()

if __name__ == "__main__":
    from sys import getsizeof
    original: str = "TAGGGATTAACCGT"*10

    size_original = getsizeof(original)
    print(f"Original is {size_original} bytes.")

    compressed: CompressedGene = CompressedGene(original)
    size_compressed = getsizeof(compressed)

    print(f"Compressed is {size_compressed} bytes.")
    print(f"Compression ration is {size_compressed*100/size_original:.2f}%")
    print(f"Orginal and decompressed are the same {original == compressed.decompress()}")
    print(f"Decompressed is {compressed}")
