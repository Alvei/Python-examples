""" chapter_9_shutil
shutil.copy(source, destination)
shutil.copy('c:\\spam.txt', 'c:\\delicious')  copies a file from a director to another
shutil.move(source, destination)
sen2trash is a safe library that moves the file to trash.
"""
import shutil, os
import send2trash

print("Type 1: To copy quiz.txt to quiz2.txt")
print("Type 2: To delete quiz2.txt")
choice = 0
while choice != 1 and choice != 2:
    choice = int(input('Make your choice: '))
    if choice == 1:
        print("Copying")
        shutil.copy('quiz.txt', 'quiz2.txt')
    elif choice == 2:
        print("Deleting")
        send2trash.send2trash('quiz2.txt')
    else:
        print("Invalide choice. Please choose 1 or 2.")