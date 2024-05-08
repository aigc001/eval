
# Convert the logical index to a list of integers
A_log = torch.nonzero(A_log).view(-1)

# Use the list of integers to slice the tensor
C = B[:, A_log]
