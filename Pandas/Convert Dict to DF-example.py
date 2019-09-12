"""
Created on Sun Apr 29 21:36:40 2018
Different ways to manipulate dictionaries in a pandas DataFrame
"""
import numpy as np
import pandas as pd


print("************** Dict examples of DF *********")
# Take a dictionary as input to DataFrame. The key becomes the name of the column
my_dict = {1: ['1', '3'], 2: ['1', '2'], 3: ['2', '4']}
my_dict_DF = pd.DataFrame(my_dict)
print("DataFrame:\n", my_dict_DF, sep='')

# Take two dictionaries as input to DataFrame but 1st doe Series
area_dict = {'California': 423967, 'Texas': 695662, 'New York': 141297,
             'Florida': 170312, 'Illinois': 149995}

population_dict = {'California': 38332521,
                   'Texas': 26448193,
                   'New York': 19651127,
                   'Florida': 19552860,
                   'Illinois': 12882135}
# Create the series
area        = pd.Series(area_dict)
population  = pd.Series(population_dict)

print("\nSeries Area:\n", area, sep='')
print("\nSeries Population:\n", population, sep='')

# Create the integrated DF. The keys are the column names
states_dict = {'population': population,'area': area}
states = pd.DataFrame({'population': population, 'area': area})
print("\nstates\n", states)
print("\nindex = ",   states.index)
print("\ncolumns = ", states.columns)

# Using as a DataFrame as a dictionary
print("\narea: \n",states['area'], sep='')