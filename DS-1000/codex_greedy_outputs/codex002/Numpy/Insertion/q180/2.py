
# Get the shape of the array
shape = Z.shape

# Create a tuple for slicing
slice_tuple = tuple(slice(None) for _ in range(len(shape) - 1)) + (-1,)

# Use the tuple to slice the array
Z_last_dim = Z[slice_tuple]
