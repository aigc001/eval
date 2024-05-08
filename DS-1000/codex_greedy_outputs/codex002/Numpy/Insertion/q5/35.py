
# Find the maximum value in the array
max_val = np.max(a)

# Create an empty 2D array with the same length as a and width as max_val+1
b = np.zeros((len(a), max_val + 1))

# For each value in a, set the corresponding value in b to 1
b[np.arange(len(a)), a] = 1
