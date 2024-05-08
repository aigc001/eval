
# Create a unique list of the 'a' column
unique_a = df['a'].unique()

# Create a dictionary mapping each unique value to a unique ID
a_to_id = {a: i+1 for i, a in enumerate(unique_a)}

# Replace the 'a' column with the unique IDs
df['a'] = df['a'].map(a_to_id)
