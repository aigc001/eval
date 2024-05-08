
# Convert the numpy array to a PyTorch tensor
softmax_output = torch.tensor(softmax_output)

# Find the index of the maximum value in each row
max_values, max_indices = torch.max(softmax_output, dim=1)

# Create a new tensor with the class labels
class_labels = max_indices.unsqueeze(1)

# Convert the tensor to a numpy array
class_labels = class_labels.numpy()
