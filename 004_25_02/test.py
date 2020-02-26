import pandas as pd
df = pd.DataFrame({
'Страна': ['Казахстан', 'Россия', 'Беларусь', 'Украина'],
'population': [17.04, 143.5, 9.5, 45.5],
'square': [2724902, 17125191, 207600, 603628]
}, index = ['KZ', 'RU', 'BY', 'UA'])

df.index=['KZ', 'RU', 'BY', 'UA']
df.index.name = '№'
df['density'] = df['population'] / df['square'] * 1000000
print(df)