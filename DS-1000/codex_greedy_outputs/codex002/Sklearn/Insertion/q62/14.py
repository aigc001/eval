
# Convert list of lists to DataFrame
df = pd.DataFrame(features)

# Fill missing values with 0
df.fillna(0, inplace=True)

# Convert DataFrame to Numpy array
features_array = df.values

# Use sklearn feature selection utilities
selector = sklearn.feature_selection.SelectKBest(sklearn.feature_selection.f_classif, k=5)
selected_features = selector.fit_transform(features_array, target)
