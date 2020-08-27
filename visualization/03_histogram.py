import numpy as np
import pandas as pd


df = pd.DataFrame(np.random.rand(1000))

# %% histogram

df.hist(bins=40)

df.plot(kind='hist', bins=40)

# %% 

df = pd.DataFrame(np.random.randn(1000))

df.hist(bins=40)