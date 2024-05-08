
# Compute the L2 norm of each row
norms = LA.norm(X, axis=1)

# Divide each row by its L2 norm
X_normalized = X / norms[:, np.newaxis]

print(X_normalized)
