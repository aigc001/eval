
# Create a temporary column to hold the forward filled values
df['B'] = df['A'].ffill()

# Replace the original column with the temporary column
df['A'] = df['B']

# Drop the temporary column
df.drop('B', axis=1, inplace=True)
