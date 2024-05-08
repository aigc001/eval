
# Find the indices of the real numbers
real_indices = np.where(np.imag(x) == 0)

# Delete the real numbers
x = np.delete(x, real_indices)
