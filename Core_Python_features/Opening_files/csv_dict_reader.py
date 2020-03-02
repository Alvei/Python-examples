""" Converts a | separated file. Use dictionary to make accessing elements easier.
    Remove one of the column
    https://www.youtube.com/watch?v=q5uM4VKywbA
    Inpsired by python morsels. """
import csv, sys
from os.path import dirname, join
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.DEBUG)

INPUTFILE = "cars-original.csv"
OUTPUTFILE = "cars-fixed.csv"

# Open context to read file with  basic error checking
with open(INPUTFILE, 'r') as csvinputfile:
    try:
        reader = csv.DictReader(csvinputfile, delimiter='|')
    except IOError:
        print(f'Unable to load {csvinputfile}.  Check that it exists.')

    # Open context to write file with basic error checking
    with open(OUTPUTFILE, 'wt', newline='') as csvoutputfile:
        # Define the field names that should be written in line 1
        fieldnames = ["Reading", "Make", "Model", "Type", "Value"]

        try:
            writer = csv.DictWriter(csvoutputfile, fieldnames=fieldnames, delimiter='\t')
        except IOError:
            print(f'Unable to load {csvoutputfile}.  Check that it exists.')

        writer.writeheader()
        # For each line in the input
        for line in reader:
            # Remove one of the element in Dictionary before saving
            del line['Type']
            logging.debug(line)
            writer.writerow(line)

