
# Create a mask of the same shape as 'a' with zeros
mask = torch.zeros_like(a)

# For each row in the mask, set the values after the corresponding length in 'lengths' to 1
for i, length in enumerate(lengths):
    mask[i, length:, :] = 1

# Use the mask to set the values in 'a' to 0
a = a * (1 - mask)
