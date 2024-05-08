
# Convert the integers to binary and then to a numpy array
binary_arrays = np.unpackbits(np.uint8(a.reshape(-1, 1)), axis=1)[:, -m:]

# Compute the exclusive or of all the rows
xor_result = np.bitwise_xor.reduce(binary_arrays, axis=0)

print(binary_arrays)
print(xor_result)
