
# Concatenate the two dataframes
df = pd.concat([df1, df2], axis=0)

# Convert date to datetime format
df['date'] = pd.to_datetime(df['date'])

# Format date as required
df['date'] = df['date'].dt.strftime('%d-%b-%Y')

# Fill city and district from df1 into df
df['city'] = df['city'].fillna(method='ffill')
df['district'] = df['district'].fillna(method='ffill')

# Sort by id and date
df = df.sort_values(['id', 'date'])

# Reset index
df = df.reset_index(drop=True)

print(df)
