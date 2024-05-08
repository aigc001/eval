
# Get the best parameters
best_params = GridSearch_fitted.best_params_

# Get the best score
best_score = GridSearch_fitted.best_score_

# Get the cv results
cv_results = GridSearch_fitted.cv_results_

# Convert the cv_results to a DataFrame
cv_results_df = pd.DataFrame(cv_results)

# Sort the DataFrame by mean fit time
cv_results_df_sorted = cv_results_df.sort_values(by='mean_fit_time')

# Print the sorted DataFrame
print(cv_results_df_sorted)
