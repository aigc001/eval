
# Find the maximum value in the array
max_value = np.max(a)

# Find the indices of the maximum value
max_indices = np.unravel_index(np.argmax(a), a.shape)

print("Maximum value:", max_value)
print("Indices of maximum value:", max_indices)
