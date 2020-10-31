# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 21:29:01 2018

https://www.computerhope.com/issues/ch001721.htm
"""
from os.path import dirname, join
import csv, sys
import numpy as np

FILENAME = "lorem.txt"
FILENAME2 = "weight-data.txt"


def read_file1(filename: str) -> str:
    """ Read the entire file into a string variable."""
    try:
        in_file = open(filename, "rt")  # open file. 'rt' means read text data."
        contents = in_file.read()
        in_file.close()
        return contents
    except IOError:
        print(f"\n*** File {filename} is unavailable. ***")
        sys.exit(1)


def read_file2(filename: str) -> str:
    """WITH creates context to open, operate, & close the file. All in one easy-to-read block of code.
    The file is automatically closed when the code block completes."""
    try:
        with open(filename, "rt") as in_file:
            # Read the entire file into a variable named contents.
            contents = in_file.read()
        return contents
    except IOError:
        print(f"\n*** File {filename} is unavailable. ***")
        sys.exit(1)


def read_file3(filename: str) -> None:
    """Read one line at a time and print it.
    The file object is an iterator. Therefore, you can use a for loop to operate on a file object
    repeatedly, and each time the same operation is performed, you'll receive a different, or next, result."""

    try:
        content = []
        with open(filename, "rt") as in_file:
            for line in in_file:  # Store each line in a string variable "line"
                print(line)  # prints that line
                content.append(line)
        print(f"Done 3: {content}")
    except IOError:
        print(f"\n*** File {filename} is unavailable. ***")
        sys.exit(1)


def read_file4(filename: str) -> None:
    """Read line by line and remove EOL.
    To remove the line separator, use append() but now we have a list."""
    try:
        lines = []
        with open(filename, "rt") as in_file:
            for line in in_file:  # Store each line in a string variable "line"
                lines.append(line)
            print(lines)
    except IOError:
        print(f"\n*** File {filename} is unavailable. ***")
        sys.exit(1)

    # We can print each elements and special version of print to remove the EOL
    for element in lines:
        print(element, end="")


def read_file5(filename: str) -> None:
    """No error checking. Read line by line and remove EOL. Also remove line breaks inside the data
    To remove the line separator, use append() but now we have a list."""

    lines = []
    with open(filename, "rt") as in_file:
        # add that line to our list of lines, stripping newlines.
        for line in in_file:
            lines.append(line.rstrip("\n"))

        for element in lines:  # For each element in our list,
            print(element)


def read_file6(filename: str) -> str:
    """ No error checking. Specific structure. Line 0 is a header.  Then data (gender, weight) separated by a comma."""

    weight = []
    with open(filename, "r") as f:
        for index, line in enumerate(f):
            if index == 0:
                pass  # skips header
            else:
                data = line.split(",")
                weight.append(
                    float(data[-1])
                )  # data[-1] ensures we take last value in line
    return weight


def read_file7(filename: str) -> str:
    """No error checking. Uses readlines()
    Specific structure. Line 0 is a header.  Then data (gender, weight) separated by a comma."""

    weight = []
    with open(filename, "r") as f:
        file_data = f.readlines()
        for line in file_data[1:]:  # Skips head by doing [1:]
            data = line.split(",")
            weight.append(float(data[-1]))

    return weight


def read_file8(filename: str) -> str:
    """No error checking. Uses csv_reader()
    Specific structure. Line 0 is a header.  Then data (gender, weight) separated by a comma."""

    weight = []
    with open(filename, "r") as f:
        contents = csv.reader(f, delimiter=",")  # CVS reader object
        for index, line in enumerate(contents):
            if index == 0:
                pass  # Skip first row
            else:
                weight.append(float(line[-1]))

    return weight


def read_file9(filename: str) -> str:
    """No error checking. Uses numpy.loadtxt(). weight is a ndarray.
    Note comma on usecols (needed if only one column is used)
    Specific structure. Line 0 is a header.  Then data (gender, weight) separated by a comma."""

    # Use loadtxt skipping 1 row and only using second column
    weight = np.loadtxt(
        filename, dtype=np.float_, delimiter=",", skiprows=1, usecols=(1,)
    )
    return weight


def read_file11(filename: str) -> list:
    """Read one line at a time and print it.
    File object is an iterator. Therefore, you can use a for loop to operate on a file object
    repeatedly, and each time the same operation is performed, you'll receive a different, or next, result."""

    try:
        content = []
        with open(filename, "rt") as in_file:
            for line in in_file:  # Store each line in a string variable "line"
                print(line)  # prints that line
                content.append(line.rstrip("\n"))
        return content
    except IOError:
        print(f"\n*** File {filename} is unavailable. ***")
        sys.exit(1)


def main():
    """ Test harness. """
    file_name = FILENAME
    current_dir = dirname(__file__)
    file_path = join(current_dir, "./", file_name)

    # print("\n1st read_file:", read_file1(file_path))
    # print("\n2nd read_file:", read_file2(file_path))
    print("\n3rd read_file:")
    read_file3(file_path)
    print("\n4th read_file:")
    read_file4(file_path)
    print("\n5th read_file:")
    read_file5(file_path)

    file_name = FILENAME2
    file_path = join(current_dir, "./", file_name)
    print("\n6th read_file:", read_file6(file_path))
    print("\n7th read_file:", read_file7(file_path))
    print("\n8th read_file:", read_file8(file_path))
    print("\n9th read_file:", read_file9(file_path))

    file_name = "my_text.txt"
    file_path = join(current_dir, "./", file_name)
    ans = read_file11(file_path)
    a = int(ans[0])
    c = ans[3].split(" ")
    print(f"\n11th read_file: {c}")


if __name__ == "__main__":
    main()
