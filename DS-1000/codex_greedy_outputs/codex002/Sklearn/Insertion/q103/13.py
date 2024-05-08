
# Split the data into features and target
X = dataframe.iloc[:, :-1].values
y = dataframe.iloc[:, -1].values
# Reshape X to be 2D
X = np.reshape(X, (X.shape[0], -1))
# Fit the model
logReg = LogisticRegression()
logReg.fit(X, y)
