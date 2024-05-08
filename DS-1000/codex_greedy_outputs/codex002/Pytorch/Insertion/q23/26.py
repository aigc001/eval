
# Convert 2D tensor to numpy array
np_array = Tensor_2D.numpy()

# Create a diagonal matrix for each row in the numpy array
diag_matrix = np.array([np.diag(row) for row in np_array])

# Convert the numpy array back to a torch tensor
diag_matrix_tensor = torch.from_numpy(diag_matrix)
