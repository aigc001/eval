
# Reshape the data into the desired bin size
bin_data = data.reshape(-1, bin_size)

# Calculate the mean of each bin
bin_data_mean = np.mean(bin_data, axis=1)

print(bin_data_mean)
