
# Create a copy of the dataframe to avoid modifying the original one
df_copy = df.copy()

# Iterate over the rows and columns
for i in range(df_copy.shape[0]):
    for j in range(df_copy.shape[1]):
        # If the value is equal to 2, replace it with 0
        if df_copy.iloc[i, j] == 2:
            df_copy.iloc[i, j] = 0
