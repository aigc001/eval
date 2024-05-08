
model.fit(X, y)
predicted_test = model.predict(x_predict)
predicted_test_scores = model.decision_function(x_predict)
