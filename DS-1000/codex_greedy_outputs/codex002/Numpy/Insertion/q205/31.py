
# Create a new array of the desired shape, filled with zeros
result = np.zeros(shape)

# Copy the original array into the new array
result[:a.shape[0], :a.shape[1]] = a

# Print the result
print(result)
