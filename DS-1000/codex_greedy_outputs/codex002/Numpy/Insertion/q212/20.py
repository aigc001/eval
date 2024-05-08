
# Use numpy's advanced indexing to select the elements in a according to b
desired = a[np.arange(a.shape[0])[:, np.newaxis, np.newaxis],
             np.arange(a.shape[1])[np.newaxis, :, np.newaxis],
             b]
