
# Convert the arrays to sets of tuples
setA = set(tuple(row) for row in A)
setB = set(tuple(row) for row in B)

# Find the symmetric difference
sym_diff = setA ^ setB

# Convert the result back to a numpy array
output = np.asarray(list(sym_diff))

# If you want the output to be sorted in the same order as in the original arrays,
# you can use the following code instead:
# output = np.asarray(list(sym_diff.union(setA).union(setB)))

print(output)
