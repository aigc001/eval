
# Use np.arange to create an array of the same shape as 'a'
# Use np.argmax to find the indices of the maximum values along axis 1
# Use np.equal to compare these indices with the array of indices created by np.arange
mask = np.equal(np.arange(a.shape[0])[:, np.newaxis], np.argmax(a, axis=1)[:, np.newaxis])
