
# Use the explode function to split the lists into separate rows
df = df.explode('col1')

# Use the unique function to get a list of unique values
unique_values = df['col1'].unique().tolist()
