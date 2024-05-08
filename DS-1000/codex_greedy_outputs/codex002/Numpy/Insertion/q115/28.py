
# Use numpy's argsort function to get the indices that would sort the array
sorted_indices = np.argsort(a)
# Use numpy's take function to reorder the indices according to the sorted indices
reordered_indices = np.take(index, sorted_indices)
# Use numpy's unique function to get the unique values in the index array and their corresponding indices
unique_values, unique_indices = np.unique(reordered_indices, return_index=True)
# Use numpy's take function again to get the maximum values for each unique index
max_values = np.take(a, sorted_indices[unique_indices])
