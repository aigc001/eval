
# Create a masked array where values less than 0 are masked
masked_data = np.ma.masked_where(DataArray < 0, DataArray)

# Calculate the percentile
prob = np.percentile(masked_data, percentile)

print(prob)
