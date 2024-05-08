
# Get the best parameters
best_params = GridSearch_fitted.best_params_

# Get the best score
best_score = GridSearch_fitted.best_score_

# Get the cv results
cv_results = GridSearch_fitted.cv_results_

# Convert the cv results to a DataFrame
cv_results_df = pd.DataFrame(cv_results)

# Print the DataFrame
print(cv_results_df)
