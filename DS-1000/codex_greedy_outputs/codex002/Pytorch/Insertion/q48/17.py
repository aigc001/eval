
# Convert the tensors to numpy arrays
A_np = A.numpy()
B_np = B.numpy()

# Compare the two arrays and get the number of equal elements
num_equal = np.sum(A_np == B_np)

# Print the number of equal elements
print(num_equal)
