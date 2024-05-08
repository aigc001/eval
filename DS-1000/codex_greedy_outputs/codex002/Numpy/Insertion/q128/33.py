
# Calculate the number of bins
num_bins = data.shape[1] // bin_size

# Reshape the data into bins and calculate the mean
bin_data_mean = np.mean(data[:, -num_bins*bin_size:].reshape(data.shape[0], num_bins, bin_size), axis=2)

print(bin_data_mean)
