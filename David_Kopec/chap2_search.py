""" Different ways of searching. Linear search with O(n) and binary search with O(nLog(n).
    Binary search requires the list to be ordered.
    The examples are done on Genes. Genes of made of Codons. Codons are 3 Nucleotides.
    Inspired by David Kopec.  """
from enum import IntEnum
from typing import Tuple, List

# Choosing type IntEnum instead of Enum gives us comparison operator required for searches
Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))
Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]   # Type alias for codons
Gene = List[Codon]                                  # Type alias for genes

def string_to_gene(in_str: str) -> Gene:
    """ Convert a string to a Gene where in_str is the input string. """
    gene: Gene = []
    for index in range(0, len(in_str), 3):
        if (index + 2) >= len(in_str):   # Do not exceed the end
            return gene

        # Initialize codon out of 3 nucleotides
        codon: Codon = (Nucleotide[in_str[index]], Nucleotide[in_str[index+1]],
                        Nucleotide[in_str[index+2]])
        gene.append(codon)
    return gene

def linear_contains(gene: Gene, key_codon: Codon) -> bool:
    """ Typical implementation of linear search. O(n). """
    for codon in gene:
        if codon == key_codon:  # Uses built-in comparator of IntEnum
            return True
    return False

def binary_contains(gene: Gene, key_codon: Codon) -> bool:
    """ Typical binary search. Assumes ordered list. O(nlog(n)). """
    low: int = 0
    high: int = len(gene) -1
    while low <= high:              # While there is still search space
        mid: int = (low + high) // 2
        if gene[mid] < key_codon:   # If key is to the right of mid, replace low
            low = mid + 1
        elif gene[mid] > key_codon: # If key is to the right of mid, replace high
            high = mid - 1
        else:
            return True             # Found the match
    return False



if __name__ == "__main__":
    gene_str: str = "ACGTGGCTCTCTAACGTACGTACGTA"
    my_gene: Gene = string_to_gene(gene_str)
    print(f"\nmy_gene:{my_gene}\n")

    # Define codons
    acg: Codon = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
    gat: Codon = (Nucleotide.G, Nucleotide.A, Nucleotide.T)

    # Apply the linear function to check presence
    print("\nLinear search contain:")
    print(f"Is ACG in my genes? {linear_contains(my_gene, acg)}")
    print(f"Is GAT in my genes? {linear_contains(my_gene, gat)}")

    # Apply the binary function to check presence
    print("\nBinary search contain:")
    print(f"Is ACG in my genes? {binary_contains(my_gene, acg)}")
    print(f"Is GAT in my genes? {binary_contains(my_gene, gat)}")

    # Use built in __contains__() operator
    print("\nBuilt-in contain:")
    print(f"Is ACG in my genes? {acg in my_gene}")
    print(f"Is GAT in my genes? {gat in my_gene}")


