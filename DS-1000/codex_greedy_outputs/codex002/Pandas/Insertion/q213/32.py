
counts = df[df['key2'] == 'two'].groupby('key1').size()
result = pd.DataFrame({'key1': counts.index, 'count': counts.values})
