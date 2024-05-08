
# Convert the tensors to numpy arrays
A_np = A.numpy()
B_np = B.numpy()

# Get the last x elements
A_last_x = A_np[-x:]
B_last_x = B_np[-x:]

# Compare the last x elements
equal_elements = np.sum(A_last_x == B_last_x)

# Print the number of equal elements
print(f"Number of equal elements: {equal_elements}")
