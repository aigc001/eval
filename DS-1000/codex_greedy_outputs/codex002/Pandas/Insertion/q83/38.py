
# Create a copy of the dataframe to avoid modifying the original one
df_copy = df.copy()

# Iterate over the dataframe in reverse order
for i in range(len(df_copy) - 1, -1, -1):
    # If the value is 0, replace it with the next non-zero value
    if df_copy.loc[i, 'A'] == 0:
        df_copy.loc[i, 'A'] = df_copy.loc[i+1:, 'A'].ne(0).idxmax()

print(df_copy)
