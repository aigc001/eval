
# Split the var2 column into a list of values
df['var2'] = df['var2'].str.split(',')

# Expand the dataframe by stacking the var2 lists
df = df.set_index(['id', 'var1']).var2.apply(pd.Series).stack().reset_index().drop('level_2', axis=1)

# Rename the column back to var2
df.columns = ['id', 'var1', 'var2']
