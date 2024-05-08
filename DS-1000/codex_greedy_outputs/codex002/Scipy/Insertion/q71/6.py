
# Create a grid of coordinates
x = np.arange(shape[1])
y = np.arange(shape[0])
x, y = np.meshgrid(x, y)

# Create a mid point
mid = np.array([shape[0]//2, shape[1]//2])

# Compute the distances
distances = distance.cdist(np.column_stack((x.ravel(), y.ravel())), mid)

# Reshape the distances to the original shape
distances = distances.reshape(shape)
