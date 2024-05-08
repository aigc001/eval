
# Convert the string data to numerical data
le = preprocessing.LabelEncoder()
X = np.array([list(map(le.fit_transform, x)) for x in X])

# Fit the model
clf.fit(X, ['4', '5'])
