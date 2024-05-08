
# Calculate the size of the slice
slice_size = high_index - low_index

# Create a new array with the desired size, filled with zeros
new_array = np.zeros((slice_size, slice_size))

# Calculate the offset from the original array's edge
offset = abs(low_index) if low_index < 0 else 0

# Copy the valid part of the original array into the new array
new_array[offset:offset+a.shape[0], offset:offset+a.shape[1]] = a

# Slice the new array
result = new_array[low_index:high_index, low_index:high_index]
