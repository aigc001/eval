
# Convert the tensors to numpy arrays
A_np = A.numpy()
B_np = B.numpy()

# Find the indices where the two arrays are not equal
diff_indices = np.where(A_np != B_np)

# Get the count of the indices
count = len(diff_indices[0])

# Print the count
print(f"Count of different elements: {count}")
