""" Search for a regex pattern in filename inside a directory."""
import os, shutil
import re

def find_file_with_text(raw_match: str) -> None:
    """ Function to find files that matches regex pattern
        Prints the results to the terminal. """

    print(f"\nString to match: {raw_match}")
    match_regex = re.compile(raw_match)

    # List all files in directory and filter those that are not txt files.
    cwd = os.getcwd()
    print(f"Current Working Directory: {cwd}\n")
    files = os.listdir(os.getcwd())

    # Doing match using list comprehension
    match_files = [doc.lower() for doc in files if match_regex.search(doc) is not None]
    print(f"Found {len(files)} files, {len(match_files)} matched the pattern\n")
    #for file in match_files:
    #    print(f"{file}")

    for doc in files:
        if match_regex.search(doc) is not None:
            new_name = doc.lower()
            print(f"{doc}\t\t\t\t {new_name}")

if __name__ == "__main__":
     MATCH = r'Chapter'
    find_file_with_text(MATCH)
