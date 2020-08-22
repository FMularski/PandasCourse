import pandas as pd
import numpy as np

# %% importing dataset

df = pd.read_csv('./data/aapl_us_d.csv', index_col=0)

# %% select only first n rows

n = 4
n_rows = df.iloc[:n]        # n rows, all columns

# %% select only first n columns

n = 3
n_columns = df.iloc[:, :n]  # all rows, n columns

temp = df.iloc[1:7, 2:4]    # from 1st to 6th row & from 2nd column to 3rd column
temp = df.iloc[16]          # 17th row ( as Series)
temp = df.iloc[[16]]        # 17th row ( as DataFrame)
temp = df.iloc[[8, 19]]     # 9th and 20th row 
temp = df.iloc[[4, 9], [1, 2]]  # 5th and 9th rows & 2nd and 3rd columns
temp = df.iloc[::2]         # every other row