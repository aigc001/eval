
# Predict probabilities
predicted_test_probs = svmmodel.predict_proba(x_test)
# The predict_proba method returns an array of shape (n_samples, n_classes).
# In a binary classification problem, n_classes is 2.
# The probability of the positive class is in the first column,
# and the probability of the negative class is in the second column.
# If you want the probability of the positive class, you can do:
predicted_test_probs = predicted_test_probs[:, 1]
