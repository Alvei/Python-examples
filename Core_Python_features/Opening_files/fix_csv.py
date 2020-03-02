""" Converts a | separated file
    https://www.youtube.com/watch?v=q5uM4VKywbA
    https://treyhunner.com/2018/03/tuple-unpacking-improves-python-code-readability/#Multiple_assignment_is_very_strict
    Inpsired by python morsels. """
import csv, sys
from argparse import ArgumentParser
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.DEBUG)

# More robust parsing of command line with argparse module
parser = ArgumentParser()           # Create the parser

# Add the arguments
parser.add_argument('inputfile')
parser.add_argument('outputfile')
parser.add_argument('--in-delimiter', dest='delim', default='|')
parser.add_argument('--in-quote', dest='quote', default='"')

args = parser.parse_args()          # Arguments are parsed and are present as object attributes

# Open context to read file with  basic error checking
with open(args.inputfile, 'r', newline='') as csvinputfile:
    # Empty directory of all arguments then load defaults
    arguments = {}
    if args.delim:
        arguments['delimiter'] = args.delim
    if args.quote:
        arguments['quotechar'] = args.quote

    # If no default, then we infer the arguments
    if not args.delim and not args.quote:
        arguments['dialect'] = csv.Sniffer().sniff(csvinputfile.read())
        csvinputfile.seek(0)    # Reset the pointer to the beginning of file
    try:
        reader = csv.reader(csvinputfile, **arguments)
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
