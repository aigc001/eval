
# Convert to PyTorch tensors
ids = torch.tensor(ids)
x = torch.tensor(x)

# Gather the selected slices
result = torch.gather(x, 1, ids.unsqueeze(-1).expand(-1, -1, x.shape[-1]))

# Squeeze the last dimension
result = result.squeeze(1)
