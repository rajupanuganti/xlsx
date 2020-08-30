import pandas as pd 

excel1 = 'test1.xlsx'
excel2 = 'test2.xlsx'

df1 = pd.read_excel(excel1)
df2 = pd.read_excel(excel2) 

values1 = df1[['city','km']]
values2 = df2[['city','km']]

dataframes = [values1, values2]

join = pd.concat(dataframes)

join.to_excel('ressult.xlsx')