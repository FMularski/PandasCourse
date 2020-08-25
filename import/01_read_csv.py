import pandas as pd


df = pd.read_csv('data/cdr_d.csv', index_col=0)

# %%

df_ = pd.read_csv('data/cdr_d.csv', index_col=0, skiprows=10)

# %%

df__ = pd.read_csv('data/cdr_d.csv', index_col=0, nrows=100)

# %%


