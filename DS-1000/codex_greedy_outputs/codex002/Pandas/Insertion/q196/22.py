
# Split the column into a list of values
df['var2'] = df['var2'].str.split('-')

# Expand the lists into separate rows
df = df.explode('var2')
