
# The diagonals of the matrix
diagonal_1 = matrix.diagonal(offset=-1)
diagonal_2 = matrix.diagonal(offset=0)
diagonal_3 = matrix.diagonal(offset=1)

# Create the tridiagonal matrix
tridiagonal_matrix = sparse.diags([diagonal_1, diagonal_2, diagonal_3], [-1, 0, 1], (5, 5)).toarray()

print(tridiagonal_matrix)
