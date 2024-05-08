
# Create a new array of the desired shape, filled with the desired element
new_a = np.full(shape, element)

# Get the original array's shape
a_shape = a.shape

# Calculate the number of rows and columns to pad on the top and left
pad_top = shape[0] - a_shape[0]
pad_left = shape[1] - a_shape[1]

# Pad the original array with the desired element
padded_a = np.pad(a, ((0, pad_top), (0, pad_left)), constant_values=element)

# Replace the corresponding part of the new array with the padded original array
new_a[:padded_a.shape[0], :padded_a.shape[1]] = padded_a

print(new_a)
