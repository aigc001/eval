
# Find the minimum and maximum values in the array
min_val = a.min()
max_val = a.max()

# Create an array of indices from 0 to the number of unique elements in a
indices = np.arange(max_val - min_val + 1)

# Create a 2D one-hot array using the indices and the array of unique elements
b = np.zeros((a.size, max_val - min_val + 1), dtype=int)
b[np.arange(a.size), a - min_val] = 1
