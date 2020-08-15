import pandas as pd
import numpy as np

# Example 1

s = pd.Series(2)

# Example 2

s_def = pd.Series(data=[42, 13, 57, 22], 
                  index=['adam', 'tomek', 'pawel', 'jan'], name='age')

# Example 3

random_data = np.random.randn(10)
random_s = pd.Series(random_data)

# %% Example 4

stocks = {'Apple': 'USA', 'CD Projekt': 'Poland', 'Amazon': 'USA'}

dict_s = pd.Series(stocks, name='Country')

# %% Example 5

stocks_price = {'Apple': 196, 'CD Projekt': 215, 'Amazon': 1877}
stocks_price_s = pd.Series(stocks_price, name='price')

stocks_price__array = stocks_price_s.values

apple_price = stocks_price_s['Apple']

'Apple' in stocks_price_s

# %% Example 6

np.random.seed(0)

nums = np.random.randn(20)
s = pd.Series(nums)
