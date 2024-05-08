
df['b'] = np.where((df['a'] > 1) & (df['a'] <= 4), df['b'], np.nan)
print(df['b'])
