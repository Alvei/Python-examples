"""
reading CSV.py

Practice using CSV using dictionary
Created on Sat Mar 31 08:39:41 2018
http://zetcode.com/python/csv/
http://www.pythonforbeginners.com/systems-programming/using-the-csv-module-in-python/

for python 3.5
"""

import csv


def readCSVinDict(csvfilename, keys):
    """ Reads data from a CSV file and save into a dictionary.
        Need for provide the filename and the keys from the 1st row.
    """
    print("keys = ", keys)

    table = {}

    with open(csvfilename, 'r', newline='') as fname:
        try:
            dreader = csv.DictReader(fname)  # Dictionary reader object
        except IOError:
            print('Unable to load "%s".  Check that it exists.' % fname)
            return

        for i, row in enumerate(dreader):
            print(row)
            table[i] = row

    return table


keys = ['Year', 'Revenues', 'Profit']
r = readCSVinDict('test1.csv', keys)
