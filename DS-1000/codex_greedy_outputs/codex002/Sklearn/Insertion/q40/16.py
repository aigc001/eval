
grid.fit(X, y)
best_params = grid.best_params_
best_model = grid.best_estimator_.named_steps["model"]
coef = best_model.coef_
