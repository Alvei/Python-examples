""" Comma Grid program.
    Transpose the grid. Ie columns become row.
    Inspired from Automate the Boring Stuff with Python - Al Sweigart. Page 102.
"""
from typing import List   # For static type checker

spam = ['apples', 'bananas', 'tofu', 'cats']
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def list_to_string(my_list: list) -> str:
    """ Converts a list to a string with items separated by commas. """
    string = my_list[0]
    for item in my_list[1:]:
        string = string + ', ' + item
    return string

#print(list_to_string(spam))


def transpose_grid(grid: List[list]) -> None:
    """ Transpose the grid. """

    # Create a list of strings representing each lines while removing the comma
    lines = []
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
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            print(grid[j][i], end='')
        print()

def main():
    transpose_grid(grid)
    transpose_grid2(grid)

if __name__ == "__main__":
    main()