
# Convert the tensors to numpy arrays
A_np = A.numpy()
B_np = B.numpy()

# Compare the two arrays
equal_elements = np.sum(A_np == B_np)

print(f"Number of equal elements: {equal_elements}")
