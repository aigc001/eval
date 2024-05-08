
# First, we need to identify the columns that are equal to 0
df['category'] = df.apply(lambda row: [col for col in df.columns if row[col] == 0], axis=1)

# Then, we need to join the lists in 'category' into a single string
df['category'] = df['category'].apply(lambda x: ''.join(x))
