
# Drop NaN values
df = df.dropna(how='all')

# Create a new column that concatenates all the rows excluding NaN values
df['keywords_all'] = df.apply(lambda row: '-'.join(row.dropna().astype(str)), axis=1)

print(df)
