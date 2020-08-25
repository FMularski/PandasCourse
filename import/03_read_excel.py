import pandas as pd


df = pd.read_excel('data/companies.xlsx', na_values='?', index_col=0)

# %%

df_msft = pd.read_excel('data/companies.xlsx', index_col=0, sheet_name='microsoft') 

# %%

df_google = pd.read_excel('data/companies.xlsx', na_values='?', index_col=0, sheet_name='google')