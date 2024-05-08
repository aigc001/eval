
# Get the shape of the array
shape = a.shape
# Calculate the number of diagonals
num_diag = min(shape)
# Get the indices of the diagonals
diagonal_indices = [np.diag_indices(i, len(shape)) for i in range(num_diag, 0, -1)]
# Get the values at the diagonal indices
diagonal_values = [a[indices] for indices in diagonal_indices]
# Concatenate the values into a single array
diagonal = np.concatenate(diagonal_values)
print(diagonal)
