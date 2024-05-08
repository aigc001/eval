
# Get the shape of the array
shape = a.shape

# Create a tuple of slices
slices = tuple(slice(-1, None) if i == 0 else slice(None) for i in range(len(shape)))

# Use the slices to get the last element along the first dimension
last_elements = a[slices]
