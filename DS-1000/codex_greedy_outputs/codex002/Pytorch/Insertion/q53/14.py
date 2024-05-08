
# Convert the tensors to numpy arrays
A_np = A.numpy()
B_np = B.numpy()

# Get the last x elements
A_last_x = A_np[-x:]
B_last_x = B_np[-x:]

# Compare the last x elements
diff = np.not_equal(A_last_x, B_last_x)

# Count the number of differences
count = np.sum(diff)

# Print the count
print(f"Number of differences in the last {x} elements: {count}")
