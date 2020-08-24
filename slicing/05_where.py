import pandas as pd
import numpy as np


s = pd.Series(np.random.randn(20))

df = pd.DataFrame(np.random.randn(31, 2),
                  columns=list('ab'),
                  index=pd.date_range('20190101', periods=31))

# %% series

out = s[s > 0]
out2 = s.where(s > 0)

# %% dataframe

out = df[df > 0]
out2 = df.where(df > 0)

out2 = df.where(df > 0, other=0)    # ustawiona wartosc domyslna 0

out = df.where(df > 0, other=0).where(df < 1, other=1)

# %%
df = df.where(df > 0, other=0).where(df < 1, other=1)