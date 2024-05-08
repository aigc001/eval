
# Convert the string data to numerical data
X = np.array(X)
X[:, 1] = X[:, 1].astype(float)

# Fit the model
clf.fit(X, ['2', '3'])
