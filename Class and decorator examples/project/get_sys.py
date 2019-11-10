import sys
import os
print(sys.version)
print(sys.executable)
path = sys.path
print("Path:")
[print(l) for l in path]
print(os.getcwd())

#print(f"\nPath: {sys.path}")