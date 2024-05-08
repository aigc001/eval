
    model = LinearSVC(penalty='l1', dual=False)
    model.fit(X, y)
    # The coefficients of the SVM model are what we are interested in.
    # They represent the weights of the features.
    # The get_support method returns a boolean mask indicating which features are selected.
    # We use this mask to select the corresponding feature names.
    feature_mask = model.coef_[0] != 0
    feature_names = np.asarray(vectorizer.get_feature_names())[feature_mask]
    return feature_names
