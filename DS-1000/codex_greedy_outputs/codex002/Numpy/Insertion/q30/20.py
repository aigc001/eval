
# Use the argmax function which returns the indices of the maximum value
# The argmax function returns a tuple of indices
# The first element of the tuple corresponds to the row index
# The second element corresponds to the column index
row_index, col_index = np.unravel_index(a.argmax(), a.shape)
print(row_index, col_index)
