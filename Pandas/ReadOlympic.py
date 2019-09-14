"""
Created on Mon May 21 07:45:01 2018
Snippet of code to load text table
"""
import pandas as pd

sub_label = ['Gold', 'Silver', 'Bronze', 'Total']
label = ["Country", 'Summer No'] + sub_label + ['Winter No'] + sub_label + ['Sum No'] + sub_label
df = pd.read_table('olympic_medals.txt', encoding='utf-8', sep='\t', header=1, names=label)
df.set_index('Country', inplace=True)
df.drop('Totals', inplace=True)
# print("\nOlympic medal tables:\n", df)
# print(df.info())

# Noticed that many columns are saved as string and not integer but cannot convert because of the ','
# But 1st create a regex dict to help remove the $ or , in the strings otherwise astype() does not work
regex_dict = {r'\$': '', ',': ''}
df.replace(regex_dict, regex=True, inplace=True)

# Convert the integer columns into integers
df = df.astype(int)
# print(df.info())

print(df.sort_values(['Total.2'], ascending=False)[['Total.2']])