
df.columns = df.columns.str.replace('Unnamed: 1', 'Concentration')
df.columns = df.columns.str.replace('Nanonose', 'Type')
df = df.dropna(how='all')
df = df.fillna(method='ffill')
