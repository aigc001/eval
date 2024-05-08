
# Find the indices that would sort 'a' in descending order along the first axis
sort_indices = np.argsort(-a, axis=0)

# Use these indices to rearrange 'b'
c = np.take_along_axis(b, sort_indices, axis=0)
