
# Find the indices of the minimum values
indices = np.where(a == a.min())
# Transform the indices into the required format
result = np.array(list(zip(indices[0], indices[1])))
print(result)
