import pandas as pd
import numpy as np


df = pd.DataFrame(np.random.randn(20, 5),
                  columns=list('abcde'),
                  index=list('abcdefghijklmnoprstu'))

# %% by col
# iloc[row_index, column_index]

col_1 = df.iloc[:, 0]
col_ab = df.iloc[:, 0:2]

col_last = df.iloc[:, -1]

other_cols = df.iloc[:, ::2]

# %% by rows

row1 = df.iloc[[0]]
row_last = df.iloc[[-1]]
other_rows = df.iloc[::2]

# %%

df_first_last_col_last_row = df.iloc[[0, -1], [0, -1]]