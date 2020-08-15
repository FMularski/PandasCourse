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