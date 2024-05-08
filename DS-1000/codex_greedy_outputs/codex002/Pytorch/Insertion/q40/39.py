
# Reshape ids to match the shape of x
ids = ids.unsqueeze(2).expand(-1,-1,x.size(2))

# Gather the elements
result = x.gather(1, ids)

# Squeeze the result to get the desired shape
result = result.squeeze(1)
