
# Convert the string data to numerical data
X = np.array(X)
le = preprocessing.LabelEncoder()
X[:, 0] = le.fit_transform(X[:, 0])
X[:, 1] = le.fit_transform(X[:, 1])

# Fit the model
clf.fit(X, ['2', '3'])
