
# Get the indexes of the N biggest elements
indexes = np.argpartition(a, -N)[-N:]
# Sort the indexes in decreasing order
indexes = indexes[np.argsort(a[indexes])][::-1]
print(indexes)
