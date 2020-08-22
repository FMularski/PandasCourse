import pandas as pd
import numpy as np

# %% importing dataset

df = pd.read_csv('./data/aapl_us_d.csv', index_col=0)
df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']

# %% compute new columns

df['Average'] = (df['Open'] + df['Close']) / 2.

# %% shifting

df['Daily_Change'] = df['Close'] / df['Close'].shift(1) - 1

# %% assign method

df = df.assign(avg=(df['Open'] + df['Close']) / 2.) # avg is new column name

# %% aggregate method (needs function reference)

max_daily_change = df['Daily_Change'].aggregate(max)
min_daily_change = df['Daily_Change'].aggregate(min)
avg_daily_change = df['Daily_Change'].aggregate(np.mean)

# %% histogram

df['Daily_Change'].hist(bins=100)   # bins = słupki wykresu

# %% True if change > 0 else False

df['Flag'] = df['Daily_Change'] > 0
df['Flag'].aggregate(sum)

# %% 
days_percentage_with_positive_return = df['Flag'].aggregate(sum) / df['Flag'].aggregate('count')