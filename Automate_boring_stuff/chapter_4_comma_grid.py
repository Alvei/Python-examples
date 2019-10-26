""" Comma Grid program.
    Transpose the grid. Ie columns become row.
    Inspired from Automate the Boring Stuff with Python - Al Sweigart. Page 102.
"""
from typing import List   # For static type checker

SPAM = ['apples', 'bananas', 'tofu', 'cats']
GRID = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def list_to_string(my_list: List[str]) -> str:
    """ Converts a list to a string with items separated by commas. """
    string = my_list[0]
    for item in my_list[1:]:
        string = string + ', ' + item
    return string


def transpose_grid(grid: List[list]) -> None:
    """ Transpose the grid. """

    # Create a list of strings representing each lines while removing the comma
    lines: List[str] = []
    for item in grid:
        line = list_to_string(item).replace(', ', '')

        # print(index, ":", line)
        lines.append(line)

    # Create new strings by taking the colums. It assumes the grid is square
    for col in range(len(lines[0])):
        new_string = ""
        for row in lines:
            new_string += row[col]
            #col += 1
        print(new_string)

def transpose_grid2(grid: List[list]) -> None:
    """ Transpose the grid. Simply flip the col and row. use end='' to avoid EOL. """
    for index in range(len(grid[0])):
        for index2 in range(len(grid)):
            print(grid[index2][index], end='')
        print()

def main():
    """ Test Harness """
    transpose_grid(GRID)
    transpose_grid2(GRID)

    #print(list_to_string(spam))

if __name__ == "__main__":
    main()
