import pandas as pd
import numpy as np

# %% importing dataset

df = pd.read_csv('./data/aapl_us_d.csv', index_col=0)
df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']

# %% creating a mask

df_bool = df > 150  # True if value > 150 else False
df_ = df[df_bool]   # show all values > 150 else nan | df[df > 150]

# %% 

df_2019 = df['2019-01-01':'2020-01-01']     # data only from 2019

# %% 
df_jan_2019 = df['2019-01-01':'2019-01-31']

# %% query method

df_jan_2019.query('Close > 160')