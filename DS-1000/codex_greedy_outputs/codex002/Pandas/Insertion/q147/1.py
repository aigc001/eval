
df['cumsum'] = df.groupby('id')['val'].cumsum()
df['cumsum'] = df['cumsum'].apply(lambda x: 0 if x < 0 else x)
