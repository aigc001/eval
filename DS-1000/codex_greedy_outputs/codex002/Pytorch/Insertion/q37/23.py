
# Convert numpy array to torch tensor
idx_tensor = torch.from_numpy(idx)

# Use the torch tensor to index the original tensor
result = t[idx_tensor]
