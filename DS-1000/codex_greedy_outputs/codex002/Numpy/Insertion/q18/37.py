
# Find the maximum value in the array
max_value = np.max(a)

# Find the position of the maximum value
max_position = np.unravel_index(np.argmax(a), a.shape)

print("Maximum value:", max_value)
print("Position of maximum value (row, column):", max_position)
