
# Flatten the array and get the second largest value
flattened_a = a.flatten()
second_largest = np.partition(flattened_a, -2)[-2]

# Get the indices of the second largest value
indices = np.where(a == second_largest)

# Unravel the indices
unraveled_indices = np.unravel_index(indices[0][0], a.shape)

print(unraveled_indices)
