""" chapter_9_dir_walk.py
    os.walk() will return 3 values on each iteration through the loop
    1- a string of the current folder's name
    2- A list of strings of the folders in the current folder
    3- A list of strings of the files in the current folder
"""
import os
for folder_name, subfolders, filenames in os.walk("."):
    for subfolder in subfolders:
        print(f"FOLDER: {folder_name} SUBFOLDER: {subfolder}")

    for filename in filenames:
        print(f"FOLDER: {folder_name} FILE INSIDE: {filename}")
print("")