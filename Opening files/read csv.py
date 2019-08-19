"""
read csv.py
Created on Sat Mar 10 21:15:18 2018
for python 3.5
"""
import csv
PREF_FILE = "test1.csv"


def loadCSVData(inputFile):
    """ Reads a file of stored users's preferences
        Signature: (str) -> list."""

    with open(inputFile, 'r') as csvfile:
        csvreader = csv.reader(csvfile)  # Object reader

        # This skips the first row of the CSV file.
        # csvreader.next() also works in Python 2.
        next(csvreader)
        data = []
        for row in csvreader:
            # do stuff with rows...
            data.append(row)

    return data


def readCSVinFloatTable(csvfilename):
    """ Read CSV file, skip the 1st row & convert all subsequent row into float
        Signature: (str) -> list of list."""
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
                """ Convert all the numbers to float.
                    Need to remove commas first then type cast to float.
                    Use enumeration on all elements of row. """
                temp = [float(x.replace(',', '')) for x in row]
                table.append(temp)
                # print(row)
            n += 1

    return table


"""def main():

if __name__ == "__main__": main()    """


print("\nWelcome")

table = readCSVinFloatTable(PREF_FILE)
for l in enumerate(table):
    print(l)
list(table)

# print(info)
#info = loadCSVData(PREF_FILE)
