import pandas as pd
import numpy as np


# %% 

df = pd.DataFrame([42, 41, 55])

# %% 2x3

df = pd.DataFrame(data=[[42, 41, 55], [44, 12, 1]], 
                  index=['first', 'second'],
                  columns=['col1', 'col2', 'col3'])

# %% 3x3

df = pd.DataFrame(data=[[42, 41, 55], [44, 12, 1], [53, 67, 91]], 
                  index=['first', 'second', 'third'],
                  columns=['col1', 'col2', 'col3'])

# %% 

d = {'one': pd.Series([1, 2, 3]),
     'two': pd.Series([4, 5, 6])
     }

df = pd.DataFrame(d)

# %% 

d = {'one': pd.Series([1, 2, 3]),
     'two': pd.Series([4, 5, 6]),
     'flag': pd.Series(['yes', 'no', 'no'])
     }

df = pd.DataFrame(d)

# %% 

d = {'one': pd.Series([1, 2, 3, 4, 5]),
     'two': pd.Series([4, 5, 6]),
     }

df = pd.DataFrame(d)

# %%
d = {'one': pd.Series(np.random.randn(100)),
     'two': pd.Series(np.random.randn(100)),
     'three': pd.Series(np.random.randn(100))
     }

df = pd.DataFrame(d)

# %%

df.index
df.columns

for idx in df.index:
    print(idx)


for col in df.columns:
    print(col)

# %%

list_of_dicts = [{'apple': 1, 'orange': 4},
                 {'apple': 3, 'orange': 3, 'mango': 2}]

df = pd.DataFrame(list_of_dicts)

# %%

for col in df.columns:
    print(col)
    
for idx in df.index:
    print(idx)
    
    
big_letters = [column.upper() for column in df.columns]
df.columns = big_letters

# %%

d = {'Wig20': ['PKN Orlen', 'PKO BP', 'LPP'],
     'mWig40': ['Amica', 'Playway', 'Benefit']}

df = pd.DataFrame(d)

# %% practice Series

s1 = pd.Series([1, 2, 3])
s2 = pd.Series([[1, 2], [3, 4]])
s3 = pd.Series([[1, 2], [3, 4], [5, 6]])

s4 = pd.Series(data=[100, -100], index=['idx1', 'idx2'], name='name')
print(s4['idx1'])

s5 = pd.Series(data=[[1, 2, 4, 8, 16], [32, 64, 128, 256, 512]], index=['list1', 'list2'])
print(s5['list2'])

s6 = pd.Series({'key1': 'value1', 'key2': 'value2'}, name='this is name of the column')

s7 = pd.Series([{'d1_key1': 'd1_value1', 'd1_key2': 'd1_value2'}, 
                {'d2_key1': 'd2_value1', 'd2_key2': 'd2_value2'}],
               index=['idx1', 'idx2'],
               name='this is name of the column')

# %% practice DataFrame

df1 = pd.DataFrame(data=[1, 2, 3])
df2 = pd.DataFrame(data=[[1, 2], [3, 4]])
df3 = pd.DataFrame(data=[[1, 2], [3, 4], [5, 6]])

df4 = pd.DataFrame(data=[[100, -100], [200, -200]], index=['idx1', 'idx2'], columns=['col1', 'col2'])
print(df4.iloc[0])

df5 = pd.DataFrame({'key1': 'value1', 'key2': 'value2'}, index=['idx1'])
print(df5.iloc[0])

df6 = pd.DataFrame([{'d1_key1': 'd1_value1', 'd1_key2': 'd1_value2'},
                    {'d1_key1': 'd2_value2', 'd1_key2': 'd2_value2'}])

df7 = pd.DataFrame([{'a': 0, 'b': 0}, {'c': 0, 'd': 0}])

df8 = pd.DataFrame([{'a': 0}, {'b': 0}, {'c': 0}, {'d': 0}])
print(df8.iloc[0])

for value in df8.iloc[0]:
    print(value)












