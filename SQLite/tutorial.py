""" Tutorial.py
https://pythonprogramming.net/sql-database-python-part-1-inserting-database/
"""
import sqlite3
import time
import datetime
import random

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser
from matplotlib import style
style.use('fivethirtyeight')

# Global variables
conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table() -> None:
    """ Create a table, called stuffToPlot, if it doesn't exist.
        This table contains the following rows: unix, datestamp, keyword, and value.
        Each column is assigned a datatype. In our case, unix is a REAL,
        which is like a Python float, then we have some TEXT variables, and another REAL.
        Check out SQLite datatype documentation for the available datatypes."""
    c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")

def data_entry() -> None:
    """ Insert data. """
    c.execute("INSERT INTO stuffToPlot VALUES(1452549219,'2016-01-11 13:53:39','Python',6)")
    conn.commit()
    c.close()
    conn.close()

def dynamic_data_entry():
    """ Create data in a more flexible way. """
    unix = int(time.time())   # Limit to int so make db more space efficient
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0, 10)

    c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
          (unix, date, keyword, value))

    conn.commit()

def read_from_db() -> None:
    """ Read the database and print. """
    c.execute('SELECT rowid, * FROM stuffToPlot')
    data = c.fetchall()
    #print(data)
    print(f"Print all the rows")
    for row in data:
        print(row)

    c.execute('SELECT * FROM stuffToPlot WHERE value = 6')
    data = c.fetchall()
    #print(data)
    print(f"\nPrint all the rows where value = 6")
    for row in data:
        print(row)

    c.execute('SELECT * FROM stuffToPlot WHERE unix > 1590895004')
    data = c.fetchall()
    #print(data)
    print(f"\nPrint all the rows with specific timestamp")
    for row in data:
        print(row)

    c.execute('SELECT value, datestamp FROM stuffToPlot WHERE unix > 1590895004')
    data = c.fetchall()
    #print(data)
    print(f"\nPrint all values on the rows with specific timestamp")
    for row in data:
        print(row[0])

def graph_data():
    """ Plot graphs of datestamp, and value from the table.. """

    # Keep datestamps and value
    c.execute('SELECT datestamp, value FROM stuffToPlot')
    data = c.fetchall()

    dates = []
    values = []

    for row in data:
        dates.append(parser.parse(row[0]))
        values.append(row[1])

    plt.plot_date(dates,values,'-')
    plt.show()

def del_and_update(switch: str) -> None:
    """ Delete and update the table. """

    # Get all the data
    c.execute('SELECT * FROM stuffToPlot')
    data = c.fetchall()

    # Print using list comprehension
    [print(row) for row in data]

    if switch == 'Update':
        c.execute('UPDATE stuffToPlot SET value = 99 WHERE value = 6')
        conn.commit()
    elif switch == 'Delete':
        c.execute('DELETE FROM stuffToPlot WHERE value = 99')
        conn.commit()
    else:
        print("Wrong argument for function del_and_update()")

    c.execute('SELECT * FROM stuffToPlot')
    data = c.fetchall()
    [print(row) for row in data]

def main():

    create_table()

    #data_entry()

    """ for i in range(10):
        dynamic_data_entry()
        print(f"{i}")
        time.sleep(1) """

    #read_from_db()
    #graph_data()
    del_and_update('Delete')

if __name__ == "__main__":
    main()