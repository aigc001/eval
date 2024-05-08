
X, Y = np.meshgrid(x, y)
Z = np.cos(X)**4 + np.sin(Y)**2

# Use Simpson's rule
integral = np.sum(Z * np.diff(x)[0] * np.diff(y)[0])
