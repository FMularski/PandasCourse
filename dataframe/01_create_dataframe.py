import pandas as pd
import numpy as np


# %% 

df = pd.DataFrame([42, 41, 55])

# %% 2x3

df = pd.DataFrame(data=[[42, 41, 55], [44, 12, 1]], 
                  index=['first', 'second'],
                  columns=['col1', 'col2', 'col3'])

# %% 3x3

df = pd.DataFrame(data=[[42, 41, 55], [44, 12, 1], [53, 67, 91]], 
                  index=['first', 'second', 'third'],
                  columns=['col1', 'col2', 'col3'])

# %% 

d = {'one': pd.Series([1, 2, 3]),
     'two': pd.Series([4, 5, 6])
     }

df = pd.DataFrame(d)

# %% 

d = {'one': pd.Series([1, 2, 3]),
     'two': pd.Series([4, 5, 6]),
     'flag': pd.Series(['yes', 'no', 'no'])
     }

df = pd.DataFrame(d)

# %% 

d = {'one': pd.Series([1, 2, 3, 4, 5]),
     'two': pd.Series([4, 5, 6]),
     }

df = pd.DataFrame(d)

# %%
d = {'one': pd.Series(np.random.randn(100)),
     'two': pd.Series(np.random.randn(100)),
     'three': pd.Series(np.random.randn(100))
     }

df = pd.DataFrame(d)

# %%

df.index
df.columns

for idx in df.index:
    print(idx)


for col in df.columns:
    print(col)

# %%

list_of_dicts = [{'apple': 1, 'orange': 4},
                 {'apple': 3, 'orange': 3, 'mango': 2}]

df = pd.DataFrame(list_of_dicts)

# %%

for col in df.columns:
    print(col)
    
for idx in df.index:
    print(idx)
    
    
big_letters = [column.upper() for column in df.columns]
df.columns = big_letters

# %%

d = {'Wig20': ['PKN Orlen', 'PKO BP', 'LPP'],
     'mWig40': ['Amica', 'Playway', 'Benefit']}

df = pd.DataFrame(d)



















