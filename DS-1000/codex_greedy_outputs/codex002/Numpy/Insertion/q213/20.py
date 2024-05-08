
# Use numpy's advanced indexing to select the elements from a based on b
selected = a[np.arange(a.shape[0])[:, np.newaxis, np.newaxis], np.arange(a.shape[1])[np.newaxis, :, np.newaxis], b]
# Sum the selected elements
result = np.sum(selected)
print(result)
