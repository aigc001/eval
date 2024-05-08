
# Calculate the outer product of each column of X
# The outer product of a vector x with itself, x.dot(x.T), is a symmetric matrix
# We can use np.einsum to calculate the outer product of each column of X
# np.einsum('ij,ik->ijk', X, X) will calculate the outer product for each column i, and stack them together
# to form a 3D array of shape (M, M, N)

# Calculate the outer product of each column of X
outer_product = np.einsum('ij,ik->ijk', X, X)

# Reshape the outer product to the desired shape (N, M, M)
result = np.transpose(outer_product, (2, 0, 1))
