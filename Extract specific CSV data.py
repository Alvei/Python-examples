"""
reading CSV.py

Practice using CSV
Created on Sat Mar 31 08:39:41 2018
http://zetcode.com/python/csv/
http://www.pythonforbeginners.com/systems-programming/using-the-csv-module-in-python/

for python 3.5
"""

import csv


def readColor():
    with open('color.csv') as csvfile:
        try:
            readCSV = csv.reader(csvfile, delimiter=',')
        except IOError:
            print('Unable to load "%s".  Check that it exists.' % csvfile)
            return

        dates = []
        colors = []
        for row in readCSV:
            color = row[3]          # Need to know the organization of data
            date = row[0]

            dates.append(date)
            colors.append(color)

        # now that we have loaded the data, print it
        print(dates)
        print(colors)

        try:
            whatColor = input('What color do you wish to know the date of?:')
            coldex = colors.index(whatColor.lower())
            theDate = dates[coldex]
            print('The date of', whatColor, 'is:', theDate)
        except Exception as e:
            print(e)


readColor()
