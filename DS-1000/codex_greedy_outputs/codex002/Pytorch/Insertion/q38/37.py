
# Convert numpy array to a tensor
idx_tensor = torch.from_numpy(idx)

# Use the tensor to index the original tensor
result = t[idx_tensor, torch.arange(t.shape[1])]
