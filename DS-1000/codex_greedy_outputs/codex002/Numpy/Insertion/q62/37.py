
# Convert the arrays to tuples
A_tuples = [tuple(row) for row in A]
B_tuples = [tuple(row) for row in B]

# Find the complement of A in B
complement = [row for row in A_tuples if row not in B_tuples]

# Convert the tuples back to arrays
output = np.asarray([list(row) for row in complement])

print(output)
