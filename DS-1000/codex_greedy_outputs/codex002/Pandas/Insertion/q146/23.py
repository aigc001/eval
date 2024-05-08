
df['cummax'] = df.groupby('id')['val'].cummax()
