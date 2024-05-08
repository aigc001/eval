
# Calculate the sum of each matrix in a
sums = np.sum(a, axis=(1, 2))

# Get the indices that would sort sums
sorted_indices = np.argsort(sums)

# Use the sorted indices to rearrange b
sorted_b = b[sorted_indices]
