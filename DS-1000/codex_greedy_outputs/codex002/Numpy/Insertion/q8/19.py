
# Get the unique values in `a` and their corresponding indices
unique_values, inverse_indices = np.unique(a, return_inverse=True)

# Create a new array `b` with the shape of `a` but with the number of unique values in `a` as the number of columns
b = np.zeros((a.shape[0], len(unique_values)), dtype=int)

# Set the corresponding elements in `b` to 1 using the inverse indices
b[np.arange(a.size).reshape(a.shape), inverse_indices.reshape(a.shape)] = 1
