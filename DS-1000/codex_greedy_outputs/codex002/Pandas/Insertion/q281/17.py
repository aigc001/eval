
# Create a mask of all values greater than 0.3
mask = corr > 0.3

# Use the mask to filter the correlation DataFrame
filtered_corr = corr[mask]

# Reset the index to get the desired output
filtered_corr.reset_index(inplace=True)

# Create a new column for the index
filtered_corr['index'] = filtered_corr['level_0']

# Drop the old index
filtered_corr.drop(columns='level_0', inplace=True)

# Set the new column as the index
filtered_corr.set_index('index', inplace=True)

# Print the filtered correlation DataFrame
print(filtered_corr)
