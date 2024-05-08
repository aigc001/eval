
df1.set_index('Timestamp', inplace=True)
df2.set_index('Timestamp', inplace=True)

result = df1.join(df2, how='left', lsuffix='_df1', rsuffix='_df2')
result.reset_index(inplace=True)

result.columns = ['Timestamp', 'data', 'stuff']
