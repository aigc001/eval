
# Merge the two dataframes on the 'A' column
merged = pd.merge(C, D, on='A', how='outer')

# Replace the NaN values in 'B_x' with the corresponding values in 'B_y'
merged['B_x'].fillna(merged['B_y'], inplace=True)

# Drop the 'B_y' column
merged.drop('B_y', axis=1, inplace=True)

# Rename the 'B_x' column to 'B'
merged.rename(columns={'B_x': 'B'}, inplace=True)

print(merged)
