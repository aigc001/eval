
# Create a grid of coordinates
x = np.arange(shape[1])
y = np.arange(shape[0])
X, Y = np.meshgrid(x, y)

# Compute the Manhattan distance from the center
mid = np.array([shape[0]//2, shape[1]//2])
dist = np.abs(X - mid[1]) + np.abs(Y - mid[0])
