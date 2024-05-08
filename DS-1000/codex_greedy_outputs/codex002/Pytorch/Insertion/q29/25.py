
# Create a tensor of the same shape as 'a' but filled with 2333
new_tensor = torch.full_like(a, 2333)

# Iterate over the batch dimension
for i in range(a.size(0)):
    # Get the length for the current sentence
    length = lengths[i]
    
    # Replace the values in 'a' with 2333 after the 'length' index
    a[i, length:, :] = new_tensor[i, length:, :]
