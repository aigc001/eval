
# Calculate the sum of each row
df['sum'] = df.sum(axis=1)

# Calculate the most frequent bit value
df['frequent'] = df.idxmax(axis=1)

# Count the frequency of the most frequent bit value
df['freq_count'] = df.apply(lambda row: row[row['frequent']], axis=1)

# Drop the sum column
df.drop('sum', axis=1, inplace=True)

# Replace the frequent column with the actual values
df['frequent'] = df['frequent'].str.replace('bit', '')

print(df)
