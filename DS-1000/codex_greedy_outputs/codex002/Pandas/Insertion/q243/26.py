
result = df.sort_values(['user', 'time']).groupby('user').apply(lambda x: x[['time', 'amount']].values.tolist())
