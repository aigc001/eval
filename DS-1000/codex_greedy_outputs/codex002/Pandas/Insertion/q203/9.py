
# Set the index as 'Name' column
df.set_index('Name', inplace=True)

# Replace 0 with NaN
df.replace(0, np.nan, inplace=True)

# Calculate the cumulative average from end to head
df = df.iloc[::-1].cumsum(axis=1) / (df.notna().sum(axis=1) + 1e-10)

# Replace NaN with 0
df.fillna(0, inplace=True)

# Reverse the dataframe back to original order
df = df.iloc[::-1]

# Reset the index
df.reset_index(inplace=True)
