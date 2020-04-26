""" Search for a regex pattern inside all files with same extension inside a directory."""
import os
import re

def find_file_with_text(ext: str, raw_match: str) -> None:
    """ Simple function to find a string in all files with the same extension.
        ext is a normal string whereas raw_match is a raw string for regex
        Prints the results to the terminal. """

    # Define extension and string
    print(f"\nExtension: {ext}\nString to match: {raw_match}")
    raw_ext = r'{}'.format(ext)             # Convert the immutabe string into a new raw string
    ext_regex = re.compile(raw_ext)
    search_regex = re.compile(raw_match)

    # List all files in directory and filter those that aren't txt files
    cwd = os.getcwd()
    print(f"Current Working Directory: {cwd}\n")
    files = os.listdir(os.getcwd())
    print(f"Found {len(files)} files")

    # Doing match using list comprehension
    ext_files = [doc for doc in files if ext_regex.search(doc) is not None]
    print(f"Found {len(ext_files)} matched extension\n")
    #print(f"Found {len(ext_files)} matched extension: \n{ext_files}\n")

    # Open each txt file in turn and if regex triggers print matches to console
    for doc in ext_files:
        # {0} is the current working and {1} is the filename
        opened_file = open('{0}/{1}'.format(cwd, doc))
        contents = opened_file.read()
        string = ''.join(contents)              # Join all the line into a long string
        found = search_regex.findall(string)    # Search for the all the pattern
        if found:
            print(f"In {doc} found: {found}")
    print("")

if __name__ == "__main__":
    MATCH = r'\s?\w*\!'              # Matches all words ending in !, must be a raw string
    #MATCH = r'edu'
    find_file_with_text(".txt", MATCH)
