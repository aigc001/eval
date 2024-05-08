
# Calculate the z-scores
z_scores = stats.zscore(df, nan_policy='omit')

# Create a new dataframe to hold the results
result = pd.DataFrame(index=df.index)

# Add the data and z-score columns
for col in df.columns:
    result[col] = df[col].round(3)
    result[col + '_zscore'] = z_scores[:, df.columns.get_loc(col)].round(3)

print(result)
