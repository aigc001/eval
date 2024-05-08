
# Create a tensor with zeros
new = torch.zeros(t.size(0)+2, t.size(1)+2)

# Assign the original tensor to the center of the new tensor
new[1:-1, 1:-1] = t

# Print the new tensor
print(new)
