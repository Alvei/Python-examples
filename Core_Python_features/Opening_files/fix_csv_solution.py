import sys, csv

old_filename = 'cars-original.csv'
new_filename = 'cars.csv'

"""
with open(old_filename, newline='') as old_file:
    reader = csv.reader(old_file, delimiter='|')
    rows = [line for line in reader]

with open(new_filename, mode='wt', newline='') as new_file:
    writer = csv.writer(new_file)
    # .writerows() requires iterator
    writer.writerows(rows)  """

""" Whenever you see a list comprehension that loops over something and
    doesn't filter anything or change any item but just makes a list,
    you can replace it with the list constructor: rows = list(reader)
    The list constructor loops over whatever you give it and makes a new list. """


with open(old_filename, newline='') as old_file:
    rows = list(csv.reader(old_file, delimiter='|'))

with open(new_filename, mode='wt', newline='') as new_file:
    # .writerows() requires an iterator
    csv.writer(new_file).writerows(rows)

def brittle_solution(old_filename: str, new_filename: str) -> None:
    """ Not very robust. Much better to use CSV module. """
    old_file = open(old_filename)
    rows = [
        line.split('|')
        for line in old_file.read().splitlines()
    ]

    new_file = open(new_filename, mode='wt', newline='\r\n')
    print("\n".join(
        ",".join(row)
        for row in rows
    ), file=new_file)
    old_file.close()
    new_file.close()