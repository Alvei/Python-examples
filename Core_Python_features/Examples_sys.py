import sys, os

for d in sys.path:
    print(d)

base_dir = os.path.dirname(__file__) or '.'
print(f'Base directory: {base_dir}')

myPath = os.path.dirname(os.path.abspath(__file__))
print(f'Abs Base directory: {myPath}')

sys.path.insert(0, myPath + '..\\Chapter_6-Manipulating_Strings\\')
for d in sys.path:
    print(d)