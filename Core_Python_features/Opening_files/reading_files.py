# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 21:29:01 2018

https://www.computerhope.com/issues/ch001721.htm
"""
from os.path import dirname, join
import csv
import numpy as np
FILENAME = "lorem.txt"
FILENAME2 = 'weight-data.txt'

def read_file1(filename):
    """ No error checking.
        Signature: (str) -> str."""

    in_file = open(filename, "rt")      # open file. 'rt' means read text data."
    contents = in_file.read()           # read the entire file into a string variable
    in_file.close()
    return contents


def read_file2(filename):
    """ No error checking.
        It opens, operates, & closes the file. All in one easy-to-read block of code.
        The file is automatically closed when the code block completes.
        Signature: (str) -> str."""
    with open (filename, 'rt') as in_file:  # Open file lorem.txt for reading of text data.
        contents = in_file.read()              # Read the entire file into a variable named contents.
    return contents


def read_file3(filename):
    """ No error checking. Read one line at a time and print it.
        The file object is an iterator. Therefore, you can use a for loop to operate on a file object
        repeatedly, and each time the same operation is performed, you'll receive a different, or next, result.
        Signature: (str) -> None."""

    with open (filename, 'rt') as in_file:  # Open file lorem.txt for reading of text data.
        for line in in_file:    # Store each line in a string variable "line"
            print(line)         # prints that line


def read_file4(filename):
    """ No error checking. Read line by line and remove EOL.
        To remove the line separator, use append() but now we have a list.
        Signature: (str) -> None."""

    lines = []
    with open (filename, 'rt') as in_file:      # Open file lorem.txt for reading of text data.
        for line in in_file:                    # Store each line in a string variable "line"
            lines.append(line)
        print(lines)

    # We can print each elements and special version of print to remove the EOL
    for element in lines:
        print(element, end='')


def read_file5(filename):
    """ No error checking. Read line by line and remove EOL. Also remove line breaks inside the data
        To remove the line separator, use append() but now we have a list.
        Signature: (str) -> None."""

    lines = []
    with open (filename, 'rt') as in_file:  # Open file lorem.txt for reading of text data.
        for line in in_file:
            lines.append(line.rstrip('\n'))   # add that line to our list of lines, stripping newlines.

        for element in lines:            # For each element in our list,
            print(element)


def read_file6(filename):
    """ No error checking. Specific structure. Line 0 is a header.  Then data (gender, weight) separated by a comma.
        Signature: (str) -> str."""

    weight = []
    with open(filename, 'r') as f:
        for index, line in enumerate(f):  # counter i is included in for loop
            if index == 0:
                pass            # skips header
            else:
                data = line.split(',')
                weight.append(float(data[-1]))  #data[-1] ensures we take last value in line
    return weight

def read_file7(filename):
    """ No error checking. Uses readlines()
        Specific structure. Line 0 is a header.  Then data (gender, weight) separated by a comma.
        Signature: (str) -> str."""

    weight = []
    with open(filename, 'r') as f:
        file_data = f.readlines()
        for line in file_data[1:]: # Skips head by doing [1:]
            data = line.split(',')
            weight.append(float(data[-1]))

    return weight

def read_file8(filename):
    """ No error checking. Uses csv_reader()
        Specific structure. Line 0 is a header.  Then data (gender, weight) separated by a comma.
        Signature: (str) -> str."""

    weight = []
    with open(filename, 'r') as f:
        contents = csv.reader(f, delimiter = ',')  # CVS reader object
        for index, line in enumerate(contents):
            if index == 0:
                pass # Skip first row
            else:
                weight.append(float(line[-1]))

    return weight

def read_file9(filename):
    """ No error checking. Uses numpy.loadtxt(). weight is a ndarray.
        Note comma on usecols (needed if only one column is used)
        Specific structure. Line 0 is a header.  Then data (gender, weight) separated by a comma.
        Signature: (str) -> str."""

    # Use loadtxt skipping 1 row and only using second column
    weight = np.loadtxt(filename, dtype = np.float_, delimiter = ',', skiprows = 1, usecols = (1,))
    return weight

def main():
    """ Test harness. """
    file_name = FILENAME
    current_dir = dirname(__file__)
    file_path = join(current_dir, "./", file_name)

    """print("\n1st read_file:", read_file1(file_path))
    print("\n2nd read_file:", read_file2(file_path))
    print("\n3rd read_file:"); read_file3(file_path)
    print("\n4th read_file:"); read_file4(file_path)
    print("\n5th read_file:"); read_file5(file_path)"""

    file_name = FILENAME2
    file_path = join(current_dir, "./", file_name)
    print("\n6th read_file:", read_file6(file_path))
    print("\n7th read_file:", read_file7(file_path))
    print("\n8th read_file:", read_file8(file_path))
    print("\n9th read_file:", read_file9(file_path))


if __name__ == "__main__":
    main()
