
# Construct a full matrix with the scalar value x
x_matrix = sparse.csr_matrix(x * np.ones(V.shape))

# Add the scalar y to the result
B = x_matrix + V + y
