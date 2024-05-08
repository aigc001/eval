
# Reshape the data into the desired bin size
bin_data = data.reshape(-1, bin_size)

# Find the maximum of each bin
bin_data_max = np.max(bin_data, axis=1)

print(bin_data_max)
