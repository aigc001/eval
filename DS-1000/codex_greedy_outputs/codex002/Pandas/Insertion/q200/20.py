
# Split the row into two columns
df[['fips', 'row']] = df['row'].str.split(expand=True)

print(df)
