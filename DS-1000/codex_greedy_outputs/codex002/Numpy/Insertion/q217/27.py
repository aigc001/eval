
# Find the indices of non-zero elements
non_zero_indices = np.nonzero(A)
# Get the minimum and maximum indices for rows and columns
min_row, max_row = min(non_zero_indices[0]), max(non_zero_indices[0])
min_col, max_col = min(non_zero_indices[1]), max(non_zero_indices[1])
# Slice the array
B = A[min_row:max_row+1, min_col:max_col+1]
