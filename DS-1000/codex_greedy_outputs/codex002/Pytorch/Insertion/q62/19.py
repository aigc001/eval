
# Convert the tensors to numpy arrays for easier manipulation
a_np = a.numpy()
b_np = b.numpy()

# Create a new array that will hold the result
result = np.zeros((a_np.shape[0], a_np.shape[1] + b_np.shape[1] - 1))

# Assign the first two columns of 'a' to the first two columns of 'result'
result[:, :2] = a_np[:, :2]

# Assign the last two columns of 'b' to the last two columns of 'result'
result[:, -2:] = b_np[:, -2:]

# Compute the average of the overlapping columns and assign it to the middle column of 'result'
result[:, 2:-2] = (a_np[:, -1] + b_np[:, 0]) / 2

# Convert the result back to a torch tensor
result = torch.from_numpy(result)
