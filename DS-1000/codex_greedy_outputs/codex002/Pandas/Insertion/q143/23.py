
df['cumsum'] = df.groupby('id')['val'].cumsum()
