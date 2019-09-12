"""
Created on Sun May 20 21:21:21 2018


"""
import pandas as pd

# Create a list of keys that will become the columns
list_keys = ['Country', 'Total']
list_values = [['United States', 'Soviet Union', 'Great Britain'], [2827, 1204, 880]]
print('\n keys:\n', list_keys)
print('\n values:\n', list_values)

# Zip the 2 lists together into one list of (key,value) tuples: zipped
zipped = list(zip(list_keys, list_values))
print('\n Zipped:\n', zipped)

# Build a dictionary with the zipped list: data
data = dict(zipped)
print('\n dict(zipped):\n', data)

# Build and inspect a DataFrame from the dictionary: df
df = pd.DataFrame(data)
print('\n DF:\n',df)
