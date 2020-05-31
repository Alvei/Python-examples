""" Simple program to learn SQLite. """
import sqlite3

# Create the database
conn = sqlite3.connect("customer.db")

# Create in memory database
conn2 = sqlite3.connect(':memory:')

# Create a cursor
c = conn.cursor()

# Update records
c.execute("""Update customers SET first_name = 'Bob'
            WHERE last_name = 'Elder'
            """)
conn.commit()

c.execute("""Update customers SET first_name = 'John'
            WHERE rowid = 4
            """)
conn.commit()

# Query the database and keep row ID
c.execute("SELECT rowid, * FROM customers ")

items = c.fetchall()

# Print but now you see rowid that you can use
for item in items:
    print(f"{item} ")

# Delete
c.execute("DELETE from customers WHERE rowid = 11")
conn.commit()
items = c.fetchall()

# Order
c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC")
conn.commit()
items = c.fetchall()

# Print but now you see rowid that you can use
for item in items:
    print(f"{item} ")

# Close connection
conn.close()
