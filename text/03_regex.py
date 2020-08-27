import pandas as pd
import numpy as np

# %%
string = 'workout summer good free holiday time time hot'

# %% splitting string

split = string.split()

s = pd.Series(split)
s.str.contains(r'[0-9]')
s.str.contains(r'[a-z]')
s.str.contains(r'[rg]')