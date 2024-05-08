
# Create a boolean array where True values correspond to elements in A that are in B
boolean_array = np.isin(A, B)

# Use the boolean array to filter out the elements in A
C = A[boolean_array]

print(C)
