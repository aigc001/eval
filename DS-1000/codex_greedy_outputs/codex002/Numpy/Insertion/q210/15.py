
# reshape b to have the same dimensions as the third dimension of a
b = b.reshape(b.shape + (1,))

# use numpy fancy indexing to select the elements in a according to b
desired = a[np.arange(a.shape[0])[:, np.newaxis, np.newaxis], np.arange(a.shape[1])[np.newaxis, :, np.newaxis], b]
