
# Find the minimum value along axis 1
min_values = a.min(axis=1)

# Create a mask where each element equals the minimum value along the axis
mask = (a.T == min_values).T
