
# Create a 2D array of indices
indices = np.indices(arr.shape)

# Create a 2D array of the number of neighbors that are less than or equal
neighbors = signal.convolve(arr, np.ones((3, 3)), mode='same', method='direct')

# Find the relative extrema
extrema = np.where((arr <= neighbors) & (arr != 0))

# Get the indices of the relative extrema
extrema_indices = indices[:, extrema[0], extrema[1]].T.tolist()

print(extrema_indices)
