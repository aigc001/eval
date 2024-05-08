
# One hot encode the categorical variable
X_train = pd.get_dummies(X_train)

# Train the model
clf = GradientBoostingClassifier(learning_rate=0.01,max_depth=8,n_estimators=50).fit(X_train, y_train)
