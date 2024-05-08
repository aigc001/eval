
# Calculate the number of rows to be sampled
n = int(len(df) * 0.2)

# Sample the rows and set the ProductId to zero
sampled_rows = df.sample(n, random_state=0)
sampled_rows['ProductId'] = 0

# Keep the indexes of the altered rows
altered_indexes = sampled_rows.index

# Update the original DataFrame
df.loc[altered_indexes, 'ProductId'] = 0
