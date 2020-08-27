import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('data/ten.csv', index_col=0)
df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
clean_price = df[['Open', 'High', 'Low', 'Close']]

# %% 

corr_matrix = clean_price.corr()

# %% 

df['Open'].corr(df['Close'])

# %% 

plt.matshow(corr_matrix)

# %% 
sns.heatmap(corr_matrix)