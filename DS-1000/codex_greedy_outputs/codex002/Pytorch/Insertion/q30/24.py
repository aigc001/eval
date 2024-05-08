
# Create a mask of the same shape as 'a' with zeros
mask = torch.zeros_like(a)

# For each row in the mask, set the values to 1 up to the corresponding length
for i, length in enumerate(lengths):
    mask[i, :length, :] = 1

# Apply the mask to 'a'
a = a * mask
