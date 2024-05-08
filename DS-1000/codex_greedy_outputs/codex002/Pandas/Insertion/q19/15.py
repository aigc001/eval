
# Get the min and max values for the products in the list
min_val = df[df['product'].isin(products)]['score'].min()
max_val = df[df['product'].isin(products)]['score'].max()

# Normalize the scores
df.loc[df['product'].isin(products), 'score'] = (df['score'] - min_val) / (max_val - min_val)

# Set the scores for the specific products to 1 and 0 respectively
df.loc[df['product'] == 1069104, 'score'] = 1
df.loc[df['product'] == 1069105, 'score'] = 0
