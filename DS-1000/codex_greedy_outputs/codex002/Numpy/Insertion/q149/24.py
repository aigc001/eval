
# Reshape Y into a 3D tensor of shape (N, M, M)
Y = np.reshape(Y, (4, 3, 3))

# Calculate the inverse of each 3x3 matrix
Y_inv = np.linalg.inv(Y)

# Extract the diagonal of each 3x3 matrix
X = np.diagonal(Y_inv, axis1=1, axis2=2)

# Reshape X into a 2D matrix of shape (M, N)
X = np.reshape(X, (3, 4))
