
# Get the last column name
last_column = df.columns[-1]

# Rename the last column
df.rename(columns={last_column: 'Test'}, inplace=True)

print(df.columns)
