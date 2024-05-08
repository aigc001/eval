
# Method 1: Using numpy.array_equal
def check_equal_arrays(a):
    return all(np.array_equal(a[i], a[i+1]) for i in range(len(a)-1))

# Method 2: Using numpy.all
def check_equal_arrays(a):
    return all(np.all(a[i] == a[i+1]) for i in range(len(a)-1))

# Testing
print(check_equal_arrays(a))  # Should return True
