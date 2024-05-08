
conditions = [df['a'].str.contains(target)]
df['b'] = np.select(conditions, choices, default='default')
