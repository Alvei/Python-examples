"""our app.py

# Create in memory database
conn2 = sqlite3.connect(':memory:')
"""

import sqlite3


def create_table(database: str) -> None:
    """ Created a table called customers. """
    # Create the database and cursor
    conn = sqlite3.connect(database)
    c = conn.cursor()

    # Create a table
    c.execute("""CREATE TABLE customers (
        first_name text,
        last_name text,
        email text
    ) """)

def show_all(database: str, table: str) -> None:
    """ Querry the database and return all Records. """
    # Create the database and cursor
    conn = sqlite3.connect(database)
    c = conn.cursor()

    action = "SELECT rowid, * FROM " + table  # Dangerous and subject to SQL Injection
    #c.execute("SELECT rowid, * FROM ?", (table))
    c.execute(action)
    items = c.fetchall()

    # Print but now you see rowid that you can use
    for item in items:
        print(f"{item} ")

    # Close connection
    conn.close()

def add_one(database: str, first, last, email) -> None:
    """ Add a new record to the table """
    # Create the database and cursor
    conn = sqlite3.connect(database)
    c = conn.cursor()

    c.execute("INSERT INTO customers VALUES (?, ?, ?)", (first, last, email))

    conn.commit()
    conn.close()

def add_many(database: str, records: list) -> None:
    """ Add a record to the table """
    # Create the database and cursor
    conn = sqlite3.connect(database)
    c = conn.cursor()

    c.executemany("INSERT INTO customers VALUES (?, ?, ?)", (records))
    conn.commit()
    conn.close()

def delete_one(database: str, id: str) -> None:
    """ Delete a record to the table """
    # Create the database and cursor
    conn = sqlite3.connect(database)
    c = conn.cursor()

    c.execute("DELETE from customers WHERE rowid = (?)", id)
    conn.commit()
    conn.close()

def email_lookup(database: str, email: str) -> None:
    """ Find a record with a given email. """

     # Create the database and cursor
    conn = sqlite3.connect(database)
    c = conn.cursor()

    # Quirky tuple nomenclature with ,
    c.execute("SELECT rowid, * from customers WHERE email = (?)", (email,))
    items = c.fetchall()

    # Print but now you see rowid that you can use
    for item in items:
        print(f"{item} ")

    # Close connection
    conn.close()


def main():
    database = "customer.db"
    table = "customers"
    first = "karine"
    last = "bard"
    email = "Kbard@aol.com"
    print("Adding {first} {last} {email}")
    #add_one(database, first, last, email)
    records = [ ('Brenda', 'Smith', 'Sim.com'),
                ('Josh', 'Brain', 'josh@com')]
    #add_many(database, records)
    #delete_one(database, '6')
    #email_lookup(database, 'John@codemy.com')
    show_all(database, table)

if __name__ == "__main__":
    main()