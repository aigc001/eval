
# Split the row column into two new columns
df[['fips', 'row']] = df['row'].str.split(expand=True)

# Drop the original row column
df.drop(columns='row', inplace=True)

# Rename the columns
df.columns = ['fips', 'row']
