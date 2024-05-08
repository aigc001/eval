
result = df.sort_values(['user', 'time']).groupby('user').apply(lambda x: x[['amount', 'time']].values.tolist()).reset_index()
result.columns = ['user', 'amount-time-tuple']
