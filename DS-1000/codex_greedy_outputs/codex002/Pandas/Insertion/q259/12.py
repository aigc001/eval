
df['TIME'] = pd.to_datetime(df['TIME'])
df['RANK'] = df.groupby('ID')['TIME'].rank(ascending=True, method='dense')
