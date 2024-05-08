
# Create a copy of the sparse matrix V and convert it to a CSR format
V_csr = V.tocsr()

# Create a new sparse matrix with the same shape as V but filled with x
x_matrix = sparse.csr_matrix(np.full(V.shape, x))

# Add the two matrices together
result = V_csr + x_matrix
