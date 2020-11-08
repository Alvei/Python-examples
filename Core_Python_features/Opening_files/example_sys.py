""" Prints the subdirectory with absolute and relative path. """
import sys, os

for d in sys.path:
    print(d)

base_dir = os.path.dirname(__file__) or '.'
print(f'\nBase directory: {base_dir}')

my_path = os.path.dirname(os.path.abspath(__file__))
print(f'\nAbs Base directory: {my_path}')

sys.path.insert(0, my_path + '..\\Chapter_6-Manipulating_Strings\\')
for d in sys.path:
    print(d)
