
# Create a new column that combines 'url' and 'drop_if_dup'
df['combined'] = df['url'] + df['drop_if_dup']

# Drop duplicates in this new column
df = df.drop_duplicates(subset='combined', keep='first')

# Drop the 'combined' column
df = df.drop(columns='combined')
