import numpy as np
import pandas as pd


# %% generate data

df1 = pd.DataFrame(np.random.randn(10, 3), columns=list('ABC'))
df2 = pd.DataFrame(np.random.randn(10, 3), columns=list('ABC'))

# %% operations
print(df1 + df2)
print(df1 - df2)
print(df1 * df2)
print(df1 / df2)
print(df1 ** 2)
print(np.exp(df1))
