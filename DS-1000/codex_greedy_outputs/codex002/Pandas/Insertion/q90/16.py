
# Create a boolean mask where True means the row is equal in both dataframes
mask = (df1[columns_check_list] == df2[columns_check_list]).all(axis=1)

# Use the mask to filter the dataframes
df1_filtered = df1[mask]
df2_filtered = df2[mask]

# Print the filtered dataframes
print(df1_filtered)
print(df2_filtered)
