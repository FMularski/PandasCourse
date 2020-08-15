import pandas as pd
import numpy as np


np.random.seed(0)

nums = np.random.randint(0, 10, 10)
series = pd.Series(nums, name='los')

# %% attributes

series.dtype
series.iloc[3]
series.index
series.name
series.shape

arr = series.values

# %% 

N = np.random.randn(10)
M = np.random.randn(10)

series_N = pd.Series(N)
series_M = pd.Series(M)

# %% basic methods

series_N.abs()
series_N.add(series_M)
series_N.subtract(series_M)
series_N.div(series_M)

series.drop_duplicates()
series[4] = np.nan
series.dropna()

series.idxmax()
series.idxmin()

series.count()
series_N.cumsum()
series_N.cummin()
series_N.cummax()

series.value_counts()

series.sum()
series.std()
series.describe()

# %% histogram


hist_data = pd.Series(np.random.randn(10000))
hist_data.hist(bins=80, color='red')

# %% top n

top_3 = series_N.nlargest(3)

# bottom n

bottom_4 = series_N.nsmallest(4)