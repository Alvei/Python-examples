""" Examples uses of Pathlib module. Trey Hunter as a Blog Dec 2018. 
https://docs.python.org/3/library/pathlib.html """
from pathlib import Path
root = Path('Blog_new_folder') # Initialize the object

print(f"\nPath object of type: {type(root)} is: {root}")

# Creat a new blog_new_folder
path = root / 'new_program'
print(f"\nNew folder: {path.resolve()}")

home = Path.home()
print(f"Home: {home}")

# Listing subdirectories
p = Path('.')
d = [x for x in p.iterdir() if x.is_dir()]
print(d)

# Listing Python source files in this directory tree
f = list(p.glob('*.py'))
print(f"files:{f}")
