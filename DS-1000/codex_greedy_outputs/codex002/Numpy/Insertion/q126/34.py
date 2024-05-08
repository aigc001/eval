
# Reshape the data into the desired bin size, then take the mean along the row axis.
bin_data_mean = np.mean(data[-bin_size:].reshape(-1, bin_size), axis=1)
print(bin_data_mean)
