
# Create a NxN identity matrix
dct_matrix = np.eye(N)

# Apply the DCT to each column of the identity matrix
dct_matrix = sf.dct(dct_matrix, norm='ortho', axis=0)

# Apply the DCT to each row of the resulting matrix
dct_matrix = sf.dct(dct_matrix, norm='ortho', axis=1)
