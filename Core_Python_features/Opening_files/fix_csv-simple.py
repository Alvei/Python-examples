""" Converts a | separated file
    https://www.youtube.com/watch?v=q5uM4VKywbA
    https://treyhunner.com/2018/03/tuple-unpacking-improves-python-code-readability/#Multiple_assignment_is_very_strict
    Inpsired by python morsels. """
import csv, sys
from argparse import ArgumentParser
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.DEBUG)

# Minimal checking for command line input to ensure 2 arguments. It does unpacking.
# Using the variable name _ to note that we don’t care about sys.argv[0] (the name of our program).
#_, INPUTFILE, OUTPUTFILE = sys.argv

# More robust parsing of command line with argparse module
parser = ArgumentParser()           # Create the parser

# Add the arguments
parser.add_argument('inputfile')
parser.add_argument('outputfile')
parser.add_argument('--in-delimiter', dest='delim', default='|')
parser.add_argument('--in-quote', dest='quote', default='"')

args = parser.parse_args()          # Arguments are parsed and are present as object attributes

""" Can be replaced by specifying the default in the argument parser.
    Need to change the reader statement
# Defaults
quotechar, delimiter = ('"', '|')

# Update if we found these optional arguments
if args.delim:
    delimiter = args.delim
if args.quote:
    quotechar = args.quote
"""

# Open context to read file with  basic error checking
with open(args.inputfile, 'r', newline='') as csvinputfile:
    try:
        reader = csv.reader(csvinputfile, delimiter=args.delim, quotechar=args.quote)
    except IOError:
        print(f'Unable to load {csvinputfile}.  Check that it exists.')

    # Open context to write file with basic error checking
    with open(args.outputfile, 'wt', newline='') as csvoutputfile:
        try:
            writer = csv.writer(csvoutputfile, delimiter=',')
        except IOError:
            print(f'Unable to load {csvoutputfile}.  Check that it exists.')

        # For each line in the input
        for line in reader:
            logging.debug(line)
            writer.writerow(line)
