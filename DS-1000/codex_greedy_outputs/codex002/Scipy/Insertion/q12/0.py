
    # Convert the sparse matrix to a dense one for multiplication
    dense_A = sA.toarray()
    # Perform the multiplication
    result = dense_A * sB.toarray()
    # Convert the result back to a sparse matrix
    result_sparse = sparse.csr_matrix(result)
    return result_sparse
