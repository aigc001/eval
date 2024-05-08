
# Drop the NaN values
df = df.dropna(how='all')

# Create a new column that concatenates all the rows
df['keywords_all'] = df.apply(lambda row: ','.join(row.dropna().astype(str)), axis=1)

print(df)
