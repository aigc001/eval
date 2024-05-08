
result = df.sort_values(['user', 'time']).groupby('user').agg(lambda x: x.tolist())
