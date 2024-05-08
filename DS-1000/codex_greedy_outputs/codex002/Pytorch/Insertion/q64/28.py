
# Create a tensor of zeros with the same shape as t
zeros = torch.zeros_like(t)

# Stack the original tensor and the zeros tensor
r = torch.stack([zeros, t])

# Add a row of zeros at the end
r = torch.cat([r, zeros.unsqueeze(0)], dim=0)

# Add a column of zeros at the end
r = torch.cat([r, zeros.unsqueeze(1)], dim=1)
