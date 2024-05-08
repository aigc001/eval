
# Compute the L1 norm of each row
l1 = np.abs(X).sum(axis=1)

# Normalize each row by dividing it by its L1 norm
X_normalized = X / l1[:, np.newaxis]

print(X_normalized)
