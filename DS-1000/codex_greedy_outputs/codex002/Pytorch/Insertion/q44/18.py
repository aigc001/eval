
# Convert the numpy array to a PyTorch tensor
softmax_output = torch.tensor(softmax_output)

# Find the index of the maximum value in each row
# The index of the maximum value corresponds to the class label
class_predictions = torch.argmin(softmax_output, dim=1)

# Reshape the tensor to be n x 1
class_predictions = class_predictions.view(-1, 1)

# Convert the tensor to a numpy array
class_predictions = class_predictions.numpy()
