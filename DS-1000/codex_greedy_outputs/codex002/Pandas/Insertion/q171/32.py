
# Find the maximum value in each row
max_values = df.max(axis=1)

# Filter the dataframe where the maximum value is not 2
filtered_df = df[max_values != 2]

# Print the filtered dataframe
print(filtered_df)
