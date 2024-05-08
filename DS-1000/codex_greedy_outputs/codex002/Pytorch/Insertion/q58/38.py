
# Get the sign of each element
sign_x = torch.sign(x)
sign_y = torch.sign(y)

# Get the minimum absolute value for each element
min_abs = torch.min(torch.abs(x), torch.abs(y))

# Get the sign of the minimum absolute value
sign_min = torch.where(torch.abs(x) < torch.abs(y), sign_x, sign_y)

# Multiply the sign with the minimum absolute value
result = sign_min * min_abs
