
model = LinearSVC(penalty='l1')
model.fit(X, y)
# Get the coefficients
coef = model.coef_[0]
# Get the indices of non-zero coefficients
selected_features = np.where(coef != 0)[0]
# Get the corresponding feature names
selected_features = np.asarray(vectorizer.get_feature_names())[selected_features]
