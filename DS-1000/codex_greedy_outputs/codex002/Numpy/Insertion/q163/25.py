
# Calculate the L∞ norm of each row
norms = LA.norm(X, axis=1, ord=np.inf)

# Divide each row by its L∞ norm
X_normalized = X / norms[:, np.newaxis]

print(X_normalized)
