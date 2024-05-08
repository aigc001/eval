
# Get the unique values in `a` and their corresponding indices
unique_values, inverse_indices = np.unique(a, return_inverse=True)

# Create a 2D one-hot array
b = np.zeros((len(a), len(unique_values)), dtype=int)
b[np.arange(len(a)), inverse_indices] = 1
