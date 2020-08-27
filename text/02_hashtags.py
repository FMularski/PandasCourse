import pandas as pd
import numpy as np


# %% generating some data

s = pd.Series(['#sport#good#time', '#workout#free#time', '#summer#holiday#hot'])

# %% splitting by hash

s = s.str.split('#')

hash1 = s.str.get(1)
hash2 = s.str.get(2)
hash3 = s.str.get(3)

# %% concatenating by row

df_concat_by_row = pd.concat([hash1, hash2, hash3], ignore_index=True)

string = df_concat_by_row.str.cat(sep=' ')

# %% concatenating by cel

df_concat_by_col = pd.concat([hash1, hash2, hash3], axis=1)

# %% other split

split_2 = s.str.split('#', expand=True)
split_2.drop(0)

# %% replace

s.str.replace('#', ' ')
s.str.replace('#', '_')