
def is_lil_matrix_only_zeroes(my_lil_matrix):
    return my_lil_matrix.nnz == 0

sa = sparse.random(10, 10, density = 0.01, format = 'lil')
print(is_lil_matrix_only_zeroes(sa))
