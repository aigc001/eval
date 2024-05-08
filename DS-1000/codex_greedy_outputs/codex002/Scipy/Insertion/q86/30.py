
# Construct a full matrix with the scalar value x
x_matrix = sparse.csr_matrix(x * np.ones(V.shape))

# Add the scalar to the non-zero values in V
V.data += x

# Add the full matrix x to V
V += x_matrix
