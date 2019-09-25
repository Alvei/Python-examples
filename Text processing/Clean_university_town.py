""" Clean_university_town.py
    We see that we have periodic state names followed by the university towns in that state:
    StateA TownA1 TownA2 StateB TownB1 TownB2.... If we look at the way state names are written
    in the file, we’ll see that all of them have the “[edit]” substring in them.
    We can take advantage of this pattern by creating a list of (state, city) tuples
    and wrapping that list in a DataFrame:"""
import pandas as pd


def get_citystate(item):
    """ Define a Python function that takes an element from the DataFrame as its parameter.
        Inside the function, checks are performed to determine whether there’s a
        ( or [ in the element or not. Depending on the check, values are returned
        accordingly by the function. """

    if ' (' in item:
        return item[:item.find(' (')]
    elif '[' in item:
        return item[:item.find('[')]
    else:
        return item

university_towns = []
with open('university_town.txt') as file:
    for line in file:
        if '[edit]' in line:
            # Remember this `state` until the next is found
            state = line
        else:
            # Otherwise, we have a city; keep `state` as last-seen
             university_towns.append((state, line))

towns_df = pd.DataFrame(university_towns, columns=['State', 'RegionName'])

# applymap() will apply a function to each of the lines independently

print(towns_df.iloc[:10])
towns_df =  towns_df.applymap(get_citystate)

print(towns_df.iloc[:10])