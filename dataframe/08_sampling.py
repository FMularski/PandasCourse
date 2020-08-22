import pandas as pd
import numpy as np



# %% importing dataset

df = pd.read_csv('data/aapl_us_d.csv', index_col=0)

# %% sampling n numbers

sample_10 = df.sample(n=10) # gets 10 samples from whole dataset

# %% sampling percentage

sample_5_perc = df.sample(frac=0.05)