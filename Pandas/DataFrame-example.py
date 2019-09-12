
"""
Created on Sun Apr 29 18:52:21 2018

DataFrame can be thought of as a generalization of a two-dimensional
NumPy array, where both the rows and columns have a generalized
index for accessing the data.

Similarly, we can also think of a DataFrame as a specialization of a
dictionary. Where a dictionary maps a key to a value,
a DataFrame maps a column name to a Series of column data.
For example, asking for the 'area' attribute returns the Series object.

Index is an immutable array and an ordered set.
"""
import numpy as np
import pandas as pd

# Example of a constructor using dictionaries
data = [{'a': i, 'b': 2 * i}
        for i in range(3)]
print('\nDF1 using dict and list comprehension:\n', pd.DataFrame(data), sep='')


# Take a 2D array as input to your DataFrame
my_2darray = np.array([[1, 2, 3], [4, 5, 6]])
print('\nDF2 using 2D array:\n', pd.DataFrame(my_2darray), sep='')

# Take a DataFrame as input to your DataFrame
my_df = pd.DataFrame(data=[4,5,6,7], index=range(0,4), columns=['A'])
print('\nDF3 by specifycing the data, index and columns:\n', pd.DataFrame(my_df), sep='')

# Take a Series as input to your DataFrame
my_series = pd.Series({"United Kingdom":"London", "India":"New Delhi", "United States":"Washington", "Belgium":"Brussels"})
my_series_DF = pd.DataFrame(my_series)
print('\nDF4 using series:\n', my_series_DF, sep='')

# Adding row
df = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'))
print('\nDF5 specifying list of lists and columns: \n', df, sep='')

# By using index=True we let it increase the index
df6 = pd.DataFrame([[5, 6], [7, 8]], columns=list('AB'))
print('\nDF6 being added: \n', df6, sep='')

df.append(df6, ignore_index=True)
print('\nDF7 with apppended DF6: \n', df, sep='')


