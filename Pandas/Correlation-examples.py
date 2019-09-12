"""
Created on Wed May 16 14:06:34 2018
"""
import pandas as pd

# Create simply y = mx + b where  m = 2 and b = 0
df = pd.DataFrame({'A': range(4), 'B': [2.0*i for i in range(4)]})
print('\nDF:\n', df)

c = df['A'].corr(df['B'])
print('\nc:\n', c)