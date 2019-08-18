# Simple module that uses easygui

import easygui
import sys


def main():
    print("starting")
    msg = "hello"
    image = "2010 Anais ecoles-soccer"
    if easygui.ccbox():
        print("exciting")
    else:
        print("finished")


main()
