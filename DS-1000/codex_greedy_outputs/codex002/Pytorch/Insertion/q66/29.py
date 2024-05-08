
# Create a tensor with the shape of the original tensor
new_tensor = torch.full(t.shape, -1)

# Stack the original tensor and the new tensor
result = torch.stack([t, new_tensor])

# Print the result
print(result)
