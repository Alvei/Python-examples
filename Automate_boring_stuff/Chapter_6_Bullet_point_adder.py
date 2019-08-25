""" Chapter_6_Bullet_point_adder.py
    Used os.path library to help find the file directory and special join to create the path.
    Inspired from Automate the Boring Stuff with Python - Al Sweigart. Chapter 6. Page 139.

"""
from os.path import dirname, join


def add_char_to_every_lines(file_name, characters, debug=False):
    """ Read a file and add characters to every line.
        Signature: (str, str, str) -> None."""

    # Find the location of the current directory. Assumes the text file is in the same directory
    current_dir = dirname(__file__)
    file_path = join(current_dir, "./", file_name)

    with open (file_path, 'rt') as in_file:
        try:
            # Read the entire file into a string variable
            contents = in_file.read()
            if debug == True:
                print("Original file:\n", contents, '\n', sep="")             # Print string
        except IOError:
            print('Unable to load "%s".  Check that it exists.' % file_path)
            return


    lines = contents.split('\n')            # Separate the string based on EOL
    # print("Convert into a list:", lines)                            # Print list(string)

    # Add the new characters in front of the line
    new_lines = []
    for line in lines:
        new_lines.append(characters + line)

    # print("Add the new characters:", new_lines)

    # Join all the string elements of the list to create a string. Method .join() applied "\n"
    new_string = "\n".join(new_lines)

    print("New file:\n", new_string, sep="")                       # Print string


def main():
    """ Test harness. Use * to create a bullet list."""
    add_char_to_every_lines("Chapter_6_old_file.md", "* ", True)

if __name__ == "__main__":
    main()
