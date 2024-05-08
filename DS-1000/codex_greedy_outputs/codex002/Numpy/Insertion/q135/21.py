
# Convert the integers to binary and then to a numpy array
binary_array = np.array(list(np.binary_repr(a, width=m)))

# Replace '0' and '1' with 0 and 1 respectively
binary_array = np.where(binary_array=='0', 0, 1)

# Reshape the array to the desired shape
binary_array = binary_array.reshape((a.shape[0], m))

print(binary_array)
