import pandas as pd
import numpy as np


# %% generate some data
np.random.seed(0)

s = pd.Series(np.random.randn(20))

# %% aggregation

minimum = s.aggregate(min)
maximum = s.aggregate(max)

suma = s.aggregate(sum)

mean = s.aggregate(np.mean) # mean => srednia
std = s.aggregate(np.std)


# %%
stats = s.aggregate(['min', 'max', 'sum', 'mean', 'std'])

stats_np = s.aggregate([np.mean, np.std, np.median])