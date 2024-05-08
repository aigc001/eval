
# Convert numpy array to torch tensor
idx_tensor = torch.from_numpy(idx)

# Use tensor indexing
result = t[idx_tensor]
