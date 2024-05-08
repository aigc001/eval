
# Reshape the data into the desired bin size
bin_data = data.reshape(data.shape[0], -1, bin_size)

# Calculate the mean of each bin
bin_data_mean = np.mean(bin_data, axis=2)

print(bin_data_mean)
