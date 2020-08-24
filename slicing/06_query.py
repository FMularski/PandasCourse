import pandas as pd
import numpy as np


df = pd.DataFrame(np.random.randn(10, 5),
                  columns=list('abcde'))

# %%
out = df.query('a < b')

# %%

out = df.query('(a < b) & (b < c)')
out = df.query('(a < b) | (b < c)')

# %% 

df = df.round(1)

# %%

out = df.query('c == [-0.4, 0.4]')
out2 = df.query('c != 0.5')
out3 = df.query('[-0.4, 0.4] in c')
