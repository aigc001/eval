
# Use numpy's in1d function to check for each element of B in A
# This will return a boolean array where True signifies that the element of B is in A
mask = np.in1d(A, B)

# Use the mask to remove the elements from A
C = A[~mask]
