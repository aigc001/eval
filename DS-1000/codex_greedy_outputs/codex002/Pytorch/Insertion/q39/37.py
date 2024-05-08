
# Reshape ids to match the dimensions of x
ids = ids.unsqueeze(1).expand(-1, x.size(1), -1)

# Gather the elements
result = x.gather(1, ids).squeeze(1)
