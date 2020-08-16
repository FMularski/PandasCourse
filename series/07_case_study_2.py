import numpy as np
import pandas as pd


list_of_wig20_stocks = ['Alior', 'CCC', 'CD Projekt', 'Cyfrowy Polsat',
                        'Dino', 'JSW', 'KGHM', 'Lotos', 'LPP', 'mBank',
                        'Orange', 'PEKAO SA', 'PGE', 'PGNIG', 'PKN ORLEN',
                        'PKO BP', 'PLAY', 'PZU', 'Santander', 'Tauron']

wig20 = pd.Series(list_of_wig20_stocks, name='WIG 20')

# %% 

wig20_names = wig20.apply(lambda word: word.upper())

wig20_names.isin(['CCC'])
wig20_names[wig20_names.isin(['CCC'])]
wig20_names[wig20_names.isin(['CCC', 'PGE'])]

for company in wig20_names:
    print(company)
    
for company in wig20_names:
    company += '_PLN'
    print(company)
    
# %% 

stocks_with_len_4 = []

for company in wig20_names:
    if len(company) == 4:
        stocks_with_len_4.append(company)
        
print(stocks_with_len_4)


stocks_with_len_3 = [company for company in wig20_names if len(company) == 3]
print(stocks_with_len_3)

stocks_with_P = [company for company in wig20_names if company.startswith('P')]
print(stocks_with_P)

stocks_replace = [company.replace(' ', '_') for company in wig20_names]
print(stocks_replace)

stocks_small = [company.lower() for company in stocks_replace]
print(stocks_small)