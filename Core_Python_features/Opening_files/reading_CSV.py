"""
reading_CSV.py

Practice using CSV using list, dictionary
Created on Sat Mar 31 08:39:41 2018
http://zetcode.com/python/csv/
http://www.pythonforbeginners.com/systems-programming/using-the-csv-module-in-python/

for python 3.5
"""

import csv
from pprint import pprint
from os.path import dirname, join
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)


FILENAME = "test1.csv"

def read_CSV_in_dict(csvfilename, keys):
    """ Reads data from a CSV file and save into a dictionary.
        Need for provide the filename and the keys from the 1st row.
        Signature: (str, list(str)) -> dict  """

    logging.debug("\nOpening load_CSV_data at %s", csvfilename)

    table = {}

    with open(csvfilename, 'r', newline='') as fname:
        try:
            dreader = csv.DictReader(fname)  # Dictionary reader object
        except IOError:
            print('Unable to load "%s".  Check that it exists.' % fname)
            return

        for index, row in enumerate(dreader):
            logging.debug(row)
            table[index] = row

    return table


def load_CSV_data(csvfilename):
    """ Reads a file of stored users's preferences.
        Signature: (str) -> list."""

    logging.debug("\nOpening load_CSV_data at %s", csvfilename)
    with open(csvfilename, 'r') as fname:
        csvreader = csv.reader(fname)  # Object reader

        # Skip the first row of the CSV file.
        next(csvreader)
        data = []
        for row in csvreader:
            # do stuff with rows...
            logging.debug("row %s", row)
            data.append(row)

    return data


def read_CSV_in_float_table(csvfilename):
    """ Read CSV file, skip the 1st row & convert all subsequent row into float
        Signature: (str) -> list of list."""

    logging.debug("\nOpening load_CSV_data at %s", csvfilename)
    table = []
    with open(csvfilename, 'r', newline='') as fname:
        try:
            reader = csv.reader(fname, skipinitialspace=True)
        except IOError:
            print('Unable to load "%s".  Check that it exists.' % fname)
            return

        n = 0
        for row in reader:
            if n == 0:
                table.append(row)  # Keep the first row as string
            else:
                """ Convert all the numbers to float. Need to remove commas first
                    then type cast to float. Use enumeration on all elements of row. """
                temp = [float(x.replace(',', '')) for x in row]
                table.append(temp)
                logging.debug(row)
            n += 1

    return table


def main():
    file_name = FILENAME
    current_dir = dirname(__file__)
    file_path = join(current_dir, "./", file_name)

    print("Select 1 to read using csv.reader and return a list")
    print("Select 2 to read using csv.reader and return a list of floats")
    print("Select 3 to read using csv.DictReader and return a dictionary")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        table = read_CSV_in_float_table(file_path)
        print("\nWelcome... reading...,", type(table))
        pprint(table)

    elif choice == 2:
        info = load_CSV_data(file_path)
        print("\nWelcome... reading...,", type(info))
        pprint(info)

    else:
        keys = ['Year', 'Revenues', 'Profit']
        my_dict = read_CSV_in_dict(file_path, keys)
        print("\nWelcome... reading...,", type(my_dict))
        pprint(my_dict)


if __name__ == "__main__":
    main()
