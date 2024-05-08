
# Create a copy of the dataframe to avoid modifying the original one
df_copy = df.copy()

# Multiply the scores of the specified products by 10
df_copy.loc[df_copy['product'].isin(products), 'score'] *= 10

print(df_copy)
