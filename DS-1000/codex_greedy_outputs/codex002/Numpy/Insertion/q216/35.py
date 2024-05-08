
# Find the indices of non-zero elements
non_zero_indices = np.nonzero(im)
# Get the unique values of the indices
unique_indices = np.unique(non_zero_indices)
# Use these indices to slice the original array
result = im[unique_indices[0].min():unique_indices[0].max()+1,
            unique_indices[1].min():unique_indices[1].max()+1]
