
# Merge the two dataframes on the 'A' column
merged = pd.merge(C, D, on='A', how='outer')

# Create a new column 'dulplicated' which is True if the 'A' column values are duplicated, else False
merged['dulplicated'] = merged['A'].duplicated(keep=False)

# Replace the NaN values in 'B_y' with the corresponding values from 'B_x'
merged['B_y'].fillna(merged['B_x'], inplace=True)

# Drop the 'B_x' column
merged.drop('B_x', axis=1, inplace=True)

# Rename the 'B_y' column to 'B'
merged.rename(columns={'B_y': 'B'}, inplace=True)

# Print the final merged dataframe
print(merged)
