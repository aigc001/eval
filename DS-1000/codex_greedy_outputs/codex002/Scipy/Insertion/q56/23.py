
# Create a list of vectors with the same length by padding zeros
padded_vectors = []
for vector in vectors:
    padded_vector = np.pad(vector, (0, max_vector_size - len(vector)), 'constant')
    padded_vectors.append(padded_vector)

# Convert the list of vectors to a sparse matrix
sparse_matrix = sparse.csr_matrix(padded_vectors)

print(sparse_matrix)
