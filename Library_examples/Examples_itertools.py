""" Series of examples using functions from itertools. """
from itertools import zip_longest

names = "Pierre Marc Ottawa Eric Martin Ozzy".split()
countries = "Australia Canada Global France".split()

# This will truncate the lists since they are not of the same lenght
ans = list(zip(names, countries))
print(f"First: {ans}")

# Adding  Name in shortest Iterator = countries
ans = list(zip_longest(names, countries))
print(f"Second: {ans}")

# Same but with a fillvalue other than None
ans = list(zip_longest(names, countries, fillvalue="Worldwide"))
print(f"Third: {ans}")
