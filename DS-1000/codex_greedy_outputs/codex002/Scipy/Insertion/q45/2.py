
def is_csr_matrix_only_zeroes(my_csr_matrix):
    return not my_csr_matrix.nnz

sa = sparse.random(10, 10, density = 0.01, format = 'csr')
print(is_csr_matrix_only_zeroes(sa))
