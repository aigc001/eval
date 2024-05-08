
# Split the row column into three new columns
df[['fips', 'medi', 'row']] = df['row'].str.split(expand=True)

# Drop the original row column
df.drop(columns='row', inplace=True)

# Rename the columns
df.columns = ['fips', 'medi', 'row']
