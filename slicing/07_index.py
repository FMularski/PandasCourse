import pandas as pd
import numpy as  np


idx = pd.Index(['4212', '5124', '6314', '6678'])
df = pd.DataFrame(np.random.randn(4, 5),
                  index=idx,
                  columns=list('abcde'))