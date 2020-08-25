import pandas as pd

df = pd.read_html('data/small.html', header=0, index_col=0)[0]

# %%

df_ = pd.read_html('https://www.biznesradar.pl/gielda/indeks:WIG20')[0]

# %%

df__ = pd.read_html('https://stooq.pl/t/?i=516')

# %%

df___ = pd.read_html('https://finance.yahoo.com/cryptocurrencies')[0]