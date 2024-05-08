
# Forward fill the non-zero values
df['A'] = df['A'].replace(0, method='ffill')

# Backward fill the non-zero values
df['A'] = df['A'].replace(0, method='bfill')
