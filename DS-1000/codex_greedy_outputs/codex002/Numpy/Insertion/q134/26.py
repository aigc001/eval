
# Convert the integers to binary and then to a numpy array
binary_array = np.unpackbits(np.uint8(a), bitorder='big')

# Reshape the array to the desired shape
binary_array = binary_array.reshape((a.size, m))

print(binary_array)
