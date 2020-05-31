""" Simple program to learn SQLite. """
import sqlite3

# Create the database
conn = sqlite3.connect("customer.db")

# Create in memory database
conn2 = sqlite3.connect(':memory:')

# Create a cursor
c = conn.cursor()


# Query the database and keep row ID
c.execute("SELECT rowid, * FROM customers")

items = c.fetchall()

# Print but now you see rowid that you can use
for item in items:
    print(f"{item} ")

# Close connection
conn.close()
