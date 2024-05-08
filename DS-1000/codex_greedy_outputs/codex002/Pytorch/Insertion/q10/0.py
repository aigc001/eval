
# Convert the ByteTensor to a boolean mask
mask = A_logical.bool()

# Use the mask to select the columns from B
C = B[:, mask]
