""" Search for a regex pattern in filenames inside the current directory."""
import os
import re
from typing import List

def find_file_with_pattern(raw_match: str) -> List[str]:
    """ Function to find files that matches regex pattern in raw string format. """

    match_regex = re.compile(raw_match)

    # List all files in directory and filter those that are not txt files.
    cwd = os.getcwd()
    print(f"Current Working Directory: {cwd}\n")
    files = os.listdir(os.getcwd())

    # Doing match using list comprehension
    #files_lower = [file.lower() for file in files]
    matches = [doc for doc in files if match_regex.search(doc) is not None]
    print(f"Found {len(files)} files, {len(matches)} had matching the pattern: '{raw_match}'\n")
    return matches

if __name__ == "__main__":
    MATCH = 'chap'
    NEW = 'chap'
    match_files = find_file_with_pattern(r'{}'.format(MATCH))
    #print(match_files)

    for doc in match_files:
        new_name = doc.replace(MATCH, NEW)
        
        print(f"Found {doc} => do you want to change to {new_name}")
        
        choice = input("1 for Yes, 2 for No")
        if choice == 1:
            os.rename(doc, new_name)
