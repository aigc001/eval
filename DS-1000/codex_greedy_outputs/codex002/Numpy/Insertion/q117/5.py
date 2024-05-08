
# We use np.unique to get the unique indices and the inverse indices
# The unique indices are the indices that we will use to get the minimum values
# The inverse indices are used to map the unique indices back to the original index array
unique_indices, inverse_indices = np.unique(index, return_inverse=True)

# We use np.minimum.reduceat to get the minimum values for each unique index
result = np.minimum.reduceat(a[unique_indices], np.cumsum(np.bincount(inverse_indices))[:-1])

# We use the inverse indices to map the result back to the original array
final_result = np.zeros_like(a)
final_result[unique_indices] = result

# We use np.take to get the values at the original index array
final_result = np.take(final_result, index)

print(final_result)
