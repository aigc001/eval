
# Concatenate the two dataframes
df = pd.concat([df1, df2], axis=0)

# Sort the dataframe by id and date
df = df.sort_values(['id', 'date'])

# Fill city and district from df1 into df
df['city'] = df['city'].fillna(method='ffill')
df['district'] = df['district'].fillna(method='ffill')

# Reset the index
df = df.reset_index(drop=True)

print(df)
