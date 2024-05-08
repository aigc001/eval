
model = SelectFromModel(clf, prefit=True)
X_new = model.transform(X)

# Get the mask of the features selected
mask = model.get_support()

# Apply the mask to get the feature names
selected_features = X.columns[mask]
