
cols = df.columns[2:4]
df[cols + '_scale'] = df[cols].groupby(df['Month']).apply(lambda x: scaler.fit_transform(x.values.reshape(-1, 1)))
