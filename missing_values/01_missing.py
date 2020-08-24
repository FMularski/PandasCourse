import pandas as pd
import numpy as np


df = pd.DataFrame(np.random.randn(10, 4),
                  columns=['one', 'two', 'three', 'four'])

# %% 

for row in df.values:
    switch = np.random.choice([0, 1])
    
    if switch:
        i = np.random.choice([0, 1, 2, 3])
        row[i] = np.nan
        
# %% isnull
df.isnull()
df[df.isnull()]

print(df['one'].isnull())
print(df[df['one'].isnull()])
print(df[~df['one'].isnull()])

# %% notnull

print(df.notnull())
print(df[df.notnull()])

# %%

df['five'] = np.nan

# %%

del df['five']