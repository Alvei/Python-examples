""" Simple program to learn SQLite. """
import sqlite3

# Create the database
conn = sqlite3.connect("customer.db")



# Create a cursor
c = conn.cursor()


# Create a table
#c.execute("""CREATE TABLE customers (
#    first_name text,
#    last_name text,
#    email text
#) """)


# Commit our command
conn.commit()
"""
# Insert data
c.execute("INSERT INTO customers VALUES ('John', 'Elder', 'John@codemy.com')")

# Commit our command
conn.commit()

# Create list of tuples
many_customers = [
                    ('Bob', 'Stern', 'bstern@test.com'),
                    ('nat', 'Leq', 'nleq@yahoo.com'),
                    ('What', 'Ever', 'WE.com')
                    ]

# Insert data
c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

# Commit our command
conn.commit() """

# Query the database
c.execute("SELECT * FROM customers")
#print(c.fetchall())

items = c.fetchall()
for item in items:
    print(f"{item[0]} {item[1]} {item[2]}")

# Close connection
conn.close()
