
model = SelectFromModel(clf, prefit=True)
X_new = model.transform(X)

# Get the mask of the features selected
mask = model.get_support()

# Get the column names of the selected features
selected_columns = X.columns[mask]

# Create a new DataFrame with only the selected features
selected_X = X[selected_columns]
