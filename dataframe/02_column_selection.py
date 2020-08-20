import pandas as pd
import numpy as np


# %%

df = pd.read_csv('./data/aapl_us_d.csv', index_col=0)
df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']

# %%
print(df.columns)

# %% 

open_price = df['Open']
open_price = df.iloc[:, 0]

high_price = df['High']

# %%

close_price = df.Close
print(type(close_price))

for price in close_price:
    print(price)
    
# %%
last_column = df.iloc[:, -1]

# %% 
two_cols = df[['Open', 'Close']]

for _open in two_cols['Open']:
    print(_open)
    
# %% 

three_cols = df.iloc[:, [0, 3]] # indexes: 0 - open 3 - close

# %%

from_open_to_close = df.iloc[:, 0:4]

# %% 

from_open_to_close = df.iloc[:, :-1]    # all columns but the last one