
# Set the diagonal to zero
b.data[b.indptr[1]::b.shape[0]+1] = 0
# Remove the zero entries
b.eliminate_zeros()
