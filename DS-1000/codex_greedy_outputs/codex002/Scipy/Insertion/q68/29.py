
# Calculate z-scores
zscores = stats.zscore(df)

# Create a new DataFrame to hold the results
result = pd.DataFrame(index=df.index, columns=df.columns)

# Add the original data and the z-scores to the new DataFrame
result['data'] = df
result['zscore'] = zscores

# Print the result
print(result)
