
# argsort along the first axis
sort_indices = np.argsort(a, axis=0)

# use the indices to rearrange the elements in b
c = np.take_along_axis(b, sort_indices, axis=0)
