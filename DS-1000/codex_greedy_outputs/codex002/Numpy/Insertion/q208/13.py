
# Calculate the padding
padding = ((0, shape[0] - a.shape[0]), (0, shape[1] - a.shape[1]))

# Apply the padding
a = np.pad(a, padding, mode='constant')
