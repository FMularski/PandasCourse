import pandas as pd
import numpy as np

# %% 

df_raw = pd.read_clipboard()

# %%
columns = [col for col in df_raw.columns]

# %%

df = df_raw.drop(['Czas', '1r 3m'], axis=1)

# %%

df['Wolumen'] = df['Wolumen'].apply(lambda s: int(s.replace(' ', '')))

# %%

df['Obrót'] = df['Obrót'].apply(lambda s: int(s.replace(' ', '')))

# %%

df['Udział'] = df['Udział'].apply(lambda s: float(s.replace('%', '')))

# %%

df['Zmiana %'] = df['Zmiana %'].apply(lambda s: float(s.replace('(', '')
                                      .replace(')', '')
                                      .replace('%', '')
                                      ))