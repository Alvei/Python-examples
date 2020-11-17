"""
Created on Sun Apr 29 21:20:59 2018

"""
import numpy as np
import pandas as pd

# Create a 2-D array. The 1st row as empty quotation ''
data3 = np.array([['','Col1','Col2'],
                ['Row1',1,2],
                ['Row2',3,4]])

# Convert the 2-D array into a data frame by slicing and assigning to
# data => skip 1st column and 1st row
# index => take all the rows except the 1st one AND keep the 1st column
# columns => take only the 1st row AND all columns except the 1st one.
df3 = pd.DataFrame(data=data3[1:,1:],
                  index=data3[1:,0],
                  columns=data3[0,1:])
print(df3, sep='')