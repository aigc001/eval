
# Create a mask of the values that are above 0.3
mask = corr.abs() > 0.3

# Use the mask to filter the values
filtered_corr = corr.where(mask)

# Drop the rows and columns that are all NaN
filtered_corr = filtered_corr.dropna(how='all', axis=0).dropna(how='all', axis=1)

print(filtered_corr)
