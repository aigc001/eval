
model = SelectFromModel(clf, prefit=True)
X_new = model.transform(X)

# Get the mask of the features selected
mask = model.get_support()

# Get the list of feature names
selected_features = [f for f, m in zip(X.columns, mask) if m]

# Create a new DataFrame with only the selected features
selected_X = X[selected_features]
