
# Create a new array with the same shape as the original
b = np.empty_like(a)

# Assign the columns of the original array to the new array according to the permutation
for i, j in enumerate(permutation):
    b[:, i] = a[:, j]

print(b)
