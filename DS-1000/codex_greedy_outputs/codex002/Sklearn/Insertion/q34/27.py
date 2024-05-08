
# Reshape y to be a column vector
y = y.reshape(-1, 1)

# Reshape X to be a matrix with one column
X = X.reshape(-1, 1)

# Reshape X_test to be a matrix with one column
X_test = X_test.reshape(-1, 1)

# Fit the model
regressor = RandomForestRegressor(n_estimators=150, min_samples_split=1.0, random_state=42)
rgr = regressor.fit(X, y)
