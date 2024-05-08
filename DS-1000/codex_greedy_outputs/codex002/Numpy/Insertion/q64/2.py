
# argsort along axis 0
sort_indices = np.argsort(a, axis=0)

# use the indices to rearrange b
c = np.take_along_axis(b, sort_indices, axis=0)
