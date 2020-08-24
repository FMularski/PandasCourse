import pandas as pd
import numpy as np


df = pd.DataFrame(np.random.randn(20, 5),
                  columns=list('abcde'),
                  index=list('abcdefghijklmnoprstu'))

# %%
col_a = df.a

mask = df.a > 0
out = df[mask]

out = df[df.a > 0]

# %%
mask = (df.a > 0) & (df.c > 0)
out = df[mask]

mask = (df.a > 0) | (df.c > 0)
out = df[mask]