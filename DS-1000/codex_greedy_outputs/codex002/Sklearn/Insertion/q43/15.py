
# Get the feature importances
importances = clf.feature_importances_

# Get the indices of the important features
indices = np.where(importances > 0)[0]

# Get the column names of the important features
important_columns = X.columns[indices]
