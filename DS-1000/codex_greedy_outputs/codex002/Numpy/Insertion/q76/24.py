
# Method 1: Use the copy() function
a = array_of_arrays.copy()

# Method 2: Use the np.copy() function
b = np.copy(array_of_arrays)

# Method 3: Use the copy parameter in np.array()
c = np.array(array_of_arrays, copy=True)
