
# Find the smallest value in the array
min_value = np.min(a)

# Find the indices of the smallest value
min_indices = np.unravel_index(np.argmin(a, axis=None), a.shape)

print("Smallest value:", min_value)
print("Indices of the smallest value:", min_indices)
