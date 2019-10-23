
""" Chapter_6_table_printer.py
    Print a right justified table.
    Inspired from Automate the Boring Stuff with Python - Al Sweigart. Chapter 6. Page 143.
"""
from typing import List

def table_printer(table_data: List[list]) -> None:
    """ Print table that is right justify. It assumes same number of elements in each list. """
    num_col = []
    max_word = 0

    # Loop over each line and keep track of number of columns
    for line in table_data:
        num_col.append(len(line))

        # Loop over the words in the line and keep track of largest word
        for word in line:
            length = len(word)
            if length > max_word:
                max_word = length

    # Remember the largest number of columns
    max_col = max(num_col)

    for line in table_data:
        for word in line:
            print(word.rjust(max_word+1), end="")
        print("")


def main():
    """ Test harness. """

    table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]
    table_printer(table_data)


if __name__ == "__main__":
    main()