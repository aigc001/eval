
# Get the first column name
first_column = df.columns[0]

# Rename the first column
df = df.rename(columns={first_column: 'Test'})
