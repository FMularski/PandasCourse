import pandas as pd
import numpy as np


# %%

df = pd.DataFrame(np.random.randn(20, 5), columns=list('abcde'), 
                  index=list('abcdefghijklmnoprstu'))

# %% loc columns

col_a = df.loc[:, 'a']
col_b = df.loc[:, 'b']
col_ab = df.loc[:, ['a', 'b']]
col_bcd = df.loc[:, 'b':'d']

# %% loc rows

row_a = df.loc['a']     # as series
row_a = df.loc[['a']]   # as dataframe

# %% loc columns and rows

row_a_col_a = df.loc['a', 'a']
row_ad_col_bd = df.loc['a':'d', 'b':'d']
