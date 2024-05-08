
# Concatenate the two dataframes
df = pd.concat([df1, df2], axis=0)

# Sort the dataframe by id
df = df.sort_values('id')

# Fill the missing city and district values
df['city'] = df['city'].fillna(method='ffill')
df['district'] = df['district'].fillna(method='ffill')

# Reset the index
df = df.reset_index(drop=True)

print(df)
