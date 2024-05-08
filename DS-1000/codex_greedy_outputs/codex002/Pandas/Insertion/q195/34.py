
# Split the strings in the 'var2' column into lists
df['var2'] = df['var2'].str.split(',')

# Explode the lists into separate rows
df = df.explode('var2')
