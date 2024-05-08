
# convert the sparse column vector to a dense numpy array
dense_col = col.toarray().flatten()

# get the median
median = np.median(dense_col)

# get the mode
mode = np.bincount(dense_col.astype(int)).argmax()

print("Median: ", median)
print("Mode: ", mode)
