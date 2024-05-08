
# Create a tensor of the same shape as 'a' but filled with 2333
new_tensor = torch.full(a.shape, 2333, dtype=torch.float)

# For each row in 'a' and corresponding length in 'lengths', replace the values up to the given length with the original values
for i in range(a.shape[0]):
    a[i, :lengths[i], :] = new_tensor[i, :lengths[i], :]
