"""
Created on Mon May 21 07:45:01 2018
Snippet of codes to load text table

"""
import pandas as pd

sub_label = ['Gold', 'Silver', 'Bronze', 'Total']
label = ["Country", 'Summer No'] + sub_label + ['Winter No'] + sub_label + ['Sum No'] + sub_label
df = pd.read_table('olympic_medals.txt', encoding='utf-8', sep='\t', header=1, names=label)
print("\nOlympic medal tables:\n", df)