
# Create a unique ID for each unique combination of 'name' and 'a'
df['ID'] = df.groupby(['name', 'a']).ngroup() + 1

# Drop the 'name' and 'a' columns
df.drop(['name', 'a'], axis=1, inplace=True)

print(df)
