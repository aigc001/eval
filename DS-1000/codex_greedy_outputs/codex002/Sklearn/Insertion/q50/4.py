
# One Hot Encoding on categorical variables
X_train = pd.get_dummies(X_train)

# Train model
clf = GradientBoostingClassifier(learning_rate=0.01,max_depth=8,n_estimators=50).fit(X_train, y_train)
